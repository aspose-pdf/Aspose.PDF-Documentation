---
title: "Java で PDF を Excel に変換"
linktitle: "PDF から Excel への変換"
type: docs
weight: 20
url: /ja/java/convert-pdf-to-excel/
lastmod: "2026-10-06"
description: Aspose.PDF を使用して Java で PDF ファイルを Excel に変換する方法を学び、XML Spreadsheet 2003、XLSX、XLSM、CSV、ODS の出力もサポートします。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF を Excel に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを Excel 互換形式に変換する方法について説明します。XML Spreadsheet 2003、XLSX、XLSM、CSV、ODS の出力に加え、空白列の挿入やシート数の最小化オプションについても取り上げます。
---
Aspose.PDF for Java は、さまざまなレイアウトオプションで PDF コンテンツを複数のスプレッドシート形式にエクスポートできます。[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を使用して、対象のワークブック形式を選択し、ページコンテンツがワークシートと列にどのようにマッピングされるかを制御します。

## PDF を Excel 2003 XML に変換

PDF コンテンツを Excel 2003 XML スプレッドシート形式にエクスポートする必要がある場合は、この例をご使用ください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を作成し、その形式を `XMLSpreadSheet2003` に設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、ロードされた PDF を Excel 2003 XML スキーマでシリアライズしてください。
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

## PDF の XLSX への変換

PDF コンテンツを Excel 2007 以降の XLSX 形式に変換する必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を作成し、その形式を `XLSX` に設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、PDF のレイアウトが Office Open XML ブックとしてエクスポートされます。
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

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を `XLSX` 出力用に作成してください。
1. PDF から作成されたワークシートのレイアウトを改善するために、先頭に追加の空白列が必要な場合は、`setInsertBlankColumnAtFirst(true)` を有効にしてください。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` を実行し、変換された XLSX ファイルを書き込んでください。

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

## PDF を単一の Excel ワークシートに変換

すべての PDF ページを 1 つのワークシートにエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. `XLSX` エクスポート用に [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を作成してください。
1. `setMinimizeTheNumberOfWorksheets(true)` を有効にして、複数の PDF ページを少ないワークシートに統合してください。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` して、XLSX 出力ファイルを保存してください。

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

## PDF から XLSM への変換

PDF 出力をマクロ有効の Excel ワークブックとして保存する必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を作成し、形式を `XLSM` に設定してください。
1. 呼び出し `document.save(outputFile.toString(), saveOptions)` して、PDF コンテンツをマクロ有効ブック コンテナにエクスポートしてください。
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

## PDF から CSV への変換

PDF の表形式コンテンツを CSV にエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を作成し、形式を `CSV` に設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、PDF のコンテンツがカンマ区切りのテキスト出力にフラット化されます。
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

## PDF から ODS への変換

PDF コンテンツを OpenDocument スプレッドシート形式にエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) を作成し、形式を `ODS` に設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、PDF は OpenDocument スプレッドシート形式でエクスポートされます。
1. 変換された ODS ファイルを保存してください。

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
