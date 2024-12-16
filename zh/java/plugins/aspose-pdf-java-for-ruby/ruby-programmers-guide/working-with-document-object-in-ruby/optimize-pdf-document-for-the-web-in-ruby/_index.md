---
title: 在 Ruby 中优化 PDF 文档以用于 Web
type: docs
weight: 70
url: /zh/java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 优化 PDF 以用于 Web

要使用 **Aspose.PDF Java for Ruby** 优化 PDF 文档以用于 Web，只需调用 **Optimize** 模块的 **optimize_web** 方法。

Ruby 代码

```java

 def optimize_web()

    # 文档目录的路径。

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # 打开一个 pdf 文档。

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # 优化以用于 Web

    doc.optimize()

    #保存输出文档

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "已优化 PDF 以用于 Web，请检查输出文件。"

end
``` 

## 下载运行代码

从以下任意社交编码网站下载 **Optimize PDF for Web (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)