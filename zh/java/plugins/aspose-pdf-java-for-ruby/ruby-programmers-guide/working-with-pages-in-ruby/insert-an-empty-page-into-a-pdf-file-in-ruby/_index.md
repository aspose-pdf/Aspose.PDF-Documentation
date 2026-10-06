---
title: 在 Ruby 中向 PDF 文件插入空白页
linktitle: 在 Ruby 中向 PDF 文件插入空白页
type: docs
weight: 70
url: /zh/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 在 PDF 文档的特定位置插入空白页，以实现精确的文档管理。
lastmod: "2026-10-06"
---
## Aspose.PDF - 插入空白页

要使用 **Aspose.PDF Java for Ruby** 在 PDF 文档中插入空白页，只需调用 **InsertEmptyPage** 模块。

Ruby 代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().insert(1)

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## 下载运行代码

下载\u0412\u00A0**插入空页面 (Aspose.PDF)**\u0412\u00A0 来自\u0412\u00A0 以下提到的任何社交编码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
