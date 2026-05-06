---
title: Извлечь таблицу из PDF-документа
linktitle: Извлечь таблицу
type: docs
weight: 20
url: /ru/python-net/extracting-table/
description: Узнайте, как извлекать данные таблиц из существующих PDF-документов на Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь таблицу из PDF с помощью Python
Abstract: В этой статье рассматривается процесс извлечения таблиц из PDF‑документов с помощью Python, с особым использованием библиотеки Aspose.PDF for Python via .NET. Приводится пример кода, демонстрирующий, как загрузить PDF‑документ, пройтись по его страницам и использовать класс `TableAbsorber` для идентификации и извлечения данных таблицы. Код проходит по каждой таблице, строке и ячейке, собирает фрагменты текста и выводит извлечённый текст. Этот метод отмечен как мощный инструмент для задач извлечения и анализа данных, связанных с табличными данными в PDF.
---

## Извлечь таблицу из PDF

Извлечение таблиц из PDF с помощью Python может быть чрезвычайно полезным для извлечения и анализа данных. С библиотекой Aspose.PDF for Python via .NET вы можете эффективно работать с таблицами, встроенными в PDF‑документы, для различных задач, связанных с данными.

Этот фрагмент кода открывает существующий PDF‑файл, сканирует каждую страницу в поисках таблиц и извлекает текстовое содержимое их ячеек. Он использует 'TableAbsorber' для обнаружения таблиц, а затем перебирает строки и ячейки, выводя содержащийся в них текст.

1. Загружает PDF в объект ap.Document.
1. Перебирает страницы.
1. Создаёт объект TableAbsorber.
1. Перебирает таблицы.
1. Итерируйте строки и ячейки.
1. Извлеките и выведите текст из ячеек.

Этот пример читает PDF, находит все таблицы и выводит содержимое их ячеек построчно.

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## Связанные темы таблицы

- [Работа с таблицами в PDF с использованием Python](/pdf/ru/python-net/working-with-tables/)
- [Добавить таблицы в PDF с помощью Python](/pdf/ru/python-net/adding-tables/)
- [Интегрировать таблицы PDF с источниками данных](/pdf/ru/python-net/integrate-table/)
- [Удалить таблицы из существующих PDF](/pdf/ru/python-net/removing-tables/)