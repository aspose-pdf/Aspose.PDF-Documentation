---
title: "Ruby での PDFファイル情報の設定"
linktitle: "Ruby での PDFファイル情報の設定"
type: docs
weight: 120
url: /ja/java/set-pdf-file-information-in-ruby/
description: Rubyを使用して、タイトル、作者、キーワードなどのPDFメタデータをプログラムで定義および更新します。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDFファイル情報の設定

**Aspose.PDF Java for Ruby** を使用して PDF ドキュメント情報を更新するには、単に **SetPdfFileInfo** モジュールを呼び出します。

Rubyコード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## 実行コードをダウンロード

ダウンロードВ **PDF ファイル情報の設定 (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれかへ:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
