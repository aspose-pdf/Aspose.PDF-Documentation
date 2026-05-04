---
title: Удалить вложения из PDF с помощью Python
linktitle: Удаление вложения из существующего PDF
type: docs
weight: 30
url: /python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF может удалять вложения из ваших PDF‑документов. Используйте Python PDF API для удаления вложений в PDF‑файлах с помощью библиотеки Aspose.PDF for Python via .NET.
lastmod: "2026-04-26"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как удалить вложения из PDF с помощью Python
Abstract: Эта статья рассматривает, как удалять вложения из PDF‑файлов с помощью Aspose.PDF for Python. Вложения в PDF‑документе хранятся в коллекции `EmbeddedFiles` объекта `Document`. Чтобы удалить все вложения из PDF, вы можете вызвать метод `delete()` у коллекции `EmbeddedFiles`, а затем сохранить обновлённый документ, используя метод `save()` объекта `Document`. Приведен фрагмент кода, демонстрирующий этот процесс, показывающий шаги открытия документа, удаления его вложений и сохранения изменённого файла.
---

Aspose.PDF for Python может удалять вложения из PDF‑файлов. Вложения PDF‑документа хранятся в объекте Document [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) коллекция.

Этот рабочий процесс полезен, когда необходимо очистить устаревшие встроенные файлы, уменьшить размер пакета или подготовить PDF для повторного распространения без прикреплённого исходного материала.

Чтобы удалить все вложения, связанные с файлом PDF:

1. Вызовите [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) коллекции [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) метод.
1. Сохраните обновлённый файл, используя [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объекта [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод.

Следующий фрагмент кода показывает, как удалить вложения из PDF‑документа.

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## Удалить конкретное вложение по имени

Если вам нужно удалить только одно вложение и оставить остальные, используйте [delete_by_key()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) метод и передайте имя вложения.

Чтобы удалить конкретное вложение:

1. Откройте исходный PDF‑файл.
1. Вызов `document.embedded_files.delete_by_key(attachment_name)`.
1. Сохраните обновлённый файл PDF.

Следующий фрагмент кода удаляет одно вложение по его имени.

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## Связанные темы вложений

- [Работа с вложениями PDF в Python](/pdf/ru/python-net/attachments/)
- [Добавить вложения в PDF с помощью Python](/pdf/ru/python-net/add-attachment-to-pdf-document/)
- [Создание и управление PDF‑портфолио в Python](/pdf/ru/python-net/portfolio/)

