---
title: 优化 PDF 文档以适应网络在 Python 中
type: docs
weight: 60
url: zh/java/optimize-pdf-document-for-the-web-in-python/
lastmod: "2021-06-05"
---

要在 Python 中使用 **Aspose.PDF Java for Python** 优化 PDF 文档以适应网络，只需调用 **Optimize** 类的 **optimize_web** 方法。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 优化以适应网络
doc.optimize();

# 保存输出文档
doc.save(self.dataDir + "Optimized_Web.pdf")

print "优化后的 PDF 适用于网络，请检查输出文件。"
```

**下载运行代码**

从以下任何一个社交编码网站下载 **Optimize PDF for Web (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)