---
title: "Ruby での PDF ファイルの連結"
linktitle: "Ruby での PDF ファイルの連結"
type: docs
weight: 10
url: /ja/java/concatenate-pdf-files-in-ruby/
description: "Ruby と Aspose.PDF を使用して、複数の PDF を効率的に単一のドキュメントに結合できます。"
lastmod: "2026-10-06"
---
## Aspose.PDF - PDF ファイルの連結

**Aspose.PDF Java for Ruby** を使用して PDF ファイルを連結するには、**ConcatenatePdfFiles** モジュールを呼び出してください。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## 実行コードのダウンロード

ダウンロード **Concatenate PDF Files (Aspose.PDF)** 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
