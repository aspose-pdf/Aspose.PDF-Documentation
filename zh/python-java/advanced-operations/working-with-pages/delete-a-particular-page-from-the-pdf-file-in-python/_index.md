---
title: 从 PDF 文件中删除特定页面在 Python 中
type: docs
weight: 20
url: zh/python-java/delete-a-particular-page-from-the-pdf-file-in-python/
---

要使用 **Aspose.PDF Java for Python** 从 PDF 文档中删除特定页面，只需调用 **DeletePage** 类。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 删除特定页面
pdf.getPages().delete(2)

# 保存新生成的 PDF 文件
doc.save(self.dataDir + "output.pdf")

print "页面删除成功!"

```

**下载运行代码**

从以下任何一个社交编码网站下载 **Delete Page (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)