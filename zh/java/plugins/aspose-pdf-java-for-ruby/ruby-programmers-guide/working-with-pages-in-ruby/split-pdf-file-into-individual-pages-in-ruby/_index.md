---
title: 在 Ruby 中将 PDF 文件拆分为单独的页面
linktitle: 在 Ruby 中将 PDF 文件拆分为单独的页面
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 将 PDF 文件拆分为单独的页面，从而更轻松地管理和提取内容。
lastmod: "2026-06-09"
---
## Aspose.PDF - 拆分页面

要使用 **Aspose.PDF Java for Ruby** 将 PDF 文档拆分为单独的页面，只需调用 **SplitAllPages** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## 下载运行代码

从以下任何一个社交编码网站下载 **拆分页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)
