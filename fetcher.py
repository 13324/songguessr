import yt_dlp
import json
import re
import os

YOUTUBE_PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLoaTDHRuxwgxk0WTXRJJJlXUYuHBSrbcF"
PLAYLIST_JS_PATH = "playlist.js"

def load_existing_playlist():
    if not os.path.exists(PLAYLIST_JS_PATH):
        return []
    with open(PLAYLIST_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        match = re.search(r"const playlist = (\[.*\]);", content, re.DOTALL)
        if match:
            js_array = match.group(1)
            try:
                # Convert JS array to JSON
                js_array_json = js_array.replace("id", "\"id\"").replace("title", "\"title\"")
                return json.loads(js_array_json)
            except Exception as e:
                print("⚠️ Fehler beim Parsen der existierenden playlist.js:", e)
    return []

def save_playlist(entries):
    with open(PLAYLIST_JS_PATH, "w", encoding="utf-8") as f:
        f.write("const playlist = [\n")
        for e in entries:
            f.write(f'  {{ id: "{e["id"]}", title: "{e["title"]}" }},\n')
        f.write("];\n")
    print(f"✅ {len(entries)} Videos in {PLAYLIST_JS_PATH} gespeichert.")

existing = load_existing_playlist()
existing_ids = {e["id"] for e in existing}
new_entries = []

# Step 1: get flat video list
print("📡 Lade YouTube-Playlist ...")
ydl_opts = {
    "quiet": True,
    "extract_flat": True,
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(YOUTUBE_PLAYLIST_URL, download=False)
    video_entries = info.get("entries", [])

# Step 2: get full metadata (title) per new video
for entry in video_entries:
    video_id = entry.get("id")
    if video_id in existing_ids:
        continue
    try:
        data = yt_dlp.YoutubeDL({"quiet": True}).extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
        title = data.get("title", video_id)
        new_entries.append({ "id": video_id, "title": title })
        print(f"➕ {video_id} - {title}")
    except Exception as e:
        print(f"⚠️ Fehler bei {video_id}: {e}")

# Step 3: merge & write
all_entries = existing + new_entries
save_playlist(all_entries)
