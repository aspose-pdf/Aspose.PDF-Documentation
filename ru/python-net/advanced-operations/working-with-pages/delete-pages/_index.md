---
title: Удалить страницы PDF в Python
linktitle: Удаление страниц PDF
type: docs
weight: 80
url: /ru/python-net/delete-pages/
description: Узнайте, как удалять страницы из файлов PDF в Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить одну или несколько страниц PDF в Python
Abstract: В этой статье объясняется, как удалять страницы из файлов PDF с использованием Aspose.PDF for Python via .NET. Узнайте, как удалить одну страницу или несколько страниц из документа, используя API PageCollection, а затем сохранить обновлённый PDF.
---

Вы можете удалять страницы из файла PDF, используя Aspose.PDF for Python via .NET. Чтобы удалить определённую страницу, используйте [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) из [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Используйте этот рабочий процесс, когда вам нужно удалить ненужные страницы из PDF перед передачей, архивированием или объединением документов.

## Удалить страницу из PDF-файла

Aspose.PDF for Python via .NET удаляет страницу 2 из входного PDF и сохраняет обновленный документ в новый файл. Эта функция полезна для удаления ненужных или конфиденциальных страниц без изменения остальной части документа.

1. Загрузите входной PDF как [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Удалите страницу с помощью [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Вызовите [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод для сохранения обновлённого PDF‑файла.

Следующий фрагмент кода показывает, как удалить определённую страницу из PDF‑файла с помощью Python.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## Удалить несколько страниц из PDF‑документа

Удаление нескольких страниц позволяет удалить набор указанных страниц за одну операцию, что эффективнее, чем удалять страницы по одной. Полученный PDF сохраняется в новый файл, при этом оригинальный документ сохраняется.

1. Загрузите входной PDF как [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Удалите страницы, указанные в массиве pages, используя [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохранить обновленное [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в новый файл.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Добавить страницы PDF в Python](/pdf/ru/python-net/add-pages/)
- [Переместить страницы PDF в Python](/pdf/ru/python-net/move-pages/)
- [Извлечь страницы PDF в Python](/pdf/ru/python-net/extract-pages/)
