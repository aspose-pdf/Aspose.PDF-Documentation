---
title: Удаление водяных знаков из PDF на Python
linktitle: Удаление водяных знаков
type: docs
weight: 90
url: /ru/python-net/remove-watermarks/
description: Удалить артефакты водяных знаков с первой страницы PDF в Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление водяных знаков из PDF на Python
Abstract: Удалить артефакты водяных знаков с первой страницы PDF в Python.
---

Удалить артефакты водяных знаков с первой страницы PDF в Python.

## Удаление артефактов водяных знаков

Пример удаляет с первой страницы только артефакты типа `PAGINATION` и подтипа `WATERMARK`. Видимые водяные знаки, сохранённые в виде обычного текста страницы, изображений или аннотаций, остаются в PDF.

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## См. также

- [Добавление водяных знаков](/pdf/ru/python-net/add-watermarks/)
- [Извлечение текста и границ водяных знаков](/pdf/ru/python-net/extract-watermarks/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
