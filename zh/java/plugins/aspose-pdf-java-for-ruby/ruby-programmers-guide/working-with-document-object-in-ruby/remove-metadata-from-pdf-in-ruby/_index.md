---
title: 在 Ruby 中从 PDF 中删除元数据
linktitle: 在 Ruby 中从 PDF 中删除元数据
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
description: 使用 Aspose.PDF for Ruby 以编程方式从 PDF 文件中删除敏感或不需要的元数据。
lastmod: "2026-06-09"
---
## Aspose.PDF - 删除元数据

要使用 **Aspose.PDF Java for Ruby** 从 Pdf 文档中删除元数据，只需调用 **RemoveMetadata** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

В В В  doc.getMetadata().removeItem("pdfaid:part")

endВ В  В

if doc.getMetadata().contains("dc:format")

В В В  doc.getMetadata().removeItem("dc:format")

end

# save update document with new information

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Removed metadata successfully, please check output file."
```

## 下载运行代码

从以下任何社交编码网站下载**删除元数据 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
