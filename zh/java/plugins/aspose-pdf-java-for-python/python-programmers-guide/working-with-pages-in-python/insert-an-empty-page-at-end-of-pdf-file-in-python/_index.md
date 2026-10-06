---
title: 在 Python 中向 PDF 文件末尾插入空白页
linktitle: 在 Python 中向 PDF 文件末尾插入空白页
type: docs
weight: 60
url: /zh/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: 了解如何在 Python 中使用 Aspose.PDF 在 PDF 文档末尾插入空白页，以便轻松扩展文档。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 在 PDF 文档末尾插入空白页，只需调用 **InsertEmptyPageAtEndOfFile** 类。

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

下载 **Insert an Empty Page at End of PDF File (Aspose.PDF)**В 来自В 以下提到的任何社交编码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
