import os
import json
import time
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_frame_with_gemini(image_path):
    image = Image.open(image_path)
    response = model.generate_content([
        "Briefly describe the key user action and the most important aspect of the screen state in this image. Keep it concise and focus on what's immediately relevant. For example: 'The user is typing in a search bar.', or 'The screen shows a login page.'",
        image
    ])
    return response.text

def main():
    frames_dir = "frames"
    output_path = "logs/video_analysis_real.json"
    frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])
    logs = []
    fps = 1

    for idx, frame_name in enumerate(frames):
        timestamp = round(idx / fps, 1)
        frame_path = os.path.join(frames_dir, frame_name)
        print(f"Analyzing {frame_name} at {timestamp}s...")
        description = analyze_frame_with_gemini(frame_path)

        log = {
            "timestamp": timestamp,
            "user_activity": "User action detected",
            "screen_info": f"Screen state from {frame_name}",
            "llm_description": description,
        }
        logs.append(log)
        time.sleep(1)

    with open(output_path, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"Real analysis JSON saved to {output_path}")

if __name__ == "__main__":
    main()