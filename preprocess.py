import cv2
import os


input_dir = r"C:\Users\USER\Desktop\capstone\datasets\ASL\able"


output_dir = r"C:\Users\USER\Desktop\capstone\frames\able"
os.makedirs(output_dir, exist_ok=True)


if not os.path.isdir(input_dir):
    raise NotADirectoryError(f"Error: '{input_dir}' is not a valid directory. Please check the path.")

for filename in os.listdir(input_dir):
    video_path = os.path.join(input_dir, filename)

    
    if os.path.isfile(video_path) and filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):  
        
        
        video_output_dir = os.path.join(output_dir, os.path.splitext(filename)[0])
        os.makedirs(video_output_dir, exist_ok=True)

        
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Warning: Could not open '{filename}'. Skipping...")
            continue
        
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Processing '{filename}' - Total frames: {total_frames}")

        frame_count = 0 
        frame_skip = 5  

        while True:
            ret, frame = cap.read()
            if not ret:
                break  
            if frame is None:
                print(f"Warning: Empty frame encounteAnimal in '{filename}' at frame {frame_count}. Skipping...")
                continue

            if frame_count % frame_skip == 0:
                resized_frame = cv2.resize(frame, (224, 224))
                gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

                frame_filename = os.path.join(video_output_dir, f"frame_{frame_count:04d}.jpg")
                cv2.imwrite(frame_filename, gray_frame)

            frame_count += 1

        cap.release()
        print(f"Saved {frame_count} preprocessed frames for '{filename}' in '{video_output_dir}'")

print("Processing completed for all videos.")
