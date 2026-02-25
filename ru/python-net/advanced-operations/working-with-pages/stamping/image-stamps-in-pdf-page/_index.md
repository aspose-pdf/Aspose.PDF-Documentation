---
title: Добавление штампов‑изображений в PDF с помощью Python
linktitle: Штампы‑изображения в PDF-файле
type: docs
weight: 10
url: /ru/python-net/image-stamps-in-pdf-page/
description: Добавьте штамп‑изображение в ваш PDF‑документ, используя класс ImageStamp библиотеки Aspose.PDF для Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить штампы‑изображения в PDF с помощью Python
Abstract: В этой статье представлено полное руководство по добавлению штампов‑изображений в PDF‑файлы с использованием библиотеки Aspose.PDF для Python. Описывается использование класса `ImageStamp`, который позволяет настраивать штампы‑изображения, включая такие свойства, как высота, ширина, непрозрачность и вращение. Процесс включает создание объекта `Document` и объекта `ImageStamp` с требуемыми свойствами, а затем добавление штампа на конкретную страницу PDF с помощью метода `add_stamp()`. В статье приведены фрагменты кода на Python, демонстрирующие, как применить штамп‑изображение к PDF и управлять его качеством с помощью свойства `quality`, регулирующего качество изображения в процентах. Кроме того, статья объясняет, как использовать штампы‑изображения в качестве фона во всплывающих коробках с классом `FloatingBox`, предоставляя еще один пример кода, показывающий, как это реализовать. Это руководство служит полезным ресурсом для разработчиков, желающих улучшить PDF с помощью штампов‑изображений, используя Aspose.PDF.
---

## Добавление штампа‑изображения в PDF‑файл

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) для добавления штампа‑изображения в PDF‑файл. Класс [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) предоставляет свойства, необходимые для создания штампа‑изображения, такие как высота, ширина, непрозрачность и т.д. Штамп можно позиционировать, изменять размер, вращать и делать полупрозрачным, что позволяет использовать его для водяных знаков, брендинга или аннотаций.

Следующий фрагмент кода показывает, как добавить штамп‑изображение в PDF‑файл.

1. Загрузите PDF, используя 'ap.Document()'.
1. Создайте штамп‑изображение с помощью 'ImageStamp()'.
1. Настройте свойства штампа.
1. Добавьте штамп на целевую страницу.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Управление качеством изображения при добавлении штампа

При добавлении изображения в качестве штампа вы можете контролировать его качество. Свойство [качество](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) класса [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) используется для этой цели. Оно указывает качество изображения в процентах (допустимые значения 0..100).
Устанавливая свойство качества, вы можете уменьшить разрешение изображения для оптимизации размера PDF или сохранить более высокую точность для чёткости.

1. Откройте PDF‑документ.
1. Создайте штамп‑изображение.
1. Установите качество изображения.
1. Добавьте штамп на целевую страницу.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp_image_control_image_quality(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Штамп‑изображение как фон в Floating Box

Создайте [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) в PDF и примените изображение в качестве его фона. Также показывается, как добавить текст, установить границы, цвет фона и точно позиционировать коробку на странице. Это полезно для создания визуально насыщенного PDF‑контента, такого как выноски, баннеры или выделенные секции с текстом поверх изображений.

1. Откройте или создайте PDF‑документ.
1. Создайте объект 'FloatingBox'.
1. Добавьте текстовое содержимое в коробку.
1. Установите границу коробки и цвет фона.
1. Добавьте фоновое изображение.
1. Добавьте FloatingBox на страницу.
1. Сохраните PDF‑документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    # Add page to PDF document
    page = document.pages.add()
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```


