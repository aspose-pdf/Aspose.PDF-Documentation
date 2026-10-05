---
title: "PHP での PDF ファイルから特定のページの削除"
linktitle: "PHP での PDF ファイルから特定のページの削除"
type: docs
weight: 20
url: /ja/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Aspose.PDF を使用して PHP で PDF ドキュメントから特定のページを削除する方法を探り、ドキュメント編集を簡素化します。
lastmod: "2026-10-05"
---
## Aspose.PDF - ページ削除

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントから特定のページを削除するには、シンプルに **DeletePage** クラスを呼び出すだけです。

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

ダウンロード **Delete Page (Aspose.PDF)**В fromВ 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
