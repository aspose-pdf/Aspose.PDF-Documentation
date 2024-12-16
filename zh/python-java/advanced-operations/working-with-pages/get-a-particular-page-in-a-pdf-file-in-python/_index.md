---
title: 在 Python 中获取 PDF 文件中的特定页面
type: docs
weight: 30
url: /zh/python-java/get-a-particular-page-in-a-pdf-file-in-python/
---

要在 PDF 文档中获取特定页面，使用 **Aspose.PDF Java for Python**，只需调用 **GetPage** 类。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取页面集合中特定索引的页面
pdf_page = pdf.getPages().get_Item(1)

# 创建一个新的 Document 对象
new_document = self.Document()

# 将页面添加到新文档对象的页面集合中
new_document.getPages().add(pdf_page)

# 保存新生成的 PDF 文件
new_document.save(self.dataDir + "output.pdf")

print "处理成功完成！

```

**下载运行代码**

从以下任意社交编码网站下载 **Get Page (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)