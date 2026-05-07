---
title: Работа с метаданными PDF‑файла в Python
linktitle: Метаданные PDF‑файла
type: docs
weight: 200
url: /ru/python-net/pdf-file-metadata/
description: Узнайте, как извлекать, обновлять и управлять метаданными PDF‑файла и свойствами XMP в Python с использованием Aspose.PDF.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получайте и задавайте информацию о документе PDF и метаданные XMP в Python
Abstract: В этой статье объясняется, как работать с метаданными PDF в Aspose.PDF for Python via .NET. Узнайте, как читать информацию о документе, такую как автор, название и ключевые слова, обновлять свойства файла, задавать поля XMP‑метаданных и регистрировать пользовательские префиксы метаданных для PDF‑файлов в Python.
---

Используйте это руководство, когда нужно просматривать свойства документа, обновлять информацию о PDF‑файле для поиска или каталогизации, либо программно управлять XMP‑метаданными в Python.

## Получить информацию о PDF‑файле

Этот фрагмент кода демонстрирует, как извлекать метаданные из PDF‑документа с использованием Aspose.PDF for Python via .NET. Получая доступ к свойству info объекта Document, он извлекает ключевую информацию, такую как автор, дата создания, ключевые слова, дата изменения, тема и название. Эта функция необходима для приложений, которым требуется каталогизация документов, оптимизация поиска или проверка свойств документа.

1. Откройте PDF‑файл, используя класс Document
1. Получите метаданные документа через свойство info
1. Отобразите информацию о метаданных. Выведите нужные поля метаданных.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## Установить информацию о PDF-файле

Aspose.PDF for Python via .NET позволяет задавать специфичную для файла информацию о PDF, такую как автор, дата создания, тема и заголовок. Чтобы задать эту информацию:

1. Откройте PDF-файл, используя класс Document.
1. Создайте [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) объект и установите желаемые свойства метаданных.
1. Сохраните изменения в новый PDF‑файл, используя метод save.

Следующий фрагмент кода показывает, как установить информацию о файле PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## Установить XMP-метаданные в PDF-файле

Этот фрагмент кода демонстрирует, как программно установить или обновить XMP‑метаданные в PDF‑документе с использованием Aspose.PDF for Python via .NET. Изменяя такие свойства, как xmp:CreateDate, xmp:Nickname и пользовательские поля, вы можете внедрять стандартизированные метаданные в свои PDF‑файлы. Такой подход особенно полезен для улучшения организации документов, облегчения их поиска и непосредственного внедрения необходимой информации в файл.

Aspose.PDF позволяет задавать метаданные в файле PDF. Чтобы задать метаданные:

1. Откройте файл PDF с помощью [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Измените метаданные XMP, присваивая значения определённым ключам.
1. Сохраните обновлённый PDF‑документ.

Следующий фрагмент кода показывает, как установить метаданные в PDF‑файле.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## Вставить метаданные с префиксом

Некоторым разработчикам необходимо создать новое пространство имён метаданных с префиксом. Следующий фрагмент кода показывает, как вставить метаданные с префиксом.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## Связанные темы

- [Расширенные операции с PDF в Python](/pdf/ru/python-net/advanced-operations/)
- [Работа с PDF-документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Работа с PDF‑вложениями в Python](/pdf/ru/python-net/attachments/)
- [Сравнение PDF‑документов в Python](/pdf/ru/python-net/compare-pdf-documents/)
