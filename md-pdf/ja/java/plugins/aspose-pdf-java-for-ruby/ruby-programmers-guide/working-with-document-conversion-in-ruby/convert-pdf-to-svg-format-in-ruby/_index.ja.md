---
title: PDFをSVG形式に変換する方法（Ruby）
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFをSVGに変換

**Aspose.PDF Java for Ruby**を使用してPDFをSVG形式に変換するには、単に**PdfToSvg**モジュールを呼び出します。

Rubyコード

```java

# ドキュメントディレクトリへのパス。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 目的のドキュメントを開く

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# SvgSaveOptionsのオブジェクトをインスタンス化する

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# SVG画像をZipアーカイブに圧縮しない

save_options.CompressOutputToZipArchive = false

# 出力をXLS形式で保存する

pdf.save(data_dir + "Output.svg", save_options)

puts "ドキュメントが正常に変換されました"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから、**Convert PDF to SVG Format (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)