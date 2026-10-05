---
title: "Ruby での PDFファイルへの空白ページの挿入"
linktitle: "Ruby での PDFファイルへの空白ページの挿入"
type: docs
weight: 70
url: /ja/java/insert-an-empty-page-into-a-pdf-file-in-ruby/
description: RubyとAspose.PDFを使用して、PDFドキュメント内の特定の位置に空白ページを挿入する方法を学び、正確なドキュメント管理を実現します。
lastmod: "2026-10-05"
---
## Aspose.PDF - 空白ページの挿入

**Aspose.PDF Java for Ruby**を使用してPDFドキュメントに空白ページを挿入するには、単に**InsertEmptyPage**モジュールを呼び出すだけです。

Rubyコード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().insert(1)

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## 実行コードをダウンロード

以下に記載されたソーシャルコーディングサイトから **Insert an Empty Page (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypage.rb)
