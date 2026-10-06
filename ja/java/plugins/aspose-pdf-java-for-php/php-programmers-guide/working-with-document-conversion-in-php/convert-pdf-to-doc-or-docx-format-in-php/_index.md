---
title: "PHP での PDF の DOC または DOCX 形式への変換"
linktitle: "PHP での PDF の DOC または DOCX 形式への変換"
type: docs
weight: 10
url: /ja/java/convert-pdf-to-doc-or-docx-format-in-php/
description: "Aspose.PDF を使用して、PHP で PDF ドキュメントを DOC または DOCX 形式に変換し、より簡単に文書を編集する方法を学びます。"
lastmod: "2026-10-06"
---
## Aspose.PDF - PDF の DOC または DOCX への変換

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントを DOC または DOCX 形式に変換するには、シンプルに **PdfToDoc** モジュールを呼び出します。

PHP コード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.doc");

print "Document has been converted successfully";

```

**実行コードをダウンロード**

ダウンロード **PDF を DOC または DOCX に変換 (Aspose.PDF)** から、以下に記載されたソーシャルコーディングサイトのいずれかで:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)
