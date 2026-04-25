from flask import Flask, request
from flask_cors import CORS
import pyautogui
import time

app = Flask(__name__)
CORS(app)

# Safety settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.005

last_gesture_time = 0
COOLDOWN = 0.8

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

@app.route('/gesture', methods=['POST'])
def handle_gesture():
    global last_gesture_time
    
    now = time.time()
    data = request.get_json()
    gesture = data.get('gesture')
    
    if not gesture:
        return {"status": "error", "message": "No gesture provided"}, 400

    # Mouse movement has no cooldown
    if gesture == "mouse_move":
        if 'x' in data and 'y' in data:
            x = data['x']
            y = data['y']
            pyautogui.moveTo(x, y, _pause=False)
        return {"status": "ok", "gesture": gesture}

    # Cooldown protection for all other gestures
    if now - last_gesture_time < COOLDOWN:
        return {"status": "cooldown", "remaining": COOLDOWN - (now - last_gesture_time)}
    
    last_gesture_time = now

    # Execute gesture actions
    if gesture == "left_click":
        pyautogui.click(button='left')
        print("[✓] Left Click")
        
    elif gesture == "right_click":
        pyautogui.click(button='right')
        print("[✓] Right Click")
        
    elif gesture == "play_pause":
        pyautogui.press('playpause')
        print("[✓] Play/Pause")
        
    elif gesture == "volume_up":
        pyautogui.press('volumeup')
        print("[✓] Volume Up")
        
    elif gesture == "volume_down":
        pyautogui.press('volumedown')
        print("[✓] Volume Down")
        
    elif gesture == "next_track":
        pyautogui.press('nexttrack')
        print("[✓] Next Track")
        
    elif gesture == "scroll_up":
        pyautogui.scroll(120)
        print("[✓] Scroll Up")
        
    elif gesture == "scroll_down":
        pyautogui.scroll(-120)
        print("[✓] Scroll Down")

    return {"status": "ok", "gesture": gesture}

if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════╗
║     GESTURE CTRL - LAPTOP CONTROL SERVER      ║
╠═══════════════════════════════════════════════╣
║  ✅ Running on:  http://localhost:5000        ║
║  ✅ Screen:     {}x{}                     ║
║  ✅ Cooldown:   {}ms                        ║
║                                               ║
║  Now open index.html and click START TRACKING ║
╚═══════════════════════════════════════════════╝
    """.format(SCREEN_WIDTH, SCREEN_HEIGHT, int(COOLDOWN*1000)))
    
    app.run(port=5000, debug=False, quiet=True)