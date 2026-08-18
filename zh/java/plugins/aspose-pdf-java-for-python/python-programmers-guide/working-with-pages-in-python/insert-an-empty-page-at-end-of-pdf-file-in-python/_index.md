---
title: 在Python中的PDF文件末尾插入一个空页
linktitle: 在Python中的PDF文件末尾插入一个空页
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中的 PDF 文档末尾插入空白页面，以轻松扩展文档。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 在 PDF 文档末尾插入空页，只需调用 **InsertEmptyPageAtEndOfFile** 类即可。

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**下载运行代码**

从以下任何社交编码网站下载 **在 PDF 文件末尾插入空页 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
