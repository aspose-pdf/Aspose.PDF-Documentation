---
title: "PHP での PDF ファイルからの特定ページの削除"
linktitle: "PHP での PDF ファイルからの特定ページの削除"
type: docs
weight: 20
url: /ja/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: "Aspose.PDF を使用して PHP で PDF ドキュメントから特定のページを削除する方法を学び、ドキュメント編集を簡素化します。"
lastmod: "2026-10-06"
---
## Aspose.PDF - ページの削除

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントから特定のページを削除するには、**DeletePage** クラスを呼び出してください。

PHP コード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**ダウンロード実行中**

以下に記載されたソーシャルコーディングサイトのいずれかから **Delete Page (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
