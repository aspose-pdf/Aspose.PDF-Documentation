---
title: Подсчёт артефактов пагинации в PDF на Python
linktitle: Подсчёт артефактов по подтипам
type: docs
weight: 40
url: /ru/python-net/counting-artifacts/
description: Подсчитать водяные знаки, фоны, заголовки и нижние колонтитулы по подтипу артефактов пагинации на странице PDF в Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подсчёт артефактов пагинации в PDF на Python
Abstract: Подсчитать артефакты пагинации на странице PDF, чтобы проверить наличие водяных знаков, фонов, заголовков и нижних колонтитулов.
---

Подсчитать артефакты пагинации на странице PDF, чтобы проверить наличие водяных знаков, фонов, заголовков и нижних колонтитулов.

## Подсчёт артефактов пагинации на странице

Отфильтруйте коллекцию `artifacts` первой страницы по типу `PAGINATION` и подсчитайте артефакты каждого подтипа. Если артефактов подтипа нет, пример выводит ноль.

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## См. также

- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
- [Извлечение текста и границ водяных знаков](/pdf/ru/python-net/extract-watermarks/)
- [Удаление водяных знаков](/pdf/ru/python-net/remove-watermarks/)
- [Удаление фона](/pdf/ru/python-net/remove-backgrounds/)
- [Удаление колонтитулов](/pdf/ru/python-net/remove-headers-footers/)
