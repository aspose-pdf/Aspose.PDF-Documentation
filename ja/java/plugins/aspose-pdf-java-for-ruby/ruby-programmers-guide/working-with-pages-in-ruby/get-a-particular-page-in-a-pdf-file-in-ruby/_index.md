---
title: "Ruby での PDF ファイルの特定のページの取得"
linktitle: "Ruby での PDF ファイルの特定のページの取得"
type: docs
weight: 30
url: /ja/java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: Ruby と Aspose.PDF を使用して、PDF ドキュメントの個々のページにアクセスし、操作します。
lastmod: "2026-10-05"
---
## Aspose.PDF - Get Page

**Aspose.PDF Java for Ruby** を使用して PDF ドキュメントの特定のページを取得するには、単に **GetPage** モジュールを呼び出します。

Ruby コード

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

## 実行中のコードをダウンロード

ダウンロード **Get Page (Aspose.PDF)**В 以下のソーシャルコーディングサイトからВ ダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
