---
title: 使用 Python 获取 PDF 文件中的特定页面
linktitle: 使用 Python 获取 PDF 文件中的特定页面
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-python/
description: 探索如何使用 Aspose.PDF 从 Python 中的 PDF 文件中提取特定页面，以进行详细的文档处理。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 获取 PDF 文档中的特定页面，只需调用 **GetPage** 类即可。

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

从以下任何社交编码网站下载 **获取页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
