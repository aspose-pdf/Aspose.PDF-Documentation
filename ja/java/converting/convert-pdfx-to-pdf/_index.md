---
title: "Java での PDF/A および PDF/UA の PDF への変換"
linktitle: "PDF/A および PDF/UA の PDF への変換"
type: docs
weight: 120
url: /ja/java/convert-pdf_x-to-pdf/
lastmod: "2026-10-06"
description: "Java で標準準拠の PDF ファイルから PDF/A および PDF/UA の準拠性を削除し、標準的な PDF ドキュメントとして保存する方法を学びます。"
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: "Java で PDF/A および PDF/UA を標準 PDF に変換する方法"
Abstract: "この記事では、Aspose.PDF for Java を使用して標準準拠の PDF ドキュメントから PDF/A および PDF/UA の準拠性を削除し、結果を標準的な PDF ファイルとして保存する方法を説明します。"
---
Aspose.PDF for Java は、標準準拠の PDF バリアントを通常の PDF ドキュメントに変換できます。

## PDF/A の標準 PDF への変換

アーカイブ用 PDF/A 文書を標準 PDF にダウングレードする必要がある場合にこの例を使用します。

1. ソース PDF/A ファイルを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスに開いてください。
1. `removePdfaCompliance()` を呼び出して、ロードされたドキュメントからアーカイブコンプライアンスプロファイルを解除してください。
1. PDF/A の制限が設定されていない、結果として得られる標準 PDF ファイルを保存してください。

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## PDF/UA の標準 PDF への変換

アクセシブルな PDF/UA ドキュメントを標準 PDF に戻す必要がある場合は、この例を使用してください。

1. ソースの PDF/UA ファイルを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. `removePdfUaCompliance()` を呼び出して、ドキュメントのメタデータおよび構造要件からアクセシビリティコンプライアンスプロファイルを削除してください。
1. 結果の PDF ドキュメントを通常の PDF ファイルとして保存してください。

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
