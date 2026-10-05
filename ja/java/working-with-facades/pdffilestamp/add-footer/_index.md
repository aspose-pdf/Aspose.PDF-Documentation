---
title: "PDF へのフッターの追加"
linktitle: "PDF へのフッターの追加"
type: docs
weight: 10
url: /ja/java/add-footer/
description: "PdfFileStamp ファサードを使用して、Java で PDF ページにテキストと画像のフッターを追加する方法を学びます。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF へのテキストと画像のフッターの追加"
Abstract: "Aspose.PDF for Java と PdfFileStamp ファサードを使用して、PDF ドキュメントにフッター コンテンツを追加する方法を学びます。Java のサンプルでは、プレーンテキストのフッター、ストリームから読み込む画像フッター、左・右・下の余白を明示したテキストフッターがカバーされています。"
---
## PDF へのフッターの追加

`PdfFileStamp` を使用すると、ドキュメントの各ページに繰り返しフッター コンテンツを追加できます。

### 手順

1. `PdfFileStamp` インスタンスを作成し、ソース PDF にバインドしてください。
2. フッターコンテンツを `FormattedText` または画像ストリームとして構築してください。
3. 適切な `addFooter` オーバーロードを呼び出してください。
4. 更新されたファイルを保存し、ファサードオブジェクトを閉じてください。

### Java の例

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
