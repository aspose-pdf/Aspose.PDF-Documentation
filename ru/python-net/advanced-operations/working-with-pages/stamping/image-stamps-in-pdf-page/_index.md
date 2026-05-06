---
title: Добавить штампы‑изображения в PDF на Python
linktitle: Штампы‑изображения в PDF‑файле
type: docs
weight: 10
url: /ru/python-net/image-stamps-in-pdf-page/
description: Узнайте, как добавить штампы‑изображения на страницы PDF с помощью Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить штампы‑изображения в PDF с использованием Python
Abstract: В этой статье представлен всесторонний гид по добавлению изображений‑штампов в PDF‑файлы с использованием библиотеки Aspose.PDF для Python. Описывается использование класса `ImageStamp`, который позволяет настраивать штампы на основе изображений, включая такие свойства, как высота, ширина, непрозрачность и вращение. Процесс включает создание объекта `Document` и объекта `ImageStamp` с нужными свойствами, а затем добавление штампа на конкретную страницу PDF с помощью метода `add_stamp()`. В статье приведены фрагменты кода на Python, демонстрирующие, как применить изображение‑штамп к PDF и управлять его качеством с помощью свойства `quality`, которое задает качество изображения в процентах. Кроме того, в статье объясняется, как использовать изображение‑штампы в качестве фона во всплывающих ограничителях с помощью класса `FloatingBox`, предоставляя ещё один пример кода, показывающий, как это реализовать. Этот гид служит полезным ресурсом для разработчиков, желающих улучшить PDF‑файлы с помощью изображений‑штампов, используя Aspose.PDF.
---

## Добавление ImageStamp в PDF-файл

Вы можете использовать [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) класс, чтобы добавить штамп изображения в PDF-файл. Этот [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) класс предоставляет свойства, необходимые для создания штампа на основе изображения, такие как высота, ширина, непрозрачность и т.д. Штамп можно позиционировать, изменять размер, вращать и делать частично прозрачным, что позволяет создавать водяные знаки, брендирование или аннотации.

В следующем фрагменте кода показано, как добавить штамп изображения в PDF‑файл.

1. Загрузите PDF, используя 'ap.Document()'.
1. Создайте штамп изображения с помощью 'ImageStamp()'.
1. Настройте свойства штампа.
1. Добавьте штамп на целевую страницу.
1. Сохранить изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

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

## Контролировать качество изображения при добавлении штампа

При добавлении изображения в качестве объекта штампа вы можете контролировать качество изображения. The [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) свойство [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) класс используется для этой цели. Он указывает качество изображения в процентах (допустимые значения от 0..100).
Устанавливая свойство quality, вы можете уменьшить разрешение изображения, чтобы оптимизировать размер PDF, или сохранить более высокую точность для ясности.

1. Откройте PDF‑документ.
1. Создать штамп изображения.
1. Установить качество изображения.
1. Добавьте штамп на целевую страницу.
1. Сохранить изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Image Stamp как фон во Floating Box

Создайте [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) в PDF и применить изображение в качестве фона. Также показывается, как добавить текст, установить границы, цвет фона и точно разместить коробку на странице. Это полезно для создания визуально насыщенного PDF‑контента, такого как выноски, баннеры или выделенные секции с текстом поверх изображений.

1. Откройте или создайте PDF‑документ.
1. Создайте объект 'FloatingBox'.
1. Добавьте текстовое содержимое в коробку.
1. Установите границу коробки и цвет фона.
1. Добавить фоновое изображение.
1. Добавить FloatingBox на страницу.
1. Сохранить PDF документ.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
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

## Связанные темы штампования

- [Нанести штамп на страницы PDF в Python](/pdf/ru/python-net/stamping/)
- [Добавить штампы страниц в PDF на Python](/pdf/ru/python-net/page-stamps-in-the-pdf-file/)
- [Добавить текстовые штампы в PDF на Python](/pdf/ru/python-net/text-stamps-in-the-pdf-file/)
- [Добавить номера страниц в PDF с помощью Python](/pdf/ru/python-net/add-page-number/)