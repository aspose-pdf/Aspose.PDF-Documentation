---
title: "Ruby での PDF のメタデータの削除"
linktitle: "Ruby での PDF のメタデータの削除"
type: docs
weight: 90
url: /ja/java/remove-metadata-from-pdf-in-ruby/
description: Aspose.PDF for Ruby を使用して、PDF ファイルの機密または不要なメタデータをプログラムで削除します。
lastmod: "2026-10-05"
---
## Aspose.PDF - メタデータの削除

**Aspose.PDF Java for Ruby** を使用して PDF ドキュメントのメタデータを削除するには、単に **RemoveMetadata** モジュールを呼び出します。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

В В В  doc.getMetadata().removeItem("pdfaid:part")

endВ В  В

if doc.getMetadata().contains("dc:format")

В В В  doc.getMetadata().removeItem("dc:format")

end

# save update document with new information

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Removed metadata successfully, please check output file."
```

## 実行中のコードをダウンロード

ダウンロードВ **メタデータの削除 (Aspose.PDF)**В 以下に記載されたソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
