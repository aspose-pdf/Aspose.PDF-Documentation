---
title: Добавить фоны PDF в Python
linktitle: Добавление фонов
type: docs
weight: 20
url: /ru/python-net/add-backgrounds/
description: Узнайте, как добавить изображение фона на страницы PDF в Python, используя класс BackgroundArtifact в Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить фон в PDF с помощью Python
Abstract: Эта статья рассматривает использование фоновых изображений в PDF‑документах с помощью Aspose.PDF for Python via .NET. В ней подчеркивается возможность добавлять водяные знаки или тонкие дизайны в документы, используя класс `BackgroundArtifact`, который позволяет встраивать фоновые изображения в отдельные объекты страниц. В статье приведён практический пример кода, демонстрирующий, как реализовать эту функцию. Процесс включает создание нового PDF‑документа, добавление страницы, создание объекта `BackgroundArtifact`, установку фонового изображения и добавление фонового артефакта в коллекцию артефактов страницы. В конце изменённый документ сохраняется в виде PDF‑файла. Эта техника позволяет улучшить визуальное представление PDF‑документов.
---

## Добавить фоновое изображение в PDF

Фоновые изображения могут использоваться для добавления водяного знака или другого тонкого дизайна в документы. В Aspose.PDF for Python via .NET каждый PDF‑документ представляет собой набор страниц, а каждая страница содержит набор артефактов. The [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) класс может использоваться для добавления фонового изображения к объекту страницы.

Этот подход полезен, когда необходимо разместить декоративное изображение за основным содержимым PDF без преобразования его в поисковый текст документа.

Следующий фрагмент кода показывает, как добавить фоновое изображение к страницам PDF, используя объект BackgroundArtifact с Python.

1. Загрузите документ PDF.
1. Создайте фоновой артефакт.
1. Загрузите файл изображения.
1. Присоедините артефакт к странице.
1. Сохраните обновлённый документ.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Добавить фоновое изображение с непрозрачностью в PDF

Добавить полупрозрачное фоновое изображение на страницу PDF с использованием Aspose.PDF for Python.

Применяя непрозрачность, фоновое изображение становится частично прозрачным, позволяя оригинальному содержимому страницы (текст, изображения и т.д.) оставаться чётко видимым. Это особенно полезно для:

- Водяные знаки
- Брендовые наложения
- Тонкие улучшения дизайна

Фон добавляется как артефакт, гарантируя, что он остаётся позади всего содержимого страницы.

1. Загрузите документ PDF.
1. Создайте фоновой артефакт.
1. Загрузите файл изображения.
1. Установите уровень непрозрачности.
1. Присоедините артефакт к странице.
1. Сохраните обновлённый документ.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Добавить цвет фона в PDF

Применить сплошной цвет фона к странице PDF с использованием Aspose.PDF for Python.

1. Загрузите документ PDF.
1. Создайте фоновой артефакт.
1. Установить цвет фона.
1. Присоедините артефакт к странице.
1. Сохраните обновлённый документ.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Удалить фон из PDF

Удалить артефакты фона со страницы PDF с помощью Aspose.PDF for Python.
Фоновые элементы в PDF часто хранятся как артефакты, и этот метод выборочно идентифицирует и удаляет только те артефакты, которые классифицированы как фоновые элементы.

1. Загрузите документ PDF.
1. Получить доступ к артефактам страницы.
1. Отфильтровать фоновые артефакты.
1. Соберите фоновые элементы.
1. Удалите фоновые артефакты.
1. Сохраните обновлённый документ.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

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

## Связанные темы артефактов

- [Работа с PDF-артефактами в Python](/pdf/ru/python-net/artifacts/)
- [Добавить водяные знаки в PDF на Python](/pdf/ru/python-net/add-watermarks/)
- [Добавить нумерацию Бейтса в PDF на Python](/pdf/ru/python-net/add-bates-numbering/)
- [Подсчитать типы артефактов в PDF‑файлах](/pdf/ru/python-net/counting-artifacts/)