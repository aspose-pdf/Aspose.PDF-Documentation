---
title: 在 Python 中向现有 PDF 添加目录
type: docs
weight: 20
url: zh/python-java/add-toc-to-existing-pdf-in-python/
---

要在 PDF 文档中使用 **Aspose.PDF Java for Python** 添加目录，只需调用 **AddToc** 类。

```python

# 打开一个 PDF 文档。
doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

# 访问 PDF 文件的第一页
toc_page = doc.getPages().insert(1)

# 创建对象以表示目录信息
toc_info = self.TocInfo()
title = self.TextFragment("目录")
title.getTextState().setFontSize(20)

# 设置目录的标题
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# 创建将用作目录元素的字符串对象
titles = ["第一页", "第二页"]

i = 0;
while (i < 2):

# 创建 Heading 对象
heading2 = self.Heading(1)

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# 指定 Heading 对象的目标页
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# 目标页
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# 目标坐标
segment2.setText(titles[i])

# 将 Heading 添加到包含目录的页
toc_page.getParagraphs().add(heading2)

i += 1

# 保存 PDF 文档
doc.save(self.dataDir + "TOC.pdf")

print "成功添加目录，请检查输出文件。"
```


**下载运行代码**

从以下任一社交编码网站下载**添加目录 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)