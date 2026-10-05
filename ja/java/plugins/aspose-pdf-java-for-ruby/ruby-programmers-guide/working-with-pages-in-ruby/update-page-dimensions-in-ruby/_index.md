---
title: "Ruby での ページサイズの更新"
linktitle: "Ruby での ページサイズの更新"
type: docs
weight: 90
url: /ja/java/update-page-dimensions-in-ruby/
description: Aspose.PDF を使用した Ruby で PDF ドキュメントのページサイズを正確に設定する方法をご覧ください。
lastmod: "2026-10-05"
---
## Aspose.PDF - ページサイズの更新

**Aspose.PDF Java for Ruby** を使用してページサイズを更新するには、単に **UpdatePageDimensions** モジュールを呼び出すだけです。

Ruby コード

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

## 実行コードをダウンロード

以下に記載されたソーシャルコーディングサイトのいずれかから **Update Page Dimensions (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)
