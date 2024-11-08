---
title: Получить, обновить и развернуть закладку с использованием Python
linktitle: Получить, обновить и развернуть закладку
type: docs
weight: 20
url: /ru/python-net/get-update-and-expand-bookmark/
description: В этой статье описывается, как использовать закладки в PDF-файле с нашей библиотекой Aspose.PDF для Python.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Получить, обновить и развернуть закладку с помощью Python",
    "alternativeHeadline": "Как получить закладки из PDF-файла",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, получить закладки",
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
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "В этой статье описывается, как использовать закладки в PDF-файле с нашей библиотекой Aspose.PDF для Python."
}
</script>


## Получение Закладок

Коллекция [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) содержит все закладки PDF файла. Эта статья объясняет, как получить закладки из PDF файла и как определить, на какой странице находится определенная закладка.

Чтобы получить закладки, пройдите по коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) и получите каждую закладку в OutlineItemCollection. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) предоставляет доступ ко всем атрибутам закладки. Следующий фрагмент кода показывает, как получить закладки из PDF файла.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Пройти по всем закладкам
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```


## Получение номера страницы закладки

После того как вы добавили закладку, вы можете узнать, на какой странице она находится, получив номер страницы назначения, связанный с объектом закладки.

```python

    import aspose.pdf as ap

    # Создание PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Открыть PDF файл
    bookmarkEditor.bind_pdf(input_pdf)
    # Извлечь закладки
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Название:", bookmark.title)
        print(str_level_seprator, "Номер страницы:", bookmark.page_number)
        print(str_level_seprator, "Действие страницы:", bookmark.action)
```

## Получение дочерних закладок из PDF документа

Закладки могут быть организованы в иерархическую структуру с родителями и детьми.
 Чтобы получить все закладки, пройдите циклом по коллекциям Outlines объекта Document. Однако, чтобы получить также дочерние закладки, пройдите циклом по всем закладкам в каждом объекте [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), полученном в первом цикле. Следующие фрагменты кода показывают, как получить дочерние закладки из PDF-документа.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Пройти циклом по всем закладкам
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Дочерние закладки")
            # Есть дочерние закладки, пройти циклом по ним
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Обновление закладок в PDF-документе

Чтобы обновить закладку в PDF-файле, сначала получите конкретную закладку из коллекции OutlineColletion объекта Document, указав индекс закладки. После того, как вы извлекли закладку в объект [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), вы можете обновить её свойства, а затем сохранить обновленный PDF-файл, используя метод Save. Следующие фрагменты кода показывают, как обновить закладки в PDF-документе.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Получить объект закладки
    outline = document.outlines[1]

    # Получить дочерний объект закладки
    child_outline = outline[1]
    child_outline.title = "Обновленная закладка"
    child_outline.italic = True
    child_outline.bold = True

    # Сохранить результат
    document.save(output_pdf)
```

## Раскрытые закладки при просмотре документа

Закладки содержатся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) объекта Document, которая сама по себе находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
 Однако, у нас может возникнуть необходимость, чтобы все закладки были развернуты при просмотре PDF файла.

Чтобы выполнить это требование, мы можем установить статус открытия для каждого элемента контура/закладки как Открыто. Следующий фрагмент кода показывает, как установить статус открытия для каждой закладки как развернутой в PDF документе.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Установить режим просмотра страницы, например, показывать миниатюры, полноэкранный режим, показывать панель вложений
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Пройтись по каждому элементу контуров в коллекции контуров PDF файла
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Установить статус открытия для элемента контура
        item.open = True

    # Сохранить результат
    document.save(output_pdf)