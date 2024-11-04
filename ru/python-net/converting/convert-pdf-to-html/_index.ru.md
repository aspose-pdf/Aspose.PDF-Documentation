---
title: Convert PDF to HTML in Python 
linktitle: Convert PDF to HTML format
type: docs
weight: 50
url: /python-net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: This topic show you how to convert PDF file to HTML format with  Aspose.PDF for Python .NET library.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Overview

Эта статья объясняет, как **конвертировать PDF в HTML с использованием Python**. Она охватывает следующие темы.

_Формат_: **HTML**
- [Python PDF в HTML](#python-pdf-to-html)
- [Python Конвертировать PDF в HTML](#python-pdf-to-html)
- [Python Как конвертировать файл PDF в HTML](#python-pdf-to-html)


## Convert PDF to HTML

**Aspose.PDF for Python via .NET** предоставляет множество функций для конвертации различных форматов файлов в документы PDF и конвертации PDF-файлов в различные выходные форматы.
 Этот документ обсуждает, как преобразовать PDF файл в <abbr title="HyperText Markup Language">HTML</abbr>. Вы можете использовать всего несколько строк кода на Python для преобразования PDF в HTML. Вам может понадобиться преобразовать PDF в HTML, если вы хотите создать веб-сайт или добавить контент на онлайн-форум. Один из способов преобразования PDF в HTML - программно использовать Python.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в HTML онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в HTML с помощью бесплатного приложения](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>Шаги: Преобразование PDF в HTML на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF-документом.
2. Сохраните его в [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) с помощью вызова метода [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_html.html"
    # Открыть документ PDF
    document = ap.Document(input_pdf)

    # сохранить документ в формате HTML
    save_options = ap.HtmlSaveOptions()
    document.save(output_pdf, save_options)
```

## См. также

Эта статья также охватывает следующие темы. Код такой же, как и выше.

_Формат_: **HTML**
- [Python PDF в HTML Код](#python-pdf-to-html)
- [Python PDF в HTML API](#python-pdf-to-html)
- [Python PDF в HTML Программно](#python-pdf-to-html)
- [Python PDF в HTML Библиотека](#python-pdf-to-html)
- [Python Сохранить PDF как HTML](#python-pdf-to-html)
- [Python Генерировать HTML из PDF](#python-pdf-to-html)
- [Python Создать HTML из PDF](#python-pdf-to-html)

- [Python Конвертер PDF в HTML](#python-pdf-to-html)