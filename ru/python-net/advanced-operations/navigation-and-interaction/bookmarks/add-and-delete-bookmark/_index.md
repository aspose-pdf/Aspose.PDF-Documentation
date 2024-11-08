---
title: Добавление и Удаление Закладки с использованием Python
linktitle: Добавление и Удаление Закладки
type: docs
weight: 10
url: /ru/python-net/add-and-delete-bookmark/
description: Вы можете добавить закладку в PDF документ с помощью Python. Возможно удалить все или конкретные закладки из PDF документа.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление и Удаление Закладки",
    "alternativeHeadline": "Как добавить и удалить закладку из PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "создание pdf документов",
    "keywords": "pdf, python, удаление закладки, добавление закладки",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Вы можете добавить закладку в PDF документ с помощью Python. Возможно удалить все или конкретные закладки из PDF документа."
}
</script>


## Добавить закладку в PDF документ

Закладки хранятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) объекта Document, которая сама находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Чтобы добавить закладку в PDF:

1. Откройте PDF документ с использованием объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте закладку и определите её свойства.
1. Добавьте коллекцию [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) в коллекцию Outlines.

Следующий фрагмент кода показывает, как добавить закладку в PDF документ.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Создать объект закладки
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Тестовая закладка"
    outline.italic = True
    outline.bold = True
    # Установить номер целевой страницы
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Добавить закладку в коллекцию контура документа.
    document.outlines.append(outline)

    # Сохранить результат
    document.save(output_pdf)
```


## Добавление дочерней закладки в PDF-документ

Закладки могут быть вложенными, указывая на иерархическую связь между родительскими и дочерними закладками. В этой статье объясняется, как добавить дочернюю закладку, то есть закладку второго уровня, в PDF.

Чтобы добавить дочернюю закладку в PDF-файл, сначала добавьте родительскую закладку:

1. Откройте документ.
1. Добавьте закладку в [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), определив ее свойства.
1. Добавьте OutlineItemCollection в коллекцию объекта Document [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Дочерняя закладка создается так же, как и родительская закладка, как объяснено выше, но добавляется в коллекцию Outlines родительской закладки.

Следующие фрагменты кода показывают, как добавить дочернюю закладку в PDF-документ.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Создать объект родительской закладки
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Родительская закладка"
    outline.italic = True
    outline.bold = True

    # Создать объект дочерней закладки
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Дочерняя закладка"
    childOutline.italic = True
    childOutline.bold = True

    # Добавить дочернюю закладку в коллекцию родительской закладки
    outline.append(childOutline)
    # Добавить родительскую закладку в коллекцию закладок документа.
    document.outlines.append(outline)

    # Сохранить результат
    document.save(output_pdf)
```


## Удаление всех закладок из PDF документа

Все закладки в PDF хранятся в коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). В этой статье объясняется, как удалить все закладки из PDF файла.

Чтобы удалить все закладки из PDF файла:

1. Вызовите метод Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
2. Сохраните измененный файл, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Следующие фрагменты кода показывают, как удалить все закладки из PDF документа.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Удалить все закладки
    document.outlines.delete()

    # Сохранить обновленный файл
    document.save(output_pdf)

```

## Удаление определенной закладки из PDF документа

Чтобы удалить определенную закладку из PDF файла:

1. Передайте заголовок закладки в качестве параметра методу Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Затем сохраните обновленный файл с помощью метода Save объекта Document.

Класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) предоставляет коллекцию [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Метод [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) удаляет любую закладку с заголовком, переданным в метод.

Следующие фрагменты кода показывают, как удалить определенную закладку из PDF-документа.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Удалить определенный элемент оглавления по заголовку
    document.outlines.delete("Child Outline")

    # Сохранить обновленный файл
    document.save(output_pdf)