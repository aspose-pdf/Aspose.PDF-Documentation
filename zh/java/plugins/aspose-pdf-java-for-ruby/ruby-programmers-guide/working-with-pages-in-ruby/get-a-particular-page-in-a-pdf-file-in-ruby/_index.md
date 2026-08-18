---
title: 使用 Ruby 获取 PDF 文件中的特定页面
linktitle: 使用 Ruby 获取 PDF 文件中的特定页面
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: 使用 Ruby 和 Aspose.PDF 访问和操作 PDF 文档中的各个页面。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取页面

要使用 **Aspose.PDF Java for Ruby** 获取 PDF 文档中的特定页面，只需调用 **GetPage** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get the page at particular index of Page Collection

pdf_page = pdf.getPages().get_Item(1)

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# add page to pages collection of new document object

new_document.getPages().add(pdf_page)

# save the newly generated PDF file

new_document.save(data_dir + "output.pdf")

puts "Process completed successfully!"
```

## 下载运行代码

从以下任何一个社交编码网站下载 **获取页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
