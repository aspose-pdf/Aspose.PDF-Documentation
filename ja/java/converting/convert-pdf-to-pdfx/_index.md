---
title: JavaでPDFをPDF/A、PDF/E、PDF/Xに変換する
linktitle: PDFをPDF/A、PDF/E、PDF/Xに変換する
type: docs
weight: 120
url: /ja/java/convert-pdf-to-pdf_x/
lastmod: "2026-10-05"
description: Aspose.PDFを使用して、アーカイブ、エンジニアリング、アクセシビリティ、印刷ワークフロー向けに、PDFファイルをPDF/A、PDF/E、PDF/Xに変換する方法を学びます。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDFをPDF/X形式に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントを PDF/A、PDF/E、PDF/X フォーマットに検証および変換する方法を説明します。ログ生成、PDF/A-3 の添付ファイルの保持、欠落フォントの置換、オートタグ付け、ICC プロファイルの構成、出力インテント設定についてカバーします。
---
Aspose.PDF for Java は、標準 PDF ファイルをアーカイブおよび交換指向の PDF 標準に検証および変換できます。

## PDF を PDF/A に変換

標準 PDF を PDF/A 準拠のアーカイブ文書に変換する必要がある場合に、このサンプルを使用してください。

1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 呼び出し `document.convert(...)` と [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` と [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`。
1. 検証ログをサイドカーXMLファイルに書き込み、変換中にコンプライアンス問題が記録されるようにしてください。
1. 検証済みのPDF/A出力を保存してください。

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## PDF を PDF/E に変換する

PDF をエンジニアリング指向の PDF/E 標準に変換する必要がある場合は、この例を使用してください。

1. 作成 [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 対象 [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` そして、目的のログファイルパス。
1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 呼び出し `document.convert(options)` したがって、コンプライアンス変換は準備されたオプションオブジェクトで実行されます。
1. 生成されたコンプライアンス準拠 PDF ファイルを保存してください。

```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## PDF を PDF/X に変換

PDF を印刷指向の PDF/X 標準に変換すべき場合に、この例を使用します。

1. 作成 [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 対象 [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` そして、目的のログファイルパス。
1. 構成してください。 [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) 例えば `FOGRA39` そのため、印刷対象のカラープロファイルが変換設定に埋め込まれます。
1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス化して呼び出す `document.convert(options)`。
1. 変換された PDF/X 出力を保存してください。

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
