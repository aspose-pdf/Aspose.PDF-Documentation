---
title: 在 Python 中获取 PDF 的页数
type: docs
weight: 40
url: /zh/python-java/get-page-count-of-pdf-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 获取 PDF 文档的页数，只需调用 **GetNumberOfPages** 类。

**Python 代码**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'
page_count = pdf.getPages().size()
print "Page Count:" . page_count

```

**下载运行代码**

从以下任何一个社交编码网站下载 **获取页数 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)