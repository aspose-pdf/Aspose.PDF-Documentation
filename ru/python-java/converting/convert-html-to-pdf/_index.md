---
title: Преобразование HTML в PDF на Python
linktitle: Преобразование HTML в файл PDF
type: docs
weight: 40
url: ru/python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: Эта тема покажет вам, как преобразовать HTML в PDF и MHTML в PDF с использованием Aspose.PDF для Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Обзор 

Aspose.PDF для Python через Java — это профессиональное решение, которое позволяет создавать PDF-файлы из веб-страниц и исходного HTML-кода в ваших приложениях.

Эта статья объясняет, как **преобразовать HTML в PDF с использованием Python**. Она охватывает следующие темы.

_Формат_: **HTML**
- [Python HTML в PDF](#python-html-to-pdf)
- [Python Преобразование HTML в PDF](#python-html-to-pdf)
- [Python Как преобразовать HTML в PDF](#python-html-to-pdf)

## Преобразование HTML в PDF на Python

**Aspose.PDF для Python** — это API для работы с PDF, который позволяет бесшовно преобразовывать любые существующие HTML-документы в PDF. Процесс преобразования HTML в PDF может гибко настраиваться.

## Преобразование HTML в PDF


Следующий пример кода на Python показывает, как преобразовать HTML-документ в PDF.

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
2. Инициализируйте объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
3. Сохраните выходной PDF-документ, вызвав метод **Document.Save()**.

```python

from asposepdf import Api


# инициализация лицензии
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# конвертация из массива байтов
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# конвертация из файла
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**Попробуйте конвертировать HTML в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование HTML в PDF с помощью бесплатного приложения](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}