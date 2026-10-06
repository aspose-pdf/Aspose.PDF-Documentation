---
title: "PHP での PDF ファイルへの空白ページの挿入"
linktitle: "PHP での PDF ファイルへの空白ページの挿入"
type: docs
weight: 70
url: /ja/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: "Aspose.PDF を使用して柔軟な文書構造を実現し、PHP で PDF ファイル内の任意の位置に空白ページを挿入する方法を学びます。"
lastmod: "2026-10-06"
---
## Aspose.PDF - 空白ページの挿入

**Aspose.PDF Java for PHP** を使用して PDF 文書に空白ページを挿入するには、**InsertEmptyPage** クラスを呼び出してください。

PHPコード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```

**実行コードをダウンロード**

以下に記載されたソーシャルコーディングサイトのいずれかから、**空ページの挿入 (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
