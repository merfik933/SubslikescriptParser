
# SubslikescriptParser

SubslikescriptParser is a Python script for scraping movie transcripts from [subslikescript.com](https://subslikescript.com). It collects transcripts for movies starting with the letter "A" and saves each transcript as a separate text file.

## Features

- Scrapes movie transcript links from the "A" movies section.
- Downloads and saves each transcript to a `.txt` file named after the movie title.
- Handles pagination (currently set to the first 5 pages).
- Gracefully skips broken or unavailable links.

## Requirements

- Python 3.7+
- See [requirements.txt](requirements.txt) for required packages:
  - beautifulsoup4
  - requests
  - lxml

## Installation

1. Clone the repository or download the script.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script with Python:

```
python main.py
```

Transcripts will be saved as `.txt` files in the current directory, each named after the corresponding movie.

## How it Works

1. The script fetches the list of movies starting with "A" from subslikescript.com.
2. It iterates through the first 5 pages of results.
3. For each movie link found, it:
   * Requests the transcript page.
   * Extracts the movie title and transcript.
   * Saves the transcript to a text file.
   * Waits 1 second between requests to avoid overloading the server.
4. If a link is broken or a transcript cannot be fetched, it prints a warning and continues.

## Notes

* The script currently processes only the first 5 pages for demonstration. You can increase the range in the code to scrape more pages.
* Filenames are based on movie titles; special characters in titles may cause issues on some filesystems.
* Use responsibly and respect the website's terms of service.

## License

This project is for educational purposes.
