---
title: RubyでSVGファイルをPDF形式に変換する
linktitle: RubyでSVGファイルをPDF形式に変換する
type: docs
weight: 60
url: /ja/java/convert-svg-file-to-pdf-format-in-ruby/
description: 正確でスケーラブルな文書変換を実現するAspose.PDFを使用して、RubyでSVGファイルをPDF形式に変換する方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - SVGをPDFに変換

**Aspose.PDF Java for Ruby**を使用してSVGファイルをPDF形式に変換するには、単に**SvgToPdf**モジュールを呼び出します。

Rubyコード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## 実行コードをダウンロード

ダウンロードВ **Convert SVG to PDF (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれか:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
