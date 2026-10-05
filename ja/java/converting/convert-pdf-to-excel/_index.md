---
title: JavaでPDFをExcelに変換
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: /ja/java/convert-pdf-to-excel/
lastmod: "2026-10-05"
description: Aspose.PDF を使用して Java で PDF ファイルを Excel に変換する方法を学び、XML Spreadsheet 2003、XLSX、XLSM、CSV、ODS の出力もサポートします。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF を Excel に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを Excel 互換形式に変換する方法について説明します。XML Spreadsheet 2003、XLSX、XLSM、CSV、ODS の出力に加え、空白列の挿入やシート数の最小化オプションについても取り上げます。
---
Aspose.PDF for Java は、さまざまなレイアウトオプションで PDF コンテンツを複数のスプレッドシート形式にエクスポートできます。使用 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 対象のワークブック形式を選択し、ページコンテンツがワークシートと列にどのようにマッピングされるかを制御します。

## PDF を Excel 2003 XML に変換

PDF コンテンツを Excel 2003 XML スプレッドシート形式にエクスポートする必要がある場合は、この例をご使用ください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) そしてその形式を設定します `XMLSpreadSheet2003`。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` そのため、ロードされた PDF は Excel 2003 XML スキーマでシリアライズされます。
1. 変換された出力ファイルを保存してください。

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDFをXLSXに変換する

PDF コンテンツを Excel 2007+ XLSX 形式に変換する必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) そしてその形式を設定します `XLSX`。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` したがって、PDFのレイアウトは Office Open XML ブックブックとしてエクスポートされます。
1. 出力スプレッドシートファイルを保存してください。

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF を XLSX に変換し、列の制御を行う

PDF から Excel への変換中に列の処理を調整する必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) のために `XLSX` 出力。
1. 有効にする `setInsertBlankColumnAtFirst(true)` PDF から作成されたワークシートのレイアウトを改善するために、追加の先頭列が必要な場合。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` そして変換されたXLSXファイルを書き込む。

```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDFを単一のExcelワークシートに変換する

すべての PDF ページを 1 つのワークシートにエクスポートする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) のために `XLSX` エクスポート。
1. 有効にする `setMinimizeTheNumberOfWorksheets(true)` 複数の PDF ページが少ないワークシートに統合されます。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` そしてXLSX出力ファイルを保存してください。

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF を XLSM に変換

PDF 出力をマクロ有効 Excel ワークブックとして保存する必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) そして形式を設定します `XLSM`。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` その結果、PDF コンテンツはマクロ有効ブック コンテナにエクスポートされます。
1. XLSM ファイルを保存してください。

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF を CSV に変換

PDF の表形式コンテンツを CSV にエクスポートする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) そして形式を設定します `CSV`。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` PDF のコンテンツはカンマ区切りのテキスト出力にフラット化されます。
1. 生成された CSV ファイルを保存してください。

```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF を ODS に変換

PDF コンテンツを OpenDocument スプレッドシート形式にエクスポートする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) そして形式を設定します `ODS`。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` そのため、PDFはOpenDocumentスプレッドシート形式でエクスポートされます。
1. 変換されたODSファイルを保存してください。

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
