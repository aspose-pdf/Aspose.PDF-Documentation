---
title: PHPでSVGファイルをPDF形式に変換する
linktitle: PHPでSVGファイルをPDF形式に変換する
type: docs
weight: 40
url: /ja/java/convert-svg-file-to-pdf-format-in-php/
description: Aspose.PDF を使用して、効果的なドキュメント管理のために、PHPでSVGファイルをPDF形式に変換する方法を探ります。
lastmod: "2026-10-05"
---
## Aspose.PDF - SVG を PDF に変換

**Aspose.PDF Java for PHP** を使用して SVG ファイルを PDF 形式に変換するには、シンプルに **SvgToPdf** モジュールを呼び出します。

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

ダウンロードВ **SVG を PDF に変換 (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
