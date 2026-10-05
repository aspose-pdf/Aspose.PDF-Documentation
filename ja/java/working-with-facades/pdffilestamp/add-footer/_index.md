---
title: "PDFにフッターの追加"
linktitle: "PDFにフッターの追加"
type: docs
weight: 10
url: /ja/java/add-footer/
description: PdfFileStamp ファサードを使用して、Javaで PDF ページにテキストと画像のフッターを追加する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで PDF にテキストと画像のフッターを追加
Abstract: Aspose.PDF for Java と PdfFileStamp ファサードを使用して PDF ドキュメントにフッター コンテンツを追加する方法を学びます。Java のサンプルでは、プレーンテキストのフッター、ストリームから読み込む画像フッター、左・右・下の余白を明示したテキストフッターがカバーされています。
---
## PDFにフッターの追加

使用 `PdfFileStamp` 文書の各ページに繰り返しフッター内容が必要な場合。

### 手順

1. 作成 `PdfFileStamp` インスタンス化してソースPDFにバインドしてください。
2. フッターコンテンツを次のいずれかとして構築する `FormattedText` または画像ストリーム。
3. 適切なものを呼び出す `addFooter` オーバーロード。
4. 更新されたファイルを保存し、ファサードオブジェクトを閉じます。

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
