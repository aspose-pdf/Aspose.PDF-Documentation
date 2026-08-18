---
title: 使用 Ruby 从 PDF 文档的所有页面中提取文本
linktitle: 使用 Ruby 从 PDF 文档的所有页面中提取文本
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 从 PDF 文档的所有页面中提取文本，非常适合内容分析。
lastmod: "2026-06-09"
---
## Aspose.PDF - 从所有页面中提取文本

要使用 **Aspose.PDF Java for Ruby** 提取 TextrFrom All Pages Pdf 文档，只需调用 **ExtractTextFromAllPages** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# create TextAbsorber object to extract text

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# accept the absorber for all the pages

pdf.getPages().accept(text_absorber)

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.

# accept the absorber for particular PDF page

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text

extracted_text = text_absorber.getText()

# create a writer and open the file

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# write a line of text to the file

# tw.WriteLine(extractedText);

# close the stream

writer.close()

puts "Text extracted successfully. Check output file."
```

## 下载运行代码

从以下任何一个社交编码网站下载**从所有页面提取文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
