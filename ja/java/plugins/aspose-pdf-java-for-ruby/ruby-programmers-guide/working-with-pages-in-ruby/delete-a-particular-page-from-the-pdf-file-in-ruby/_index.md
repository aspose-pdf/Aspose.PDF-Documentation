---
title: "Ruby での PDFファイルから特定のページの削除"
linktitle: "Ruby での PDFファイルから特定のページの削除"
type: docs
weight: 20
url: /ja/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: Aspose.PDF for Rubyを使用して、プログラムでPDFファイルから特定のページを削除します。
lastmod: "2026-10-05"
---
## Aspose.PDF - ページ削除

**Aspose.PDF Java for Ruby** を使用してPDFドキュメントから特定のページを削除するには、単に **DeletePage** モジュールを呼び出します。

Rubyコード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## 実行中のコードをダウンロード

ダウンロード **Delete Page (Aspose.PDF)**В fromВ 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
