---
title: 使用 DOM 在 Ruby 中添加 HTML 字符串
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 添加 HTML

要在 Pdf 文档中使用 **Aspose.PDF Java for Ruby** 添加 HTML 字符串，只需调用 **AddHtml** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 实例化 Document 对象

doc = Rjb::import('com.aspose.pdf.Document').new

# 向 PDF 文件的页面集合中添加页面

page = doc.getPages().add()

# 用 HTML 内容实例化 HtmlFragment

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# 设置 MarginInfo 以获取边距详细信息

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# 设置边距信息

title.setMargin(margin)

# 将 HTML Fragment 添加到页面的段落集合中

page.getParagraphs().add(title)

# 保存 PDF 文件

doc.save(data_dir + "html.output.pdf")

puts "HTML 添加成功"
```


## 下载运行代码

从以下任一社交编码网站下载**添加 HTML (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)