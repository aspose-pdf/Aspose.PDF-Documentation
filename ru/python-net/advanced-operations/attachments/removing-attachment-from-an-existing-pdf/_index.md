---
title: Удаление вложения из PDF с помощью Python
linktitle: Удаление вложения из существующего PDF
type: docs
weight: 30
url: /ru/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF может удалять вложения из ваших PDF‑документов. Используйте Python PDF API для удаления вложений в PDF‑файлах с помощью библиотеки Aspose.PDF for Python via .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как удалить вложения из PDF с помощью Python
Abstract: В этой статье рассматривается, как удалить вложения из PDF‑файлов с помощью Aspose.PDF for Python. Вложения в PDF‑документе хранятся в коллекции `EmbeddedFiles` объекта `Document`. Чтобы удалить все вложения из PDF, можно вызвать метод `delete()` у коллекции `EmbeddedFiles`, а затем сохранить обновлённый документ, используя метод `save()` объекта `Document`. Приведен фрагмент кода, демонстрирующий этот процесс, показывающий шаги открытия документа, удаления его вложений и сохранения изменённого файла.
---

Aspose.PDF for Python может удалять вложения из PDF‑файлов. Вложения PDF‑документа находятся в коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) объекта Document.

Чтобы удалить все вложения, связанные с PDF‑файлом:

1. Вызовите метод [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/).
1. Сохраните обновлённый файл, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Следующий фрагмент кода демонстрирует, как удалить вложения из PDF‑документа.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


