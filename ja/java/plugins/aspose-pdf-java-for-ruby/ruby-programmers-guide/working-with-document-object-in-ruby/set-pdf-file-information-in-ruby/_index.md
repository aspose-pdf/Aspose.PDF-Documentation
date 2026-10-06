---
title: "Ruby での PDF ファイル情報の設定"
linktitle: "Ruby での PDF ファイル情報の設定"
type: docs
weight: 120
url: /ja/java/set-pdf-file-information-in-ruby/
description: "Ruby を使用して、タイトル、作者、キーワードなどの PDF メタデータをプログラムで定義および更新してください。"
lastmod: "2026-10-06"
---
## Aspose.PDF - PDF ファイル情報の設定

**Aspose.PDF Java for Ruby** を使用して PDF ドキュメント情報を更新するには、**SetPdfFileInfo** モジュールを呼び出してください。

Ruby コード

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

## 実行コードのダウンロード

**PDF ファイル情報の設定 (Aspose.PDF)** をダウンロードするには、以下のいずれかのソーシャルコーディングサイトから取得してください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
