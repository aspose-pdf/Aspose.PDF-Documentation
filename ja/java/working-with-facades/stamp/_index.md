---
title: Stamp クラス
linktitle: Stamp クラス
type: docs
weight: 150
url: /ja/java/stamp-class/
description: "Java で Stamp クラスを使用して、画像、PDF、テキストベースのスタンプを PDF ドキュメントに追加する方法を学習してください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での画像、PDF、テキストスタンプの PDF ドキュメントへの追加"
Abstract: "このセクションでは、Aspose.PDF for Java の Stamp クラスと PdfFileStamp を組み合わせて、PDF ドキュメントに再利用可能なスタンプ コンテンツを追加する方法を説明します。現在の Java のサンプルでは、画像スタンプ、PDF ページスタンプ、カスタム TextState を使用したテキストスタンプ、ページ固有のスタンプ、および不透明度・サイズ・回転設定を備えた背景画像スタンプをカバーしています。"
---
Java の `StampExamples` クラスは、Facades API を通じて利用可能な主要なスタンプ構築ワークフローを示します。

## 画像スタンプの追加

画像ファイルを PDF にスタンプとして配置する必要がある場合は、このワークフローを使用してください。

### 手順

1. `PdfFileStamp` のインスタンスを作成し、ソース PDF にバインドしてください。
2. `Stamp` オブジェクトを作成し、画像ファイルにバインドしてください。
3. スタンプの識別子と配置原点を設定してください。
4. スタンプをドキュメントに追加してください。
5. 結果を保存し、facade オブジェクトを閉じてください。

### Java の例

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## PDF ページをスタンプとして追加

別の PDF ページからのコンテンツをスタンプの内容として再利用する場合は、このワークフローを使用してください。

### 手順

1. `PdfFileStamp` のインスタンスを作成し、対象の PDF にバインドしてください。
2. `Stamp` オブジェクトを作成してください。
3. スタンプを別の PDF ファイルの特定のページにバインドしてください。
4. 配置対象のページ番号と原点を設定してください。
5. スタンプを追加し、出力を保存し、facade オブジェクトを閉じてください。

### Java の例

```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## TextState を使用したテキストスタンプの追加

スタンプに画像ではなく装飾テキストを含める場合は、このワークフローを使用してください。

### 手順

1. `PdfFileStamp` のインスタンスを作成し、ソース PDF にバインドしてください。
2. `Stamp` オブジェクトを作成してください。
3. バインドする `FormattedText` ロゴとカスタム `TextState` をスタンプに設定してください。
4. スタンプの原点と回転を設定してください。
5. スタンプを追加し、出力を保存し、facade オブジェクトを閉じてください。

### Java の例

```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 特定のページへのスタンプの追加

スタンプをドキュメント全体ではなく選択したページのみに表示したい場合は、このワークフローを使用してください。

### 手順

1. `PdfFileStamp` のインスタンスを作成し、ソース PDF にバインドしてください。
2. `Stamp` オブジェクトを作成し、画像ファイルにバインドしてください。
3. 対象ページリスト、原点、画像サイズを設定してください。
4. スタンプをドキュメントに追加してください。
5. 結果を保存し、facade オブジェクトを閉じてください。

### Java の例

```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 背景画像スタンプの追加

スタンプをページコンテンツの背面に表示し、透明度と回転を制御する場合は、このワークフローを使用してください。

### 手順

1. `PdfFileStamp` のインスタンスを作成し、ソース PDF にバインドしてください。
2. `Stamp` オブジェクトを作成し、画像ファイルにバインドしてください。
3. スタンプを背景コンテンツとしてマークしてください。
4. 透明度、品質、回転、サイズ、および原点を設定してください。
5. スタンプを追加し、出力を保存し、facade オブジェクトを閉じてください。

### Java の例

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
