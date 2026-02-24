---
title: 在 Python 中创建符合 PDF/3-A 标准的 PDF 并附加 ZUGFeRD 发票
linktitle: 将 ZUGFeRD 附加到 PDF
type: docs
weight: 10
url: /zh/python-net/attach-zugferd/
description: 了解如何在 Aspose.PDF for Python via .NET 中生成带有 ZUGFeRD 的 PDF 文档
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何将 ZUGFeRD 附加到 PDF 文档
Abstract: 本文提供了使用 Aspose.PDF 库将 ZUGFeRD（电子发票的一种格式）附加到 PDF 文档的分步指南。该过程首先导入必要的库并设置输入和输出文件的目录路径。随后将目标 PDF 文件加载到 Document 对象中，并为 XML 发票元数据文件创建 FileSpecification 对象。设置 `mime_type` 和 `af_relationship` 等关键属性，以确保元数据的正确集成。然后将 XML 文件添加到 PDF 的嵌入文件集合中，从而将其作为元数据附加。接下来，将 PDF 文档转换为 PDF/A-3A 格式，该格式适用于归档电子文档，最后保存包含嵌入 ZUGFeRD 的最终 PDF。文章最后提供了一个 Python 代码片段，演示了这些步骤的实现，展示了 ZUGFeRD 与 PDF 的集成，以增强文档管理。
---

## 将 ZUGFeRD 附加到 PDF

我们推荐以下步骤将 ZUGFeRD 附加到 PDF：

1. 导入 Aspose.PDF 库，并为方便起见给它起别名 ap。
1. 定义输入和输出 PDF 文件所在目录的路径。
1. 定义要处理的 PDF 文件的路径。
1. 从路径变量加载 PDF 文件并创建 Document 对象。
1. 为包含发票元数据的 XML 文件创建 FileSpecification 对象。使用路径变量和描述字符串来创建该对象。
1. 将 FileSpecification 对象的 `mime_type` 和 `af_relationship` 属性分别设置为 `text/xml` 和 `ALTERNATIVE`。
1. 将 fileSpecification 对象添加到 Document 对象的嵌入文件集合中。这会将 XML 文件作为发票元数据文件附加到 PDF 文档。
1. 将 PDF 文档转换为 PDF/A-3A 格式。使用日志文件路径、`PdfFormat.PDF_A_3A` 枚举以及 `ConvertErrorAction.DELETE` 枚举来转换 Document 对象。
1. 保存带有已附加 ZUGFeRD 的 PDF 文档。

```python
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```

