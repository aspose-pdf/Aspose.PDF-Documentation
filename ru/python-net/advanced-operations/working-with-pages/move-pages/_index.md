---
title: Переместить страницы PDF в Python
linktitle: Перемещение страниц PDF
type: docs
weight: 100
url: /ru/python-net/move-pages/
description: Узнайте, как перемещать страницы PDF внутри документа или между документами в Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переместить страницы PDF между документами в Python
Abstract: В этой статье объясняется, как перемещать страницы в PDF с помощью Aspose.PDF for Python via .NET. Узнайте, как переместить одну страницу или несколько страниц в другой документ, а также как изменить положение страницы в том же PDF, используя API Document и PageCollection.
---

## Переместить страницу из одного PDF‑документа в другой

Aspose.PDF for Python позволяет переместить страницу (а не только скопировать её) из одного PDF в другой. Она удаляет выбранную страницу из оригинального документа, а затем добавляет её в новый PDF‑файл.

Можно представить это как вырезание страницы из одной книги и приклеивание её в другую — страница больше не существует в оригинальном файле после перемещения.

1. Откройте исходный PDF‑документ, используя [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Выберите конкретную страницу для перемещения (в данном случае, страница 2) — это относится к [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Создайте новый PDF‑документ (создайте еще один [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Добавьте выбранную страницу в новый PDF‑документ, используя документ‑назначения [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (например, `another_document.pages.add(page)`).
1. Удалите страницу из исходного документа через его [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (например, `document.pages.delete(index)`).
1. Сохраните оба документа.

Следующий фрагмент кода показывает, как переместить одну страницу.

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## Переместить несколько страниц из одного PDF‑документа в другой

В отличие от копирования, эта операция перемещает выбранные страницы — удаляя их из исходного файла и сохраняя в новом PDF.

1. Создайте новый, пустой документ назначения (`Document`).
1. Выберите несколько страниц (в данном случае страницы 1 и 3) из исходного документа [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Пройдитесь по выбранным страницам и добавьте каждую в документ назначения [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните целевой документ, содержащий перемещённые страницы.
1. Удалите перемещённые страницы из исходного документа, используя его [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните изменённый исходный документ под новым именем файла, чтобы сохранить обе версии.

Следующий фрагмент кода показывает, как переместить несколько страниц.

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## Переместить страницу в новое место в том же PDF Document

Показано, как переместить определённую страницу в другое положение внутри того же документа — распространённая необходимость при реорганизации или редактировании макетов PDF.

1. Загрузите входной документ PDF, используя [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Выберите страницу, которую хотите переместить (страница 2) — это [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Добавьте её в конец документа, используя [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Удалите оригинальную страницу из её предыдущего местоположения через [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Сохраните изменённый документ как новый файл.

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Добавить страницы PDF в Python](/pdf/ru/python-net/add-pages/)
- [Удалить страницы PDF в Python](/pdf/ru/python-net/delete-pages/)
- [Извлечь страницы PDF в Python](/pdf/ru/python-net/extract-pages/)
