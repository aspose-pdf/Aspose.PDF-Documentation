---
title: Манипулировать таблицами в существующем PDF
linktitle: Манипулировать таблицами
type: docs
weight: 40
url: /ru/python-net/manipulating-tables/
description: Узнайте, как работать с таблицами в существующих PDF с помощью Aspose.PDF for Python via .NET, обеспечивая гибкость в изменении документов.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Манипулировать таблицами в существующем PDF

Aspose.PDF for Python показывает, как изменить содержимое конкретной ячейки в таблице PDF‑документа. Он использует класс TableAbsorber для поиска таблиц на первой странице, получает определённый текстовый фрагмент внутри первой ячейки первой таблицы, обновляет его текст и сохраняет изменённый PDF в новый файл.

1. Откройте PDF‑файл, используя 'ap.Document()'.
1. Создайте объект TableAbsorber для обнаружения таблиц в PDF.
1. Вызывается absorber.visit() для поиска всех таблиц на первой странице.
1. Доступ к конкретному текстовому фрагменту:
- Получает первую таблицу.
- Получает первую строку таблицы.
- Выбирает второй текстовый фрагмент в ячейке.
1. Измените текст.
1. Сохраните обновлённый PDF.
1. Выводит подтверждение сохранения файла.

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## Заменить старую таблицу новой в PDF‑документе

Aspose.PDF позволяет заменить существующую таблицу в PDF новой таблицей. Фрагмент кода открывает PDF, определяет первую таблицу на первой странице с помощью TableAbsorber, создаёт новую таблицу с пользовательскими ширинами столбцов и содержимым, а затем заменяет оригинальную таблицу новой. В конце сохраняет обновлённый PDF в новый файл.

Он демонстрирует, как изменять структуру и содержимое таблицы в PDF, не затрагивая остальную часть документа.

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

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

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
