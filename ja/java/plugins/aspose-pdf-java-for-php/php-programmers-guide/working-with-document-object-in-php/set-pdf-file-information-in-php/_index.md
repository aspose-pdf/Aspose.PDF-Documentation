---
title: "PHP での PDFファイル情報の設定"
linktitle: "PHP での PDFファイル情報の設定"
type: docs
weight: 90
url: /ja/java/set-pdf-file-information-in-php/
description: Aspose.PDF を使用して PHP で PDF ドキュメントのメタデータなど、さまざまなファイルプロパティを設定する方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDFファイル情報の設定

**Aspose.PDF Java for PHP** を使用して PDF ドキュメント情報を更新するには、単に **SetPdfFileInfo** クラスを呼び出すだけです。

PHPコード

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# save update document with new information
$doc->save($dataDir . "Updated_Information.pdf");

print "Update document information, please check output file.";

```

**コードのダウンロード**

Download\u0412\u00A0**PDF ファイル情報の設定 (Aspose.PDF)**\u0412\u00A0以下に示すソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
