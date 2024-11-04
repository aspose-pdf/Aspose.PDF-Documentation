---
title: PHPでPDFの有効期限を設定
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFの有効期限を設定

**Aspose.PDF Java for PHP**を使用してPDFドキュメントの有効期限を設定するには、単に**SetExpiration**クラスを呼び出します。

PHPコード

```php

# PDFドキュメントを開きます。
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('ファイルの有効期限が切れています。新しいファイルが必要です。');");
$doc->setOpenAction($javascript);

# 新しい情報で更新されたドキュメントを保存します
$doc->save($dataDir . "set_expiration.pdf");

print "ドキュメント情報を更新しました。出力ファイルを確認してください。" . PHP_EOL;

```

**実行コードをダウンロード**

以下に記載されたソーシャルコーディングサイトのいずれかから**Set PDF Expiration (Aspose.PDF)**をダウンロードできます：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)