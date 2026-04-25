# 🖐 GestureCtrl — Camera Laptop Controller

Control your laptop with hand gestures via your webcam. No hardware needed.

---

## 🚀 Quick Start

### Option A — VS Code Live Server (recommended)
1. Open this folder in VS Code
2. Install the **Live Server** extension (Ritwick Dey)
3. Right-click `index.html` → **Open with Live Server**
4. Click **▶ START TRACKING** and allow camera access

### Option B — Any local server
```bash
# Python
python -m http.server 8080

# Node (npx)
npx serve .

# Then open http://localhost:8080
```

> ⚠️ Must be served over HTTP/HTTPS (not opened as a file://). Camera API requires a server.

---

## 🖐 Gesture Reference

| Gesture | Action | Mode |
|---|---|---|
| 🖐 Open Palm | Move mouse cursor | Mouse |
| 🤏 Pinch (thumb + index) | Left click | Mouse |
| ✊ Closed Fist | Play / Pause | Media |
| 👍 Thumbs Up | Volume Up | Media |
| 👎 Thumbs Down | Volume Down | Media |
| ✌️ Victory / Peace | Next Track | Media |
| ☝️ Index finger up | Scroll Up | Scroll |
| 👇 Pinky finger down | Scroll Down | Scroll |

---

## ⚙️ Settings (in the sidebar)

- **Mouse / Media / Scroll** — toggle each control mode on/off
- **Show skeleton** — see hand landmark overlay on camera feed
- **Mouse sensitivity** — how fast cursor tracks your hand (0.5× to 3.0×)
- **Gesture cooldown** — time between repeated action fires (300–2000ms)

---

## 🧠 How It Works

Uses **MediaPipe Hands** (Google's ML model) in the browser to:
1. Detect your hand landmarks (21 points per hand) in real-time
2. Classify which gesture you're making using fingertip geometry
3. Fire keyboard/media events or track your index finger for mouse control

No data leaves your browser. Everything runs locally on your GPU/CPU.

---

## 🔧 Extending / Hacking

All gesture logic is in `index.html`:

- `classifyGesture(landmarks)` — add new gesture patterns here
- `executeGestureAction(gesture, landmarks)` — map gestures to actions here
- MediaPipe settings at `hands.setOptions({ ... })` — tune detection sensitivity

### Add a custom gesture
```js
// In classifyGesture():
if (index && middle && ring && !thumb && !pinky) return 'three_fingers';

// In executeGestureAction():
three_fingers: () => { addLog('Screenshot', 'three_fingers'); /* your action */ }
```

---

## 📦 Dependencies (CDN — no install needed)

- `@mediapipe/hands` — hand landmark detection
- `@mediapipe/camera_utils` — webcam abstraction
- `@mediapipe/drawing_utils` — skeleton rendering
- Google Fonts — JetBrains Mono, Space Grotesk

---

## 💡 Tips

- **Good lighting** dramatically improves tracking accuracy
- Hold your hand **30–60 cm** from camera for best results
- Use a **plain background** behind your hand
- The skeleton overlay helps you see what the model detects
- Adjust **cooldown** if gestures fire too fast or too slow

---

Made with ❤️ and MediaPipe
