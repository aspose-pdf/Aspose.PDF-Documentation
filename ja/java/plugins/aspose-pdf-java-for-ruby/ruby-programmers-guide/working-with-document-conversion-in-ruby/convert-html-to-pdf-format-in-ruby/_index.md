---
title: RubyでHTMLをPDF形式に変換する
linktitle: RubyでHTMLをPDF形式に変換する
type: docs
weight: 10
url: /ja/java/convert-html-to-pdf-format-in-ruby/
description: Aspose.PDF を使用して、信頼性と正確性の高い文書生成を実現しながら、RubyでHTMLコンテンツをPDF形式に変換する方法を学びましょう。
lastmod: "2026-10-05"
---
## Aspose.PDF - HTMLをPDF形式に変換

**Aspose.PDF Java for Ruby** を使用してHTMLをPDF形式に変換するには、単に **HtmlToPdf** モジュールを呼び出すだけです。

Rubyコード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## 実行コードをダウンロード

ダウンロードВ **HTMLをPDF形式に変換 (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれか:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
