from flask import Flask, request, jsonify, render_template_string
import requests
import re
import os

app = Flask(__name__)

# Premium Ultra-Fast UI with Automated Client-Side Failover Engine
HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ StreamGrab Pro - Premium Multi-Engine Downloader</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body { background: linear-gradient(135deg, #090d16 0%, #111428 100%); }
        .glass-card { background: rgba(22, 28, 45, 0.8); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.05); }
        .glow-btn { box-shadow: 0 0 25px rgba(6, 182, 212, 0.35); }
    </style>

    <!-- MONETAG AD INTEGRATION -->
    <script src="https://quge5.com/88/tag.min.js" data-zone="232482" async data-cfasync="false"></script>
</head>
<body class="text-slate-200 min-h-screen font-sans flex flex-col justify-between">

    <div class="w-full text-center py-2 bg-slate-950/80 border-b border-slate-900 text-xs text-slate-500">
        <div class="inline-block bg-slate-900/60 px-4 py-1 rounded text-[10px]">ADVERTISEMENT SPACE</div>
    </div>

    <main class="container mx-auto px-4 py-12 flex-grow flex flex-col items-center justify-center max-w-2xl">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-black tracking-wider bg-gradient-to-r from-cyan-400 via-teal-400 to-indigo-400 bg-clip-text text-transparent sm:text-5xl mb-2 uppercase">
                StreamGrab Pro
            </h1>
            <p class="text-slate-400 text-xs tracking-widest uppercase">Decentralized High-Speed Media Extractor</p>
        </div>

        <div class="w-full glass-card rounded-2xl p-6 sm:p-8 shadow-2xl relative overflow-hidden">
            <div class="absolute top-0 left-0 w-full h-[3px] bg-gradient-to-r from-cyan-400 via-indigo-500 to-purple-500"></div>
            
            <div class="space-y-4">
                <div class="relative">
                    <span class="absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-500">
                        <i class="fa-solid fa-link text-lg"></i>
                    </span>
                    <input type="text" id="mediaUrl" placeholder="Paste YouTube Shorts, Video or Reel link..." class="w-full pl-11 pr-4 py-4 bg-slate-950 border border-slate-800 rounded-xl text-white placeholder-slate-600 focus:outline-none focus:border-cyan-500 transition-all duration-200 text-sm sm:text-base">
                </div>

                <button onclick="startExtraction()" id="btnText" class="w-full bg-gradient-to-r from-cyan-600 via-teal-600 to-indigo-600 hover:opacity-95 text-white font-black py-4 px-4 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 glow-btn">
                    <i class="fa-solid fa-circle-notch id-icon"></i>
                    <span>DOWNLOAD NOW (HIGH SPEED)</span>
                </button>
            </div>

            <!-- Loader View -->
            <div id="loader" class="hidden mt-8 text-center py-6">
                <div class="inline-block animate-spin rounded-full h-9 w-9 border-4 border-cyan-400 border-t-transparent mb-3"></div>
                <p id="loaderText" class="text-slate-400 text-xs tracking-wider animate-pulse">Initializing cloud decryption pipeline...</p>
            </div>

            <!-- Result Matrix -->
            <div id="resultCard" class="hidden mt-8 border-t border-slate-900 pt-6">
                <div class="bg-slate-950/60 p-4 rounded-xl border border-slate-900 mb-4">
                    <span class="text-[10px] font-black tracking-widest uppercase bg-cyan-950 text-cyan-400 border border-cyan-900 px-2.5 py-0.5 rounded-md">DECRYPTED</span>
                    <h3 id="resTitle" class="text-sm font-bold text-slate-300 mt-2">Media File Ready For Extraction</h3>
                </div>

                <!-- Anti-Ad Confusion Warning to keep revenue clean -->
                <p class="text-[11px] text-amber-400 bg-amber-950/30 border border-amber-950 px-3 py-2.5 rounded-lg text-center mb-4">
                    ⚠️ <b>Note:</b> First click may open a sponsor tab due to active script load. Close that tab immediately and click the button again to instantly save the file!
                </p>

                <a id="resDlLink" href="" target="_blank" rel="noopener noreferrer" class="w-full bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-black py-4 px-4 rounded-xl text-center block tracking-wider shadow-lg">
                    <i class="fa-solid fa-download mr-1.5"></i> SAVE TO DEVICE
                </a>
            </div>
        </div>
    </main>

    <footer class="w-full text-center py-6 border-t border-slate-950 bg-slate-950/40 text-[10px] text-slate-600 tracking-widest uppercase">
        <p>&copy; 2026 StreamGrab Cloud Network. Powered by Private Layer Protocols.</p>
    </footer>

    <script>
        // Extracting Video ID helper
        function getYoutubeId(url) {
            const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|shorts\/|watch\?v=|\&v=)([^#\&\?]*).*/;
            const match = url.match(regExp);
            return (match && match[2].length === 11) ? match[2] : null;
        }

        async function startExtraction() {
            const urlInput = document.getElementById('mediaUrl').value.trim();
            const loader = document.getElementById('loader');
            const resCard = document.getElementById('resultCard');
            const loaderText = document.getElementById('loaderText');

            if (!urlInput) return alert("Please enter a valid link!");

            resCard.classList.add('hidden');
            loader.classList.remove('hidden');
            
            // STEP 1: Server Side Processing Request
            loaderText.innerText = "Querying production cloud servers...";
            try {
                const response = await fetch('/api/download', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url: urlInput })
                });
                const data = await response.json();
                
                if (data.success) {
                    showFinalLink(data.title, data.download_url);
                    return;
                }
            } catch (e) { console.log("Server pipeline blocked. Engaging Client-Side Engine..."); }

            // STEP 2: CLIENT-SIDE DIRECT BYPASS (If server IP is rate-limited by YouTube)
            loaderText.innerText = "Bypassing data-center blocks via Native Client Network...";
            
            const ytId = getYoutubeId(urlInput);
            if (ytId) {
                // Hitting highly-resilient public API endpoint directly from user IP
                const clientApi = `https://api.savetube.me/download/video/${ytId}`;
                try {
                    const clientRes = await fetch(clientApi);
                    const clientData = await clientRes.json();
                    if (clientData && clientData.status === true && clientData.data) {
                        // Picking highest quality progressive available stream
                        const streamUrl = clientData.data.video_formats['720p'] || clientData.data.video_formats['360p'] || Object.values(clientData.data.video_formats)[0];
                        if (streamUrl) {
                            showFinalLink(clientData.data.title || "Decrypted YouTube Short", streamUrl);
                            return;
                        }
                    }
                } catch(err) { console.log("Client cluster engine drop."); }
            }

            // STEP 3: MASTER UNFAILING FAILOVER GATEWAY (Like vidssave professional mirror routing)
            const backupGateway = `https://9xbuddy.xyz/process?url=${encodeURIComponent(urlInput)}`;
            showFinalLink("Universal Backup Link Generated", backupGateway);
        }

        function showFinalLink(title, dlUrl) {
            document.getElementById('loader').classList.add('hidden');
            document.getElementById('resTitle').innerText = title;
            document.getElementById('resDlLink').href = dlUrl;
            document.getElementById('resultCard').classList.remove('hidden');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_UI)

@app.route('/api/download', methods=['POST'])
def download_video():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"success": False, "error": "Target parameter empty"}), 400
        
    video_url = data['url'].strip()
    
    # Direct internal extraction from a highly stable multi-format public engine
    try:
        # Parsing YouTube links directly via Savetube backend architecture relay
        video_id_match = re.search(r'(?:v=|\/shorts\/|\/embed\/|\/vi\/|youtu\.be\/|v\/|e\/|shorts|embed|video\/)([^#\&\?]*).', video_url)
        if video_id_match:
            vid_id = video_id_match.group(1)[:11]
            api_target = f"https://api.savetube.me/download/video/{vid_id}"
            response = requests.get(api_target, headers={"User-Agent": "Mozilla/5.0"}, timeout=4)
            if response.status_code == 200:
                res_json = response.json()
                if res_json.get("status") is True:
                    formats = res_json.get("data", {}).get("video_formats", {})
                    dl_url = formats.get("720p") or formats.get("360p") or list(formats.values())[0]
                    return jsonify({
                        "success": True,
                        "title": res_json.get("data", {}).get("title", "Decrypted Media"),
                        "download_url": dl_url
                    })
    except Exception:
        pass

    # Standard Cobalt Cluster fallbacks for general social formats (Instagram/Twitter)
    fallback_nodes = ["https://co.wuk.sh", "https://cobalt.moe", "https://api.cobalt.lol"]
    for node in fallback_nodes:
        try:
            endpoint = node if node.endswith('/') else f"{node}/"
            res = requests.post(endpoint, json={"url": video_url}, headers={"Accept": "application/json", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}, timeout=3)
            if res.status_code == 200:
                r_data = res.json()
                if r_data.get("status") in ["stream", "redirect"]:
                    return jsonify({"success": True, "title": r_data.get("title", "Decrypted Stream"), "download_url": r_data.get("url")})
        except Exception:
            continue

    return jsonify({"success": False, "error": "Switching to native engine..."}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
    
