---
title: Работа с фоновыми изображениями как артефактами с помощью Python
linktitle: Добавление фонов
type: docs
weight: 20
url: /ru/python-net/add-backgrounds/
description: Добавьте фоновое изображение в ваш PDF‑файл с помощью Python. Используйте класс BackgroundArtifact.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить фон в PDF с помощью Python
Abstract: В этой статье рассматривается использование фоновых изображений в PDF‑документах с помощью Aspose.PDF for Python via .NET. Отмечается возможность добавлять водяные знаки или легкие дизайны в документы путем использования класса `BackgroundArtifact`, который позволяет внедрять фоновые изображения в отдельные объекты страниц. В статье приводится практический пример кода, демонстрирующий, как реализовать эту функцию. Процесс включает создание нового PDF‑документа, добавление страницы, создание объекта `BackgroundArtifact`, установку фонового изображения и добавление фонового артефакта в коллекцию артефактов страницы. В конце изменённый документ сохраняется как PDF‑файл. Эта техника позволяет улучшить визуальное оформление PDF‑документов.
---

Фоновые изображения можно использовать для добавления водяного знака или другого тонкого дизайна в документы. В Aspose.PDF for Python via .NET каждый PDF‑документ представляет собой коллекцию страниц, а каждая страница содержит коллекцию артефактов. Класс [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) можно использовать для добавления фонового изображения к объекту страницы.

Следующий фрагмент кода показывает, как добавить фоновое изображение на страницы PDF с использованием объекта BackgroundArtifact в Python.

```python

import aspose.pdf as ap
import io

def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```


