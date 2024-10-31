---
title: Конвертация HTML в PDF на Python
linktitle: Конвертация HTML в файл PDF
type: docs
weight: 40
url: /python-net/convert-html-to-pdf/
lastmod: "2022-12-22"
description: В этой теме показано, как конвертировать HTML в PDF и MHTML в PDF, используя Aspose.PDF для Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Обзор

Aspose.PDF для Python через .NET — это профессиональное решение, которое позволяет создавать PDF файлы из веб-страниц и сырого HTML кода в ваших приложениях.

Эта статья объясняет, как **конвертировать HTML в PDF, используя Python**. Она охватывает следующие темы.

_Формат_: **HTML**
- [Python HTML в PDF](#python-html-to-pdf)
- [Python Конвертация HTML в PDF](#python-html-to-pdf)
- [Python Как конвертировать HTML в PDF](#python-html-to-pdf)

## Конвертация HTML в PDF на Python

**Aspose.PDF для Python** — это API для работы с PDF, который позволяет беспрепятственно конвертировать любые существующие HTML документы в PDF. Процесс конвертации HTML в PDF может быть гибко настроен.

## Конвертация HTML в PDF

Следующий пример кода на Python показывает, как конвертировать HTML документ в PDF.

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Инициализируйте объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Сохраните выходной PDF-документ, вызвав метод **Document.Save()**.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "little_html.html"
    output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
    options = ap.HtmlLoadOptions()
    document = ap.Document(input_pdf, options)
    document.save(output_pdf)
```

{{% alert color="success" %}}
**Попробуйте конвертировать HTML в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["HTML в PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), где вы можете исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация HTML в PDF с использованием бесплатного приложения](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}