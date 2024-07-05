# video-caption-slides
Some snippets to use Quarto to create a slide deck for visualizing videos

## Usage 

1. Update `video_data.jsonl` with the path to videos and the corresponding captsions.
2. Execute `python generate_qmd.py`
3. Then run `quarto render slides.qmd`

To check the generated webpage, open `slides.html` in a browser.
