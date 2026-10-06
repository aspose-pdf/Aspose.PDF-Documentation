---
title: "PHP での SVG ファイルの PDF 形式への変換"
linktitle: "PHP での SVG ファイルの PDF 形式への変換"
type: docs
weight: 40
url: /ja/java/convert-svg-file-to-pdf-format-in-php/
description: "Aspose.PDF を使用して、PHP で SVG ファイルを PDF 形式に変換する方法を学び、効果的なドキュメント管理を実現してください。"
lastmod: "2026-10-06"
---
## Aspose.PDF - SVG を PDF に変換

**Aspose.PDF Java for PHP** を使用して SVG ファイルを PDF 形式に変換するには、**SvgToPdf** モジュールを呼び出してください。

PHP コード

```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```

**実行コードをダウンロード**

**SVG を PDF に変換 (Aspose.PDF)** を、以下に記載されたソーシャルコーディングサイトのいずれかからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
