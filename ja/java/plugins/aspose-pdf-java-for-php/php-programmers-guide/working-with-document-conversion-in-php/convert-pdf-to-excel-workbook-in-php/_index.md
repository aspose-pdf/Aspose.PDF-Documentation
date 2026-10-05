---
title: PHPでPDFをExcelブックに変換する
linktitle: PHPでPDFをExcelブックに変換する
type: docs
weight: 20
url: /ja/java/convert-pdf-to-excel-workbook-in-php/
description: Aspose.PDF を使用して PHP で PDF ファイルを Excel ブックに変換する方法を学び、シームレスなデータ抽出と操作を可能にします。
lastmod: "2026-10-05"
---
## Aspose.PDF - PDFをExcelブックに変換

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントを Excel ブックに変換するには、単に **PdfToExcel** モジュールを呼び出します。

PHPコード

```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```

**実行コードをダウンロード**

ダウンロードВ **PDF を Excel ブックに変換 (Aspose.PDF)**В 以下のソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
