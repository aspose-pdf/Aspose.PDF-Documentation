---
title: "Java を使用した AcroForm からデータの抽出"
linktitle: "AcroForm からデータの抽出"
type: docs
weight: 50
url: /ja/java/extract-data-from-acroform/
description: Aspose.PDF は、PDF ファイルからフォーム フィールド データを抽出することを簡単にします。AcroForms からデータを抽出し、JSON、XML、または FDF 形式で保存する方法をご紹介します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して AcroForm からデータを抽出する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルから AcroForm データを抽出およびエクスポートする方法を説明します。すべてのフォームフィールドの読み取り、名前でフィールド値を取得、フィールドデータを JSON にエクスポート、そしてフォームデータを XML、FDF、XFDF 形式で書き出すことをカバーしています。
---

## PDF文書からフォームフィールドの抽出

使用 `com.aspose.pdf.facades.Form` ドキュメントオブジェクトモデル全体を経由せずに、フィールド名と値を読み取る。

1. 次の方法で元の PDF フォームを開く [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade により、AcroForm フィールドを全文書オブジェクトモデルを走査せずに読み取ることができます。
1. 呼び出し `getFieldNames()` フォームに存在するすべてのフィールド識別子を収集してください。
1. それらのフィールド名を反復処理し、呼び出す `getField(fieldName)` 各フィールドの値を読むために。
1. 抽出したキーと値のペアから出力文字列を作成し、集約されたフォームデータを表示してください。
1. 閉じる [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードの `finally` ブロック。

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

PDF フォームで定義された正確なフィールド名が分かっている場合、その値を直接取得できます。 `getField(fieldName)`
フィールド コレクション全体を反復処理せずに

1. 次の方法で元の PDF フォームを開く [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサード。
1. 呼び出し `getField(fieldName)` 要求されたフィールド名を使用して、AcroForm データから現在の値を読み取ります。
1. 抽出されたフィールド値を印刷してください。
1. 閉じる [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードの `finally` ブロック。

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

## PDF文書からフォームフィールドをJSONに抽出する

Form field の値は JSON として抽出し、保存することもできます。これは、PDF フォームデータを消費する必要がある場合に便利です。
JSON と連携するウェブアプリケーション、API、またはその他のシステム。

1. 次の方法で元の PDF フォームを開く [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサード。
1. 呼び出し `getFieldNames()` AcroForm から利用可能なすべてのフィールド識別子を収集してください。
1. それらのフィールドを反復処理し、名前と値をエスケープして、JSON オブジェクト文字列を作成してください。
1. JSON結果を出力ファイルに書き込んでください。
1. 閉じる [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) ファサードの `finally` ブロック。

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

## PDF ファイルから XML へフォームデータのエクスポート

PDF フォーム データを構造化された XML データで動作するシステムで利用する必要がある場合、XML エクスポートは便利です。

1. 作成 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) まだドキュメントをバインドしていないファサード。
1. XML ファイル用の出力ストリームを開き、ソース PDF をファサードにバインドします `bindPdf(...)`。
1. 呼び出し `exportXml(stream)` そのため、現在のフォームフィールドデータは XML としてシリアル化されます。
1. 閉じる [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) エクスポートが完了した後のファサード。

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

## PDFファイルからFDFへデータのエクスポート

FDF（Forms Data Format）は、PDFドキュメントとは別にAcroFormフィールドデータを交換するためによく使用されます。

1. 作成 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) まだドキュメントをバインドしていないファサード。
1. FDF ファイルの出力ストリームを開き、ソース PDF をファサードにバインドします `bindPdf(...)`。
1. 呼び出し `exportFdf(stream)` したがって、フォームフィールドデータはFDF形式でシリアライズされます。
1. 閉じる [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) エクスポートが完了した後のファサード。

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

## PDF ファイルから XFDF へデータのエクスポート

XFDF は、Forms Data Format の XML ベースの表現であり、XML で動作するシステムとのフォームデータの交換に便利です。

1. 作成 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) まだドキュメントをバインドしていないファサード。
1. XFDF ファイルの出力ストリームを開き、ソース PDF をファサードにバインドします `bindPdf(...)`。
1. 呼び出し `exportXfdf(stream)` したがって、フォームフィールドデータはXFDF形式でシリアライズされます。
1. 閉じる [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) エクスポートが完了した後のファサード。

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
