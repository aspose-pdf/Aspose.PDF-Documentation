---
title: 优化 PDF 文件大小在 Ruby 中
type: docs
weight: 80
url: zh/java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 优化 PDF 文件大小

要使用 **Aspose.PDF Java for Ruby** 优化 PDF 文档的文件大小，请调用 **Optimize** 模块的 **optimize_filesize** 方法。

Ruby 代码

```java

def optimize_filesize()

    # 文档目录的路径。

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # 打开一个 pdf 文档。

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # 通过删除未使用的对象优化文件大小

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # 保存输出文档

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "优化的 PDF 文件大小，请检查输出文件。"

end 
```

## 下载运行代码

Download **优化 PDF 文件大小 (Aspose.PDF)** 从以下任意一个社交编程网站：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)