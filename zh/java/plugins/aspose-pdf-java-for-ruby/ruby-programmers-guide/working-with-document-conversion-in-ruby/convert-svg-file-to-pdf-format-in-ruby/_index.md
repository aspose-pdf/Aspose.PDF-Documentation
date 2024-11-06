---
title: 将SVG文件转换为PDF格式在Ruby中
type: docs
weight: 60
url: zh/java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将SVG转换为PDF

要使用**Aspose.PDF Java for Ruby**将SVG文件转换为PDF格式，只需调用**SvgToPdf**模块。

Ruby代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 使用SVG加载选项实例化LoadOption对象

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# 创建文档对象

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# 将输出保存为XLS格式

pdf.save(data_dir + "SVG.pdf")

puts "文档已成功转换"
```

## 下载运行代码

从以下任何一个社交编码网站下载**Convert SVG to PDF (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)