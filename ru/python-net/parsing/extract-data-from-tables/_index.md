---
title: Извлечение данных из таблицы в PDF с помощью Python
linktitle: Извлечение данных из таблицы
type: docs
weight: 40
url: /ru/python-net/extract-data-from-table-in-pdf/
description: Узнайте, как извлекать табличные данные из PDF-файлов с помощью Aspose.PDF for Python и экспортировать результаты для дальнейшей обработки.
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь данные из таблицы в PDF через Python
Abstract: Эта статья объясняет, как извлекать и обрабатывать табличные данные из PDF-документов с помощью Aspose.PDF for Python. В ней показано, как сканировать каждую страницу с помощью TableAbsorber, читать строки и ячейки из найденных таблиц, ограничивать извлечение определённой размеченной областью и экспортировать содержимое PDF в формат CSV для использования в табличных инструментах и последующей обработке.
---

## Извлеките таблицы из PDF программно

Используйте [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/), чтобы находить таблицы на каждой странице [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). После обхода страницы переберите `table_list`, затем последовательно пройдите по строкам и ячейкам, чтобы восстановить содержимое таблицы в удобном текстовом виде.

1. Откройте PDF как `Document`.
1. Переберите страницы в `document.pages`.
1. Создайте `TableAbsorber` для каждой страницы и вызовите `visit(page)`.
1. Переберите найденные таблицы, строки и ячейки.
1. Прочитайте текстовые фрагменты из каждой ячейки и соберите результат по строкам.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Извлеките таблицу из определённой области PDF-страницы

Если нужно извлекать только таблицы, расположенные внутри отмеченной области, объедините [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) с [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). В этом примере прямоугольник аннотации используется как граница, и обрабатываются только таблицы, полностью находящиеся внутри неё.

1. Откройте PDF как `Document`.
1. Выберите целевую страницу.
1. Найдите квадратную аннотацию, которая отмечает интересующую область.
1. Создайте `TableAbsorber` и обработайте страницу.
1. Сравните прямоугольник каждой найденной таблицы с прямоугольником аннотации.
1. Обработайте только таблицы, полностью попадающие в отмеченную область.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Экспортируйте табличные данные из PDF в CSV

Если извлечённые данные должны использоваться в табличном формате, сохраните PDF с помощью [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) и укажите формат вывода CSV. Полученный файл можно открыть в Excel, Google Sheets или импортировать в аналитические процессы.

1. Откройте исходный PDF как [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте экземпляр `ExcelSaveOptions`.
1. Установите `excel_save.format` в `ExcelSaveOptions.ExcelFormat.CSV`.
1. Сохраните документ по целевому пути CSV.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
