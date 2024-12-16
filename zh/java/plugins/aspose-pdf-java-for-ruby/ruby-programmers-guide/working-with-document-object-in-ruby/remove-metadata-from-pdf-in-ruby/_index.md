---
title: 从 PDF 中删除元数据（使用 Ruby）
type: docs
weight: 90
url: /zh/java/remove-metadata-from-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 删除元数据

要使用 **Aspose.PDF Java for Ruby** 从 Pdf 文档中删除元数据，只需调用 **RemoveMetadata** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开一个 pdf 文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

    doc.getMetadata().removeItem("pdfaid:part")

end    

if doc.getMetadata().contains("dc:format")

    doc.getMetadata().removeItem("dc:format")

end

# 保存更新后的文档

doc.save(data_dir + "Remove_Metadata.pdf")

puts "成功移除元数据，请检查输出文件。"
```

## 下载运行代码

从以下任一社交编码网站下载 **Remove Metadata (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)