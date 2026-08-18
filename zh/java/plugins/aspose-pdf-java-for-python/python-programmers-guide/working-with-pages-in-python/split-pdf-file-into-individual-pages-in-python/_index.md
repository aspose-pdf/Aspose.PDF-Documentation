---
title: 在Python中将PDF文件分割成单独的页面
linktitle: 在Python中将PDF文件分割成单独的页面
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-python/
description: 探索如何使用 Aspose.PDF 在 Python 中将 PDF 拆分为单独的页面，从而轻松提取和管理页面。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for PHP** 将 PDF 文档拆分为单独的页面，只需调用 **SplitAllPages** 类即可。

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

从以下任何一个社交编码网站下载 **拆分页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
