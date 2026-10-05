---
title: "Ruby での PDF の DOC または DOCX 形式への変換"
linktitle: "Ruby での PDF の DOC または DOCX 形式への変換"
type: docs
weight: 30
url: /ja/java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: "Aspose.PDF を使って Ruby で PDF ドキュメントを DOC または DOCX 形式に変換する方法を学び、編集や処理を容易にします。"
lastmod: "2026-10-06"
---
## Aspose.PDF - PDF から DOC または DOCX への変換

Ruby 用 **Aspose.PDF Java** を使用して PDF ドキュメントを DOC または DOCX 形式に変換するには、**PdfToDoc** モジュールを呼び出してください。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## 実行中のコードのダウンロード

**Convert PDF to DOC or DOCX (Aspose.PDF)** を、以下に記載されたいずれかのソーシャルコーディングサイトからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
