import cv2
import numpy as np
import os
import sys


def generate_random_binary_file(file_name, size):
    with open(file_name, 'wb') as f:
        f.write(os.urandom(size))


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: encode <input_file> <output_video> <duration_ms>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_video = sys.argv[2]
    duration_ms = int(sys.argv[3])

    # 生成随机二进制文件
    generate_random_binary_file(input_file, 1024)  # 1KB

    # 生成图像
    with open(input_file, 'rb') as f:
        data = f.read()
        images = []
        for byte in data:
            img = np.zeros((50, 50, 3), dtype=np.uint8)
            img[:, :] = (byte, byte, byte)  # 用字节值生成灰度图
            images.append(img)

        # 保存图像
        for index, img in enumerate(images):
            cv2.imwrite(f"frame_{index:04d}.png", img)

    # 调用FFMPEG将图像转换为视频
    os.system(f"ffmpeg -framerate 30 -i frame_%04d.png -c:v libx264 -pix_fmt yuv420p {output_video}")

    # 清理临时图像文件
    for index in range(len(images)):
        os.remove(f"frame_{index:04d}.png")