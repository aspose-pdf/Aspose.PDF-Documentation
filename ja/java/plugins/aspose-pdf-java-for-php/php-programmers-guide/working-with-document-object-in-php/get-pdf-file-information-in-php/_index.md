---
title: "PHP での PDF ファイル情報の取得"
linktitle: "PHP での PDF ファイル情報の取得"
type: docs
weight: 40
url: /ja/java/get-pdf-file-information-in-php/
description: Aspose.PDF を使用して、PHP で PDF ファイルのメタデータやプロパティを含む詳細情報を取得する方法をご紹介します。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDF ファイル情報の取得

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントのファイル情報を取得するには、シンプルに **GetPdfFileInfo** クラスを呼び出します。

PHP コード

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

# Show document information
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```

**実行コードをダウンロード**

ダウンロードВ **PDF ファイル情報の取得 (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれか:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
