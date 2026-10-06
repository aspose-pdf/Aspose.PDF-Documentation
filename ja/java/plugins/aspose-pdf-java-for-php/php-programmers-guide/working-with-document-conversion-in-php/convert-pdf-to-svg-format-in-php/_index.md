---
title: "PHP での PDFのSVG形式への変換"
linktitle: "PHP での PDFのSVG形式への変換"
type: docs
weight: 30
url: /ja/java/convert-pdf-to-svg-format-in-php/
description: Aspose.PDF を使用して、PHPで PDF ドキュメントを SVG 形式に変換し、高品質なベクターグラフィックス変換を実現する方法をご紹介します。
lastmod: "2026-10-06"
---
## Aspose.PDF - PDF を SVG に変換

**Aspose.PDF Java for PHP** を使用して PDF を SVG 形式に変換するには、**PdfToSvg** モジュールを呼び出すだけです。

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

**PDFをSVG形式に変換 (Aspose.PDF)** を、以下のいずれかのソーシャルコーディングサイトからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
