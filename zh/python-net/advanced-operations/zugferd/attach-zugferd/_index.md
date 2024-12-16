---
title: 创建符合PDF/3-A标准的PDF并在Python中附加ZUGFeRD发票
linktitle: 将ZUGFeRD附加到PDF
type: docs
weight: 10
url: /zh/python-net/attach-zugferd/
description: 了解如何通过Aspose.PDF for Python via .NET生成带有ZUGFeRD的PDF文档
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 将ZUGFeRD附加到PDF

我们建议按照以下步骤将ZUGFeRD附加到PDF：

1. 导入Aspose.PDF库，并为方便起见给它一个别名ap。
1. 定义输入和输出PDF文件所在目录的路径。
1. 定义将被处理的PDF文件的路径。
1. 从路径变量加载PDF文件并创建一个Document对象。
1. 为包含发票元数据的XML文件创建一个FileSpecification对象。使用路径变量和描述字符串来创建FileSpecification对象。

1. 将 FileSpecification 对象的 `mime_type` 和 `af_relationship` 属性分别设置为 `text/xml` 和 `ALTERNATIVE`。
1. 将 fileSpecification 对象添加到文档对象的嵌入文件集合中。这会将 XML 文件作为发票元数据文件附加到 PDF 文档中。
1. 将 PDF 文档转换为 PDF/A-3A 格式。使用日志文件的路径、`PdfFormat.PDF_A_3A` 枚举和 `ConvertErrorAction.DELETE` 枚举来转换文档对象。
1. 保存附加了 ZUGFeRD 的 PDF 文档。

```python
import aspose.pdf as ap

# 定义输入和输出 PDF 文件所在目录的路径
_dataDir = "./"

# 加载将被处理的 PDF 文件
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# 为包含发票元数据的 XML 文件创建一个 FileSpecification 对象
description = "符合 ZUGFeRD 标准的发票元数据"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# 设置嵌入文件的 MIME 类型和 AFRelationship 属性
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# 将嵌入的文件添加到 PDF 文档的嵌入文件集合中
document.embedded_files.add("factur",fileSpecification)

# 将 PDF 文档转换为 PDF/A-3A 格式
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# 保存附加了 ZUGFeRD 的 PDF 文档
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```