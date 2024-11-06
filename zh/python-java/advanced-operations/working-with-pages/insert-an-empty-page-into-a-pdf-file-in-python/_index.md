---
title: 在 Python 中插入一个空白页到 PDF 文件
type: docs
weight: 70
url: zh/python-java/insert-an-empty-page-into-a-pdf-file-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 在 PDF 文档中插入一个空白页，只需调用 **InsertEmptyPage** 类。

**Python 代码**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# 在 PDF 中插入一个空白页
pdf_document.getPages().insert(1)

# 保存合并后的输出文件（目标文档）
pdf_document.save(self.dataDir + "output.pdf")

print "空白页添加成功！"

```

**下载运行代码**

从以下任何一个社交编码网站下载 **插入空白页 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)