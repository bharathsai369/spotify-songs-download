import cmd
import os
import subprocess

def check_ffmpeg():
    """Check and install ffmpeg if not available"""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("✅ FFmpeg is already installed.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚙️ Installing FFmpeg via winget...")
        subprocess.run(["winget", "install", "--id", "Gyan.FFmpeg", "-e", "--source", "winget"], check=True)

def install_spotdl():
    """Install spotdl using pip"""
    try:
        __import__('spotdl')
        print("✅ spotDL is already installed.")
    except ImportError:
        print("⚙️ Installing spotDL...")
        subprocess.run(["pip", "install", "--upgrade", "spotdl"], check=True)

def main():
    print("\n🎵 Spotify Downloader (spotDL)")
    print("Enter either a single track URL or a playlist/album URL.\n")

    url = input("🔗 Enter Spotify URL: ").strip()
    if not url:
        print("❌ URL cannot be empty.")
        return

    print("\n📥 Downloading... please wait.\n")
    command = ["spotdl", url]
    try:
        subprocess.run(command, check=True)
        print("\n✅ Download complete!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Download failed: {e}")

if __name__ == "__main__":
    check_ffmpeg()
    install_spotdl()
    main()
