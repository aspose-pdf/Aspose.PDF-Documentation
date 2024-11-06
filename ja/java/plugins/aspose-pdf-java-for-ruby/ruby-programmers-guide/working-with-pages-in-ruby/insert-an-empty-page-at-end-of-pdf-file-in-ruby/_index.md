---
title: PDFファイルの末尾に空のページを挿入する（Ruby）
type: docs
weight: 60
url: ja/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイルの末尾に空のページを挿入する

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントの末尾に空のページを挿入するには、単に**InsertEmptyPageAtEndOfFile**モジュールを呼び出します。

Rubyコード

```java
# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 対象ドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# PDFに空のページを挿入する

pdf.getPages().add()

# 結合された出力ファイル（対象ドキュメント）を保存する

pdf.save(data_dir+ "output.pdf")

puts "空のページが正常に追加されました！"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**PDFファイルの末尾に空のページを挿入する（Aspose.PDF）**をダウンロードできます：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)