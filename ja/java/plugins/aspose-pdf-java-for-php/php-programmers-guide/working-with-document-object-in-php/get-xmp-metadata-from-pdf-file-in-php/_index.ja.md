---
title: PHPでPDFファイルからXMPメタデータを取得する
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - XMPメタデータを取得

**Aspose.PDF Java for PHP**を使用してPDFドキュメントからXMPメタデータを取得するには、単に**GetXMPMetadata**クラスを呼び出します。

PHPコード

```php

# PDFドキュメントを開く。
$doc = new Document($dataDir . "input1.pdf");

# プロパティを取得
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Get XMP Metadata (Aspose.PDF)**をダウンロードします：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)