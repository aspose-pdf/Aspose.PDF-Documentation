---
title: Удаление фона из PDF на Python
linktitle: Удаление фона
type: docs
weight: 80
url: /ru/python-net/remove-backgrounds/
description: Удалить артефакты фона с первой страницы PDF в Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление фона из PDF на Python
Abstract: Удалить артефакты фона с первой страницы PDF в Python.
---

Удалить артефакты фона с первой страницы PDF в Python.

## Удаление артефактов фона

Соберите артефакты пагинации с подтипом `BACKGROUND` перед удалением.

```python
import aspose.pdf as ap

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## См. также

- [Добавление фона](/pdf/ru/python-net/add-backgrounds/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
