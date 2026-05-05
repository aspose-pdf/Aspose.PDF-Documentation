---
title: Получить, обновить и развернуть закладки PDF в Python
linktitle: Получить, обновить и развернуть закладку
type: docs
weight: 20
url: /ru/python-net/get-update-and-expand-bookmark/
description: Узнайте, как извлекать, обновлять и развертывать закладки в PDF‑документах с помощью Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как использовать закладки в PDF с помощью Python
Abstract: В этой статье представлен всесторонний гид по управлению закладками в PDF‑документе с использованием библиотеки Aspose.PDF для Python. Сначала объясняется, как получить закладки из PDF‑файла через `OutlineCollection`, которая содержит все закладки, и подробно описывается доступ к атрибутам закладок через `OutlineItemCollection`. Затем в статье рассматривается процесс определения номера страницы, связанной с закладкой, с помощью `PdfBookmarkEditor`. Далее объясняется, как работать с иерархическими структурами закладок, получая дочерние закладки внутри каждого `OutlineItemCollection`. Описывается также обновление свойств закладок, демонстрируется, как изменять атрибуты закладки и сохранять изменения в PDF. Наконец, в статье рассматривается требование раскрытия закладок при просмотре документа, показывая, как задать статус открытости каждой закладки, чтобы они были раскрыты по умолчанию. К каждому разделу прилагаются фрагменты кода, предоставляющие практические примеры реализации этих функций.
---

## Получить закладки

Эта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объекта [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) Коллекция содержит все закладки PDF‑файла. Эта статья объясняет, как получить закладки из PDF‑файла и как определить, на какой странице находится конкретная закладка.

Чтобы получить закладки, пройдите цикл по [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) коллекции и получите каждую закладку в OutlineItemCollection. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) предоставляет доступ ко всем атрибутам закладок. В следующем фрагменте кода показано, как получить закладки из PDF‑файла.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Получение номера страницы закладки

После того как вы добавили закладку, вы можете узнать, на какой странице она находится, получив номер страницы назначения (PageNumber), связанный с объектом Bookmark.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## Получить дочерние закладки из PDF‑документа

Закладки могут быть организованы в иерархическую структуру с родителями и дочерними элементами. Чтобы получить все закладки, пройдите в цикле коллекцию Outlines объекта Document. Однако, чтобы также получить дочерние закладки, также пройдите в цикле все закладки в каждом [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) объект, полученный в первом цикле. Следующие фрагменты кода показывают, как получить дочерние закладки из PDF‑документа.

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Обновить закладки в PDF-документе

Чтобы обновить закладку в PDF файле, сначала получите конкретную закладку из коллекции OutlineColletion объекта Document, указав индекс закладки. Как только вы получили закладку в [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) объект, вы можете обновить его свойства, а затем сохранить обновлённый PDF файл, используя метод Save. Ниже приведены фрагменты кода, показывающие, как обновлять закладки в PDF документе.

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## Развернутые закладки при просмотре документа

Закладки хранятся в объекте Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) коллекция, сама в [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. Однако нам может потребоваться, чтобы все закладки были развернуты при просмотре PDF‑файла.

Чтобы выполнить это требование, мы можем установить статус открытости для каждого элемента оглавления/закладки как Open. Следующий фрагмент кода показывает, как установить статус открытости для каждой закладки как развернутый в PDF‑документе.

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## Связанные темы закладок

- [Работа с закладками PDF в Python](/pdf/ru/python-net/bookmarks/)
- [Добавление и удаление закладок PDF в Python](/pdf/ru/python-net/add-and-delete-bookmark/)
- [Навигация и взаимодействие с PDF с использованием Python](/pdf/ru/python-net/navigation-and-interaction/)

