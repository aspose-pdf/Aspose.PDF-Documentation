---
title: "Java での PDF ドキュメントのフォーマット"
linktitle: "PDF ドキュメントのフォーマット"
type: docs
weight: 11
url: /ja/java/formatting-pdf-document/
description: "Java で PDF 文書の書式設定、フォントの埋め込み、ビューア設定の制御、表示オプションの調整方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ドキュメントのウィンドウ、フォント、ズーム動作の設定"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントをフォーマットする方法を説明します。ドキュメントウィンドウ設定の読み取りと更新、フォントの埋め込み、デフォルトフォントの設定、フォントの一覧表示、埋め込みフォントのサブセット化、初期ズームファクターの制御について扱います。
---
Aspose.PDF for Java のフォーマットには、ビューアの動作、フォントの埋め込み、および表示設定が含まれます。

## ドキュメントウィンドウ設定の取得

この例を使用して、既存の PDF ドキュメントに保存されている現在のビューア設定を検査してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントから必要なウィンドウおよび表示プロパティを読み取ってください。
1. 現在の設定を検査またはデバッグのために出力してください。

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
1. 必要なウィンドウ、レイアウト、ページモードの設定を行ってください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

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

## 既存の PDF にフォントを埋め込む

ドキュメントに必要なフォントを含める必要がある場合は、他のシステムでの表示をより確実にするためにこの方法を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 標準フォントの埋め込みを有効にして、各 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) で使用されているフォントを順に処理してください。
1. 埋め込み対象として、非埋め込みの [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) オブジェクトをマークしてください。
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

## 新しい PDF を作成する際にフォントを埋め込む

この例では、新しい PDF を作成し、テキスト コンテンツに対して最初から埋め込みフォントを割り当てます。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. 必要な [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)、[TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/)、および [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) を作成してください。
1. ターゲットの [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) をリポジトリから解決し、埋め込みとしてマークしてください。
1. テキスト コンテンツをページに追加し、出力ドキュメントを保存してください。

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

## PDF 出力のデフォルトフォントの設定

出力生成時に、保存されたドキュメントが特定のフォントにフォールバックする必要がある場合は、この方法を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) を作成し、デフォルトのフォント名を設定してください。
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

## PDF で使用されているすべてのフォントの取得

この例では、ドキュメントで検出されたすべてのフォントを一覧表示し、エクスポートまたはファイルの更新を行う前にフォントの使用状況を監査できるようにします。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントフォントユーティリティで返されるフォントを列挙してください。
1. 検出された各 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) の名前を出力してください。

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## フォントをサブセット化して埋め込みの改善

ドキュメントの使用に合わせて埋め込みフォントデータを調整しながら、フォントのペイロードを削減したい場合にこのアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要な [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) 値とともに、ドキュメントフォントユーティリティでフォントサブセットを実行してください。
1. 最適化されたドキュメントを保存してください。

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

この例では、PDF を開くときに適用される初期ズームレベルを設定します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) と [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/) を作成してください。
1. アクションをドキュメントのオープン時アクションとして割り当てて、結果を保存してください。

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

この例を使用して、PDF がすでにオープン時アクションに対して明示的なズーム率を定義しているかどうかを確認してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. オープン時アクションが [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) かつ [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/) を持っているかどうかを確認してください。
1. 設定されたズーム値を出力するか、ズームが設定されていないことを報告してください。

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
