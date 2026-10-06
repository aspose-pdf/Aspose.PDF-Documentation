---
title: 在 Ruby 中提取 PDF 文档所有页面的文本
linktitle: 在 Ruby 中提取 PDF 文档所有页面的文本
type: docs
weight: 30
url: /zh/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 从 PDF 文档的所有页面提取文本，适用于内容分析。
lastmod: "2026-10-06"
---
## Aspose.PDF - 提取所有页面的文本

要使用 **Aspose.PDF Java for Ruby** 提取 PDF 文档所有页面的文本，只需调用 **ExtractTextFromAllPages** 模块。

Ruby 代码

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

DownloadВ **从所有页面提取文本 (Aspose.PDF)**В 来自以下列出的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
