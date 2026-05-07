---
title: Добавить и удалить закладки PDF в Python
linktitle: Добавить и удалить закладку
type: docs
weight: 10
url: /ru/python-net/add-and-delete-bookmark/
description: Узнайте, как добавлять и удалять закладки в PDF‑документах с помощью Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить и удалить закладки с помощью Python
Abstract: Эта статья предоставляет комплексные инструкции по управлению закладками в PDF‑документах с использованием библиотеки Aspose.PDF для Python. В ней описываются процессы добавления, изменения и удаления закладок в PDF. Статья начинается с руководства по добавлению закладки посредством создания объекта `OutlineItemCollection` и добавления его в `OutlineCollection` документа. Приводятся примеры кода, демонстрирующие создание и добавление как родительских, так и дочерних закладок, подчёркивая иерархическую связь. Кроме того, статья охватывает методы удаления всех закладок или конкретной закладки по названию. Каждый раздел содержит фрагменты кода на Python, иллюстрирующие операции, что позволяет читателям легко внедрять описанные возможности в задачи по работе с PDF.
---

## Добавить закладку в PDF‑документ

Закладки хранятся в объекте Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) коллекция, сама в [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) коллекция.

Чтобы добавить закладку в PDF:

1. Откройте документ PDF с помощью [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект.
1. Создайте закладку и определите её свойства.
1. Добавьте [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) коллекцию в коллекцию Outlines.

Следующий фрагмент кода показывает, как добавить закладку в PDF‑документ.

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Добавить дочернюю закладку в PDF‑документ

Закладки могут быть вложенными, указывая иерархические отношения между родительскими и дочерними закладками. В этой статье объясняется, как добавить дочернюю закладку, то есть закладку второго уровня, в PDF.

Чтобы добавить дочернюю закладку в PDF‑файл, сначала добавьте родительскую закладку:

1. Откройте документ.
1. Добавьте закладку в [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), определяя её свойства.
1. Добавьте OutlineItemCollection к объекту Document [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) коллекция.

Дочерняя закладка создаётся так же, как и родительская закладка, описанная выше, но добавляется в коллекцию Outlines родительской закладки.

Следующие фрагменты кода показывают, как добавить дочернюю закладку в PDF‑документ.

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Удалить все закладки из PDF‑документа

Все закладки в PDF хранятся в [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. Эта статья объясняет, как удалить все закладки из PDF-файла.

Чтобы удалить все закладки из PDF-файла:

1. Вызовите [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) метод Delete коллекции.
1. Сохраните изменённый файл, используя [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объекта [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод.

Следующие фрагменты кода показывают, как удалить все закладки из PDF‑документа.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## Удалить определенную закладку из PDF‑документа

Чтобы удалить определённую закладку из PDF‑файла:

1. Передайте заголовок закладки в качестве параметра функции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) метод Delete коллекции.
1. Затем сохраните обновлённый файл, используя метод Save объекта Document.

Эта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс предоставляет [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) коллекцию. Это [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) метод удаляет любую закладку с заголовком, переданным в метод.

Следующие фрагменты кода показывают, как удалить конкретную закладку из PDF-документа.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## Связанные темы закладок

- [Работа с закладками PDF в Python](/pdf/ru/python-net/bookmarks/)
- [Получение, обновление и расширение закладок PDF в Python](/pdf/ru/python-net/get-update-and-expand-bookmark/)
- [Навигация и взаимодействие с PDF с использованием Python](/pdf/ru/python-net/navigation-and-interaction/)

