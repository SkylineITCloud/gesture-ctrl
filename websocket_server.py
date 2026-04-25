import asyncio
import websockets
import json
import pyautogui

# Safety settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.005

async def handler(websocket):
    print("✅ Client connected")
    try:
        async for message in websocket:
            data = json.loads(message)
            gesture = data.get("gesture")

            if gesture == "left_click":
                pyautogui.click()
                print("[✓] Left Click")
                
            elif gesture == "right_click":
                pyautogui.click(button='right')
                print("[✓] Right Click")
                
            elif gesture == "mouse_move":
                if 'x' in data and 'y' in data:
                    x = data['x']
                    y = data['y']
                    pyautogui.moveTo(x, y, _pause=False)
                    
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

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        print("❌ Client disconnected")

print("GESTURE CTRL - WEBSOCKET SERVER")
print("Running on:  ws://localhost:8765")
print("Now open index.html and click START TRACKING")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
