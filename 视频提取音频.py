from moviepy.editor import VideoFileClip


def extract_audio_from_mp4(video_path, output_audio_path=None):
    """
    从MP4视频中提取音频并保存为MP3
    :param video_path: 输入视频的完整路径
    :param output_audio_path: 输出音频路径（不传则自动生成同名MP3）
    """
    try:
        # 自动生成同名MP3路径（如果没手动指定）
        if output_audio_path is None:
            # 把.mp4后缀替换成.mp3
            output_audio_path = video_path.replace('.mp4', '.mp3')

        # 加载视频
        video = VideoFileClip(video_path)
        # 提取音频
        audio = video.audio
        # 保存为MP3
        audio.write_audiofile(output_audio_path)
        # 释放资源
        audio.close()
        video.close()
        print(f"✅ 音频提取完成！\n输入文件：{video_path}\n输出文件：{output_audio_path}")
    except Exception as e:
        print(f"❌ 提取失败，错误信息：{e}")


# ========== 直接用你提供的路径 ==========
if __name__ == "__main__":
    # 你的MP4文件完整路径
    INPUT_VIDEO = r"C:\Users\战神\Desktop\PPT\lv_0_20260421203151.mp4"
    # 不手动指定输出路径，自动生成同名MP3
    extract_audio_from_mp4(INPUT_VIDEO)
