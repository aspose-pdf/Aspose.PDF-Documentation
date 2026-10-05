---
title: Javaで他のファイル形式をPDFに変換する
linktitle: 他のファイル形式をPDFに変換する
type: docs
weight: 80
url: /ja/java/convert-other-files-to-pdf/
lastmod: "2026-10-05"
description: Aspose.PDF を使用して Java で EPUB、Markdown、PCL、XPS、PostScript、XML、XSL-FO、OFD、TeX ファイルを PDF に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java で他のファイル形式を PDF に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して複数のソースファイル形式を PDF に変換する方法を説明します。EPUB、Markdown、OFD、PCL、PostScript、EPS、TeX、テキスト、XML、XPS、および XSL-FO の変換ワークフローを、フォーマット固有のロードオプションと、必要に応じた前処理手順を使用して網羅しています。
---
Aspose.PDF for Java は、ドキュメント、マークアップ、およびページ記述フォーマットから PDF への変換をサポートしています。

## OFD を PDF に変換

OFD ドキュメントを PDF に変換する必要がある場合は、この例を使用してください。

1. ファイルパスを渡してOFDソースを開く [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) へ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF に OFD パッケージを PDF ドキュメントモデルに解析させる。
1. 結果のPDFをターゲット出力パスに保存してください。

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## TeXをPDFに変換する

TeX コンテンツを直接 PDF としてレンダリングすべき場合は、この例を使用してください。

1. ファイルパスを渡して TeX ソースを開く [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) へ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF に TeX マークアップを解釈させ、ロード中に PDF レイアウトを構築させましょう。
1. 生成されたPDFを保存してください。

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PostScript を PDF に変換する

PostScript ファイルを PDF ドキュメントに変換する必要がある場合は、この例を使用してください。

1. PostScript ソースを開くには [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) の中で [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF に PostScript ページ記述ストリームを PDF ドキュメントモデルに変換させます。
1. 変換された PDF ファイルを保存してください。

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## EPS を PDF に変換

Encapsulated PostScript ファイルを PDF に変換する必要がある場合は、この例を使用してください。

1. EPS ソースを開くには [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) EPSは同じPostScriptベースのロードパスに従うためです。
1. ファイルをロードする [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) そのため、ページ記述のコンテンツはインポート時に変換されます。
1. 出力 PDF を保存してください。

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## EPUB を PDF に変換

EPUB eブックをPDFに変換する必要がある場合は、この例を使用してください。

1. ファイルパスを渡してEPUBソースを開く [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) へ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF に ebook の構造をロードさせ、PDF ページに変換させます。
1. 変換されたPDFを保存してください。

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Markdown を PDF に変換する

Markdown コンテンツをレンダリングして PDF として保存する場合は、この例を使用してください。

1. ファイルパスを渡してMarkdownソースを開く [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) へ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF が Markdown コンテンツを解釈し、PDF ページコンテンツにレンダリングします。
1. 出力PDFファイルを保存してください。

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## テキストをPDFに変換するシンプルなワークフロー

プレーンテキストファイルを迅速に PDF に変換する必要がある場合は、この例を使用してください。

1. プレーンテキストのソースを UTF-8 デコードで読み取り、テキストコンテンツを Java の文字列として利用できるようにしてください。
1. 空のものを作成する [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) そして追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. テキストを...で囲む [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) そしてそれをページ段落コレクションに追加します。
1. 生成されたPDFを保存してください。

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 高度なオプションでテキストをPDFに変換する

プレーンテキストを追加のレイアウトやエンコーディングオプションで変換する必要がある場合は、この例を使用してください。

1. 入力ファイルからすべてのテキスト行を読み取り、変換中にページ区切りマーカーを検査できるようにしてください。
1. 空のものを作成する [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) そしてそれぞれを構成する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 余白とデフォルトのテキスト状態で。
1. 等幅フォントを介して解決する [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) 各行を～として追加 [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. ページ構築ループが完了したら、出力ファイルを保存してください。

```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PCL を PDF に変換

PCL 印刷ストリームを PDF に変換する必要があるときは、この例を使用してください。

1. 作成 [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) そして、寛容なインポート動作が必要な場合に抑制されたパースエラーを有効にしてください。
1. ファイルパスとロードオプションを渡して、PCL ソースを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. 結果を PDF として保存してください。

```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## XSLT と HTML を使用して XML を PDF に変換する

最終的なPDF生成の前にXMLデータを変換する必要がある場合は、この例を使用してください。

1. 専用の変換メソッドを呼び出して、XML ソースを XSLT ファイルで変換し、一時的な HTML ファイルにします。
1. 生成されたHTMLファイルを既存のHTMLからPDFへの変換関数に渡し、最終的なPDFが標準を使用するようにします。 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) Workflow。
1. 一時的なHTMLファイルを削除する `finally` 変換が完了した後にブロックしてください。
1. 生成された PDF ファイルを保存してください。

```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## XPS を PDF に変換

XPS ドキュメントを PDF に変換する必要がある場合は、この例を使用してください。

1. ファイルパスを渡してXPSソースを開く [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) へ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF がドキュメントの読み込み中に XPS ページ記述を解釈するようにします。
1. 変換されたPDFを保存してください。

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## XSL-FOをPDFに変換

XSL-FO コンテンツを PDF としてレンダリングする必要がある場合は、この例を使用してください。

1. 作成 [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) XML ソースをロード中に変換できるよう、XSLT パスを指定して
1. 無効な XSL‑FO が検出されたときに、直ちに例外をスローするように解析エラー処理モードを設定してください。
1. XML ソースを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) それらのロードオプションで。
1. 結果のPDFドキュメントを保存してください。

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## XML を中間的な HTML に変換する

XML データを最終的な PDF 変換ステップの前に HTML に変換する必要がある場合は、このメソッドを使用します。

1. XML と XSLT の入力ファイルを変換ソースとして開いてください。
1. 作成 `Transformer` XSLTスタイルシートから取得し、XMLソースに対して実行してください。
1. 変換されたHTMLファイルを書き込み、下流のPDF変換関数が読み込めるようにしてください。

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
