---
title: 在 Ruby 中的 PDF 文件末尾插入一个空页
linktitle: 在 Ruby 中的 PDF 文件末尾插入一个空页
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 在 PDF 文档末尾插入空白页面，从而提高 PDF 处理任务的灵活性。
lastmod: "2026-06-09"
---
## Aspose.PDF - 在 PDF 文件末尾插入空白页

要使用 **Aspose.PDF Java for Ruby** 在 PDF 文档末尾插入空页，只需调用 **InsertEmptyPageAtEndOfFile** 模块即可。

红宝石代码

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

从以下任何社交编码网站下载 **在 PDF 文件末尾插入空页 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
