---
title: Подсчёт артефактов определённого типа в Python через .NET
linktitle: Подсчёт артефактов
type: docs
weight: 40
url: /ru/python-net/counting-artifacts/
description: В этой статье показано, как проверять артефакты разметки в PDF‑документе с помощью Aspose.PDF для Python через .NET.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подсчёт артефактов в PDF с использованием Python
Abstract: Артефакты разметки, такие как водяные знаки, фоны, верхние и нижние колонтитулы, часто используются в PDF‑документах для обеспечения структуры, брендинга и идентификации. В этом примере показано, как программно проверять и подсчитывать эти артефакты с помощью Aspose.PDF для Python через .NET. Фильтруя артефакты на странице и группируя их по подтипу, разработчики могут быстро анализировать состав документа и проверять наличие конкретных элементов. Предоставленный код демонстрирует, как открыть PDF, извлечь артефакты разметки с первой страницы, подсчитать каждый подтип и вывести результаты, предлагая практический подход к аудиту и проверке документов.
---

## Подсчёт артефактов определённого типа

Проверьте и подсчитайте артефакты разметки в PDF‑[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с помощью Aspose.PDF для Python через .NET. Артефакты разметки включают такие элементы, как водяные знаки, фоны, верхние и нижние колонтитулы, которые применяются к страницам для оформления и целей идентификации. Фильтруя объекты [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) на [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) и группируя их по подтипу (`Artifact.ArtifactSubtype`), разработчики могут быстро анализировать структуру документа и проверять наличие конкретных элементов.

Чтобы посчитать общее количество артефактов определённого типа (например, общее число водяных знаков), используйте следующий код. В примере коллекция [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы (это [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) фильтруется по [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties), а затем подсчитываются подтипы (`Artifact.ArtifactSubtype`).

1. Откройте PDF‑документ (см. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Отфильтруйте артефакты разметки, используя коллекцию [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы.
1. Подсчитайте артефакты по подтипу (`Artifact.ArtifactSubtype`).
1. Выведите результаты.

```python

import aspose.pdf as ap

def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(1 for artifact in pagination_artifacts 
                         if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)
        backgrounds = sum(1 for artifact in pagination_artifacts 
                          if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)
        headers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)
        footers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```

