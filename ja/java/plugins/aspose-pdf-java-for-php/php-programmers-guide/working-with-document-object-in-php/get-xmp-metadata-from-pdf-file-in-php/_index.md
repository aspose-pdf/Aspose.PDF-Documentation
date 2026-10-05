---
title: "PHP での PDF ファイルから XMP メタデータの取得"
linktitle: "PHP での PDF ファイルから XMP メタデータの取得"
type: docs
weight: 50
url: /ja/java/get-xmp-metadata-from-pdf-file-in-php/
description: "Aspose.PDF を使用して、PHP で PDF ドキュメントから XMP メタデータを抽出し、詳細なコンテンツ分析を行う方法を学びます。"
lastmod: "2026-10-06"
---
## Aspose.PDF - XMPメタデータの取得

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントから XMP メタデータを取得するには、**GetXMPMetadata** クラスを呼び出すだけです。

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

ダウンロード **XMP メタデータを取得 (Aspose.PDF)** は、以下に記載されたソーシャルコーディングサイトのいずれかから行えます。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
