---
title: Извлечение данных из таблицы в PDF с помощью Python
linktitle: Извлечение данных из таблицы
type: docs
weight: 40
url: /ru/python-net/extract-data-from-table-in-pdf/
description: Узнайте, как извлекать табличные данные из PDF с помощью Aspose.PDF для Python
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь данные из таблицы в PDF с помощью Python
Abstract: Эта статья предоставляет всестороннее руководство по программному извлечению и обработке таблиц из PDF‑документов с использованием Aspose.PDF, библиотеки Python. В статье представлен Python‑скрипт, который открывает PDF‑документ, проходит по каждой странице и извлекает таблицы с помощью класса `TableAbsorber`. Извлечённые данные таблиц затем структурируются и выводятся для дальнейшего анализа. Этот раздел описывает, как извлекать таблицы из конкретных помеченных областей внутри PDF, таких как зоны, ограниченные квадратными аннотациями. Скрипт идентифицирует эти аннотации, инициализирует `TableAbsorber` и проверяет, находятся ли таблицы внутри аннотированных регионов, прежде чем извлечь и вывести данные. Последний раздел подробно объясняет метод конвертации извлечённых табличных данных из PDF в формат CSV.
---

## Программное извлечение таблиц из PDF

Этот код извлекает таблицы из PDF и преобразует табличные данные из PDF‑файла в удобочитаемый и структурированный формат для дальнейшей обработки или анализа.

1. Открытие PDF‑документа
1. Перебор страниц PDF
1. Извлечение данных таблицы

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Iterate through each page in the document
    for page in document.pages:
        absorber = apdf.text.TableAbsorber()
        absorber.visit(page)

        for table in absorber.table_list:
            print("Table")
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Извлечение таблицы в определённой области страницы PDF

Этот фрагмент кода извлекает табличные данные из конкретных помеченных областей в PDF, например данные внутри выделенного бокса или определённой аннотации.

1. Открыть PDF‑документ
1. Получить первую страницу
1. Найти первую квадратную аннотацию
1. Инициализировать TableAbsorber
1. Перебрать таблицы на странице
1. Проверить, находится ли таблица внутри области аннотации

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Get the first page (index starts from 1 in Aspose.PDF)
    page = document.pages[1]

    # Find the first square annotation
    square_annotation = next(
        (
            ann
            for ann in page.annotations
            if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
        ),
        None,
    )

    if square_annotation is None:
        print("No square annotation found.")
        return

    # Initialize the TableAbsorber
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    # Iterate through tables on the page
    for table in absorber.table_list:
        table_rect = table.rectangle
        annotation_rect = square_annotation.rect

        # Check if the table is inside the annotation region
        is_in_region = (
            annotation_rect.llx < table_rect.llx
            and annotation_rect.lly < table_rect.lly
            and annotation_rect.urx > table_rect.urx
            and annotation_rect.ury > table_rect.ury
        )

        if is_in_region:
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Извлечение данных таблицы из PDF и сохранение в файл Excel

Следующий фрагмент кода извлекает табличные данные из PDF и экспортирует их в файл CSV для дальнейшего анализа или обработки в табличных приложениях, таких как Excel или Google Sheets.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```

