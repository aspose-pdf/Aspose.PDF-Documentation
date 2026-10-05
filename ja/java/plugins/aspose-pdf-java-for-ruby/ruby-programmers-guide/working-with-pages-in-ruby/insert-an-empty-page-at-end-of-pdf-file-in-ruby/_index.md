---
title: "Ruby での PDFファイルの末尾に空白ページの挿入"
linktitle: "Ruby での PDFファイルの末尾に空白ページの挿入"
type: docs
weight: 60
url: /ja/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/
description: Ruby と Aspose.PDF を使用して PDF 文書の末尾に空白ページを挿入する方法を見つけ、PDF 処理タスクに柔軟性を加えます。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDF ファイルの末尾に空白ページの挿入

**Aspose.PDF Java for Ruby** を使用して PDF 文書の末尾に空白ページを挿入するには、単に **InsertEmptyPageAtEndOfFile** モジュールを呼び出します。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# insert a empty page in a PDF

pdf.getPages().add()

# Save the concatenated output file (the target document)

pdf.save(data_dir+ "output.pdf")

puts "Empty page added successfully!"
```

## 実行コードをダウンロード

ダウンロード **PDF ファイルの末尾に空のページを挿入 (Aspose.PDF)**\u0412\u00A0から\u0412\u00A0以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/insertemptypageatendoffile.rb)
