---
title: "Java での 他のファイル形式の PDF への変換"
linktitle: "他のファイル形式の PDF への変換"
type: docs
weight: 80
url: /ja/java/convert-other-files-to-pdf/
lastmod: "2026-10-06"
description: "Aspose.PDF を使用して、Java で EPUB、Markdown、PCL、XPS、PostScript、XML、XSL-FO、OFD、TeX ファイルを PDF に変換する方法を学びます。"
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

1. ファイルパスと [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、OFD ソースを開いてください。
1. Aspose.PDF に OFD パッケージを PDF ドキュメントモデルに解析させてください。
1. 結果の PDF をターゲット出力パスに保存してください。

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## TeX から PDF への変換

TeX コンテンツを直接 PDF としてレンダリングする必要がある場合は、この例を使用してください。

1. ファイルパスと [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、TeX ソースを開いてください。
1. Aspose.PDF に TeX マークアップを解釈させ、ロード中に PDF レイアウトを構築させてください。
1. 生成された PDF を保存してください。

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PostScript から PDF への変換

PostScript ファイルを PDF ドキュメントに変換する必要がある場合は、この例を使用してください。

1. [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、PostScript ソースを開いてください。
1. Aspose.PDF に PostScript ページ記述ストリームを PDF ドキュメントモデルに変換させてください。
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

1. EPS ソースを [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) を使用して開いてください。EPS は同じ PostScript ベースのロードパスに従うためです。
1. ファイルを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にロードしてください。これにより、ページ記述のコンテンツがインポート時に変換されます。
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

EPUB e ブックを PDF に変換する必要がある場合は、この例を使用してください。

1. ファイルパスと [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、EPUB ソースを開いてください。
1. Aspose.PDF に e ブックの構造をロードさせ、PDF ページに変換させてください。
1. 変換された PDF を保存してください。

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Markdown を PDF に変換

Markdown コンテンツをレンダリングして PDF として保存する場合は、この例を使用してください。

1. ファイルパスと [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、Markdown ソースを開いてください。
1. Aspose.PDF が Markdown コンテンツを解釈し、PDF ページのコンテンツにレンダリングしてください。
1. 出力 PDF ファイルを保存してください。

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## テキストから PDF への変換のシンプルなワークフロー

プレーンテキストファイルを迅速に PDF に変換する必要がある場合は、この例を使用してください。

1. プレーンテキストのソースを UTF-8 でデコードして読み込み、テキストコンテンツを Java の文字列として取得してください。
1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、[`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. テキストを [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) で囲み、ページの段落コレクションに追加してください。
1. 生成された PDF を保存してください。

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

## 高度なオプションによるテキストから PDF への変換

プレーンテキストを追加のレイアウトやエンコーディングオプションで変換する必要がある場合は、この例を使用してください。

1. 入力ファイルからすべてのテキスト行を読み取り、変換中にページ区切りマーカーを検査できるようにしてください。
1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、各 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を余白およびデフォルトのテキスト状態で構成してください。
1. 等幅フォントを [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) を通じて解決し、各行を [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) として追加してください。
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

## PCL から PDF への変換

PCL 印刷ストリームを PDF に変換する必要がある場合は、この例を使用してください。

1. [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) を作成し、寛容なインポート動作が必要な場合は抑制されたパースエラーを有効にしてください。
1. ファイルパスとロードオプションを [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、PCL ソースを開いてください。
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

## XSLT と HTML を使用した XML から PDF への変換

最終的な PDF を生成する前に XML データを変換する必要がある場合は、この例を使用してください。

1. 専用の変換メソッドを呼び出して、XML ソースを XSLT ファイルで変換し、一時的な HTML ファイルに変換してください。
1. 生成した HTML ファイルを既存の HTML から PDF への変換関数に渡し、最終的な PDF に標準の [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) ワークフローを使用してください。
1. 変換が完了した後に、一時的な HTML ファイルを `finally` ブロックで削除してください。
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

## XPS から PDF への変換

XPS ドキュメントを PDF に変換する必要がある場合は、この例を使用してください。

1. ファイルパスと [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、XPS ソースを開いてください。
1. Aspose.PDF がドキュメントの読み込み中に XPS ページ記述を解釈するようにしてください。
1. 変換された PDF を保存してください。

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## XSL-FO から PDF への変換

XSL-FO コンテンツを PDF としてレンダリングする必要がある場合は、この例を使用してください。

1. 読み込み時に XML ソースを変換できるように、XSLT パスを指定した [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) を作成してください。
1. 無効な XSL-FO が検出されたときに直ちに例外をスローするように、解析エラー処理モードを設定してください。
1. XML ソースを、そのロードオプションを指定して [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトで開いてください。
1. 結果の PDF ドキュメントを保存してください。

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

## XML の中間的な HTML への変換

XML データを最終的な PDF 変換ステップの前に HTML に変換する必要がある場合は、このメソッドを使用してください。

1. XML および XSLT の入力ファイルを変換ソースとして開いてください。
1. `Transformer` を XSLT スタイルシートから作成し、XML ソースに対して実行してください。
1. 変換された HTML ファイルをディスクに書き込んで、下流の PDF 変換関数が読み込めるようにしてください。

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
