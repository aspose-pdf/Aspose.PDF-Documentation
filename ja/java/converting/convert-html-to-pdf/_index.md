---
title: "Java での HTML から PDF への変換"
linktitle: "HTML から PDF ファイルへの変換"
type: docs
weight: 40
url: /ja/java/convert-html-to-pdf/
lastmod: "2026-10-06"
description: Java と Aspose.PDF を使用して HTML、MHTML、Web ページを PDF に変換する方法を学びます。メディア設定、CSS ページルール、フォント埋め込み、SVG コンテンツ、単一ページ出力を含みます。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: "Java と Aspose.PDF を使用した HTML から PDF への変換方法"
Abstract: この記事では、Aspose.PDF for Java を使用して HTML および MHTML ファイルを PDF に変換する方法について説明します。基本的な HTML から PDF へのワークフローをカバーし、メディアタイプ、CSS ページルールの優先順位、埋め込みフォント、SVG コンテンツ、単一ページ出力、ライブウェブページからの直接変換によってレンダリングを制御する方法を示します。
---
Aspose.PDF for Java は、ローカルの HTML ファイル、アーカイブされた MHTML コンテンツ、ライブ Web ページを PDF ドキュメントに変換できます。変換パイプラインは、`HtmlLoadOptions` および `MhtLoadOptions` を使用して制御でき、レイアウトのスケーリング、CSS メディアの処理、ページルールの優先度、フォントの埋め込み、リソースの解決、単一ページのレンダリング動作に影響を与えます。

## HTML から PDF への変換

ローカルの HTML ファイルを直接 PDF 文書に変換する必要がある場合は、この例を使用してください。

1. [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) インスタンスを作成し、インポート中に HTML ソースがどのように解釈されるかを構成してください。
1. [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) を `ScaleToPageWidth` に設定し、幅の広い HTML コンテンツが切り取られるのではなく、対象の PDF ページ幅に合わせてスケーリングされるようにしてください。
1. 構成したロードオプションとパスを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、ソース HTML ファイルを開いてください。
1. 生成された [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を、対象の出力パスに PDF ファイルとして保存してください。

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

## メディアタイプオプションを使用した HTML から PDF への変換

HTML 変換中に CSS メディアタイプの処理を制御する必要がある場合は、この例を使用してください。

1. [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) インスタンスを作成し、変換設定を行ってください。
1. [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) を `Screen` に設定し、HTML を画面表示用の CSS ルールでレンダリングするようにしてください。
1. 変換中にメディアクエリ依存のスタイルが適用されるよう、設定されたロードオプションで HTML ファイルを開いてください。
1. 結果を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) として PDF ファイルに保存してください。

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

## CSS ページルールの優先順位を考慮して HTML の PDF への変換

CSS の `@page` ルールが最終的な PDF ページレイアウトに影響を与える必要がある場合は、この例をご利用ください。

1. HTML ファイルを開く前に、[`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) インスタンスを作成してください。
1. その他のレイアウト設定を CSS の `@page` 宣言より優先させる場合は、`setPriorityCssPageRule(false)` を設定してください。
1. 構成されたオプションを使用して、HTML コンテンツを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にロードし、インポート中にページレイアウトが解決されるようにしてください。
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

## HTML の埋め込みフォントで PDF への変換

出力 PDF に HTML フォントを埋め込んで保持する必要がある場合は、この例を使用してください。

1. HTML インポート構成用に [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) インスタンスを作成してください。
1. `setEmbedFonts(true)` を有効にしてください。これにより、HTML のレンダリング中に解決されたフォントが、出力 PDF に保存されます。
1. これらの読み込みオプションを使用して HTML ソースを開いてください。これにより、最終文書で元のタイポグラフィを利用可能に保つことができます。
1. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を、埋め込まれたフォントリソースを含む PDF として保存してください。

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

## 単一の PDF ページへの HTML コンテンツのレンダリング

長い HTML コンテンツを複数ページにまたがらず、1 ページの PDF に収める必要がある場合は、この例を使用してください。

1. [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) インスタンスを作成し、変換設定を行ってください。
1. `setRenderToSinglePage(true)` を有効にしてください。これにより、インポートされた HTML が複数のページに分割されるのではなく、1 つの PDF ページにレイアウトされます。
1. 構成された読み込みオプションでソース HTML を開き、Aspose.PDF に [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 内でページレイアウトを構築させてください。
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

## インライン SVG を含む HTML の変換

HTML ソースにインライン SVG データが含まれ、PDF にレンダリングする必要がある場合は、この例を使用してください。

1. 変換時に関連リソースを一貫して解決できるように、HTML ファイルの親ディレクトリをベースパスとして指定した [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) インスタンスを作成してください。
1. インライン SVG マークアップを含む HTML ファイルを、ソースパスとロードオプションを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタに渡して開いてください。
1. Aspose.PDF が HTML DOM と埋め込まれた SVG 要素を PDF ページのコンテンツにレンダリングできるようにしてください。
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

## ウェブページの PDF への変換

ライブのウェブ URL を PDF ドキュメントとしてレンダリングし、保存する場合はこの例を使用してください。

1. スタイルシートや画像などの相対リソースを対象 URL に対して解決できるように、その URL を指定した [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) インスタンスを作成してください。
1. URL 文字列を `URL` オブジェクトに変換し、その入力ストリームを開いてライブ HTML コンテンツを取得してください。
1. ダウンロードしたページを正しいベース URL で処理できるように、レスポンスストリームと設定済みの読み込みオプションから [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. レンダリングされたウェブページを PDF ファイルとして保存し、try-with-resources を使用してストリームリソースを自動的に閉じてください。

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

1. [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) のインスタンスを作成し、Aspose.PDF にソースを MIME HTML コンテンツとしてロードさせるように指定してください。
1. `.mht` または `.mhtml` ファイルのパスと MHTML のロードオプションを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、ファイルを開いてください。
1. Aspose.PDF にアーカイブされた HTML コンテンツとその埋め込まれたリソースを PDF ドキュメントモデルに解析させてください。
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
