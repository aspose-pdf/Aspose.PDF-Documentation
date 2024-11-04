---
title: 在 Ruby 中向现有 PDF 文件添加文本
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 添加文本

要使用 **Aspose.PDF Java for Ruby** 在 Pdf 文档中添加文本字符串，只需调用 **AddText** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 实例化 Document 对象

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 获取特定页面

pdf_page = doc.getPages().get_Item(1)

# 创建文本片段

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# 设置文本属性

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# 创建 TextBuilder 对象

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# 将文本片段附加到 PDF 页面

text_builder.appendText(text_fragment)

# 保存 PDF 文件

doc.save(data_dir + "Text_Added.pdf")

puts "Text added successfully"
```


## 下载运行代码

从以下任何一个社交编码网站下载**添加文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)