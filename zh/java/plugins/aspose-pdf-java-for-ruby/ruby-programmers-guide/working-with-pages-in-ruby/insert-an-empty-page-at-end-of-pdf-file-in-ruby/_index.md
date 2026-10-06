---
title: 在 Ruby 中向 PDF 文件末尾插入空白页
linktitle: 在 Ruby 中向 PDF 文件末尾插入空白页
type: docs
weight: 60
url: /zh/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: 了解如何使用 Ruby 与 Aspose.PDF 在 PDF 文档末尾插入空白页，为您的 PDF 处理任务增添灵活性。
lastmod: "2026-10-06"
---
## Aspose.PDF - 在 PDF 文件末尾插入空白页

要使用 **Aspose.PDF Java for Ruby** 在 PDF 文档末尾插入空白页，只需调用 **InsertEmptyPageAtEndOfFile** 模块。

Ruby 代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## 下载运行代码

下载 **在 PDF 文件末尾插入空页 (Aspose.PDF)**В 来自以下提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
