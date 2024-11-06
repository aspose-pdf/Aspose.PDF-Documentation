---
title: 在 PDF 文件中插入空白页（Python）
type: docs
weight: 70
url: zh/java/insert-an-empty-page-into-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

要在 PDF 文档中使用 **Aspose.PDF Java for Python** 插入空白页，只需调用 **InsertEmptyPage** 类。

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# 在 PDF 中插入空白页
pdf_document.getPages().insert(1)

# 保存合并后的输出文件（目标文档）
pdf_document.save(self.dataDir + "output.pdf")

print "空白页已成功添加！"

```

**下载运行代码**

从以下任一社交编码网站下载 **Insert an Empty Page (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)