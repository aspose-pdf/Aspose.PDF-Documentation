---
title: 在 Python 中创建符合 PDF/3-A 标准的 PDF 并附加 ZUGFeRD 发票
linktitle: 将 ZUGFeRD 附加到 PDF
type: docs
weight: 10
url: /zh/python-net/attach-zugferd/
description: 了解如何在 Aspose.PDF for Python via .NET 中使用 ZUGFeRD 生成 PDF 文档
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何将 ZUGFeRD 附加到 PDF 文档
Abstract: 本文提供了一个分步指南，说明如何使用 Aspose.PDF 库将 ZUGFeRD（电子发票格式）附加到 PDF 文档。该过程从导入必要的库并设置输入和输出文件的目录路径开始。它涉及将目标 PDF 文件加载到 Document 对象中，并为 XML 发票元数据文件创建一个 FileSpecification 对象。关键属性如 `mime_type` 和 `af_relationship` 被设置，以确保元数据的正确集成。随后将 XML 文件添加到 PDF 的嵌入文件集合中，从而将其作为元数据附加。接下来，PDF 文档被转换为 PDF/A-3A 格式，适用于归档电子文档，然后将包含嵌入 ZUGFeRD 的最终 PDF 保存。文章最后提供了一个 Python 代码片段，演示了这些步骤的实现，展示了 ZUGFeRD 与 PDF 的集成以提升文档管理。
---

## 将 ZUGFeRD 附加到 PDF

我们建议遵循以下步骤将 ZUGFeRD 附加到 PDF：

1. 导入 Aspose.PDF 库，并为方便起见给它一个别名 ap。
1. 定义输入和输出 PDF 文件所在目录的路径。
1. 定义将要处理的 PDF 文件的路径。
1. 从 path 变量加载 PDF 文件并创建一个 Document 对象。
1. 为包含发票元数据的 XML 文件创建一个 FileSpecification 对象。使用 path 变量和描述字符串来创建该 FileSpecification 对象。
1. 设置 `mime_type` 和 `af_relationship` FileSpecification 对象的属性 `text/xml` 和 `ALTERNATIVE`，分别。
1. 将 fileSpecification 对象添加到 document 对象的嵌入文件集合中。这会将 XML 文件作为发票元数据文件附加到 PDF 文档。
1. 将 PDF 文档转换为 PDF/A-3A 格式。使用日志文件的路径， `PdfFormat.PDF_A_3A` 枚举，以及 `ConvertErrorAction.DELETE` 用于转换文档对象的枚举。
1. 将带有附加 ZUGFeRD 的 PDF 文档保存。

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
