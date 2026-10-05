---
title: RubyでPDFをDOCまたはDOCX形式に変換する
linktitle: RubyでPDFをDOCまたはDOCX形式に変換する
type: docs
weight: 30
url: /ja/java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Aspose.PDFを使ってRubyでPDFドキュメントをDOCまたはDOCX形式に変換する方法を学び、編集や処理を容易にします。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDFをDOCまたはDOCXに変換

Ruby用 **Aspose.PDF Java** を使用してPDFドキュメントをDOCまたはDOCX形式に変換するには、**PdfToDoc** モジュールを呼び出すだけです。

Rubyコード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## 実行中のコードをダウンロード

ダウンロードВ **Convert PDF to DOC or DOCX (Aspose.PDF)**В 以下に記載されたソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
