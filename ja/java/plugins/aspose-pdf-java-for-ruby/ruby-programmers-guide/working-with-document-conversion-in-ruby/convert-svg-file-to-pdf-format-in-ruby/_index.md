---
title: "Ruby での SVG ファイルの PDF 形式への変換"
linktitle: "Ruby での SVG ファイルの PDF 形式への変換"
type: docs
weight: 60
url: /ja/java/convert-svg-file-to-pdf-format-in-ruby/
description: "正確でスケーラブルな文書変換を実現する Aspose.PDF を使用して、Ruby で SVG ファイルを PDF 形式に変換する方法を学びます。"
lastmod: "2026-10-06"
---
## Aspose.PDF - SVG を PDF に変換

**Aspose.PDF Java for Ruby** を使用して SVG ファイルを PDF 形式に変換するには、単に **SvgToPdf** モジュールを呼び出してください。

Ruby コード

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

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから **Convert SVG to PDF (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
