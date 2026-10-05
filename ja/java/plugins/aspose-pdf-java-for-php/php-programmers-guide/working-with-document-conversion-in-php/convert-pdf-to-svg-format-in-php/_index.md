---
title: PHPでPDFをSVG形式に変換する
linktitle: PHPでPDFをSVG形式に変換する
type: docs
weight: 30
url: /ja/java/convert-pdf-to-svg-format-in-php/
description: Aspose.PDF を使用して、PHPで PDF ドキュメントを SVG 形式に変換し、高品質なベクターグラフィックス変換を実現する方法をご紹介します。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDF を SVG に変換

**Aspose.PDF Java for PHP** を使用して PDF を SVG 形式に変換するには、単に **PdfToSvg** モジュールを呼び出すだけです。

PHP コード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# instantiate an object of SvgSaveOptions
$save_options = new SvgSaveOptions();

# do not compress SVG image to Zip archive
$save_options->CompressOutputToZipArchive = false;

# Save the output to XLS format
$pdf->save($dataDir . "Output.svg", $save_options);

print "Document has been converted successfully" . PHP_EOL;

```

**実行コードをダウンロード**

ダウンロードВ **PDFをSVG形式に変換 (Aspose.PDF)**В 以下の任意のソーシャルコーディングサイトから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
