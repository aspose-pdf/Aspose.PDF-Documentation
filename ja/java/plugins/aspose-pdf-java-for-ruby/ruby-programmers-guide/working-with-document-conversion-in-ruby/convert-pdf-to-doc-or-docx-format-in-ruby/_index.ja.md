---
title: RubyでPDFをDOCまたはDOCX形式に変換
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFをDOCまたはDOCXに変換

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントをDOCまたはDOCX形式に変換するには、単に**PdfToDoc**モジュールを呼び出します。

Ruby コード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 対象ドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 連結された出力ファイル（対象ドキュメント）を保存する

pdf.save(data_dir + "output.doc")

puts "ドキュメントは正常に変換されました"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Convert PDF to DOC or DOCX (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)