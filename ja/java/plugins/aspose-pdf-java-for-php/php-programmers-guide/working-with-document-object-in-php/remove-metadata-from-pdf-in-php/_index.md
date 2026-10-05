---
title: "PHP での PDFのメタデータの削除"
linktitle: "PHP での PDFのメタデータの削除"
type: docs
weight: 70
url: /ja/java/remove-metadata-from-pdf-in-php/
description: Aspose.PDF を使用して PHP で PDF ドキュメントのメタデータを削除し、プライバシーとドキュメントのセキュリティを向上させる方法を探ります。
lastmod: "2026-10-05"
---
## Aspose.PDF - メタデータの削除

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントからメタデータを削除するには、単に **RemoveMetadata** クラスを呼び出すだけです。

PHP コード

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# save update document with new information
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Removed metadata successfully, please check output file." . PHP_EOL;

```

**実行コードをダウンロード**

ダウンロードВ **Remove Metadata (Aspose.PDF)**В 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
