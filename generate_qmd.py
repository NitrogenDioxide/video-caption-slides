import json

import typer

HEADER_TEMPLATE = """---
title: {title}
slide_subtitle: {subtitle}
format:
  revealjs:
    transition: slide
    theme: simple
    css: custom.css
    background-transition: fade
    transition-speed: fast
    smaller: true
    controls: true
    slide-number: true
    loop: true
---
"""


SECTION_TEMPLATE = """
##  {{data-menu-title="{data_menu_title}"}}

<video data-autoplay muted loop controls src="{video_path}"></video>

::: {{.scroll-container}}

{caption}

:::"""


def main(
    slide_title: str = "Example Video Captions",
    slide_subtitle: str = "",
    video_data_file: str = "video_data.jsonl",
    output_file: str = "slides.qmd",
):
    with open(video_data_file, "r") as f:
        video_data = [json.loads(line) for line in f]

    with open(output_file, "w") as f:
        print(HEADER_TEMPLATE.format(title=slide_title), file=f)

        for video in video_data:
            print(
                SECTION_TEMPLATE.format(
                    data_menu_title=video["file"].split("/")[-1],
                    video_path=video["file"],
                    caption=video["caption"],
                ),
                file=f,
            )


if __name__ == "__main__":
    typer.run(main)
