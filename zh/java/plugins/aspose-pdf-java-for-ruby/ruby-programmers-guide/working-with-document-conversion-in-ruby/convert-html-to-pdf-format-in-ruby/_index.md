---
title: 将HTML转换为PDF格式在Ruby中
type: docs
weight: 10
url: zh/java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将HTML转换为PDF格式

要使用**Aspose.PDF Java for Ruby**将HTML转换为PDF格式，只需调用**HtmlToPdf**模块。

Ruby代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# 加载HTML文件

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# 保存连接后的输出文件（目标文档）

pdf.save(data_dir + "html.pdf")

puts "文档已成功转换"
```

## 下载运行代码

从以下任一社交编码网站下载**Convert HTML to PDF Format (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)