---
title: "Ruby での PDF ファイルから XMP メタデータの取得"
linktitle: "Ruby での PDF ファイルから XMP メタデータの取得"
type: docs
weight: 60
url: /ja/java/get-xmp-metadata-from-pdf-file-in-ruby/
description: "Aspose.PDF を使用して、Ruby で PDF ドキュメントの XMP メタデータにアクセスし、操作します。"
lastmod: "2026-10-06"
---
## Aspose.PDF - XMPメタデータの取得

**Aspose.PDF Java for Ruby** を使用して PDF ドキュメントから XMP メタデータを取得するには、**GetXMPMetadata** モジュールを呼び出してください。

Ruby コード

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get properties

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## 実行中のコードのダウンロード

以下に記載されたソーシャルコーディングサイトのいずれかから **Get XMP Metadata (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
