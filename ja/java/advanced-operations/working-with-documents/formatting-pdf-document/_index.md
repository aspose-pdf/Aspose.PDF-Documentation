---
title: JavaでPDFドキュメントをフォーマットする
linktitle: PDFドキュメントのフォーマット
type: docs
weight: 11
url: /ja/java/formatting-pdf-document/
description: JavaでPDF文書の書式設定、フォントの埋め込み、ビューア設定の制御、表示オプションの調整方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFファイルのドキュメントウィンドウ、フォント、ズーム動作を設定します。
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントをフォーマットする方法を説明します。ドキュメントウィンドウ設定の読み取りと更新、フォントの埋め込み、デフォルトフォントの設定、フォントの一覧表示、埋め込みフォントのサブセット化、初期ズームファクターの制御について扱います。
---
Aspose.PDF for Java のフォーマットには、ビューアの動作、フォントの埋め込み、および表示設定が含まれます。

## ドキュメントウィンドウ設定の取得

この例を使用して、既存の PDF ドキュメントに保存されている現在のビューア設定を検査します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 文書から必要なウィンドウおよび表示プロパティを読み取ります。
1. 現在の設定を検査またはデバッグのために出力します。

```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## ドキュメントウィンドウの設定

この例では、互換性のあるビューアで開かれたときに PDF の表示方法を更新します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要なウィンドウ、レイアウト、ページモードの設定を行います。
1. 更新された PDF を保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## 既存のPDFにフォントを埋め込む

文書が必要なフォントを含んでいるべき場合、他のシステムでの表示をより確実にするためにこのアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 標準フォントの埋め込みを有効にし、各フォントの使用状況を反復処理します [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 非埋め込みのものをマークする [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 埋め込み用オブジェクト。
1. 更新されたドキュメントを保存してください。

```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 新しいPDFを作成する際にフォントを埋め込む

この例は新しい PDF を作成し、最初からテキストコンテンツに埋め込みフォントを割り当てます。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 必要なものを作成する [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/)、そして [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/)。
1. ターゲットを解決する [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) リポジトリから取得し、埋め込みとしてマークします。
1. テキストコンテンツをページに追加し、出力ドキュメントを保存してください。

```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## PDF出力のデフォルトフォントの設定

出力生成時に、保存されたドキュメントが特定のフォントにフォールバックする必要がある場合は、このパターンを使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成 [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) そして、デフォルトのフォント名を設定してください。
1. 設定された保存オプションでドキュメントを保存してください。

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## PDFで使用されているすべてのフォントの取得

この例は、ドキュメントで検出されたすべてのフォントを一覧表示し、エクスポートまたはファイルの更新を行う前にフォント使用状況を監査できるようにします。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントフォントユーティリティで返されるフォントを列挙します。
1. 検出された各項目の名前を出力します [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## フォントをサブセット化して埋め込みを改善する

ドキュメントの使用に合わせて埋め込みフォントデータを調整しながら、フォントのペイロードを削減したい場合にこのアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要なものとともに、ドキュメント フォント ユーティリティでフォントサブセットを実行する [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) 値。
1. 最適化された文書を保存してください。

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## ドキュメントを開くときのズーム倍率の設定

この例では、PDFを開くときに適用されるべき初期ズームレベルを設定します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成 [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) と [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/)。
1. アクションを文書のオープン アクションとして割り当て、結果を保存してください。

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## ドキュメントのオープン時ズーム率の取得

この例を使用して、PDF がすでにオープンアクションのために明示的なズームレベルを定義しているかどうかを確認してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. open actionがaかどうか確認してください [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) と [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/)。
1. 設定されたズーム値を出力するか、ズームが設定されていないことを報告します。

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
