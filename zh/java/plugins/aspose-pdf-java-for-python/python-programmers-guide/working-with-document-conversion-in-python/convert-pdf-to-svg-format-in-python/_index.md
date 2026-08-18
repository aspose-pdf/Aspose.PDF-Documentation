---
title: 在 Python 中将 PDF 转换为 SVG 格式
linktitle: 在 Python 中将 PDF 转换为 SVG 格式
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
description: 了解如何在 Python 中使用 Aspose.PDF 将 PDF 文档转换为 SVG 格式，以实现可扩展的矢量输出。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 将 PDF 转换为 SVG 格式，只需调用 **PdfToSvg** 模块即可。

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

从以下任何社交编码网站下载**将 PDF 转换为 SVG 格式 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
