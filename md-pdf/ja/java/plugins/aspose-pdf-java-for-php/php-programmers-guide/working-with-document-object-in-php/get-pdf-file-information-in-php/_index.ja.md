---
title: PHPでPDFファイル情報を取得する
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイル情報を取得する

**Aspose.PDF Java for PHP**を使用してPdfドキュメントのファイル情報を取得するには、単に**GetPdfFileInfo**クラスを呼び出します。

PHPコード

```php

# PDFドキュメントを開く。
$doc = new Document($dataDir . "input1.pdf");

# ドキュメント情報を取得
$doc_info = $doc->getInfo();

# ドキュメント情報を表示
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Get PDF File Information (Aspose.PDF)**をダウンロードします:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)