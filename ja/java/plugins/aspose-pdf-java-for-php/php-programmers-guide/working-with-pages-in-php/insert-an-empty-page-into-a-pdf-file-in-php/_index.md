---
title: PDFファイルに空のページを挿入する方法（PHP）
type: docs
weight: 70
url: ja/java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 空のページを挿入

**Aspose.PDF Java for PHP**を使用してPDFドキュメントに空のページを挿入するには、**InsertEmptyPage**クラスを呼び出すだけです。

PHPコード

```php

# ターゲットドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# PDFに空のページを挿入
$pdf->getPages()->insert(1);

# 結合された出力ファイルを保存（ターゲットドキュメント）
$pdf->save($dataDir . "output.pdf");

print "空のページが正常に追加されました！";

```

**実行可能なコードをダウンロード**

以下に挙げるいずれかのソーシャルコーディングサイトから**Insert an Empty Page (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)