---
title: PHPでPDFをExcelワークブックに変換
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFをExcelワークブックに変換

**Aspose.PDF Java for PHP**を使用してPDFドキュメントをExcelワークブックに変換するには、**PdfToExcel**モジュールを呼び出します。

PHPコード

```php
# 対象のドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# ExcelSaveオプションオブジェクトをインスタンス化する
$excelsave = new ExcelSaveOptions();

# 出力をXLS形式で保存する
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "ドキュメントが正常に変換されました" . PHP_EOL;

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Convert PDF to Excel Workbook (Aspose.PDF)**をダウンロードします：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)