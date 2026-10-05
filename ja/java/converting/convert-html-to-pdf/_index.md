---
title: JavaでHTMLをPDFに変換する
linktitle: HTMLをPDFファイルに変換する
type: docs
weight: 40
url: /ja/java/convert-html-to-pdf/
lastmod: "2026-10-05"
description: Java と Aspose.PDF を使用して HTML、MHTML、Web ページを PDF に変換する方法を学びます。メディア設定、CSS ページルール、フォント埋め込み、SVG コンテンツ、単一ページ出力を含みます。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Java と Aspose.PDF を使用して HTML を PDF に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して HTML および MHTML ファイルを PDF に変換する方法について説明します。基本的な HTML から PDF へのワークフローをカバーし、メディアタイプ、CSS ページルールの優先順位、埋め込みフォント、SVG コンテンツ、単一ページ出力、ライブウェブページからの直接変換によってレンダリングを制御する方法を示します。
---
Aspose.PDF for Java はローカルの HTML ファイル、アーカイブされた MHTML コンテンツ、ライブ Web ページを PDF ドキュメントに変換できます。変換パイプラインは次のものを使用して制御できます `HtmlLoadOptions` そして `MhtLoadOptions` レイアウトのスケーリング、CSSメディアの処理、ページルールの優先度、フォントの埋め込み、リソースの解決、単一ページのレンダリング動作に影響を与えるために。

## HTMLをPDFに変換

ローカルHTMLファイルを直接PDF文書に変換する必要がある場合は、この例を使用してください。

1. 作成する [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) インスタンスは、インポート中にHTMLソースがどのように解釈されるかを構成してください。
1. 設定 [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) へ `ScaleToPageWidth` そのように幅の広いHTMLコンテンツは、切り取られるのではなく、対象のPDFページ幅に合わせてスケーリングされます。
1. 構成されたロードオプションとパスを渡すことで、ソースHTMLファイルを開きます [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. 生成されたものを保存 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 対象出力パスに PDF ファイルとして。

```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## メディアタイプオプションを使用して HTML を PDF に変換する

HTML 変換中に CSS メディアタイプの処理を制御する必要がある場合は、この例を使用してください。

1. 作成する [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 変換設定のインスタンス。
1. 設定 [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) へ `Screen` HTML を画面表示用の CSS ルールでレンダリングすべきで、印刷メディア用ではない場合。
1. 変換中にメディアクエリ依存のスタイルが適用されるよう、設定されたロードオプションでHTMLファイルを開いてください。
1. 結果を保存する [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) PDF ファイルとして。

```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## CSSページルールの優先順位を考慮してHTMLをPDFに変換する

CSS を使用する場合はこの例をご利用ください `@page` ルールは最終的なPDFページレイアウトに影響を与えるべきです。

1. 作成する [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) HTML ファイルを開く前のインスタンス。
1. 設定 `setPriorityCssPageRule(false)` 他のレイアウト設定が CSS より優先されるべき場合 `@page` ソースマークアップ内の宣言。
1. HTML コンテンツを a にロードする [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 構成されたオプションで、インポート中にページレイアウトが解決されるようにしてください。
1. 生成された PDF ファイルを保存してください。

```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## HTML を埋め込みフォントで PDF に変換

出力PDFがHTMLフォントを埋め込んで保持すべき場合は、この例を使用してください。

1. 作成する [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) HTMLインポート構成用のインスタンス。
1. 有効にする `setEmbedFonts(true)` HTMLレンダリング中に解決されたフォントは、出力PDFに保存されます。
1. これらの読み込みオプションを使用して HTML ソースを開くと、最終文書で元のタイポグラフィを利用可能に保つことができます。
1. 保存する [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 埋め込まれたフォントリソースが含まれる PDF として。

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 単一の PDF ページに HTML コンテンツをレンダリング

長いHTMLコンテンツを複数ページにまたがらせず、1ページのPDFに収める必要がある場合は、この例を使用してください。

1. 作成する [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 変換設定のインスタンス。
1. 有効にする `setRenderToSinglePage(true)` そのため、インポートされたHTMLは、複数のページに分割されるのではなく、1つのPDFページにレイアウトされます。
1. 構成された読み込みオプションでソースHTMLを開き、Aspose.PDF にページレイアウトを構築させます。 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 出力 PDF ファイルを保存してください。

```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## インラインSVGを含むHTMLの変換

HTML ソースにインライン SVG データが含まれ、PDF にレンダリングする必要がある場合は、この例を使用してください。

1. 作成する [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) HTML ファイルの親ディレクトリをベースパスとして使用するインスタンスで、変換時に関連リソースを一貫して解決できるようにしてください。
1. インラインSVGマークアップを含むHTMLファイルを、ソースパスとロードオプションを渡して開きます。 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF が HTML DOM と埋め込まれた SVG 要素を PDF ページのコンテンツにレンダリングできるようにします。
1. 生成された PDF ドキュメントを保存してください。

```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## ウェブページをPDFに変換する

ライブのウェブ URL を PDF ドキュメントとしてレンダリングし、保存する場合はこの例を使用してください。

1. 作成する [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) ターゲットURLをインスタンスに指定し、スタイルシートや画像などの相対リソースがそのアドレスに対して解決できるようにしてください。
1. URL文字列を変換する `URL` オブジェクトを取得し、その入力ストリームを開いてライブHTMLコンテンツを取得してください。
1. 作成する [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) レスポンスストリームと構成されたロードオプションから取得し、ダウンロードされたページが正しいベース URL で処理されるようにしてください。
1. レンダリングされたウェブページをPDFファイルとして保存し、try-with-resources を使用してストリームリソースを自動的に閉じます。

```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## MHTML を PDF に変換

アーカイブされた MHTML ファイルを PDF ドキュメントに変換する必要がある場合は、この例を使用してください。

1. 作成する [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) Aspose.PDF にソースを MIME HTML コンテンツとしてロードさせるインスタンス
1. 開く `.mht` または `.mhtml` ファイルをそのパスと MHTML のロードオプションに渡すことで [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF にアーカイブされた HTML コンテンツとその埋め込まれたリソースを PDF ドキュメントモデルに解析させます。
1. 生成された PDF ファイルを保存してください。

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
