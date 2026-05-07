---
title: Управление таблицами в существующем PDF
linktitle: Управление таблицами
type: docs
weight: 40
url: /ru/python-net/manipulating-tables/
description: Узнайте, как просматривать и изменять таблицы в существующих PDF‑документах с помощью Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Измените существующие таблицы PDF с помощью Python
Abstract: В этой статье объясняется, как управлять таблицами, уже присутствующими в PDF‑документах, с использованием Aspose.PDF for Python via .NET. Узнайте, как находить таблицы с помощью TableAbsorber, получать доступ к конкретным строкам и ячейкам, обновлять текстовое содержимое таблиц и сохранять изменённый PDF в Python.
---

## Управление таблицами в существующем PDF

Aspose.PDF for Python via .NET позволяет обновлять таблицы, которые уже существуют в PDF‑документе. Вы можете использовать [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) класс для поиска таблиц на странице, доступа к строкам и ячейкам, изменения текстового содержимого и сохранения обновлённого файла.

Используйте эту страницу, когда необходимо обновить существующее содержимое таблиц в PDF без воссоздания полной компоновки документа.

## Поиск и замена текста в ячейках таблицы PDF

В этом примере находится первая таблица на странице 1, осуществляется доступ к первой ячейке, её текст заменяется, и сохраняется результирующий PDF.

1. Откройте входной PDF.
1. Создайте TableAbsorber и перейдите к странице 1.
1. Убедитесь, что обнаружена хотя бы одна таблица.
1. Получите первую ячейку в первой строке первой таблицы.
1. Убедитесь, что ячейка содержит фрагменты текста, затем обновите первый фрагмент.
1. Сохраните модифицированный PDF.

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## Заменить существующую таблицу новой таблицей

Вы также можете заменить обнаруженную таблицу вновь созданной. Этот подход полезен, когда необходимо изменить и структуру, и содержание.

Код ниже открывает PDF, находит первую таблицу на странице 1, создает заменяющую таблицу, меняет старую таблицу на новую и сохраняет результат.

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## Другие темы по таблицам

- [Работа с таблицами в PDF с использованием Python](/pdf/ru/python-net/working-with-tables/)
- [Добавить таблицы в PDF с помощью Python](/pdf/ru/python-net/adding-tables/)
- [Извлекать таблицы из PDF‑документов](/pdf/ru/python-net/extracting-table/)
- [Удалить таблицы из существующих PDF](/pdf/ru/python-net/removing-tables/)
