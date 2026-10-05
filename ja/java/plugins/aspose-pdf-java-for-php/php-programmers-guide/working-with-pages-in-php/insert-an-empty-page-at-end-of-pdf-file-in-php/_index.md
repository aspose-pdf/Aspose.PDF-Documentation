---
title: "PHP での PDF ファイルの末尾に空白ページの挿入"
linktitle: "PHP での PDF ファイルの末尾に空白ページの挿入"
type: docs
weight: 60
url: /ja/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: Aspose.PDF を使用してドキュメントを拡張する方法として、PHP で PDF ドキュメントの末尾に空白ページを挿入する方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDF ファイルの末尾に空白ページの挿入

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントの末尾に空白ページを挿入するには、単に **InsertEmptyPageAtEndOfFile** クラスを呼び出します。

PHP コード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## 実行コードをダウンロード

ダウンロード **PDF ファイルの末尾に空のページを挿入 (Aspose.PDF)**В からВ 以下に挙げるソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
