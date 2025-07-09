from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>  
<html lang="en">  
<head>  
  <meta charset="UTF-8">  
  <title>Public Server By Faiizu</title>  
  <link href="https://fonts.cdnfonts.com/css/mona-sans" rel="stylesheet">  
  <style>  
    @import url("https://fonts.cdnfonts.com/css/mona-sans");  
    * {  
      box-sizing: border-box;  
      -webkit-font-smoothing: antialiased;  
      text-rendering: optimizeLegibility;  
      scroll-behavior: smooth;  
    }  
    html, body {  
      overflow-x: hidden;  
      margin: 0;  
      background: linear-gradient(180deg, #343434 0%, #252525 100%);  
      font-family: "Mona Sans", sans-serif;  
    }  

    body {  
      display: flex;  
      flex-direction: column;  
      align-items: center;  
      padding-top: 80px;  
      gap: 60px;  
    }  

    .card {  
      position: relative;  
      width: 320px;  
      height: 500px;  
      border-radius: 16px;  
      background: linear-gradient(180deg, #292929aa 0%, #191919cc 50%);  
      backdrop-filter: blur(4px);  
      box-shadow: inset 0 2px 2px 0 #e7c4a088, inset 0 -2px 2px 0 #0003;  
      color: #ccc;  
      text-shadow: 1px 1px 3px #333a;  
      padding: 24px;  
      padding-right: 42px;  
      display: flex;  
      flex-direction: column;  
      justify-content: end;  
    }  

    .card h2, .card p {  
      margin: 8px 0;  
    }  

    .card h2 {  
      font-size: 1.1em;  
    }  

    .card p {  
      font-size: 0.9em;  
      font-weight: 800;  
      color: #aaa;  
    }  

    .card a.button {  
      text-decoration: none;  
      color: #fff;  
      width: fit-content;  
      border-radius: 100px;  
      padding: 8px 36px;  
      margin-top: 12px;  
      background: #fff2;  
      box-shadow:  
        0 0 0 1px #fff3,  
        inset 120px 0 100px -100px #000c,  
        0 0 0 0 #fff1;  
      transition: box-shadow 0.4s ease-in-out;  
      cursor: pointer;  
      display: inline-block;  
    }  

    .card a.button:hover {  
      box-shadow:  
        0 0 0 1px #fff3,  
        inset 200px 0px 100px -100px #000a,  
        -4px 0 8px 2px #fff2;  
    }  

    .card img {  
      position: absolute;  
      top: 32px;  
      left: 0;  
      right: 0;  
      width: 80%;  
      margin: auto;  
      object-fit: contain;  
      user-select: none;  
      pointer-events: none;  
    }  
    
    /* Offline message styles */  
    #offline-message {  
      display: none;  
      position: fixed;  
      top: 0;  
      left: 0;  
      width: 100%;  
      height: 100%;  
      background: linear-gradient(180deg, #343434 0%, #252525 100%);  
      z-index: 1000;  
      flex-direction: column;  
      justify-content: center;  
      align-items: center;  
      text-align: center;  
      color: #fff;  
      font-family: "Mona Sans", sans-serif;  
    }  
    
    #offline-message .wifi-icon {  
      width: 60px;  
      height: 60px;  
      margin-bottom: 20px;  
    }  
    
    #offline-message h1 {  
      font-size: 24px;  
      margin-bottom: 10px;  
    }  
    
    #offline-message p {  
      font-size: 16px;  
      color: #aaa;  
      max-width: 300px;  
    }  
  </style>  
</head>  
<body>  

  <!-- First Card -->  
  <div class="card">  
    <img src="https://raw.githubusercontent.com/Faiizuxd/Prvt-pblic-dpz/refs/heads/main/08f8bf4c1077187b0cb468a9c5c7a0c9.jpg" alt="">  
    <h2>Public Server By Faiizu</h2>  
    <p>The Power Full Tools in This Server Made Aura By [ Awiiso ]</p>  
    <a class="button" href="https://gangster-2-0.onrender.com/300.com" target="_blank">Get Started</a>  
  </div>  

  <!-- Second Card -->  
  <div class="card">  
    <img src="https://raw.githubusercontent.com/Faiizuxd/The_Faizu_dpz/refs/heads/main/399bbed38a87aa72d19877e638df7be9.jpg" alt="">  
    <h2>Private Server</h2>  
    <p>The Power Full Tools By Awiiso in This Server Made Aura By [ Faiizu ]</p>  
    <a class="button" href="https://gangster-2-0.onrender.com/" target="_blank">Get Started</a>  
  </div>  
    
  <!-- Offline Message -->  
  <div id="offline-message">  
    <svg class="wifi-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">  
      <path d="M5 12.55a11 11 0 0 1 14.08 0"></path>  
      <path d="M1.42 9a16 16 0 0 1 21.16 0"></path>  
      <path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path>  
      <line x1="12" y1="20" x2="12.01" y2="20"></line>  
    </svg>  
    <h1>Hi Dear User</h1>  
    <p>Please connect to the internet and try again</p>  
  </div>  

  <script>  
    // Check online/offline status  
    function updateOnlineStatus() {  
      const msg = document.getElementById('offline-message');  
      if (navigator.onLine) {  
        msg.style.display = 'none';  
      } else {  
        msg.style.display = 'flex';  
      }  
    }  

    updateOnlineStatus();  
    window.addEventListener('online', updateOnlineStatus);  
    window.addEventListener('offline', updateOnlineStatus);  
  </script>  
</body>  
</html>
'''

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
