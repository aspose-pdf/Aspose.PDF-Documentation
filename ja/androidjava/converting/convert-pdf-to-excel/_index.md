---
title: PDFをExcelに変換する
linktitle: PDFをExcelに変換する
type: docs
weight: 90
url: ja/androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via JavaはPDFをExcel形式に変換することができます。この際、PDFファイルの個々のページがExcelのワークシートに変換されます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java APIを使用すると、PDFファイルをExcelの[XLS](https://docs.fileformat.com/spreadsheet/xls/)および[XLSX](https://docs.fileformat.com/spreadsheet/xlsx/)ファイル形式にレンダリングできます。既存のExcelワークブックを作成および操作する機能を提供する別のAPIである[Aspose.Cells for Java](https://products.aspose.com/cells/java)もあります。また、ExcelワークブックをPDF形式に変換する機能も提供しています。

{{% alert color="primary" %}}

オンラインで試してみてください。
 Aspose.PDF の変換品質を確認し、オンラインで結果を表示するには、このリンクをクリックしてください [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

{{% /alert %}}

## PDF を Excel XLS に変換

PDF ファイルを XLS 形式に変換するには、Aspose.PDF には [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) というクラスがあります。[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) クラスのオブジェクトは、Document.Save(..) コンストラクタの第 2 引数として渡されます。

PDF ファイルを XLSX 形式に変換することは、Aspose.PDF for Java 18.6 バージョンのライブラリの一部です。PDF ファイルを XLSX 形式に変換するには、[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) クラスの setFormat() メソッドを使用して形式を XLSX に設定する必要があります。

以下のコードスニペットは、PDF ファイルを xls および .xlsx 形式に変換する方法を示しています。

```java
public void convertPDFtoExcelSimple() {
        // ソース PDF ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSave Option オブジェクトをインスタンス化
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // ファイルを MS ドキュメント形式で保存
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDFをXLSに変換して列を制御する

PDFをXLS形式に変換する際、出力ファイルの最初の列として空白の列が追加されます。[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) クラスの InsertBlankColumnAtFirst オプションはこの列を制御するために使用されます。デフォルト値は true です。

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // ソースPDFドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSave Optionオブジェクトをインスタンス化
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // ファイルをMSドキュメント形式で保存
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDFを単一のExcelワークシートに変換

ページ数の多いPDFファイルをXLSにエクスポートする場合、各ページはExcelファイルの異なるシートにエクスポートされます。これは、MinimizeTheNumberOfWorksheetsプロパティがデフォルトでfalseに設定されているためです。出力Excelファイルで全ページを単一のシートにエクスポートするには、MinimizeTheNumberOfWorksheetsプロパティをtrueに設定します。

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // ソースPDFドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSave Optionオブジェクトをインスタンス化
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // 出力をXLSXで保存
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // MS Excel形式でファイルを保存
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## XLSX形式に変換する

デフォルトでAspose.PDFはデータを保存するためにXML Spreadsheet 2003を使用します。PDFファイルをXLSX形式に変換するために、Aspose.PDFにはFormatを持つExcelSaveOptionsというクラスがあります。[ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions)クラスのオブジェクトは、Document.Save(..)メソッドの第二引数として渡されます。

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // PDFドキュメントをロード
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSave Optionオブジェクトをインスタンス化
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // 出力をCSVで保存
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // ファイルをCSV形式で保存
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```