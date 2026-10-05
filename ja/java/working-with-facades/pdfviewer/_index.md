---
title: PdfViewer クラス
linktitle: PdfViewer クラス
type: docs
weight: 135
url: /ja/java/pdfviewer-class/
description: Java で PdfViewer ファサードを使用して PDF ページをデコードし、ビューア関連の設定を検査する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PdfViewer を使用して Java で PDF ページをデコードし、ビューア データを検査します。
Abstract: このセクションでは、Aspose.PDF for Java の PdfViewer ファサードを使用してページのデコードおよびビューア関連の検査タスクを実行する方法を説明します。現在の Java のサンプルでは、すべてのページを画像にレンダリングすること、特定のページをデコードすること、ページ数、座標タイプ、解像度、バウンドビューア設定を検査することがカバーされています。
---
Java `PdfViewerExamples` クラスは Facades API を通じて利用可能な主要なビューア ワークフローを示します。

## すべての PDF ページをデコード

ソース PDF のすべてのページを画像としてレンダリングする必要がある場合に、このワークフローを使用します。

### 手順

1. 作成して構成する `PdfViewer` インスタンス。
2. ソース PDF をバインドする `bindPdf`。
3. 呼び出す `decodeAllPages()` ドキュメントを...にレンダリングする `BufferedImage` 配列。
4. デコードされた各ページを出力画像ファイルに保存してください。
5. バインドされた PDF ファイルを閉じます。

### Java の例

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## 特定の PDF ページをデコードする

ページが1つだけ画像にレンダリングする必要がある場合は、このワークフローを使用してください。

### 手順

1. 作成して構成する `PdfViewer` インスタンス。
2. ソース PDF をバインドしてください。
3. 呼び出す `decodePage()` レンダリングしたいページ用に。
4. デコードされたページを出力画像ファイルに保存してください。
5. ビューアを閉じます。

### Java の例

```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## PDF メタデータの検査

レンダリングまたは印刷の前にビューア関連のドキュメント情報が必要な場合は、このワークフローを使用してください。

### 手順

1. 作成して構成する `PdfViewer` インスタンス。
2. ソース PDF をバインドしてください。
3. ページ数、座標タイプ、レンダリング解像度を読み取ります。
4. 取得した値を使用するか、印刷してください。
5. バインドされた PDF ファイルを閉じます。

### Java の例

```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## バインドされたビューア設定を確認する

PDF をバインドした後にビューアの動作を確認または調整する必要がある場合にこのワークフローを使用します。

### 手順

1. 作成して構成する `PdfViewer` インスタンス。
2. ソース PDF をバインドしてください。
3. 自動リサイズ、自動回転、印刷ダイアログの表示などのビューアオプションを設定してください。
4. アクティブなビューア設定とページ数を読み取ります。
5. ビューアを閉じます。

### Java の例

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```
