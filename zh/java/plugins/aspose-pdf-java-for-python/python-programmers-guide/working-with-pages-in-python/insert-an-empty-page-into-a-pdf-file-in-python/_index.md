---
title: 在 Python 中向 PDF 文件插入空白页
linktitle: 在 Python 中向 PDF 文件插入空白页
type: docs
weight: 70
url: /zh/java/insert-an-empty-page-into-a-pdf-file-in-python/
description: 了解如何使用 Python 和 Aspose.PDF 在 PDF 文件中的任意位置插入空白页，以实现灵活的文档结构。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 将空白页插入 PDF 文档，只需调用 **InsertEmptyPage** 类。

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().insert(1)

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**下载运行代码**

下载В **插入空白页 (Aspose.PDF)**В 来自В 以下任意提到的社交编码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
