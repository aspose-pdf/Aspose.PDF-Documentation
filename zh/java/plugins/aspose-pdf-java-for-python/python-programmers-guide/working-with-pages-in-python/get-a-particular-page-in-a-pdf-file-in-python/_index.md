---
title: 在 Python 中获取 PDF 文件的特定页面
linktitle: 在 Python 中获取 PDF 文件的特定页面
type: docs
weight: 30
url: /zh/java/get-a-particular-page-in-a-pdf-file-in-python/
description: 探索如何使用 Aspose.PDF 在 Python 中提取 PDF 文件的特定页面，以实现详细的文档处理。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 获取 PDF 文档的特定页面，只需调用 **GetPage** 类。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get the page at particular index of Page Collection
pdf_page = pdf.getPages().get_Item(1)

# create a new Document object
new_document = self.Document()

# add page to pages collection of new document object
new_document.getPages().add(pdf_page)

# save the newly generated PDF file
new_document.save(self.dataDir + "output.pdf")

print "Process completed successfully!

```

 **下载运行代码**

下载 **Get Page (Aspose.PDF)**В fromВ 以下提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
