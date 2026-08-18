---
title: 在 Ruby 中更新页面尺寸
linktitle: 在 Ruby 中更新页面尺寸
type: docs
weight: 90
url: /java/update-page-dimensions-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 更新 PDF 文档的页面尺寸，以实现精确的页面格式设置。
lastmod: "2026-06-09"
---
## Aspose.PDF - 更新页面尺寸

要使用 **Aspose.PDF Java for Ruby** 更新页面尺寸，只需调用 **UpdatePageDimensions** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get page collection

page_collection = pdf.getPages()

# get particular page

pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points

# so A4 dimensions in points will be (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Dimensions updated successfully!"
```

## 下载运行代码

从以下任何一个社交编码网站下载**更新页面尺寸 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)
