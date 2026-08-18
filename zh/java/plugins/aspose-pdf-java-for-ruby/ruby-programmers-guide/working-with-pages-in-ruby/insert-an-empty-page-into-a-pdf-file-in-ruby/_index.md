---
title: 在 Ruby 中将空页面插入 PDF 文件
linktitle: 在 Ruby 中将空页面插入 PDF 文件
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 将空白页面插入 PDF 文档中的特定位置，以实现精确的文档管理。
lastmod: "2026-06-09"
---
## Aspose.PDF - 插入空白页

要使用 **Aspose.PDF Java for Ruby** 将空页面插入 Pdf 文档中，只需调用 **InsertEmptyPage** 模块即可。

红宝石代码

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

从以下任何一个社交编码网站下载**插入空页 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
