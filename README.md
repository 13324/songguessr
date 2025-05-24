# 🎧 SongGuessr

**A retro-style, two-player music guessing game — fast, fun, and loud.**

SongGuessr is an arcade-inspired browser game that lets two players compete to identify random songs from a YouTube playlist. Perfect for parties, team-building, or just flexing your music knowledge. No points for knowing the lyrics — only speed and song recognition count.

## 🚀 Features

- 🎮 2-player buzzer gameplay (Player 1: `S`, Player 2: `K`)
- 🔊 Embedded YouTube playback with randomized start time
- 🎵 Manual reveal and scoring for full arcade drama
- 💾 Local playlist-based, no backend required
- 🕹 Retro aesthetic with animated background and pixel font

## 🛠 How to Play

1. Press **START ROUND** to begin.
2. A random song starts playing.
3. Players buzz in by pressing `S` (Player 1) or `K` (Player 2).
4. Use the buttons to reveal the title and assign points.
5. Play the next round!

## 🎯 Controls

| Action              | Key/Button          |
|---------------------|---------------------|
| Start round         | `START ROUND` / `Space` |
| Buzz in             | `S` (Player 1), `K` (Player 2) |
| Reveal title        | `REVEAL TITLE` |
| Award points        | `✅ CORRECT` / `❌ WRONG` |
| Skip round          | `SKIP ROUND` |
| Next round          | `NEXT ROUND` / `Space` |

## 📁 Folder Structure

```
.
├── index.html          # Main game interface
├── playlist.js         # Your custom list of songs (YouTube video IDs & titles)
├── static/
│   ├── buzzer.mp3      # Buzzer sound
│   └── hmmm.mp3        # Thinking sound
└── README.md           # This file
```

## 🧠 Requirements

- Modern web browser
- Internet connection (for YouTube playback)

## 📝 Customization

To add your own songs:

1. Edit `playlist.js` with a list of objects like:
```js
const playlist = [
  { id: "dQw4w9WgXcQ", title: "Rick Astley - Never Gonna Give You Up" },
  { id: "Zi_XLOBDo_Y", title: "a-ha - Take On Me" },
  // ...
];
```

2. Place it in the root folder with `index.html`.

## 🌐 Hosting

You can host this game on:

- GitHub Pages
- Any static file server (e.g., Netlify, Vercel, nginx)
- Local browser via `file://`

## 📦 Setup with Git

```bash
git clone https://github.com/YOUR_USERNAME/songguessr.git
cd songguessr
open index.html
```

## 📜 License

MIT License — do what you want, just don't sue us.

---

Game on. 🎶
