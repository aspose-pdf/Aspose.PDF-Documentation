---
title: 从 PDF 中删除页面
type: docs
weight: 20
url: /zh/python-net/delete-pages-from-pdf/
description: 使用 Aspose.PDF for Python 从 PDF 文档中删除选定的页面。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中从 PDF 文档中删除特定页面
Abstract: 了解如何使用 Aspose.PDF for Python 从 PDF 文档中删除选定的页面。此示例演示如何以编程方式删除现有 PDF 文件中的特定页面，创建一个不包含已删除页面的新文档。
---

有时 PDF 文档包含不必要或敏感的页面，需要将其删除。使用 Aspose.PDF for Python，开发人员可以以编程方式从 PDF 中删除特定页面，而无需手动编辑文件。

我们的示例展示了如何使用 delete 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 用于从 PDF 文档中删除页面的类。通过指定要删除的页码，可以创建一个不包含不需要页面的新 PDF。此功能在清理报告、去除机密信息或准备自定义文档摘录时非常有用。

1. 创建一个 PdfFileEditor 对象。
1. 定义要删除的页面。
1. 删除页面。

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir


    # Delete Pages from PDF
    def delete_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        pdf_editor.delete(infile, pages_to_delete, outfile)
```