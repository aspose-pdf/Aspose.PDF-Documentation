---
title: Создать PDF‑документ программно
linktitle: Создать PDF
type: docs
weight: 10
url: /ru/python-net/create-document/
description: На этой странице описывается, как создать PDF‑документ с нуля с помощью библиотеки Aspose.PDF for Python via .NET.
TechArticle: true
AlternativeHeadline: Создание PDF‑файлов с помощью Aspose.PDF for Python
Abstract: В разработке программного обеспечения генерация PDF‑файлов программно является общей потребностью, особенно при создании отчетов и других документов. Написание пользовательского кода для этой задачи может быть неэффективным и затратным по времени. Вместо этого разработчики могут использовать **Aspose.PDF for Python via .NET**, надёжное решение для создания PDF‑файлов с помощью Python. Процесс включает создание объекта `Document`, добавление объекта `Page` в коллекцию `Pages` документа, вставку `TextFragment` в коллекцию `paragraphs` страницы, а затем сохранение документа. Пример фрагмента кода на Python демонстрирует эти шаги, показывая простоту генерации PDF‑файлов с использованием Aspose.PDF.
---

Для разработчиков существует множество сценариев, когда необходимо программно генерировать PDF‑файлы. Вам может понадобиться программно создавать PDF‑отчёты и другие PDF‑документы в вашем программном обеспечении. Писать собственный код и функции с нуля довольно долго и неэффективно. Чтобы создать PDF‑файл с помощью Python, существует лучшее решение — **Aspose.PDF for Python via .NET**.

## Как создать PDF‑файл с помощью Python

Для создания PDF‑файла с помощью Python можно использовать следующие шаги.

1. Создать объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class
1. Добавить объект [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в коллекцию [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) объекта Document
1. Добавить [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) в коллекцию [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы
1. Сохранить полученный PDF‑документ

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```



