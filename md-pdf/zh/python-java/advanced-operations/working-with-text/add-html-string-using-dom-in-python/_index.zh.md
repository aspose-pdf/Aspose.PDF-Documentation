---
title: 在 Python 中使用 DOM 添加 HTML 字符串
type: docs
weight: 10
url: /python-java/add-html-string-using-dom-in-python/
---

要在使用 **Aspose.PDF Java for Python** 的 Pdf 文档中添加 HTML 字符串，只需调用 **AddHtml** 模块。

```python

# 实例化 Document 对象
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# 设置边距信息
title.setMargin(margin)

# 将 HTML 片段添加到页面的段落集合中
page.getParagraphs().add(title)

# 保存 PDF 文件
doc.save(self.dataDir + 'html.output.pdf')

print "HTML 添加成功"
```

**下载运行代码**

从以下任意一个社交编码网站下载 **Add HTML (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)