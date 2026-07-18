from flask import Flask, request, jsonify, render_template
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/download', methods=['POST'])
def download_video():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"success": False, "error": "URL missing!"}), 400
        
    video_url = data['url'].strip()
    
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'cachedir': False,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            stream_url = info.get('url')
            title = info.get('title', 'Downloaded_Video')
            thumbnail = info.get('thumbnail', '')
            duration = info.get('duration', 0)
            
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            duration_str = f"{minutes:02d}:{seconds:02d}"
            
            if not stream_url:
                formats = info.get('formats', [])
                for f in reversed(formats):
                    if f.get('vcodec') != 'none' and f.get('url'):
                        stream_url = f.get('url')
                        break

            if stream_url:
                return jsonify({
                    "success": True,
                    "title": title,
                    "download_url": stream_url,
                    "thumbnail": thumbnail,
                    "duration": duration_str,
                    "source": "YouTube" if "youtube.com" in video_url or "youtu.be" in video_url else "Instagram"
                })
            else:
                return jsonify({"success": False, "error": "Direct stream not found."}), 400
                
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
