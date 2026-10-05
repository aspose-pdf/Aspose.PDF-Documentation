---
title: RubyでPDFをSVG形式に変換
linktitle: RubyでPDFをSVG形式に変換
type: docs
weight: 50
url: /ja/java/convert-pdf-to-svg-format-in-ruby/
description: Ruby と Aspose.PDF を使用して PDF ファイルを SVG 形式に変換する方法を確認し、スケーラブルで編集可能なベクターグラフィックスを実現します。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDF を SVG に変換

**Aspose.PDF Java for Ruby** を使用して PDF を SVG 形式に変換するには、単に **PdfToSvg** モジュールを呼び出すだけです。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## 実行中のコードをダウンロード

ダウンロードВ **Convert PDF to SVG Format (Aspose.PDF)**В 以下に示すソーシャルコーディングサイトから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
