---
title: PHPファイルから特定のページを削除する
type: docs
weight: 20
url: ja/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページの削除

**Aspose.PDF Java for PHP**を使用してPDFドキュメントから特定のページを削除するには、**DeletePage**クラスを呼び出します。

PHPコード

```php

# 対象のドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# 特定のページを削除する
$pdf->getPages()->delete(2);

# 新しく生成されたPDFファイルを保存する
$pdf->save($dataDir . "output.pdf");

print "ページが正常に削除されました！";

```

**実行のダウンロード**

以下に記載されたいずれかのソーシャルコーディングサイトから**Delete Page (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)