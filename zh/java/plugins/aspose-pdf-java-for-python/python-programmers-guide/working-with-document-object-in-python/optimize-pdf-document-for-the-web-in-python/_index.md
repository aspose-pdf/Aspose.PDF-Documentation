---
title: 使用 Python 优化 Web PDF 文档
linktitle: 使用 Python 优化 Web PDF 文档
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-python/
description: 了解如何使用 Aspose.PDF 优化 PDF 文件，以便在 Python 中更快地加载网页，从而改善用户体验和性能。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 优化 Web PDF 文档，只需调用 **Optimize** 类的 **optimize_web** 方法即可。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimize for web
doc.optimize();

#Save output document
doc.save(self.dataDir + "Optimized_Web.pdf")

print "Optimized PDF for the Web, please check output file."
```

**下载运行代码**

从以下任何一个社交编码网站下载**优化 Web PDF (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
