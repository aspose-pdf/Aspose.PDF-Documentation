---
title: 使用 Python 从 PDF 中提取表格数据
linktitle: 提取表格
type: docs
weight: 40
url: /zh/python-net/extract-data-from-table-in-pdf/
description: 了解如何使用 Aspose.PDF for Python 从 PDF 中提取表格
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Python 从 PDF 中提取表格数据
Abstract: 本文提供了使用 Aspose.PDF（一个 Python 库）对 PDF 文档中的表格进行编程提取和处理的完整指南。文章展示了一个 Python 脚本，该脚本打开 PDF 文档，遍历每一页，并通过使用 `TableAbsorber` 类来提取表格。提取的表格数据随后被结构化并打印，以便进一步分析。本节描述了如何从 PDF 中的特定标记区域（例如由方形批注围住的区域）提取表格。脚本识别这些批注，初始化 `TableAbsorber`，并在提取并打印数据之前检查表格是否位于批注区域内。最后一节详细说明了将从 PDF 中提取的表格数据转换为 CSV 文件格式的方法。
---

## 以编程方式提取 PDF 表格

此代码提取 PDF 表格并将 PDF 文件中的表格数据转换为可读且结构化的格式，以便进一步处理或分析。

1. 打开 PDF 文档
1. 遍历 PDF 页面
1. 提取表格数据

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

## 在 PDF 页面特定区域提取表格

此代码片段从 PDF 的特定标记区域提取表格数据，例如高亮框或特定批注内的数据。

1. 打开 PDF 文档
1. 获取第一页
1. 查找第一个方形批注
1. 初始化 TableAbsorber
1. 遍历页面上的表格
1. 检查表格是否在批注区域内

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

## 从 PDF 提取表格数据并存储到 Excel 文件

以下代码片段从 PDF 中提取表格数据，并将其导出为 CSV 文件，以便在 Excel 或 Google 表格等电子表格应用中进一步分析或处理。

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

