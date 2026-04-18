# Bandcamp Release ID Extractor

Extracts the release ID and image from a Bandcamp album or track URL and optionally downloads the cover image.

## Usage

```
bandcamp <url> [--no-image]
```

| Argument | Description |
|---|---|
| `url` | Bandcamp album or track URL |
| `--no-image` | Skip downloading the cover image |
| `-h`, `--help` | Show help |

## Examples

```bash
# Extract ID and download cover
bandcamp https://logicmoon.bandcamp.com/album/sun

# Extract ID only
bandcamp https://logicmoon.bandcamp.com/album/sun --no-image
```

The cover image is saved in the current directory as `cover_artist_title.jpg`.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourname/bandcamp-id.git
cd bandcamp-id
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make the script executable and add it to your PATH:

```bash
chmod +x bandcamp
export PATH="$PATH:/path/to/bandcamp-id"
```

> If needed, update the Python path in the first line of `./bandcamp` to match your system (`which python3`).

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`
