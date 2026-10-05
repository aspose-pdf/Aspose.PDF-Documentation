---
title: JavaでPDF/AとPDF/UAをPDFに変換する
linktitle: PDF/AとPDF/UAをPDFに変換する
type: docs
weight: 120
url: /ja/java/convert-pdf_x-to-pdf/
lastmod: "2026-10-05"
description: Javaで標準に準拠したPDFファイルからPDF/AおよびPDF/UAの準拠性を削除し、標準的なPDFドキュメントとして保存する方法を学びます。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: JavaでPDF/AとPDF/UAを標準PDFに変換する方法
Abstract: この記事では、Aspose.PDF for Javaを使用して標準に準拠したPDFドキュメントからPDF/AおよびPDF/UAの準拠性を削除し、結果を標準的なPDFファイルとして保存する方法を説明します。
---
Aspose.PDF for Javaは、標準準拠のPDFバリアントを通常のPDFドキュメントに変換できます。

## PDF/A を標準 PDF に変換する

アーカイブ用 PDF/A 文書を標準 PDF にダウングレードする必要がある場合にこの例を使用します。

1. ソース PDF/A ファイルを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 呼び出す `removePdfaCompliance()` ロードされたドキュメントからアーカイブコンプライアンスプロファイルをデタッチしてください。
1. PDF/A の制限が設定されていない、結果として得られる標準 PDF ファイルを保存してください。

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## PDF/UA を標準 PDF に変換する

アクセシブルな PDF/UA ドキュメントを標準 PDF に戻す必要がある場合は、この例を使用してください。

1. ソースの PDF/UA ファイルを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 呼び出す `removePdfUaCompliance()` 文書のメタデータと構造要件からアクセシビリティコンプライアンスプロファイルを削除してください。
1. 結果の PDF ドキュメントを通常の PDF ファイルとして保存してください。

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
