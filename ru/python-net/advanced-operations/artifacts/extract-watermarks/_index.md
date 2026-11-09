---
title: Извлечение текста и границ водяных знаков в PDF на Python
linktitle: Извлечение текста и границ водяных знаков
type: docs
weight: 50
url: /ru/python-net/extract-watermarks/
description: Прочитайте текст и ограничивающий прямоугольник артефактов водяного знака на первой странице PDF с помощью Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение текста и границ водяных знаков в PDF на Python
Abstract: Прочитайте текст и ограничивающий прямоугольник артефактов водяного знака на первой странице PDF с помощью Python.
---

Прочитайте текст и ограничивающий прямоугольник артефактов водяного знака на первой странице PDF с помощью Python.

## Извлечение текста и границ водяных знаков

Выведите текст и ограничивающий прямоугольник каждого артефакта пагинации с подтипом `WATERMARK`.

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## См. также

- [Добавление водяных знаков](/pdf/ru/python-net/add-watermarks/)
- [Удаление водяных знаков](/pdf/ru/python-net/remove-watermarks/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
