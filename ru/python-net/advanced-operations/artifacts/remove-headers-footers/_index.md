---
title: Удаление верхних и нижних колонтитулов из PDF на Python
linktitle: Удаление колонтитулов
type: docs
weight: 110
url: /ru/python-net/remove-headers-footers/
description: Удалить артефакты заголовка и нижнего колонтитула с первой страницы PDF в Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление верхних и нижних колонтитулов из PDF на Python
Abstract: Удалить артефакты заголовка и нижнего колонтитула с первой страницы PDF в Python.
---

Удалить артефакты заголовка и нижнего колонтитула с первой страницы PDF в Python.

## Удаление артефактов колонтитулов

Соберите артефакты пагинации с подтипом `HEADER` или `FOOTER` перед удалением.

```python
import aspose.pdf as ap

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## См. также

- [Добавление колонтитулов](/pdf/ru/python-net/artifacts-header-footer/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
