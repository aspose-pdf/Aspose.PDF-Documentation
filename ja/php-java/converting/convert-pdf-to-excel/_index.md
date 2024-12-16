---
title: PDFをMicrosoft Excelに変換 
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: /ja/php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
description: Aspose.PDF for PHPを使用すると、PDFをExcel形式に変換できます。この過程で、PDFファイルの各ページはExcelワークシートに変換されます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for PHP APIを使用すると、PDFファイルをExcelの[XLS](https://docs.fileformat.com/spreadsheet/xls/)および[XLSX](https://docs.fileformat.com/spreadsheet/xlsx/)ファイル形式にレンダリングできます。既存のExcelワークブックを作成および操作する機能を提供する別のAPI、[Aspose.Cells for PHP via Java](https://products.aspose.com/cells/php-java)もあります。これにより、ExcelワークブックをPDF形式に変換する機能も提供されます。

{{% alert color="primary" %}}

**PDFをExcelにオンラインで変換してみる**

Aspose.PDF for PHPは、オンラインで無料のアプリケーション["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)を提供しており、ここでその機能と作業品質を調査することができます。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## PDFをExcel XLSに変換する

PDFファイルをXLS形式に変換するには、Aspose.PDFには[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)というクラスがあります。[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)クラスのオブジェクトは、Document.Save(..)メソッドの2番目の引数として渡されます。

PDFファイルをXLSX形式に変換することは、Aspose.PDF for PHP 18.6バージョンのライブラリの一部です。PDFファイルをXLSX形式に変換するには、[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)クラスのsetFormat()メソッドを使用して形式をXLSXに設定する必要があります。

以下のコードスニペットは、PDFファイルをXLSおよびXLSX形式に変換する方法を示しています。

```php
// Documentクラスを使用して入力PDFドキュメントを読み込みます。
$document = new Document($inputFile);

// 保存オプションを指定するためにExcelSaveOptionsクラスのインスタンスを作成します。
$saveOption = new ExcelSaveOptions();

// 出力フォーマットをXLSに設定します。
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// 出力フォーマットをXLSXに設定します。
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// 指定された保存オプションを使用してPDFドキュメントをExcelファイルとして保存します。
$document->save($outputFile, $saveOption);
```