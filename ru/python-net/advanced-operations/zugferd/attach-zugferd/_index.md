---
title: Создание PDF/3-A совместимого PDF и прикрепление счета ZUGFeRD в Python
linktitle: Прикрепить ZUGFeRD к PDF
type: docs
weight: 10
url: /ru/python-net/attach-zugferd/
description: Узнайте, как создать PDF‑документ с ZUGFeRD в Aspose.PDF for Python via .NET
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как прикрепить ZUGFeRD к PDF‑документу
Abstract: В статье представлено пошаговое руководство по прикреплению ZUGFeRD (формата электронных счетов) к PDF‑документу с использованием библиотеки Aspose.PDF. Процедура начинается с импорта необходимой библиотеки и настройки путей к каталогам входных и выходных файлов. Затем целевой PDF‑файл загружается в объект Document, а для XML‑файла метаданных счета создаётся объект FileSpecification. Ключевые свойства, такие как `mime_type` и `af_relationship`, устанавливаются для обеспечения правильной интеграции метаданных. XML‑файл затем добавляется в коллекцию встроенных файлов PDF, эффективно прикрепляя его в качестве метаданных. Далее PDF‑документ конвертируется в формат PDF/A-3A, который подходит для архивного хранения электронных документов, после чего сохраняется окончательный PDF с вложенным ZUGFeRD. В статье завершается фрагментом кода на Python, демонстрирующим реализацию этих шагов и показывающим интеграцию ZUGFeRD с PDF для улучшенного управления документами.
---

## Прикрепить ZUGFeRD к PDF

Мы рекомендуем выполнить следующие шаги, чтобы прикрепить ZUGFeRD к PDF:

1. Импортируйте библиотеку Aspose.PDF и присвойте ей псевдоним ap для удобства.
1. Определите путь к каталогу, в котором находятся входные и выходные файлы PDF.
1. Определите путь к файлу PDF, который будет обрабатываться.
1. Загрузите файл PDF из переменной path и создайте объект Document.
1. Создайте объект FileSpecification для XML‑файла, содержащего метаданные счета. Используйте переменную path и строку‑описание для создания объекта FileSpecification.
1. Установите `mime_type` и `af_relationship` свойства объекта FileSpecification к `text/xml` и `ALTERNATIVE`, соответственно.
1. Добавьте объект fileSpecification в коллекцию встроенных файлов объекта document. Это присоединит XML‑файл к PDF‑документу в качестве файла метаданных счёта.
1. Преобразуйте PDF‑документ в формат PDF/A-3A. Используйте путь к файлу журнала, the `PdfFormat.PDF_A_3A` перечисление, и `ConvertErrorAction.DELETE` перечисление для преобразования объекта документа.
1. Сохраните PDF‑документ с присоединённым ZUGFeRD.

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
