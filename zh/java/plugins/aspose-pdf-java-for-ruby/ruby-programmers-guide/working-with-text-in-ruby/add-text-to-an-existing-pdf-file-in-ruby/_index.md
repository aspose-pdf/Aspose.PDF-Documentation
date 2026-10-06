---
title: 在 Ruby 中向现有 PDF 文件添加文本
linktitle: 在 Ruby 中向现有 PDF 文件添加文本
type: docs
weight: 20
url: /zh/java/add-text-to-an-existing-pdf-file-in-ruby/
description: 了解如何使用 Aspose.PDF 在 Ruby 中向现有 PDF 文档添加文本，以增强或更新您的 PDF 内容。
lastmod: "2026-10-06"
---
## Aspose.PDF - 添加文本

要在 PDF 文档中使用 **Aspose.PDF Java for Ruby** 添加文本字符串，只需调用 **AddText** 模块。

Ruby 代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get particular page

pdf_page = doc.getPages().get_Item(1)

# create text fragment

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# set text properties

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# create TextBuilder object

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# append the text fragment to the PDF page

text_builder.appendText(text_fragment)

# Save PDF file

doc.save(data_dir + "Text_Added.pdf")

puts "Text added successfully"
```

## 下载运行代码

下载В **Add Text (Aspose.PDF)**В 来自В 以下提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)
