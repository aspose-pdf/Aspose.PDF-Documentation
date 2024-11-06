---
title: Преобразование PDF в различные форматы изображений на Python
linktitle: Преобразование PDF в изображения
type: docs
weight: 70
url: ru/python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: Эта тема показывает, как использовать Aspose.PDF для Python для преобразования PDF в различные форматы изображений, такие как TIFF, BMP, EMF, JPEG, PNG, GIF, SVG с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Обзор

Эта статья объясняет, как преобразовать PDF в различные форматы изображений с использованием Python. Она охватывает следующие темы.

## Преобразование PDF в изображение на Python

### Преобразование PDF в PNG на Python

1. Импортируйте модуль AsposePdfPython, который предоставляет оболочку Python для библиотеки Aspose.PDF.
1. Откройте PDF-документ с помощью функции `document_open`, которая принимает имя файла в качестве аргумента и возвращает объект Document.
1. Получите страницы документа с помощью функции `document_get_pages`, которая принимает объект Document в качестве аргумента и возвращает объект PageCollection.

1. Получите нужную страницу документа, используя функцию `page_collection_get_page`, которая принимает объект PageCollection и индекс в качестве аргументов и возвращает объект Page.
1. Создайте объект PngDevice, используя функцию `png_device_create`, которая не принимает аргументов. Этот объект может конвертировать страницы PDF в изображения PNG с параметрами по умолчанию.
1. Сохраните нужную страницу документа как изображение PNG, используя функцию `png_device_save_page_to_file`, которая принимает объект PngDevice, объект Page и имя файла в качестве аргументов.
1. Закройте дескрипторы объектов PngDevice и Document, используя функцию close_handle, которая принимает объект в качестве аргумента и освобождает его ресурсы.

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### Python Преобразование PDF в JPEG

1. Откройте PDF-документ с помощью функции `document_open`, которая принимает имя файла в качестве аргумента и возвращает объект Document.
1. Получите страницы документа с помощью функции `document_get_pages`, которая принимает объект Document в качестве аргумента и возвращает объект PageCollection.
1. Получите нужную страницу документа с помощью функции `page_collection_get_page`, которая принимает объект PageCollection и индекс в качестве аргументов и возвращает объект Page.
1. Создайте объект Resolution с помощью функции `resolution_create`, которая принимает значение разрешения в точках на дюйм (DPI) в качестве аргумента.
1. Создайте объект JpegDevice с помощью функции `jpeg_device_create_from_width_height_resolution`, которая принимает значения ширины, высоты и разрешения в качестве аргументов. Этот объект может преобразовывать страницы PDF в изображения JPEG с указанными параметрами.

1. Сохраните нужную страницу документа как изображение в формате JPEG, используя функцию `jpeg_device_save_page_to_file`, которая принимает объект JpegDevice, объект Page и имя файла в качестве аргументов.
1. Закройте дескрипторы объектов JpegDevice и Document, используя функцию `close_handle`, которая принимает объект в качестве аргумента и освобождает его ресурсы.

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```