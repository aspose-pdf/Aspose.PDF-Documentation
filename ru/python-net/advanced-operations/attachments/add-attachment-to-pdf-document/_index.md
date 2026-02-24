---
title: Добавление вложения в PDF‑документ с помощью Python
linktitle: Добавление вложения в PDF‑документ
type: docs
weight: 10
url: /ru/python-net/add-attachment-to-pdf-document/
description: На этой странице описывается, как добавить вложение в PDF‑файл с помощью библиотеки Aspose.PDF для Python через .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить вложения в PDF с помощью Python
Abstract: В этой статье представлено пошаговое руководство по добавлению вложений в PDF‑файл с использованием Python и библиотеки Aspose.PDF. Описывается процесс настройки нового проекта Python, импорта необходимого пакета Aspose.PDF и создания объекта `Document`. Статья объясняет, как создать объект `FileSpecification` с нужным файлом и описанием, а также как добавить этот объект в `EmbeddedFileCollection` PDF‑документа с помощью метода `add`. `EmbeddedFileCollection` хранит все вложения в PDF. Включён фрагмент кода, демонстрирующий процесс открытия документа, подготовки файла для вложения, добавления его в коллекцию вложений документа и сохранения обновлённого PDF.
---

Вложения могут содержать разнообразную информацию и быть различных типов файлов. Эта статья объясняет, как добавить вложение в PDF‑файл.

1. Создайте новый проект Python.
1. Импортируйте пакет Aspose.PDF
1. Создайте объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте объект [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) с добавляемым файлом и его описанием.
1. Добавьте объект [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) к объекту [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в его коллекцию [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/), используя метод [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) этой коллекции.

Коллекция [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) содержит все вложения в PDF‑файле. Ниже приведён фрагмент кода, показывающий, как добавить вложение в PDF‑документ.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```


