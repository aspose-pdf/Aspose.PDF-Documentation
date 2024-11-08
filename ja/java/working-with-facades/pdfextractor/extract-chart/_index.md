---
title: PDFドキュメントからチャートオブジェクトを抽出する（ファサード）
type: docs
weight: 20
url: /ja/java/extract-chart-objects/
description: このセクションでは、PdfExtractorクラスを使用してAspose.PDF FacadesでPDFからチャートオブジェクトを抽出する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントからチャートオブジェクトを抽出する（ファサード）

PDFは、ページの内容を**マーク付きコンテンツ**という名前の要素にグループ化することを可能にします。Adobe Acrobatはそれらを「コンテナ」として表示します。チャートオブジェクトはそのようなオブジェクトに配置されています。これらのオブジェクトを抽出するために、PdfExtractorクラスに新しいメソッドextractMarkedContentAsImages()を導入しました。このメソッドは、すべての**マーク付きコンテンツ**を個別の画像にレンダリングします。すべてのチャートが1つのコンテナに完全に配置されているわけではないことに注意してください。このため、一部のチャートは部分ごとに別々の画像として保存されます。

コンテナへの内容の正しいグループ化は、PDFドキュメントデザイナーの責任であることに注意してください。
 If you want to get charts with header or other objects you should either edit/create the PDF document where whole chart is placed in one container.

チャートをヘッダーや他のオブジェクトと一緒に取得したい場合は、チャート全体が1つのコンテナに配置されているPDFドキュメントを編集/作成する必要があります。

```java

 // ドキュメントを開く

Document document = new Document("sample.pdf");

// PdfExtractorをインスタンス化

PdfExtractor pdfExtractor = new PdfExtractor();

// チャートオブジェクトを画像としてフォルダに抽出

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```