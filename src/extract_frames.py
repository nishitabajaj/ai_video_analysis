import cv2
import os

def extract_frames(video_path, output_dir, fps=1):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    vidcap = cv2.VideoCapture(video_path)
    video_fps = vidcap.get(cv2.CAP_PROP_FPS)

    if not vidcap.isOpened():
        print(f"[!] Error: Cannot open video file: {video_path}")
        return

    interval = int(video_fps // fps) if video_fps >= fps else 1

    count = 0
    saved = 0
    while True:
        success, image = vidcap.read()
        if not success:
            break

        if count % interval == 0:
            filename = os.path.join(output_dir, f"frame_{saved:04d}.jpg")
            cv2.imwrite(filename, image)
            print(f"[+] Saved {filename}")
            saved += 1
        count += 1

    vidcap.release()
    print(f"✅ Done: {saved} frames saved.")

if __name__ == "__main__":
    video_path = "input_video/screen_recording.mp4"
    output_dir = "frames"
    extract_frames(video_path, output_dir, fps=1)