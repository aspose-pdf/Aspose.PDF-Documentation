---
title: 在 Python 中将 PDF 文件拆分为单独页面
linktitle: 在 Python 中将 PDF 文件拆分为单独页面
type: docs
weight: 80
url: /zh/java/split-pdf-file-into-individual-pages-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中将 PDF 拆分为单独页面，以实现轻松的页面提取和管理。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for PHP** 将 PDF 文档拆分为单独页面，只需调用 **SplitAllPages** 类。

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop through all the pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# create a new Document object
new_document = self.Document();

# get the page at particular index of Page Collection
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Split process completed successfully!";
```

**下载运行代码**

下载 **Split Pages (Aspose.PDF)**В 从В 以下提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
