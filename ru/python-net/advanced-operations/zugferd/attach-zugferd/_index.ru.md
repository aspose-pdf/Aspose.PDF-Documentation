---
title: Создание PDF/3-A совместимого PDF и прикрепление счета ZUGFeRD на Python
linktitle: Прикрепить ZUGFeRD к PDF
type: docs
weight: 10
url: /python-net/attach-zugferd/
description: Узнайте, как создать PDF-документ с ZUGFeRD в Aspose.PDF для Python через .NET
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Прикрепить ZUGFeRD к PDF

Рекомендуем следующие шаги для прикрепления ZUGFeRD к PDF:

1. Импортируйте библиотеку Aspose.PDF и дайте ей псевдоним ap для удобства.
1. Определите путь к каталогу, где расположены входные и выходные PDF-файлы.
1. Определите путь к PDF-файлу, который будет обработан.
1. Загрузите PDF-файл из переменной пути и создайте объект Document.
1. Создайте объект FileSpecification для XML-файла, содержащего метаданные счета. Используйте переменную пути и строку описания для создания объекта FileSpecification.

1. Установите свойства `mime_type` и `af_relationship` объекта FileSpecification в `text/xml` и `ALTERNATIVE`, соответственно.
1. Добавьте объект fileSpecification в коллекцию встроенных файлов объекта документа. Это прикрепляет XML файл к PDF документу в качестве файла метаданных счета.
1. Преобразуйте PDF документ в формат PDF/A-3A. Используйте путь к файлу журнала, перечисление `PdfFormat.PDF_A_3A` и перечисление `ConvertErrorAction.DELETE` для преобразования объекта документа.
1. Сохраните PDF документ с прикрепленным ZUGFeRD.

```python
import aspose.pdf as ap

# Определите путь к каталогу, где находятся входные и выходные PDF файлы
_dataDir = "./"

# Загрузите PDF файл, который будет обработан
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Создайте объект FileSpecification для XML файла, содержащего метаданные счета
description = "Метаданные счета, соответствующие стандарту ZUGFeRD"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Установите MIME тип и свойства AFRelationship встроенного файла
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Добавьте встроенный файл в коллекцию встроенных файлов PDF документа
document.embedded_files.add("factur",fileSpecification)

# Преобразуйте PDF документ в формат PDF/A-3A
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Сохраните PDF документ с прикрепленным ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```