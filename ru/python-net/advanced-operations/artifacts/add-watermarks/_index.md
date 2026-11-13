---
title: Добавление водяных знаков в PDF на Python
linktitle: Добавление водяных знаков
type: docs
weight: 30
url: /ru/python-net/add-watermarks/
description: Добавить стилизованные текстовые артефакты водяных знаков на страницы PDF в Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление водяных знаков в PDF на Python
Abstract: Добавить стилизованные текстовые артефакты водяных знаков на страницы PDF в Python.
---

Использовать `WatermarkArtifact` добавить текстовый водяной знак на первую страницу PDF.

## Добавление артефакта водяного знака

Установите текст и стиль, затем настройте выравнивание, вращение и непрозрачность. Установите `is_background` разместить водяной знак за содержимым страницы.

```python
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)
```

## См. также

- [Извлечение текста и границ водяных знаков](/pdf/ru/python-net/extract-watermarks/)
- [Удаление водяных знаков](/pdf/ru/python-net/remove-watermarks/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
