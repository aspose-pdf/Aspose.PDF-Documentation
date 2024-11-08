---
title: Создание PDF документа программно
linktitle: Создание PDF
type: docs
weight: 10
url: /ru/python-net/create-document/
description: Эта страница описывает, как создать PDF документ с нуля с помощью библиотеки Aspose.PDF для Python через .NET.
---

Для разработчиков существует множество сценариев, когда необходимо программно генерировать PDF файлы. Возможно, вам потребуется программно создавать PDF отчеты и другие PDF файлы в вашем программном обеспечении. Писать собственный код и функции с нуля довольно долго и неэффективно. Чтобы создать PDF файл с помощью Python, существует лучшее решение - **Aspose.PDF для Python через .NET**.

## Как создать PDF файл с помощью Python

Для создания PDF файла с помощью Python можно использовать следующие шаги.

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)

1. Добавьте объект [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в коллекцию [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) объекта Document
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) в коллекцию [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы
1. Сохраните полученный PDF-документ

```python

    import aspose.pdf as ap

    # Инициализировать объект документа
    document = ap.Document()
    # Добавить страницу
    page = document.pages.add()
    # Инициализировать объект текстового фрагмента
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Добавить текстовый фрагмент на новую страницу
    page.paragraphs.add(text_fragment)
    # Сохранить обновленный PDF
    document.save("output.pdf")
```