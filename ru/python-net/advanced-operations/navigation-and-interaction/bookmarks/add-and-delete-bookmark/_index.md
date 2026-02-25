---
title: Добавление и удаление закладки с помощью Python
linktitle: Добавить и удалить закладку
type: docs
weight: 10
url: /ru/python-net/add-and-delete-bookmark/
description: Вы можете добавить закладку в PDF‑документ с помощью Python. Можно удалить все или отдельные закладки из PDF‑документа.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить и удалить закладки с помощью Python
Abstract: В этой статье предоставлены подробные инструкции по управлению закладками в PDF‑документах с использованием библиотеки Aspose.PDF для Python. Описаны процессы добавления, изменения и удаления закладок в PDF. Статья начинается с руководства по добавлению закладки путем создания объекта `OutlineItemCollection` и добавления его в `OutlineCollection` документа. В ней представлены примеры кода, демонстрирующие создание и добавление как родительских, так и дочерних закладок, подчёркивая иерархические отношения. Кроме того, статья охватывает методы удаления всех закладок или конкретной закладки по названию. Каждый раздел содержит фрагменты кода на Python, иллюстрирующие операции, позволяя читателям легко реализовать описанные функции в своих задачах по работе с PDF.
---

## Добавить закладку в PDF‑документ

Закладки хранятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) объекта Document, которая находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Чтобы добавить закладку в PDF:

1. Откройте PDF‑документ, используя объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте закладку и задайте её свойства.
1. Добавьте коллекцию [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) в коллекцию Outlines.

Следующий фрагмент кода показывает, как добавить закладку в PDF‑документ.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Set the destination page number
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Add bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Добавить дочернюю закладку в PDF‑документ

Закладки могут быть вложенными, указывая на иерархические отношения между родительскими и дочерними закладками. В этой статье объясняется, как добавить дочернюю закладку, то есть закладку второго уровня, в PDF.

Чтобы добавить дочернюю закладку в PDF‑файл, сначала добавьте родительскую закладку:

1. Откройте документ.
1. Добавьте закладку в [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), задав её свойства.
1. Добавьте OutlineItemCollection в коллекцию [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) объекта Document.

Дочерняя закладка создаётся так же, как и родительская, описанная выше, но добавляется в коллекцию Outlines родительской закладки.

Следующие фрагменты кода показывают, как добавить дочернюю закладку в PDF‑документ.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a parent bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Create a child bookmark object
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Add child bookmark in parent bookmark's collection
    outline.append(childOutline)
    # Add parent bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Удалить все закладки из PDF‑документа

Все закладки в PDF хранятся в коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). В этой статье объясняется, как удалить все закладки из PDF‑файла.

Чтобы удалить все закладки из PDF‑файла:

1. Вызовите метод Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Сохраните изменённый файл, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Следующие фрагменты кода показывают, как удалить все закладки из PDF‑документа.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## Удалить конкретную закладку из PDF‑документа

Чтобы удалить конкретную закладку из PDF‑файла:

1. Передайте название закладки в качестве параметра методу Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Затем сохраните обновлённый файл, используя метод Save объекта Document.

Класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) предоставляет коллекцию [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Метод [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) удаляет любую закладку с переданным в метод названием.

Следующие фрагменты кода показывают, как удалить конкретную закладку из PDF‑документа.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```


