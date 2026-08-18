---
title: 在 Python 中使用 DOM 添加 HTML 字符串
linktitle: 在 Python 中使用 DOM 添加 HTML 字符串
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2026-06-09"
description: 解释如何使用 Python 和 PDF 文件格式库在 DOM 中添加 HTML 字符串
---
## 使用 Python 在 PDF DOM 中添加 HTML 字符串

要使用 **Aspose.PDF Java for Python** 在 Pdf 文档中添加 HTML 字符串，只需调用 **AddHtml** 模块即可。

```python

# Instantiate Document object
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Set margin information
title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page
page.getParagraphs().add(title)

# Save PDF file
doc.save(self.dataDir + 'html.output.pdf')

print "HTML added successfully"
```

**下载运行代码**

从以下任何一个社交编码网站下载**添加 HTML (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
