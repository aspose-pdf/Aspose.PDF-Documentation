---
title: 在 Python 中针对 Web 优化 PDF 文档
linktitle: 在 Python 中针对 Web 优化 PDF 文档
type: docs
weight: 60
url: /zh/java/optimize-pdf-document-for-the-web-in-python/
description: 了解如何在 Python 中使用 Aspose.PDF 优化 PDF 文件以实现更快的 Web 加载，从而提升用户体验和性能。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 对 Web 优化 PDF 文档，只需调用 **optimize_web** 方法 ofВ  **Optimize** 类。

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

下载В **Optimize PDF for Web (Aspose.PDF)**В 来自В 以下提到的社交编码站点中的任意一个：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
