---
title: "PHP での PDF の有効期限の設定"
linktitle: "PHP での PDF の有効期限の設定"
type: docs
weight: 80
url: /ja/java/set-pdf-expiration-in-php/
description: "Aspose.PDF を使用して、PHP で PDF ファイルの有効期限を設定し、アクセスを制御する方法を確認してください。"
lastmod: "2026-10-06"
---
## Aspose.PDF - PDF の有効期限の設定

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントの有効期限を設定するには、単に **SetExpiration** クラスを呼び出してください。

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

ダウンロード **Set PDF Expiration (Aspose.PDF)** は、以下に記載されたソーシャルコーディングサイトのいずれかから行ってください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
