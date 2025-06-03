import os
import json
from datetime import timedelta

def generate_mock_json(frames_dir, output_json_path, fps=1):
    frames = sorted([f for f in os.listdir(frames_dir) if f.endswith('.jpg')])
    logs = []

    for idx, frame_name in enumerate(frames):
        timestamp = round(idx * (1 / fps), 1)  # seconds
        log = {
            "timestamp": timestamp,
            "user_activity": f"Frame captured from video",
            "screen_info": f"Image file: {frame_name}",
            "llm_description": f"Simulated description for {frame_name}"
        }
        logs.append(log)

    with open(output_json_path, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"✅ JSON log written to {output_json_path} with {len(logs)} entries.")

if __name__ == "__main__":
    frames_dir = "frames"
    output_json_path = "logs/video_analysis_mock.json"
    generate_mock_json(frames_dir, output_json_path)