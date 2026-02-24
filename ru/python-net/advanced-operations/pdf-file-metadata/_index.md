---
title: Работа с метаданными PDF-файлов в Python
linktitle: Метаданные PDF-файла
type: docs
weight: 200
url: /ru/python-net/pdf-file-metadata/
description: Узнайте, как извлекать и управлять метаданными PDF, такими как автор и заголовок, в Python с помощью Aspose.PDF.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получение и установка метаданных в PDF с помощью Python
Abstract: В статье представлено всестороннее руководство по работе с метаданными PDF с использованием Aspose.PDF для Python через .NET. Описываются методы извлечения и установки свойств метаданных, включая автора, дату создания, ключевые слова и прочее, что важно для каталогизации документов, оптимизации поиска или валидации. Примеры кода демонстрируют, как получить метаданные из PDF с помощью класса `Document` и свойства `info`, установить новые метаданные с помощью объекта `DocumentInfo` и сохранить изменения. Кроме того, показывается, как программно обновлять XMP‑метаданные, что улучшает организацию и поиск документов. В статье также объясняется, как вставлять метаданные с пользовательским префиксом, регистрируя URI пространства имён. Эти возможности жизненно важны для разработчиков, желающих эффективно управлять информацией PDF‑документов в приложениях.
---

## Получить информацию о PDF-файле

Этот фрагмент кода демонстрирует, как извлечь метаданные из PDF‑документа с помощью Aspose.PDF для Python через .NET. Получая доступ к свойству info объекта Document, он извлекает ключевую информацию, такую как автор, дата создания, ключевые слова, дата изменения, тема и заголовок. Эта возможность важна для приложений, которым требуется каталогизация документов, оптимизация поиска или проверка свойств документа.

1. Откройте PDF‑файл с помощью класса Document
1. Получите метаданные документа через свойство info
1. Отобразите информацию о метаданных. Выведите нужные поля метаданных

```python

    import aspose.pdf as ap

    def get_pdf_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "GetFileInfo.pdf")

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

Aspose.PDF для Python через .NET позволяет установить файловую информацию для PDF, такую как автор, дата создания, тема и заголовок. Чтобы установить эту информацию:

1. Откройте PDF‑файл с помощью класса Document.
1. Создайте объект [DocumentInfo]() и установите нужные свойства метаданных.
1. Сохраните изменения в новый PDF‑файл, используя метод save.

Следующий фрагмент кода показывает, как установить информацию о PDF‑файле.

```python

    import aspose.pdf as ap
    import datetime

    def set_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

        # Open PDF document
        document = ap.Document(data_dir + "SetFileInfo.pdf")

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
        document.save(data_dir + "SetFileInfo_out.pdf")
```

## Установить XMP‑метаданные в PDF‑файле

Этот фрагмент кода демонстрирует, как программно задавать или обновлять XMP‑метаданные в PDF‑документе с помощью Aspose.PDF для Python через .NET. Изменяя свойства, такие как xmp:CreateDate, xmp:Nickname и пользовательские поля, вы можете внедрять стандартизированные метаданные в ваши PDF‑файлы. Такой подход особенно полезен для улучшения организации документов, облегчения их поиска и встраивания важной информации непосредственно в файл.

Aspose.PDF позволяет задавать метаданные в PDF‑файле. Чтобы задать метаданные:

1. Откройте PDF‑файл, используя класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Измените XMP‑метаданные, присвоив значения конкретным ключам.
1. Сохраните обновлённый PDF‑документ.

Следующий фрагмент кода показывает, как задать метаданные в PDF‑файле.

```python

    import aspose.pdf as ap
    import datetime

    def set_xmp_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Set XMP metadata properties
        document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
        document.metadata["xmp:Nickname"] = "Nickname"
        document.metadata["xmp:CustomProperty"] = "Custom Value"

        # Save the updated PDF document
        document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## Вставка метаданных с префиксом

Некоторым разработчикам необходимо создать новое пространство имён метаданных с префиксом. Следующий фрагмент кода показывает, как вставить метаданные с префиксом.

```python

    import aspose.pdf as ap
    import datetime

    def set_prefix_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Register a namespace URI for the 'xmp' prefix
        document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

        # Set the metadata property using the registered prefix
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```
