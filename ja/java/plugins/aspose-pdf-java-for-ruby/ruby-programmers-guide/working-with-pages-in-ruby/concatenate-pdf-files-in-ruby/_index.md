---
title: RubyでPDFファイルを連結する
type: docs
weight: 10
url: /ja/java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイルの連結

**Aspose.PDF Java for Ruby**を使用してPDFファイルを連結するには、**ConcatenatePdfFiles**モジュールを呼び出します。

Ruby コード

```java
# ドキュメントディレクトリへのパス

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# ターゲットドキュメントを開く

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# ソースドキュメントを開く

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# ソースドキュメントのページをターゲットドキュメントに追加

pdf1.getPages().add(pdf2.getPages())

# 連結された出力ファイル（ターゲットドキュメント）を保存

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "新しいドキュメントが保存されました。出力ファイルを確認してください"
```

## 実行コードのダウンロード

以下に記載されたソーシャルコーディングサイトから**Concatenate PDF Files (Aspose.PDF)**をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)