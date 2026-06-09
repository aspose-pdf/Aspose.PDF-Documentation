---
title: 使用 Python 从 PDF 中的表格提取数据
linktitle: 从表格提取数据
type: docs
weight: 40
url: /zh/python-net/extract-data-from-table-in-pdf/
description: 了解如何使用 Aspose.PDF for Python 从 PDF 文件中提取表格数据，并导出结果以进行进一步处理。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 从 PDF 中提取表格数据
Abstract: 本文介绍了如何使用 Aspose.PDF for Python 从 PDF 文档中提取和处理表格数据。它展示了如何使用 TableAbsorber 扫描每一页，读取检测到的表格中的行和单元格，将提取限制在特定的注释区域，并将 PDF 内容导出为 CSV 格式，以便在电子表格工具和后续处理过程中使用。
---

## 以编程方式从 PDF 提取表格

使用 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 检测每页的表格 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). 在访问页面后，遍历 `table_list`, 然后遍历每一行和每个单元格，以可读的文本格式重建表格内容。

1. 将 PDF 打开为 `Document`.
1. 遍历页面 `document.pages`.
1. 创建一个 `TableAbsorber` 对每页调用 `visit(page)`.
1. 遍历检测到的表格、行和单元格。
1. 读取每个单元格中的文本片段并组装提取的行输出。

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

## 在PDF页面的特定区域提取表格

如果您只需要提取位于标记区域内的表格，请结合 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 与 [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). 在本例中，注释矩形用作边界，仅处理完全位于该区域内的表格。

1. 将 PDF 打开为 `Document`.
1. 选择目标页面。
1. 查找标记感兴趣区域的方形注释。
1. 创建一个 `TableAbsorber` 并访问该页面。
1. 将每个检测到的表格矩形与注释矩形进行比较。
1. 仅处理完全位于标记区域内的表格。

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

## 将 PDF 表格数据导出为 CSV

当您需要以电子表格友好的格式提取数据时，使用以下方式保存 PDF [Excel保存选项](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 并将输出格式设置为 CSV。生成的文件可以在 Excel、Google Sheets 中打开，或导入到分析工作流中。

1. 打开源 PDF 作为 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 创建一个 `ExcelSaveOptions` 实例。
1. 设置 `excel_save.format` 到 `ExcelSaveOptions.ExcelFormat.CSV`.
1. 将文档保存到目标 CSV 路径。

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
