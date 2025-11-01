# Spotify Playlist/Track Downloader

A simple and efficient Python script that allows you to download your favorite music from Spotify. This tool uses **[spotDL](https://github.com/spotDL/spotify-downloader)** to download songs, albums, or playlists directly from Spotify in high-quality MP3 format.

## Features

- Download individual tracks from Spotify
- Download entire playlists
- Download complete albums
- Automatic metadata and artwork embedding
- Organized file structure
- High-quality audio output

## Requirements

- Windows 10/11
- Python 3.9 or higher
- Internet connection
- Spotify account (free or premium)

## Installation Steps

### 1. Install FFmpeg

FFmpeg is required for audio conversion. Install it using Windows Package Manager:

```powershell
winget install --id Gyan.FFmpeg -e --source winget
```

**Note about Windows PATH**: After installing FFmpeg via winget, you might need to restart your terminal or add FFmpeg to PATH manually for it to be recognized immediately.

### 2. Install spotDL

Install the spotDL package using pip:

```powershell
pip install spotdl
```

### 3. Run the Script

Execute the script using Python:

```powershell
python main.py
```

## Usage

1. Launch the script
2. Enter your Spotify URL when prompted
3. Wait for the download to complete
4. Find your downloaded music in the output directory

Supported URL formats:
- Track: `https://open.spotify.com/track/...`
- Album: `https://open.spotify.com/album/...`
- Playlist: `https://open.spotify.com/playlist/...`

## Important Notes

- Ensure you have sufficient storage space for downloads
- A stable internet connection is recommended
- Downloaded files are for personal use only
- Respect copyright laws and Spotify's terms of service

## Troubleshooting

If you encounter any issues:

1. Verify that FFmpeg is properly installed
2. Check your Python version (`python --version`)
3. Ensure all dependencies are up to date
4. Verify your internet connection
5. Check if the Spotify URL is valid