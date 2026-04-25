import asyncio
import websockets
import pyautogui
import json
import logging

# Configure pyautogui for safety
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

connected_clients = set()

async def handle_connection(websocket):
    logger.info("✅ Client connected")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                action = data.get('action')
                
                if action == 'mouse_move':
                    x = data.get('x')
                    y = data.get('y')
                    pyautogui.moveTo(x, y, _pause=False)
                
                elif action == 'left_click':
                    pyautogui.click(button='left')
                    logger.info("🖱️ Left click")
                
                elif action == 'right_click':
                    pyautogui.click(button='right')
                    logger.info("🖱️ Right click")
                
                elif action == 'volume_up':
                    pyautogui.press('volumeup')
                    logger.info("🔊 Volume Up")
                
                elif action == 'volume_down':
                    pyautogui.press('volumedown')
                    logger.info("🔉 Volume Down")
                
                elif action == 'play_pause':
                    pyautogui.press('playpause')
                    logger.info("⏯ Play/Pause")
                
                elif action == 'next_track':
                    pyautogui.press('nexttrack')
                    logger.info("⏭ Next Track")
                
                elif action == 'scroll_up':
                    pyautogui.scroll(100)
                    logger.info("⬆ Scroll Up")
                
                elif action == 'scroll_down':
                    pyautogui.scroll(-100)
                    logger.info("⬇ Scroll Down")
                
            except Exception as e:
                logger.error(f"Error processing message: {e}")
                
    finally:
        connected_clients.remove(websocket)
        logger.info("❌ Client disconnected")

async def main():
    logger.info(f"""
╔════════════════════════════════════════════╗
║     GESTURE CTRL - SYSTEM CONTROL SERVER   ║
╠════════════════════════════════════════════╣
║  Running on ws://localhost:8765           ║
║  Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}                ║
║  Press Ctrl+C to stop                     ║
╚════════════════════════════════════════════╝
    """)
    
    async with websockets.serve(handle_connection, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("\nServer stopped")