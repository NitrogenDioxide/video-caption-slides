import json

import typer

HEADER_TEMPLATE = """---
title: {title}
slide_subtitle: {subtitle}
format:
  revealjs:
    transition: slide
    theme: simple
    background-transition: fade
    transition-speed: fast
    smaller: true
    scrollable: true
    width: 100%
    height: 100%
    controls: true
    slide-number: true
    loop: true
---
"""


SECTION_TEMPLATE = """
##  {{data-menu-title="{data_menu_title}"}}

<video data-autoplay muted loop controls src="{video_path}"></video>

{caption}
"""

SECTION_WITH_TABS_TEMPLATE = """
##  {{data-menu-title="{data_menu_title}"}}

<video data-autoplay muted loop controls src="{video_path}"></video>

::: {{.panel-tabset}}
{caption_tabs}
:::
"""

SECTION_TAB_TEMPLATE = """
### {model_name}

{caption}
"""


def main(
    slide_title: str = "Example Video Captions",
    slide_subtitle: str = "",
    video_data_file: str = "video_data.jsonl",
    output_file: str = "slides.qmd",
):
    with open(video_data_file, "r") as f:
        video_data = [json.loads(line) for line in f]

    with open(output_file, "w") as f:
        print(
            HEADER_TEMPLATE.format(title=slide_title, subtitle=slide_subtitle), file=f
        )

        for video in video_data:
            caption = video["caption"]
            if isinstance(caption, dict):
                caption_tabs = ""
                for model_name, model_caption in caption.items():
                    caption_tabs += SECTION_TAB_TEMPLATE.format(
                        model_name=model_name, caption=model_caption
                    )
                print(
                    SECTION_WITH_TABS_TEMPLATE.format(
                        data_menu_title=video["file"].split("/")[-1],
                        video_path=video["file"],
                        caption_tabs=caption_tabs,
                    ),
                    file=f,
                )

            else:
                print(
                    SECTION_TEMPLATE.format(
                        data_menu_title=video["file"].split("/")[-1],
                        video_path=video["file"],
                        caption=caption,
                    ),
                    file=f,
                )


if __name__ == "__main__":
    typer.run(main)
