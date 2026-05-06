---
title: Добавление вложения в PDF с помощью Python
linktitle: Добавление вложения в PDF‑документ
type: docs
weight: 10
url: /ru/python-net/add-attachment-to-pdf-document/
description: Узнайте, как добавлять файловые вложения в PDF‑документы на Python с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить вложения в PDF с помощью Python
Abstract: В этой статье представлено пошаговое руководство по добавлению вложений в PDF‑файл с использованием Python и библиотеки Aspose.PDF. Описывается процесс создания нового проекта Python, импорта необходимого пакета Aspose.PDF и создания объекта `Document`. В статье объясняется, как создать объект `FileSpecification` с нужным файлом и описанием, а также как добавить этот объект в `EmbeddedFileCollection` PDF‑документа с помощью метода `add`. `EmbeddedFileCollection` хранит все вложения в PDF. Включён фрагмент кода, демонстрирующий процесс открытия документа, подготовки файла для вложения, добавления его в коллекцию вложений документа и сохранения обновлённого PDF.
---

Вложения могут содержать широкий спектр информации и могут быть разных типов файлов. В этой статье объясняется, как добавить вложение в PDF‑файл.

Используйте встроенные вложения PDF, когда вам нужно упаковать сопутствующие исходные файлы, таблицы, изображения или связанные документы вместе с основным PDF.

1. Создайте новый проект Python.
1. Импортируйте пакет Aspose.PDF
1. Создайте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект.
1. Создайте [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) объект с файлом, который вы добавляете, и описанием файла.
1. Добавьте [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) объект к [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объекта [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) коллекция, с коллекцией [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) метод.

Эта [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) коллекция содержит все вложения в PDF‑файле. Следующий фрагмент кода показывает, как добавить вложение в PDF‑документ.

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## Связанные темы вложений

- [Работа с вложениями PDF в Python](/pdf/ru/python-net/attachments/)
- [Удалить вложения из PDF в Python](/pdf/ru/python-net/removing-attachment-from-an-existing-pdf/)
- [Создание и управление PDF‑портфолио в Python](/pdf/ru/python-net/portfolio/)

