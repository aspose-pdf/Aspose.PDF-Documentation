---
title: 在 Python 中在 PDF 文件末尾插入空白页
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-python/
lastmod: "2021-06-05"
---

要使用 **Aspose.PDF Java for Python** 在 PDF 文档末尾插入空白页，只需调用 **InsertEmptyPageAtEndOfFile** 类。

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# 在 PDF 中插入一个空白页
pdf_document.getPages().add();

# 保存合并后的输出文件（目标文档）
pdf_document.save(self.dataDir + "output.pdf")

print "空白页成功添加！"

```

**下载运行代码**

从以下任一社交编码网站下载 **在 PDF 文件末尾插入空白页 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)