---
title: Как создать PDF с помощью Python
linktitle: Создать PDF документ
type: docs
weight: 10
url: /ru/python-net/create-pdf-document/
description: Создавайте и форматируйте PDF документ с помощью Aspose.PDF для Python через .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать PDF файл с помощью Python
Abstract: Aspose.PDF for Python via .NET — это универсальный API, разработанный для разработчиков, позволяющий манипулировать PDF‑файлами в Python‑приложениях, ориентированных на платформу .NET. Он предоставляет возможность пользователям легко создавать, загружать, изменять и конвертировать PDF‑документы. В этой статье представлено пошаговое руководство по созданию простого PDF‑файла с использованием Aspose.PDF. Процесс включает инициализацию объекта `Document`, добавление `Page` в документ, вставку `TextFragment` в параграфы страницы и сохранение файла в формате PDF. Приведенный фрагмент кода на Python демонстрирует эти шаги, создавая PDF‑документ, содержащий текст "Hello World!". Этот API упрощает работу с PDF, требуя минимального количества кода, повышая продуктивность разработчиков, работающих с PDF в среде .NET.
---

**Aspose.PDF for Python via .NET** — это API для работы с PDF, позволяющее разработчикам создавать, загружать, изменять и конвертировать PDF‑файлы напрямую из Python для приложений .NET, используя всего несколько строк кода.

## Как создать простой PDF файл

Чтобы создать PDF с использованием Python через .NET и Aspose.PDF, вы можете выполнить следующие шаги:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Добавьте объект [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в коллекцию [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) объекта Document
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) в коллекцию [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы
1. Сохраните полученный PDF документ

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```


