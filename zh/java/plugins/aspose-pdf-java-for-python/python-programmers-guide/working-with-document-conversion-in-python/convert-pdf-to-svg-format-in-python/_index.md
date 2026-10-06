---
title: 在 Python 中将 PDF 转换为 SVG 格式
linktitle: 在 Python 中将 PDF 转换为 SVG 格式
type: docs
weight: 30
url: /zh/java/convert-pdf-to-svg-format-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中将 PDF 文档转换为 SVG 格式，以实现可伸缩的矢量输出。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 将 PDF 转换为 SVG 格式，只需调用 **PdfToSvg** 模块。

```python

# Open the target document
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instantiate an object of SvgSaveOptions
save_options = self.SvgSaveOptions()

# do not compress SVG image to Zip archive
save_options.CompressOutputToZipArchive = False;

# Save the output to XLS format
doc.save(self.dataDir + "Output1.svg", save_options)

print "Document has been converted successfully"
```

**下载运行代码**

下载\u0412\u00A0**Convert PDF to SVG Format (Aspose.PDF)**\u0412\u00A0来自\u0412\u00A0以下任意提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
