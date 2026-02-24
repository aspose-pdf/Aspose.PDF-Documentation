---
title: 从现有 PDF 中删除表格
linktitle: 删除表格
type: docs
weight: 50
url: /zh/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 删除 PDF 中的表格
Abstract: 本文讨论了 Aspose.PDF for Python via .NET 的功能，特别关注 PDF 文档中表格的操作。该库允许用户在新建和现有 PDF 文件中插入或创建表格，并能够对现有 PDF 中的表格进行操作或删除。文章介绍了 `TableAbsorber` 类，它在识别和处理 PDF 中的表格方面至关重要。新增了 `remove()` 方法，以实现表格的删除。文档提供了两个代码片段——一个演示如何从 PDF 中删除单个表格，另一个演示如何删除多个表格。这些示例突出了 `TableAbsorber` 类在实现 PDF 文档表格删除中的实际应用。
---

## 从 PDF 文档中删除表格

Aspose.PDF for Python 允许您从 PDF 中删除表格。它打开现有的 PDF，使用 TableAbsorber 检测第一页面的第一个表格，使用 [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) 删除该表格。保存更新后的 PDF 到新文件。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## 从 PDF 文档中删除所有表格

使用我们的库，您可以从 PDF 的特定页面中删除所有表格。代码打开现有的 PDF，使用 TableAbsorber 检测第二页面的所有表格，遍历检测到的表格，逐一删除，然后将修改后的 PDF 保存到新文件。当您需要批量删除页面上的表格而保持 PDF 其余内容完整时，这非常有用。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


