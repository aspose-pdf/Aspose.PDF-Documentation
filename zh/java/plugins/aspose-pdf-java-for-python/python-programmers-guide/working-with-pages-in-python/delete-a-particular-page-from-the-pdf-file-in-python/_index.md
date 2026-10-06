---
title: 在 Python 中删除 PDF 文件的特定页面
linktitle: 在 Python 中删除 PDF 文件的特定页面
type: docs
weight: 20
url: /zh/java/delete-a-particular-page-from-the-pdf-file-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中删除 PDF 文档的特定页面，实现高效的文档编辑。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 删除 PDF 文档的特定页面，只需调用 **DeletePage** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# delete a particular page
pdf.getPages().delete(2)

# save the newly generated PDF file
doc.save(self.dataDir + "output.pdf")

print "Page deleted successfully!"

```

**下载运行代码**

下载 **Delete Page (Aspose.PDF)**В 从В 以下提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
