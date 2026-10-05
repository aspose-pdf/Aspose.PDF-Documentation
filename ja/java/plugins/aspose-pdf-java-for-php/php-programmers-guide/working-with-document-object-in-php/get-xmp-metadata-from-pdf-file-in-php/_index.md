---
title: "PHP での PDFファイルからXMPメタデータの取得"
linktitle: "PHP での PDFファイルからXMPメタデータの取得"
type: docs
weight: 50
url: /ja/java/get-xmp-metadata-from-pdf-file-in-php/
description: Aspose.PDF を使用して、PHPでPDFドキュメントからXMPメタデータを抽出し、詳細なコンテンツ分析を行う方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - XMPメタデータの取得

**Aspose.PDF Java for PHP** を使用してPDFドキュメントからXMPメタデータを取得するには、単に **GetXMPMetadata** クラスを呼び出すだけです。

PHPコード

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**実行中のコードをダウンロード**

ダウンロードВ **XMP メタデータを取得 (Aspose.PDF)**В 以下に記載されたソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
