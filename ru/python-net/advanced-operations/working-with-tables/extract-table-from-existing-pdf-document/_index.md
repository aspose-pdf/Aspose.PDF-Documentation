---
title: Извлечь таблицу из PDF‑документа
linktitle: Извлечь таблицу
type: docs
weight: 20
url: /ru/python-net/extracting-table/
description: Aspose.PDF for Python через .NET позволяет выполнять различные операции с таблицами, содержащимися в вашем PDF‑документе.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь таблицу из PDF с помощью Python
Abstract: В этой статье рассматривается процесс извлечения таблиц из PDF‑документов с использованием Python, в частности с применением библиотеки Aspose.PDF for Python via .NET. Приводится пример кода, демонстрирующий, как загрузить PDF‑документ, пройтись по его страницам и использовать класс `TableAbsorber` для обнаружения и извлечения данных таблицы. Код перебирает каждую таблицу, строку и ячейку, собирает фрагменты текста и выводит извлечённый текст. Этот метод отмечен как мощный инструмент для задач извлечения и анализа данных, связанных с табличными данными в PDF.
---

## Извлечение таблицы из PDF

Извлечение таблиц из PDF с помощью Python может быть чрезвычайно полезным для извлечения и анализа данных. С библиотекой Aspose.PDF for Python via .NET вы можете эффективно работать с таблицами, встроенными в PDF‑документы, для различных задач, связанных с данными.

Этот фрагмент кода открывает существующий PDF‑файл, сканирует каждую страницу в поисках таблиц и извлекает текстовое содержимое их ячеек. Он использует `TableAbsorber` для обнаружения таблиц, а затем проходит по строкам и ячейкам, выводя текст внутри.

1. Загружает PDF в объект ap.Document.
1. Проходит по страницам.
1. Создаёт объект TableAbsorber.
1. Перебирает таблицы.
1. Перебирает строки и ячейки.
1. Извлекает и выводит текст из ячеек.

В этом примере читается PDF, находятся все таблицы, и их содержимое ячеек выводится построчно.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```


