---
title: Добавление фона в PDF на Python
linktitle: Добавление фона
type: docs
weight: 20
url: /ru/python-net/add-backgrounds/
description: Добавить изображения и одноцветные фоны на страницы PDF в Python и отрегулировать непрозрачность фонового изображения.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление фона в PDF на Python
Abstract: Добавить изображения и одноцветные фоны на страницы PDF в Python и отрегулировать непрозрачность фонового изображения.
---

Использовать `BackgroundArtifact` для размещения изображения или сплошного цвета за содержимым страницы PDF. Эти примеры изменяют первую страницу.

## Добавление фонового изображения в PDF

Передайте поток изображения в свойство `background_image` и добавьте артефакт на страницу.

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Настройка непрозрачности фонового изображения

Передайте той же функции значение непрозрачности от 0 до 1. Для полупрозрачного изображения укажите `0.5`.

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## Добавление сплошного фона в PDF

Задайте свойство `background_color`, чтобы установить однотонный фон.

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## См. также

- [Удаление фона](/pdf/ru/python-net/remove-backgrounds/)
- [Работа с PDF-артефактами](/pdf/ru/python-net/artifacts/)
