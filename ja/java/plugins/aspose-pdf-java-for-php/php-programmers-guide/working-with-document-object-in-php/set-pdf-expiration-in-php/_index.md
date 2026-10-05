---
title: "PHP での PDFの有効期限の設定"
linktitle: "PHP での PDFの有効期限の設定"
type: docs
weight: 80
url: /ja/java/set-pdf-expiration-in-php/
description: Aspose.PDF を使用して、PHPでPDFファイルの有効期限を設定し、アクセスを制御する方法を確認してください。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDFの有効期限の設定

**Aspose.PDF Java for PHP** を使用して В  PDF ドキュメントの有効期限を設定するには、単に **SetExpiration** クラスを呼び出します。

PHPコード

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('The file is expired. You need a new one.');");
$doc->setOpenAction($javascript);

# save update document with new information
$doc->save($dataDir . "set_expiration.pdf");

print "Update document information, please check output file." . PHP_EOL;

```

**実行コードをダウンロード**

ダウンロードВ **Set PDF Expiration (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれかで:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
