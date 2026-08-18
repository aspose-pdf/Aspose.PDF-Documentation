---
title: 使用 Ruby 从 PDF 文件中删除特定页面
linktitle: 使用 Ruby 从 PDF 文件中删除特定页面
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: 使用 Aspose.PDF for Ruby 以编程方式从 PDF 文件中删除特定页面。
lastmod: "2026-06-09"
---
## Aspose.PDF - 删除页面

要使用 **Aspose.PDF Java for Ruby** 从 PDF 文档中删除特定页面，只需调用 **DeletePage** 模块即可。

红宝石代码

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

从以下任何社交编码网站下载 **删除页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
