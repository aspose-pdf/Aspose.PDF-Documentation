---
title: PHPでPDFをDOCまたはDOCX形式に変換する
linktitle: PHPでPDFをDOCまたはDOCX形式に変換する
type: docs
weight: 10
url: /ja/java/convert-pdf-to-doc-or-docx-format-in-php/
description: Aspose.PDF を使用して、PHPで PDF ドキュメントを DOC または DOCX 形式に変換し、より簡単に文書を編集する方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDF を DOC または DOCX に変換する

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

ダウンロードВ **PDF を DOC または DOCX に変換 (Aspose.PDF)**В からВ 以下に記載されたソーシャル コーディング サイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)
