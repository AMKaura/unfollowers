
# FollowSifter

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyScript](https://img.shields.io/badge/PyScript-7C3AED?style=flat-square)
![Open Source](https://img.shields.io/badge/Open_Source-22C55E?style=flat-square)
![Status](https://img.shields.io/badge/Status-In_Development-F59E0B?style=flat-square)

**Find out who doesn't follow you back on Instagram.**

A free, open-source Instagram following analyzer built with Python and PyScript. No Instagram login required.

---

## 🔎 Overview

FollowSifter compares your Instagram followers and following lists to identify accounts that don't follow you back.

Simply export your Instagram data, run the application locally, and see the results in your browser.

## 🚀 Getting Started

### Prerequisites

- Python installed on your computer
- Instagram followers and following data exported in JSON format
- A modern web browser

### Installation

**1. Clone or download the repository.**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Export your Instagram data.**

Download your *Followers and Following* information from Instagram. Select **All time** as the date range and **JSON** as the format.

[Instagram's official export instructions](https://help.instagram.com/181231772500920/)

**3. Add your JSON files.**

Place `followers_1.json` and `following.json` in the repository's root directory.

**4. Start the local server.**

Open a terminal in the project directory and run:

```bash
py -m http.server 8000 --bind 127.0.0.1
```

**5. Launch FollowSifter.**

Open the following address in your browser:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 🎬 Video Walkthrough

![Work In Progress](https://img.shields.io/badge/Video_Tutorial-Work_in_Progress-F59E0B?style=flat-square)

*The installation and usage walkthrough is currently in production. Coming soon!*

---

## ⚙️ How It Works

1. **Read** — Loads your exported Instagram JSON files.
2. **Compare** — Uses Python dictionary lookups to identify non-mutual follows.
3. **Display** — Shows matching usernames and their Instagram profile links.

The comparison algorithm runs in linear time, **O(n + m)**, where *n* and *m* represent the sizes of your following and followers lists.

## 📌 Important Notes

- Results may include deactivated or renamed accounts due to outdated information in Instagram's exports.
- FollowSifter identifies accounts that don't follow you back, not necessarily accounts that previously unfollowed you.
- Never commit your personal Instagram export files to GitHub.
- The current local version serves JSON files through your development server. Run it only on a trusted computer.

---

**Built with Python, PyScript, and a little curiosity.**