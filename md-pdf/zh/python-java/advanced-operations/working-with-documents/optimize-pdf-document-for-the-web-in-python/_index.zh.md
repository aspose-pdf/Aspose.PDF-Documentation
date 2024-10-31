---
title: 在 Python 中优化 PDF 文档以用于网络
type: docs
weight: 60
url: /python-java/optimize-pdf-document-for-the-web-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 优化 PDF 文档以用于网络，只需调用 **Optimize** 类的 **optimize_web** 方法。

**Python 代码**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 优化用于网络
doc.optimize();

# 保存输出文档
doc.save(self.dataDir + "Optimized_Web.pdf")

print "已优化 PDF 用于网络，请检查输出文件。"
```


**下载运行代码**

从以下任一社交编码网站下载 **Optimize PDF for Web (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/Optimize/Optimize.py)