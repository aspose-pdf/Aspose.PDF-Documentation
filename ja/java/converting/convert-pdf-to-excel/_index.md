---
title: PDFをExcelに変換 
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: ja/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
keywords: Javaを使用してPDFをExcelに変換, Javaを使用してPDFをXLSに変換, Javaを使用してPDFをXLSXに変換, JavaでPDFからExcelにテーブルをエクスポート
description: Aspose.PDF for Javaを使用すると、PDFをExcel形式に変換できます。この間、PDFファイルの個々のページがExcelワークシートに変換されます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Java APIを使用すると、PDFファイルをExcel [XLS](https://docs.fileformat.com/spreadsheet/xls/) および [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) ファイル形式にレンダリングできます。既存のExcelワークブックを作成および操作する機能を提供する別のAPI、[Aspose.Cells for Java](https://products.aspose.com/cells/java)もあります。また、ExcelワークブックをPDF形式に変換する機能も提供します。

{{% alert color="primary" %}}

**PDFをExcelにオンラインで変換してみてください**

Aspose.PDF for Java は、オンラインで無料のアプリケーション ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) を提供しており、機能性と品質を調査することができます。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## PDFをExcel XLSに変換する

PDFファイルをXLS形式に変換するには、Aspose.PDFには[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)というクラスがあります。[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)クラスのオブジェクトをDocument.Save(..)メソッドの第二引数として渡します。

PDFファイルをXLSX形式に変換することは、Aspose.PDF for Java 18.6バージョンのライブラリの一部です。PDFファイルをXLSX形式に変換するためには、[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)クラスのsetFormat()メソッドを使用して形式をXLSXに設定する必要があります。

以下のコードスニペットは、PDFファイルをxlsおよび.xlsx形式に変換する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // ドキュメントディレクトリへのパス。
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // PDFドキュメントを読み込む
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // ExcelSave Optionオブジェクトをインスタンス化する
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // 出力をXLS形式で保存する
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```

## PDFを制御列でXLSに変換する

PDFをXLS形式に変換すると、最初の列として空白の列が出力ファイルに追加されます。この列を制御するために、[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)クラスのInsertBlankColumnAtFirstオプションが使用されます。そのデフォルト値はtrueです。

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // PDFドキュメントを読み込む
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Excel保存オプションオブジェクトをインスタンス化
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // 出力をXLS形式で保存
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## PDFを単一のExcelワークシートに変換

ページ数が多いPDFファイルをXLSにエクスポートする場合、各ページがExcelファイルの異なるシートにエクスポートされます。
 これは、MinimizeTheNumberOfWorksheets プロパティがデフォルトで false に設定されているためです。出力される Excel ファイルですべてのページを1つのシートにエクスポートするには、MinimizeTheNumberOfWorksheets プロパティを true に設定します。

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // PDFドキュメントを読み込む
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Excel保存オプションオブジェクトをインスタンス化
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // 出力をXLS形式で保存
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## XLSX形式に変換

デフォルトでは、Aspose.PDF はデータを保存するために XML スプレッドシート 2003 を使用します。 PDFファイルをXLSX形式に変換するために、Aspose.PDFにはFormatを持つExcelSaveOptionsというクラスがあります。[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)クラスのオブジェクトは、Document.Save(..)メソッドの第2引数として渡されます。

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // PDFドキュメントをロード
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // ExcelSaveオプションオブジェクトをインスタンス化
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // 出力をXLS形式で保存
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```