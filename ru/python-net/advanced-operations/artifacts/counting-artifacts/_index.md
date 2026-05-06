---
title: Подсчёт артефактов PDF на Python
linktitle: Подсчёт артефактов
type: docs
weight: 40
url: /ru/python-net/counting-artifacts/
description: Узнайте, как просматривать и подсчитывать артефакты разметки страниц в PDF‑документах с помощью Python и Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Подсчёт артефактов в PDF с использованием Python
Abstract: Артефакты разметки страниц, такие как водяные знаки, фоны, заголовки и колонтитулы, обычно используются в PDF‑документах для обеспечения структуры, брендинга и идентификации. Этот пример демонстрирует, как программно просматривать и подсчитывать эти артефакты с помощью Aspose.PDF for Python via .NET. Фильтруя артефакты на странице и группируя их по подтипу, разработчики могут быстро анализировать состав документа и проверять наличие определённых элементов. Приведённый код иллюстрирует, как открыть PDF, извлечь артефакты разметки страниц с первой страницы, подсчитать каждый подтип и вывести результаты, предлагая практический подход к аудиту и проверке документов.
---

## Подсчёт артефактов определённого типа

Проверьте и подсчитайте артефакты пагинации в PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя Aspose.PDF for Python via .NET. Артефакты пагинации включают такие элементы, как водяные знаки, фон, заголовки и нижние колонтитулы, которые применяются к страницам для целей оформления и идентификации. Фильтруя [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) объекты на [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) и группируя их по подтипу (`Artifact.ArtifactSubtype`), разработчики могут быстро проанализировать структуру документа и проверить наличие конкретных элементов.

Чтобы вычислить общее количество артефактов определённого типа (например, общее число водяных знаков), используйте следующий код. Пример фильтрует страницу [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) коллекция (an [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) по [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) а затем подсчитывает подтипы (`Artifact.ArtifactSubtype`).

1. Откройте PDF-документ (см [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Отфильтруйте артефакты пагинации, используя страницу [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) коллекцию.
1. Подсчитайте артефакты по подтипу (`Artifact.ArtifactSubtype`).
1. Выведите результаты.

```python

from os import path
from collections import Counter
import sys
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

## Связанные темы артефактов

- [Работа с PDF-артефактами в Python](/pdf/ru/python-net/artifacts/)
- [Добавить водяные знаки в PDF на Python](/pdf/ru/python-net/add-watermarks/)
- [Добавить фон PDF в Python](/pdf/ru/python-net/add-backgrounds/)
- [Добавить нумерацию Бейтса в PDF на Python](/pdf/ru/python-net/add-bates-numbering/)
