---
title: 将 PDF 文件拆分为单个页面的 Python
type: docs
weight: 80
url: zh/python-java/split-pdf-file-into-individual-pages-in-python/
---

<ins>要使用 **Aspose.PDF Java for PHP** 将 PDF 文档拆分为单个页面，只需调用 **SplitAllPages** 类。

**Python 代码**
```

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 遍历所有页面
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# 创建一个新的 Document 对象
new_document = self.Document();

# 获取页面集合中特定索引的页面
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# 保存新生成的 PDF 文件
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "拆分过程已成功完成!";
```


**下载运行代码**

从以下任一社交编码网站下载 **Split Pages (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/SplitAllPages/SplitAllPages.py)