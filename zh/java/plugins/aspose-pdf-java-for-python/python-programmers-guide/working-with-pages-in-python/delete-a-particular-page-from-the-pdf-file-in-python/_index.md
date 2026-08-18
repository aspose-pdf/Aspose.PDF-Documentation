---
title: 使用 Python 从 PDF 文件中删除特定页面
linktitle: 使用 Python 从 PDF 文件中删除特定页面
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-python/
description: 了解如何使用 Aspose.PDF 从 Python 中的 PDF 文档中删除特定页面，从而提供高效的文档编辑。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 从 PDF 文档中删除特定页面，只需调用 **DeletePage** 类即可。

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

从以下任何社交编码网站下载 **删除页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
