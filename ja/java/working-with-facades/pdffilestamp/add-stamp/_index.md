---
title: "PDF にスタンプの追加"
linktitle: "PDF にスタンプの追加"
type: docs
weight: 40
url: /ja/java/add-stamp/
description: PdfFileStamp ファサードを使用して、Java で PDF ページに画像スタンプを追加する方法を学びます。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF に画像スタンプを追加
Abstract: "PdfFileStamp ファサードを使用して Aspose.PDF for Java で PDF 文書にスタンプ コンテンツを追加する方法を学びます。現在の Java のサンプルセットでは、`Stamp` オブジェクトを作成し、画像ファイルにバインドし、文書に追加して、スタンプされた PDF を保存する方法が示されています。"
---
## PDF にスタンプの追加

画像ベースのスタンプを PDF に適用する必要がある場合は、このワークフローを使用してください。

### 手順

1. `PdfFileStamp` のインスタンスを作成して、ソース PDF にバインドしてください。
2. `Stamp` オブジェクトを作成してください。
3. `bindImage` を使用して、スタンプを画像ファイルにバインドしてください。
4. `addStamp` を使用して、スタンプを文書に追加してください。
5. 出力を保存し、ファサードオブジェクトを閉じてください。

### Java の例

```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

現在の `PdfFileStampExamples.java` クラスには、テキストのみのスタンプ、回転、または不透明度設定に関する個別の Java サンプルが含まれていません。
