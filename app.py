from flask import Flask, request, jsonify, render_template_string
import requests
import re
import os

app = Flask(__name__)

# Premium Self-Contained UI with Client-Side Direct Decryption
HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ StreamGrab Pro - Premium Downloader</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body { background: linear-gradient(135deg, #090d16 0%, #111428 100%); }
        .glass-card { background: rgba(22, 28, 45, 0.8); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.05); }
    </style>

    <!-- MONETAG AD TAG INTEGRATION -->
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

                <button onclick="startExtraction()" id="btnText" class="w-full bg-gradient-to-r from-cyan-600 via-teal-600 to-indigo-600 hover:opacity-95 text-white font-black py-4 px-4 rounded-xl transition-all duration-200 flex items-center justify-center space-x-2 shadow-lg shadow-cyan-950">
                    <i class="fa-solid fa-bolt"></i>
                    <span>DOWNLOAD NOW (HIGH SPEED)</span>
                </button>
            </div>

            <!-- Enhanced Status Loader -->
            <div id="loader" class="hidden mt-8 text-center py-6">
                <div class="inline-block animate-spin rounded-full h-9 w-9 border-4 border-cyan-400 border-t-transparent mb-3"></div>
                <p id="loaderText" class="text-slate-400 text-xs tracking-wider animate-pulse">Bypassing data-center restrictions...</p>
            </div>

            <!-- Result Box (Everything Happens Here) -->
            <div id="resultCard" class="hidden mt-8 border-t border-slate-900 pt-6">
                <div class="bg-slate-950/60 p-4 rounded-xl border border-slate-900 mb-4">
                    <span class="text-[10px] font-black tracking-widest uppercase bg-cyan-950 text-cyan-400 border border-cyan-900 px-2.5 py-0.5 rounded-md">DECRYPTED SUCCESSFULLY</span>
                    <h3 id="resTitle" class="text-sm font-bold text-slate-300 mt-2">Your High-Speed Download Stream Is Ready</h3>
                </div>

                <!-- Guidance for Monetag Ads -->
                <p class="text-[11px] text-amber-400 bg-amber-950/30 border border-amber-900/30 px-3 py-2.5 rounded-lg text-center mb-4">
                    ⚠️ <b>Note:</b> First click will trigger a sponsor ad tab. Just close that tab immediately, come back here, and click the button a second time to save your video!
                </p>

                <a id="resDlLink" href="" target="_blank" rel="noopener noreferrer" class="w-full bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-black py-4 px-4 rounded-xl text-center block tracking-wider shadow-lg">
                    <i class="fa-solid fa-download mr-1.5"></i> SAVE TO DEVICE NOW
                </a>
            </div>
        </div>
    </main>

    <footer class="w-full text-center py-6 border-t border-slate-950 bg-slate-950/40 text-[10px] text-slate-600 tracking-widest uppercase">
        <p>&copy; 2026 StreamGrab Cloud Network. All Rights Reserved.</p>
    </footer>

    <script>
        // Clean client-side regex extraction for full YouTube strings and clipped inputs
        function getYoutubeId(url) {
            const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|shorts\/|watch\?v=|\&v=)([^#\&\?]*).*/;
            const match = url.match(regExp);
            if (match && match[2]) {
                return match[2].substring(0, 11);
            }
            return null;
        }

        async function startExtraction() {
            const urlInput = document.getElementById('mediaUrl').value.trim();
            const loader = document.getElementById('loader');
            const resCard = document.getElementById('resultCard');
            const loaderText = document.getElementById('loaderText');

            if (!urlInput) return alert("Please paste a valid video URL!");

            resCard.classList.add('hidden');
            loader.classList.remove('hidden');
            
            // Step 1: Client-Side Direct Phone Internet Extraction (Bypasses Render Block)
            const ytId = getYoutubeId(urlInput);
            if (ytId) {
                loaderText.innerText = "Connecting to high-speed client nodes using your native IP...";
                
                // Testing direct public endpoints with open CORS policies right from the browser
                const clientApis = [
                    `https://api.savetube.me/download/video/${ytId}`,
                    `https://api.cobalt.lol/`
                ];

                try {
                    const response = await fetch(clientApis[0]);
                    const jsonRes = await response.json();
                    if (jsonRes && jsonRes.status === true && jsonRes.data) {
                        const directUrl = jsonRes.data.video_formats['720p'] || jsonRes.data.video_formats['360p'] || Object.values(jsonRes.data.video_formats)[0];
                        if (directUrl) {
                            showFinalLink(jsonRes.data.title || "Decrypted YouTube Stream", directUrl);
                            return;
                        }
                    }
                } catch(err) { console.log("Client cluster node 1 skipped."); }

                // Client-side Direct Cobalt Processing Call
                try {
                    const cobaltRes = await fetch("https://api.cobalt.lol", {
                        method: "POST",
                        headers: { "Accept": "application/json", "Content-Type": "application/json" },
                        body: JSON.stringify({ url: urlInput })
                    });
                    const cobaltData = await cobaltRes.json();
                    if (cobaltData && cobaltData.url) {
                        showFinalLink(cobaltData.title || "Decrypted Short Stream", cobaltData.url);
                        return;
                    }
                } catch(e) { console.log("Client cluster node 2 skipped."); }
            }

            // Step 2: Server-Side Processing Relay (Fallback)
            loaderText.innerText = "Routing payload through global backup server array...";
            try {
                const srvResponse = await fetch('/api/download', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url: urlInput })
                });
                const srvData = await srvResponse.json();
                if (srvData.success) {
                    showFinalLink(srvData.title, srvData.download_url);
                    return;
                }
            } catch(e) { console.log("Server fallback pipeline exhausted."); }

            // Step 3: Clean web portal backup redirect (NO MORE 9XBUDDY WHITE SCREEN)
            loaderText.innerText = "Finalizing secure conversion layout...";
            const cleanBackup = `https://en.savefrom.net/1-youtube-video-downloader-4v8.html?url=${encodeURIComponent(urlInput)}`;
            showFinalLink("Universal Secure Extraction Gateway", cleanBackup);
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
        return jsonify({"success": False, "error": "Empty tracking target"}), 400
        
    video_url = data['url'].strip()
    
    # Fast Server-side backup loop for general items
    fallback_nodes = ["https://co.wuk.sh", "https://cobalt.moe", "https://api.cobalt.lol"]
    for node in fallback_nodes:
        try:
            endpoint = node if node.endswith('/') else f"{node}/"
            res = requests.post(endpoint, json={"url": video_url}, headers={"Accept": "application/json", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}, timeout=3)
            if res.status_code == 200:
                r_data = res.json()
                if r_data.get("status") in ["stream", "redirect"]:
                    return jsonify({"success": True, "title": r_data.get("title", "Decrypted Server Stream"), "download_url": r_data.get("url")})
        except Exception:
            continue

    return jsonify({"success": False, "error": "Server proxy busy, processing via client network."}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
    
