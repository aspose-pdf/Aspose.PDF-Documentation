---
title: "Java での PDFヘッダーとフッターの追加"
linktitle: "PDFにヘッダーとフッターの追加"
type: docs
weight: 50
url: /ja/java/add-headers-and-footers-of-pdf-file/
description: Java を使用してテキスト、画像、構造化コンテンツで PDF ファイルにヘッダーとフッターを追加する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ファイルにヘッダーとフッターを追加する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントにヘッダーとフッターを追加する方法を示します。テキスト、ページ番号、HTML、画像、テーブル、そして LaTeX ベースのヘッダーおよびフッターコンテンツについて説明します。
---
Aspose.PDF for Java は割り当てることができます `HeaderFooter` 各ページにオブジェクトを配置し、異なるコンテンツタイプでそれらを埋め込みます。

## テキストヘッダーとフッターの追加

各ページの上部と下部にシンプルなテキストコンテンツが必要な場合は、この例を使用してください。

1. 作成 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) オブジェクトにテキストフラグメントを追加してください。
1. ヘッダーとフッターの余白を設定してください。
1. それらをソースPDFの各ページに適用し、結果を保存してください。

```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## ヘッダーとフッターにページ番号の追加

ヘッダーまたはフッターに現在のページ番号と総ページ数を表示する必要がある場合は、この例を使用してください。

1. 作成 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) ページ番号プレースホルダーを持つオブジェクト。
1. 両方のオブジェクトの余白を設定してください。
1. それらを各ページに適用し、更新されたPDFを保存してください。

```java
public static void usingHeaderAndFooterForPageNumbering(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Page $p from $P"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Page $p / $P"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## HTMLヘッダーとフッターの追加

ヘッダーとフッターの内容にインラインHTMLフォーマットを含める必要がある場合は、この例を使用してください。

1. 作成 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) オブジェクトと追加 [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) コンテンツ。
1. 配置のために余白を設定してください。
1. ヘッダーとフッターを各ページに割り当て、ドキュメントを保存してください。

```java
public static void addHeaderAndFooterAsHtml(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new HtmlFragment("This is an HTML <strong>Header</strong>"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new HtmlFragment("Powered by <i>Aspose.PDF</i>"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 画像ヘッダーとフッターの追加

ヘッダーとフッターに毎ページ画像を表示する必要がある場合は、この例を使用してください。

1. 作成 [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) オブジェクトをヘッダーとフッターのコンテナに追加してください。
1. 余白を設定し、各ページにコンテナを割り当てます。
1. 更新された PDF を保存してください。

```java
public static void addHeaderAndFooterAsImage(Path inputFile, Path imageFile, Path outputFile) {
    Image headerImage = new Image();
    headerImage.setFile(imageFile.toString());
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(headerImage);

    Image footerImage = new Image();
    footerImage.setFile(imageFile.toString());
    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(footerImage);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            MarginInfo margin = new MarginInfo();
            margin.setLeft(50);
            header.setMargin(margin);
            footer.setMargin(margin);
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## テーブルベースのヘッダーとフッターの追加

ヘッダーとフッターのコンテンツがテーブルレイアウトとテキストスタイリングを使用すべき場合は、この例を使用してください。

1. 必要なテキストスタイルとテーブルオブジェクトを作成してください。
1. テーブルを追加 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) コンテナ。
1. ヘッダーとフッターを各ページに適用し、ドキュメントを保存してください。

```java
public static void addHeaderAndFooterAsTable(Path inputFile, Path outputFile) {
    TextState textStateHeader = new TextState();
    textStateHeader.setFont(FontRepository.findFont("Arial"));
    textStateHeader.setFontSize(12);
    textStateHeader.setHorizontalAlignment(HorizontalAlignment.Center);

    TextState textStateFooter = new TextState();
    textStateFooter.setFont(FontRepository.findFont("Arial"));
    textStateFooter.setFontSize(12);
    textStateFooter.setHorizontalAlignment(HorizontalAlignment.Left);

    HeaderFooter header = new HeaderFooter();
    HeaderFooter footer = new HeaderFooter();

    Table tableHeader = new Table();
    tableHeader.setColumnWidths(String.valueOf(594 - header.getMargin().getLeft() - header.getMargin().getRight()));
    tableHeader.getRows().add().getCells().add("This is a Table Header", textStateHeader);

    Table table = new Table();
    table.setColumnWidths(String.valueOf(594 - footer.getMargin().getLeft() - footer.getMargin().getRight()));
    table.getRows().add().getCells().add("Powered by Aspose.PDF", textStateFooter);

    header.getParagraphs().add(tableHeader);
    footer.getParagraphs().add(table);
    footer.getMargin().setLeft(150);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## LaTeXのヘッダーとフッターの追加

ヘッダーとフッターが TeX または LaTeX コンテンツをレンダリングする必要がある場合は、この例を使用してください。

1. ソースPDFを開き、総ページ数を確認してください。
1. 作成 [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) 各ページのヘッダーとフッターの内容。
1. コンテンツを割り当て、ドキュメントを保存してください。

```java
public static void addHeaderAndFooterAsLatex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int pageCount = document.getPages().size();
        for (int i = 1; i <= pageCount; i++) {
            HeaderFooter header = new HeaderFooter();
            header.getParagraphs().add(new TeXFragment("This is a LaTeX Header. \\today\\", true));

            HeaderFooter footer = new HeaderFooter();
            footer.getParagraphs().add(new TeXFragment("\\copyright\\ 2025 My Company -- Page \\thepage\\ is " + pageCount, true));

            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```
