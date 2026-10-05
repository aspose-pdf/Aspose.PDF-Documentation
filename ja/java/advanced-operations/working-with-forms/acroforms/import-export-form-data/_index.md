---
title: フォーム データのインポートとエクスポート
linktitle: フォーム データのインポートとエクスポート
type: docs
weight: 80
url: /ja/java/import-export-form-data/
description: Aspose.PDF for Java を使用して、XML、FDF、XFDF、JSON 形式で AcroForm フィールド データのインポートとエクスポートを行います。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: JavaでPDFフォームデータをインポートおよびエクスポート
Abstract: この記事では、Aspose.PDF for Java を使用して AcroForm データを外部フォーマットとやり取りする方法を説明します。Form ファサードを介した XML、FDF、XFDF データのインポートおよびエクスポートと、フォームフィールドの値を JSON に抽出する方法をカバーしています。
---
Aspose.PDF for Java は、インタラクティブ フォーム用のいくつかの一般的なデータ交換フォーマットをサポートしています。

## XMLからFormデータのインポート

フォームの値がXMLファイルに保存されており、PDFフォームに適用する必要がある場合は、この例を使用してください。

1. 作成する [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードとソースPDFをバインドしてください。
1. XML入力ストリームを開き、データをフォームにインポートしてください。
1. 更新された PDF ドキュメントを保存してください。

```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## フォーム データを XML にエクスポート

現在の AcroForm の値を XML 形式で保存する必要がある場合は、この例を使用してください。

1. 作成する [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードとソースPDFをバインドしてください。
1. XML ファイルの出力ストリームを開いてください。
1. フォームデータをXMLにエクスポートしてください。

```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## FDF からフォーム データのインポート

フォームの値が FDF 交換形式で到着したときは、この例を使用してください。

1. 作成する [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードとソースPDFをバインドしてください。
1. FDF入力ストリームを開き、データをインポートしてください。
1. 記入済みのPDF文書を保存してください。

```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## フォームデータをFDFにエクスポート

PDFフォームの値をFDFファイルとして共有する必要がある場合は、この例を使用してください。

1. 作成する [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードとソースPDFをバインドしてください。
1. FDF ファイルの出力ストリームを開いてください。
1. FDF 形式でフォーム データをエクスポートしてください。

```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## XFDF からフォームデータのインポート

XFDF 形式で提供されたフォームデータを PDF にマージする必要がある場合は、この例を使用してください。

1. 作成する [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードとソースPDFをバインドしてください。
1. XFDF入力ストリームを開き、値をインポートしてください。
1. 更新された PDF ドキュメントを保存してください。

```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## XFDF にフォームデータのエクスポート

AcroForm の値のために XML ベースの交換ファイルが必要なときは、この例を使用してください。

1. 作成する [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードとソースPDFをバインドしてください。
1. XFDF ファイルの出力ストリームを開いてください。
1. 現在のフォーム値をXFDFにエクスポートしてください。

```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## フォームフィールドをJSONに抽出

フォーム値を軽量なJSON表現にエクスポートする場合は、この例を使用してください。

1. PDF を開くには [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサード。
1. フィールド名を反復処理し、その値を JSON テキストにシリアライズしてください。
1. JSON コンテンツをターゲット ファイルに書き込む。

```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## JSON抽出ヘルパーを再利用する

メインのJSONエクスポートルーチンに委譲する専用のラッパーメソッドが必要なときは、この例を使用してください。

1. 既存の JSON 抽出ヘルパーを、ソース PDF と出力パスで呼び出してください。
1. シリアライズコードを重複させずに、同じ抽出ロジックを再利用する。

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
