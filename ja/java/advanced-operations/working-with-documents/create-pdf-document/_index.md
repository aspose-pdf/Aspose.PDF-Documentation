---
title: "Java での PDFファイルの作成"
linktitle: "PDFドキュメントの作成"
type: docs
weight: 10
url: /ja/java/create-pdf-document/
description: Aspose.PDF を使用して Java で PDF ファイルの作成方法と検索可能な PDF の構築方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ファイルと検索可能な PDF ドキュメントを作成します。
Abstract: この記事では、Aspose.PDF for Java を使用して PDF 文書を作成する方法を示します。新規に PDF をスクラッチで作成する方法と、外部 OCR エンジンからの HOCR 出力を提供して画像ベースの文書を検索可能な PDF に変換する方法をカバーします。
---
Aspose.PDF for Java は、シンプルなドキュメント作成と OCR を利用した検索可能な PDF ワークフローの両方をサポートしています。

## 新しい PDF ドキュメントの作成

シンプルなPDFファイルを最初から生成する必要がある場合は、このアプローチを使用してください。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を作成し、ページに追加してください。
1. 出力PDFを保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## 検索可能なPDFの作成

その `createSearchablePdf` 使用例 `Document.convert(...)` と `CallBackGetHocr` 実装。コールバックはソース画像を一時ファイルに書き込み、Tesseract を使用して `hocr` オプションは、生成されたHOCRマークアップを読み取り、Aspose.PDFに返します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成する `CallBackGetHocr` コールバックして、ソースドキュメントを検索可能な PDF コンテンツに変換してください。
1. 更新されたPDFを保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## ドキュメントウィンドウ設定の取得

この例を使用して、既存の PDF ドキュメントに保存されている現在のビューア設定を確認します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントから必要なウィンドウと表示プロパティを読み取ります。
1. 検査やデバッグのために、現在の設定を出力します。

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

## 文書ウィンドウの設定

この例は、PDFが互換性のあるビューアで開かれたときの表示方法を更新します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要なウィンドウ、レイアウト、およびページモードの設定を行います。
1. 更新されたPDFを保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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

ドキュメントが必要なフォントを保持し、他のシステムでのレンダリングをより確実にする必要がある場合に、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 標準フォントの埋め込みを有効にし、各で使用されているフォントを反復処理します。 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
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

## 新しいPDFを作成するときにフォントを埋め込む

この例では、新しい PDF を作成し、最初からテキスト コンテンツに埋め込みフォントを割り当てます。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 必要なものを作成する [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/)、そして [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/)。
1. 対象を解決する [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) リポジトリから取得し、埋め込みとしてマークする。
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

## PDF 出力のデフォルトフォントの設定

保存されたドキュメントが出力生成時に特定のフォントにフォールバックすべき場合にこのパターンを使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成 [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) そしてデフォルトのフォント名を設定してください。
1. 設定された保存オプションを使用してドキュメントを保存してください。

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

この例では、ドキュメントで検出されたすべてのフォントを一覧表示し、エクスポートまたはファイルの更新を行う前にフォント使用状況を監査できるようにします。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 文書フォントユーティリティが返すフォントを列挙します。
1. 検出された各項目の名前を出力 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

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

埋め込みフォントデータを文書の使用状況に合わせながら、フォントのペイロードを削減したい場合にこのアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要なフォントサブセット処理をドキュメントフォントユーティリティで実行する [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) 値。
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

## 文書のオープン時ズーム倍率の設定

この例では、PDF が開かれたときに適用されるべき初期ズームレベルを設定します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成する [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) と [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/)。
1. アクションをドキュメントのオープンアクションとして割り当て、結果を保存してください。

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## ドキュメントを開く際のズーム倍率の取得

この例を使用して、PDFが開く際のアクションで明示的なズームレベルをすでに定義しているかどうかを確認してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 開くアクションが a かどうか確認してください [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) と [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/)。
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
