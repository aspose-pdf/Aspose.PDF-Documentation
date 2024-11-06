---
title: 将 PDF 转换为 SVG 格式在 Ruby 中
type: docs
weight: 50
url: zh/java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将 PDF 转换为 SVG

要使用 **Aspose.PDF Java for Ruby** 将 PDF 转换为 SVG 格式，只需调用 **PdfToSvg** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 实例化 SvgSaveOptions 对象

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# 不将 SVG 图像压缩到 Zip 压缩包中

save_options.CompressOutputToZipArchive = false

# 将输出保存为 XLS 格式

pdf.save(data_dir + "Output.svg", save_options)

puts "文档已成功转换"
```

## 下载运行代码

从以下任一社交编码网站下载 **Convert PDF to SVG Format (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)