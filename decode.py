import cv2
import numpy as np
import sys
import os


def decode_video(input_video, output_file, validation_file):
    cap = cv2.VideoCapture(input_video)
    bytes_data = bytearray()
    validation_data = bytearray()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        avg_intensity = int(np.mean(frame))  # 计算图像平均强度
        bytes_data.append(avg_intensity)
        validation_data.append(1 if avg_intensity >= 128 else 0)  # 简单有效性检查

    cap.release()
    with open(output_file, 'wb') as f:
        f.write(bytes_data)
    with open(validation_file, 'wb') as f:
        f.write(validation_data)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: decode <input_video> <output_file> <validation_file>")
        sys.exit(1)

    input_video = sys.argv[1]
    output_file = sys.argv[2]
    validation_file = sys.argv[3]

    decode_video(input_video, output_file, validation_file)