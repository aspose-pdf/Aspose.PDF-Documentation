---
title: 从PDF文档的所有页面中提取文本在Ruby中
type: docs
weight: 30
url: zh/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 从所有页面中提取文本

要使用**Aspose.PDF Java for Ruby**从PDF文档的所有页面中提取文本，只需调用**ExtractTextFromAllPages**模块。

Ruby代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 创建TextAbsorber对象以提取文本

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# 接受所有页面的吸收器

pdf.getPages().accept(text_absorber)

# 为了从文档的特定页面提取文本，我们需要使用其索引指定特定页面以针对accept(..)方法。

# 接受特定PDF页面的吸收器

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# 获取提取的文本

extracted_text = text_absorber.getText()

# 创建一个写入器并打开文件

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# 将一行文本写入文件

# tw.WriteLine(extractedText);

# 关闭流

writer.close()

puts "文本提取成功。检查输出文件。"
```


## 下载运行代码

从以下任意一个社交编程网站下载**从所有页面提取文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)