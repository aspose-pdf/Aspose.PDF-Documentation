---
title: 从 PDF 文档中提取表格
linktitle: 提取表格
type: docs
weight: 20
url: /zh/python-net/extracting-table/
description: Aspose.PDF for Python via .NET 使您能够对 PDF 文档中包含的表格进行各种操作。
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 从 PDF 中提取表格
Abstract: 本文讨论了使用 Python 从 PDF 文档中提取表格的过程，特别是利用 Aspose.PDF for Python via .NET 库。它提供了一个代码示例，演示如何加载 PDF 文档，遍历其页面，并使用 `TableAbsorber` 类来识别和提取表格数据。代码遍历每个表格、行和单元格，收集文本片段并打印提取的文本。该方法被强调为在 PDF 中处理表格数据的强大数据提取和分析工具。
---

## 从 PDF 中提取表格

使用 Python 从 PDF 中提取表格对于数据提取和分析非常有用。借助 Aspose.PDF for Python via .NET 库，您可以高效地处理嵌入在 PDF 文档中的表格，以完成各种数据相关任务。

此代码片段打开现有的 PDF 文件，扫描每页的表格，并提取其单元格文本内容。它使用 'TableAbsorber' 检测表格，然后遍历行和单元格，打印内部文本。

1. 将 PDF 加载到 ap.Document 对象中。
1. 循环遍历页面。
1. 创建 TableAbsorber 对象。
1. 遍历表格。
1. 遍历行和单元格。
1. 提取并打印单元格文本。

此示例读取 PDF，查找所有表格，并逐行打印其单元格内容。

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


