---
title: "Java を使用した AcroForm からのデータ抽出"
linktitle: "AcroForm からのデータ抽出"
type: docs
weight: 50
url: /ja/java/extract-data-from-acroform/
description: "Aspose.PDF を使用すると、PDF ファイルからフォーム フィールドのデータを簡単に抽出できます。AcroForms からデータを抽出し、JSON、XML、または FDF 形式で保存する方法をご紹介します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して AcroForm からデータを抽出する方法
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ファイルから AcroForm データを抽出およびエクスポートする方法を説明します。すべてのフォームフィールドの読み取り、名前でフィールド値を取得、フィールドデータを JSON にエクスポート、およびフォームデータを XML、FDF、XFDF 形式で書き出す方法をカバーしています。"
---

## PDF 文書からフォームフィールドの抽出

`com.aspose.pdf.facades.Form` を使用して、ドキュメントオブジェクトモデル全体を経由せずにフィールド名と値を読み取ります。

1. 元の PDF フォームを [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードで開いてください。これにより、AcroForm フィールドを全文書オブジェクトモデルを走査せずに読み取ることができます。
1. `getFieldNames()` を呼び出して、フォームに存在するすべてのフィールド識別子を取得してください。
1. それらのフィールド名を反復処理し、`getField(fieldName)` を呼び出して各フィールドの値を読み取ってください。
1. 抽出したキーと値のペアから出力文字列を作成し、集約されたフォームデータを表示してください。
1. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを `finally` ブロックで閉じてください。

```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## 名前でフォームフィールドの値の取得

PDF フォームで定義された正確なフィールド名が分かっている場合、その値を直接取得できます。`getField(fieldName)`
フィールド コレクション全体を反復処理せずに

1. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを使用して元の PDF フォームを開いてください。
1. `getField(fieldName)` を呼び出して、要求されたフィールド名を使用し、AcroForm データから現在の値を読み取ってください。
1. 抽出されたフィールド値を印刷してください。
1. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを `finally` ブロックで閉じてください。

```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## PDF 文書からフォームフィールドを JSON に抽出

Form field の値は JSON として抽出し、保存することもできます。これは、PDF フォームデータを消費する必要がある場合に便利です。
JSON と連携するウェブアプリケーション、API、またはその他のシステム

1. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを使用して元の PDF フォームを開いてください。
1. `getFieldNames()` を呼び出して、AcroForm から利用可能なすべてのフィールド識別子を取得してください。
1. それらのフィールドを反復処理し、名前と値をエスケープして、JSON オブジェクト文字列を作成してください。
1. JSON 結果を出力ファイルに書き込んでください。
1. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを `finally` ブロックで閉じてください。

```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
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

## PDF ファイルから XML へのフォームデータのエクスポート

PDF フォームデータを、構造化された XML データを処理するシステムで利用する必要がある場合、XML エクスポートは便利です。

1. まだドキュメントをバインドしていない状態で、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを作成してください。
1. XML ファイル用の出力ストリームを開き、ソース PDF をファサードに `bindPdf(...)` でバインドしてください。
1. `exportXml(stream)` を呼び出して、現在のフォームフィールドデータを XML としてシリアル化してください。
1. エクスポートが完了した後、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを閉じてください。

```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## PDF ファイルから FDF へのデータのエクスポート

FDF（Forms Data Format）は、PDF ドキュメントとは別に AcroForm フィールドデータを交換するためによく使用されます。

1. まだドキュメントをバインドしていない状態で、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを作成してください。
1. FDF ファイル用の出力ストリームを開き、ソース PDF をファサードに `bindPdf(...)` でバインドしてください。
1. 呼び出し `exportFdf(stream)` してください。これにより、フォームフィールドデータが FDF 形式でシリアライズされます。
1. エクスポートが完了した後、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを閉じてください。

```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## PDF ファイルから XFDF へのデータのエクスポート

XFDF は、Forms Data Format の XML ベースの表現であり、XML を使用するシステムとのフォームデータの交換に便利です。

1. まだドキュメントをバインドしていない状態で、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを作成してください。
1. XFDF ファイルの出力ストリームを開き、ソース PDF をファサードに `bindPdf(...)` でバインドしてください。
1. `exportXfdf(stream)` を呼び出して、フォームフィールドデータを XFDF 形式でシリアライズしてください。
1. エクスポートが完了した後、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードを閉じてください。

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
