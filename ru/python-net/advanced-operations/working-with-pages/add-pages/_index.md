---
title: Добавить страницы PDF в Python
linktitle: Добавление страниц
type: docs
weight: 10
url: /ru/python-net/add-pages/
description: Узнайте, как добавлять или вставлять страницы в PDF‑документы с помощью Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавляйте или вставляйте PDF‑страницы с помощью Python
Abstract: В этой статье объясняется, как добавлять страницы в PDF‑файлы с помощью Aspose.PDF for Python via .NET. Узнайте, как вставлять пустые страницы в определённые позиции, добавлять страницы в конец документа и импортировать страницу из другого PDF, используя API Document и PageCollection.
---

Aspose.PDF for Python via .NET предоставляет гибкие операции на уровне страниц для PDF‑документов. Вы можете управлять страницами через [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) и добавлять страницы в [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в определённых позициях или в конце файла.

Используйте эту страницу, когда необходимо вставить новые пустые страницы в существующий PDF или добавить страницы в конец Document во время рабочих процессов генерации.

## Добавить или вставить страницы в PDF-файл

Aspose.PDF for Python via .NET поддерживает как вставку страниц по указанному индексу, так и добавление страниц в конец PDF.

### Вставить пустую страницу в PDF‑файл

Чтобы вставить пустую страницу в PDF‑файл:

1. Откройте существующий [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя соответствующие методы.
1. Вставьте новую пустую страницу в определённый индекс, используя [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` метод.
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в желаемый путь вывода.

Вставьте пустую страницу в существующий PDF-файл в указанной позиции:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Добавить пустую страницу в конец PDF‑файла

Иногда вы хотите убедиться, что документ заканчивается пустой страницей. Эта тема объясняет, как вставить пустую страницу в конец PDF‑документа.

Чтобы вставить пустую страницу в конец PDF‑файла:

1. Откройте существующий [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя соответствующие методы.
1. Добавьте новую пустую страницу в конец документа, используя [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` метод.
1. Сохраните обновленное [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

В следующем фрагменте кода показано, как вставить пустую страницу в конец PDF‑файла.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### Добавить страницу из другого PDF‑документа

С помощью Aspose.PDF for Python via .NET вы можете создать новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), добавить начальную страницу, а затем импортировать страницу из другого PDF в неё.

1. Создайте новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Добавьте новый пустой [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) и написать некоторый текст на нём, используя [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Откройте другой существующий [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Скопируйте [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) из этого документа.
1. Вставьте скопированную страницу в основной документ, используя [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните объединённый файл.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Переместить страницы PDF в Python](/pdf/ru/python-net/move-pages/)
- [Удалить страницы PDF в Python](/pdf/ru/python-net/delete-pages/)
- [Извлечь страницы PDF в Python](/pdf/ru/python-net/extract-pages/)
