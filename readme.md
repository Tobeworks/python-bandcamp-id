Here's a sample `README.md` file for this script:

# Bandcamp Release ID Extractor

A command-line tool to extract the release ID from a Bandcamp album URL.

## Usage

```
bandcamp --url [your bandcamp url]
```

## Example

```
bandcamp --url https://logicmoon.bandcamp.com/album/sun
```

## Requirements

- Python 3.7 or higher
- `bandcamp_scraper` module

## Installation

1. Clone the repository or download the script.
2. Install the required modules by running the following command:

```
pip install -r requirements.txt
```

3. Make the script executable:

```
chmod +x bandcamp
```

4. Add the location of the script to your PATH environment variable so that it can be run from anywhere in the terminal:

```
export PATH="$PATH:/path/to/script"
```

## Contributing

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.