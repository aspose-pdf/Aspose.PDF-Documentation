---
title: 在 Ruby 中删除 PDF 文件的特定页面
linktitle: 在 Ruby 中删除 PDF 文件的特定页面
type: docs
weight: 20
url: /zh/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: 使用 Aspose.PDF for Ruby 以编程方式删除 PDF 文件中的特定页面。
lastmod: "2026-10-06"
---
## Aspose.PDF - 删除页面

要使用 **Aspose.PDF Java for Ruby** 删除 PDF 文档的特定页面，只需调用 **DeletePage** 模块。

Ruby 代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## 下载运行代码

下载 **Delete Page (Aspose.PDF)**\u0412\u00A0从\u0412\u00A0以下提及的任何社交编码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
