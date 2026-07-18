from flask import Flask, request, jsonify, render_template_string
import requests
import os

app = Flask(__name__)

# Premium UI with Monetag Ad Integrated
HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ NextGen Premium Downloader | YT & Insta</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); }
        .glass-card { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); }
    </style>

    <!-- MONETAG AD TAG INTEGRATED -->
    <script src="https://quge5.com/88/tag.min.js" data-zone="232482" async data-cfasync="false"></script>
</head>
<body class="text-slate-100 min-h-screen font-sans flex flex-col justify-between">

    <div class="w-full text-center py-2 bg-slate-900/60 border-b border-slate-800 text-xs tracking-wider text-slate-400">
        <div class="inline-block bg-slate-800/40 px-4 py-1 rounded text-[10px]">ADVERTISEMENT SPACE</div>
    </div>

    <main class="container mx-auto px-4 py-12 flex-grow flex flex-col items-center justify-center max-w-2xl">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-extrabold tracking-tight bg-gradient-to-r from-cyan-400 via-indigo-400 to-purple-400 bg-clip-text text-transparent sm:text-5xl mb-3">
                StreamGrab Pro
            </h1>
            <p class="text-slate-400 text-sm sm:text-base">Download High-Speed Video Content Instantly</p>
        </div>

        <div class="w-full glass-card rounded-2xl p-6 sm:p-8 shadow-2xl relative overflow-hidden">
            <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-cyan-500 via-indigo-500 to-purple-500"></div>
            
            <div class="space-y-4">
                <div class="relative">
                    <span class="absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
                        <i class="fa-solid fa-link text-lg"></i>
                    </span>
                    <input type="text" id="mediaUrl" placeholder="Paste YouTube or Instagram link here..." class="w-full pl-11 pr-4 py-3.5 bg-slate-950/60 border border-slate-700/60 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-all duration-200 text-sm sm:text-base">
                </div>

                <button onclick="processMediaLink()" id="btnText" class="w-full bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white font-semibold py-3.5 px-4 rounded-xl shadow-lg shadow-indigo-900/40 transition-all duration-200 flex items-center justify-center space-x-2">
                    <i class="fa-solid fa-circle-down"></i>
                    <span>Fetch Media Stream</span>
                </button>
            </div>

            <div id="loader" class="hidden mt-8 text-center py-6">
                <div class="inline-block animate-spin rounded-full h-8 w-8 border-4 border-indigo-500 border-t-transparent mb-3"></div>
                <p id="loaderText" class="text-slate-400 text-xs animate-pulse">Scanning global bypass array...</p>
            </div>

            <div id="errorMessage" class="hidden mt-6 bg-red-950/40 border border-red-800/60 text-red-300 px-4 py-3 rounded-xl text-sm flex items-center space-x-2">
                <i class="fa-solid fa-circle-exclamation text-red-400"></i>
                <span id="errText">Failed to resolve media string.</span>
            </div>

            <div id="resultCard" class="hidden mt-8 border-t border-slate-800 pt-6">
                <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
                    <img id="resThumb" src="https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=200" alt="Thumbnail" class="w-full sm:w-36 h-24 object-cover rounded-lg border border-slate-700/50 bg-slate-900">
                    <div class="flex-1 flex flex-col justify-between">
                        <div>
                            <span id="resSource" class="text-[10px] font-bold tracking-widest uppercase bg-indigo-950 text-indigo-300 border border-indigo-800 px-2 py-0.5 rounded-full">SUCCESS</span>
                            <h3 id="resTitle" class="text-sm font-semibold text-slate-200 line-clamp-2 mt-1.5">Link Decrypted Successfully</h3>
                        </div>
                    </div>
                </div>

                <a id="resDlLink" href="" target="_blank" rel="noopener noreferrer" class="mt-4 w-full bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold py-3 px-4 rounded-xl text-center block shadow-lg">
                    <i class="fa-solid fa-download mr-1.5"></i> Download Instantly
                </a>
            </div>
        </div>
    </main>

    <footer class="w-full text-center py-6 border-t border-slate-900 bg-slate-950/40 text-xs text-slate-500">
        <p>&copy; 2026 StreamGrab Network. Powered by Hyper-Resilient Mirror Routing.</p>
    </footer>

    <script>
        async function processMediaLink() {
            const urlInput = document.getElementById('mediaUrl').value.trim();
            const btn = document.getElementById('btnText');
            const loader = document.getElementById('loader');
            const errCard = document.getElementById('errorMessage');
            const resCard = document.getElementById('resultCard');

            if (!urlInput) return alert("Please paste a URL first!");

            errCard.classList.add('hidden');
            resCard.classList.add('hidden');
            loader.classList.remove('hidden');
            btn.disabled = true;

            try {
                const response = await fetch('/api/download', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url: urlInput })
                });
                const data = await response.json();
                
                if (data.success) {
                    document.getElementById('resTitle').innerText = data.title;
                    document.getElementById('resSource').innerText = data.source;
                    document.getElementById('resDlLink').href = data.download_url;
                    resCard.classList.remove('hidden');
                } else {
                    showError(data.error || "All endpoints congested. Re-fetch in 5 seconds.");
                }
            } catch (err) {
                showError("Server Connection Interrupted. Try again.");
            } finally {
                loader.classList.add('hidden');
                btn.disabled = false;
            }
        }
        function showError(msg) {
            document.getElementById('errText').innerText = msg;
            document.getElementById('errorMessage').classList.remove('hidden');
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
        return jsonify({"success": False, "error": "URL missing!"}), 400
        
    video_url = data['url'].strip()
    
    # Massive Pool of Open Global Cobalt API Mirrors
    bypass_nodes = [
        "https://cobalt.moe",
        "https://cobalt.bndkt.me",
        "https://cobalt.lewd.tech",
        "https://api.cobalt.lol",
        "https://cobalt.perennialte.ch",
        "https://cobalt.api.kwiatecka.xyz",
        "https://cobalt.q67.me",
        "https://co.wuk.sh",
        "https://api.cobalt.tools"
    ]
    
    # Spoofed Desktop Browser Headers to completely trick firewalls & prevent rate-limiting
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Origin": "https://cobalt.tools",
        "Referer": "https://cobalt.tools/",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    payload = {
        "url": video_url,
        "videoQuality": "720",
        "downloadMode": "video"
    }

    # Brute force rotation logic
    for index, node in enumerate(bypass_nodes):
        try:
            endpoint = node if node.endswith('/') else f"{node}/"
            
            # Fast aggressive timeout (4 seconds per node)
            response = requests.post(endpoint, json=payload, headers=headers, timeout=4)
            
            if response.status_code == 200:
                res_data = response.json()
                status = res_data.get("status")
                
                if status in ["stream", "redirect"]:
                    return jsonify({
                        "success": True,
                        "title": res_data.get("title", "Decrypted Stream"),
                        "download_url": res_data.get("url"),
                        "source": "YouTube" if "youtu" in video_url else "Instagram"
                    })
                elif status == "picker":
                    picker_items = res_data.get("picker", [])
                    if picker_items:
                        return jsonify({
                            "success": True,
                            "title": res_data.get("title", "Multi-Stream Content"),
                            "download_url": picker_items[0].get("url"),
                            "source": "Media Stream"
                        })
            
            # If current node fails or returns non-200, log silently and cycle to next
            print(f"Node {index} ({node}) bypassed with status code: {response.status_code}")
            continue
            
        except Exception as e:
            print(f"Node {index} timed out or failed. Error: {str(e)}")
            continue
            
    return jsonify({"success": False, "error": "All premium cloud filters are actively rate-limiting this video right now. Please re-fetch in a few moments."}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
    
