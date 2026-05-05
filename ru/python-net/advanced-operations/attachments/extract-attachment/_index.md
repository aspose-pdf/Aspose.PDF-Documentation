---
title: Извлечение вложений из PDF
linktitle: Извлечение вложений
type: docs
weight: 50
url: /ru/python-net/extract-attachment/
description: Узнайте, как работать с вложениями PDF, используя Python и Aspose.PDF.
lastmod: "2026-04-26"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Полное руководство по управлению вложениями PDF в Python: добавление, извлечение и обработка вложенных файлов"
Abstract: PDF‑вложения широко используются для хранения сопутствующих документов, отчетов, изображений и других ресурсов непосредственно внутри файла PDF. В этой статье представлено полное руководство по работе с PDF‑вложениями в Python с использованием Aspose.PDF. Описывается, как внедрять внешние файлы в существующие PDF, извлекать отдельные или все вложения, просматривать метаданные, такие как размер файла и метки времени, а также восстанавливать файлы, сохранённые как аннотации FileAttachment. Каждый пример демонстрирует практические методы автоматизации процессов работы с вложениями, повышения переносимости документов и упрощения управления файлами. Независимо от того, создаёте ли вы корпоративные системы документооборота или пользовательские скрипты автоматизации, разработчики могут использовать эти методы для эффективного управления вложенными файлами в PDF‑документах.
---

## Извлечь конкретное вложение из PDF

Извлеките один встраиваемый файл из PDF‑документа с помощью Python и Aspose.PDF. Он ищет вложение по имени, извлекает его содержимое и сохраняет как отдельный файл. Это полезно для доступа к вложенным документам, таким как отчёты, журналы или вспомогательные файлы, хранящиеся внутри PDF.

1. Определите функцию ‘extract_single_attachment()’.
1. Откройте PDF‑документ.
1. Найдите вложение.
1. Извлечь содержимое вложения.

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## Отобразить метаданные файлового вложения

Эта вспомогательная функция выводит информацию о метаданных из объекта спецификации файла. Обычно она используется при работе с внедрёнными файловыми вложениями в PDF с помощью Aspose.PDF, позволяя разработчикам просматривать такие детали, как контрольная сумма, дата создания, дата модификации и размер файла.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## Извлечь и проверить все вложения PDF

Этот фрагмент кода демонстрирует, как извлекать все вложенные файлы из PDF‑документа с использованием Python и Aspose.PDF. Он не только сохраняет каждое вложение в указанную папку, но и выводит подробные метаданные, такие как имя файла, описание, тип MIME, контрольная сумма и метки времени. Это полезно для аудита, экспорта или обработки вложенного контента в PDF‑файлах.

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## Извлечение файлов из аннотаций вложений PDF

Извлеките вложенный файл из аннотации FileAttachment в PDF с помощью Python и Aspose.PDF. Он ищет на первой странице первую аннотацию вложения, извлекает вложенный файл и сохраняет его в выбранный выходной каталог. Это полезно, когда PDF‑файлы содержат кликабельные значки вложения файлов вместо стандартных коллекций вложенных файлов.

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```