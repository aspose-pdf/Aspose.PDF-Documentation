---
title: SVGファイルをRubyでPDF形式に変換
type: docs
weight: 60
url: ja/java/convert-svg-file-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - SVGをPDFに変換

**Aspose.PDF Java for Ruby**を使用してSVGファイルをPDF形式に変換するには、単に**SvgToPdf**モジュールを呼び出します。

Rubyコード

```java

# ドキュメントディレクトリへのパス

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# SVGロードオプションを使用してLoadOptionオブジェクトをインスタンス化

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# ドキュメントオブジェクトを作成

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# 出力をXLS形式で保存

pdf.save(data_dir + "SVG.pdf")

puts "ドキュメントが正常に変換されました"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Convert SVG to PDF (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)