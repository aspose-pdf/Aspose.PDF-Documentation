---
title: Создание PDF/3-A совместимого PDF и прикрепление счета ZUGFeRD в Python
linktitle: Прикрепить ZUGFeRD к PDF
type: docs
weight: 10
url: /ru/python-net/attach-zugferd/
description: Узнайте, как создать PDF‑документ с ZUGFeRD в Aspose.PDF для Python через .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как прикрепить ZUGFeRD к PDF‑документу
Abstract: Статья предоставляет пошаговое руководство о том, как прикрепить ZUGFeRD (формат электронных счетов) к PDF‑документу с использованием библиотеки Aspose.PDF. Процедура начинается с импорта необходимой библиотеки и настройки путей к каталогам входных и выходных файлов. Затем загружается целевой PDF‑файл в объект Document и создаётся объект FileSpecification для XML‑файла с метаданными счета. Ключевые свойства, такие как `mime_type` и `af_relationship`, устанавливаются для обеспечения корректной интеграции метаданных. XML‑файл добавляется в коллекцию вложенных файлов PDF, эффективно прикрепляя его как метаданные счета. Затем PDF‑документ конвертируется в формат PDF/A-3A, подходящий для архивирования электронных документов, после чего сохраняется окончательный PDF с вложенным ZUGFeRD. Статья завершается фрагментом кода на Python, демонстрирующим реализацию этих шагов и показывающим интеграцию ZUGFeRD с PDF для улучшенного управления документами.
---

## Прикрепить ZUGFeRD к PDF

Мы рекомендуем выполнить следующие шаги для прикрепления ZUGFeRD к PDF:

1. Импортируйте библиотеку Aspose.PDF и дайте ей псевдоним ap для удобства.
1. Укажите путь к каталогу, где находятся входные и выходные PDF‑файлы.
1. Укажите путь к PDF‑файлу, который будет обрабатываться.
1. Загрузите PDF‑файл из переменной пути и создайте объект Document.
1. Создайте объект FileSpecification для XML‑файла, содержащего метаданные счета. Используйте переменную пути и строку описания для создания объекта FileSpecification.
1. Установите свойства `mime_type` и `af_relationship` объекта FileSpecification в значения `text/xml` и `ALTERNATIVE` соответственно.
1. Добавьте объект fileSpecification в коллекцию вложенных файлов объекта document. Это прикрепит XML‑файл к PDF‑документу в качестве файла метаданных счета.
1. Преобразуйте PDF‑документ в формат PDF/A-3A. Используйте путь к файлу журнала, перечисление `PdfFormat.PDF_A_3A` и перечисление `ConvertErrorAction.DELETE` для преобразования объекта документа.
1. Сохраните PDF‑документ с прикреплённым ZUGFeRD.

```python
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```

