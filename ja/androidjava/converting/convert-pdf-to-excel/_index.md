---
title: PDF を Excel に変換
linktitle: PDF を Excel に変換
type: docs
weight: 90
url: /ja/androidjava/convert-pdf-to-excel/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java は、PDF を Excel 形式に変換できるようにします。この際、PDF ファイルの個々のページが Excel のワークシートに変換されます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API を使用すると、PDF ファイルを Excel にレンダリングできます。 [XLS](https://docs.fileformat.com/spreadsheet/xls/) そして [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) ファイル形式です。すでに別の API があり、その名前は [Aspose.Cells for Java](https://products.aspose.com/cells/java), 既存のExcelワークブックを作成および操作する機能を提供します。\u00A0ExcelワークブックをPDF形式に変換する機能も提供します。

{{% alert color="primary" %}}

オンラインでお試しください。Aspose.PDF 変換の品質を確認し、結果をオンラインでこのリンクから表示できます。 [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## PDFをExcel XLSに変換

PDFファイルをXLS形式に変換するには、Aspose.PDFにクラスがあります [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). オブジェクトは [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) クラスは、 Document.Save(..) コンストラクタへの第2引数として渡されます。 

PDF ファイルを XLSX 形式に変換することは、Aspose.PDF for Java 18.6 バージョンのライブラリの一部です。PDF ファイルを XLSX 形式に変換するには、setFormat() メソッドを使用して形式を XLSX に設定する必要があります。 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) クラス。

以下のコードスニペットは、PDFファイルをxlsおよび.xlsx形式に変換する方法を示しています:

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Control Column を使用して PDF を XLS に変換

PDF を XLS 形式に変換する際、出力ファイルの最初の列として空白列が追加されます。The in [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) class InsertBlankColumnAtFirst オプションはこの列を制御するために使用されます。そのデフォルト値は true です。

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF を単一の Excel ワークシートに変換 

ページ数の多い PDF ファイルを XLS にエクスポートする場合、各ページが Excel ファイル内の別々のシートにエクスポートされます。これは、デフォルトで MinimizeTheNumberOfWorksheets プロパティが false に設定されているためです。すべてのページを出力 Excel ファイルの 1 つのシートにエクスポートするには、MinimizeTheNumberOfWorksheets プロパティを true に設定してください。

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## XLSX 形式に変換 

既定では Aspose.PDF はデータの保存に XML Spreadsheet 2003 を使用します。PDF ファイルを XLSX 形式に変換するために、Aspose.PDF には Format プロパティを持つ ExcelSaveOptions というクラスがあります。そのクラスのオブジェクトは [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) クラスは Document.Save(..) メソッドの第二引数として渡されます。

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
