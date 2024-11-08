---
title: RubyでPDFファイル情報を設定する
type: docs
weight: 120
url: /ja/java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイル情報を設定する

**Aspose.PDF Java for Ruby**を使用してPdfドキュメント情報を更新するには、単に**SetPdfFileInfo**モジュールを呼び出します。

Rubyコード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDFドキュメントを開く。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# ドキュメント情報を取得

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF情報")

doc_info.setTitle("PDFドキュメント情報の設定")

# 新しい情報で更新されたドキュメントを保存

doc.save(data_dir + "Updated_Information.pdf")

puts "ドキュメント情報を更新しました。出力ファイルを確認してください。"
```


## ダウンロード実行コード

以下のいずれかのソーシャルコーディングサイトから**Set PDF File Information (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)