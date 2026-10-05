---
title: "Ruby での PDF ファイル情報の取得"
linktitle: "Ruby での PDF ファイル情報の取得"
type: docs
weight: 50
url: /ja/java/get-pdf-file-information-in-ruby/
description: Ruby で Aspose.PDF を使用して、PDF ファイルからメタデータと詳細情報をプログラムで抽出します。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDF ファイル情報の取得

Ruby 用 **Aspose.PDF Java for Ruby** を使用して PDF 文書のファイル情報を取得するには、単に **GetPdfFileInfo** モジュールを呼び出します。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## 実行コードをダウンロード

ダウンロードВ **Get PDF File Information (Aspose.PDF)**В からВ 以下に示すソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
