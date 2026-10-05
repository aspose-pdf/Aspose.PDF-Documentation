---
title: "Java での PDFドキュメントの操作"
linktitle: "PDFドキュメントの操作"
type: docs
weight: 20
url: /ja/java/manipulate-pdf-document/
description: JavaでPDFドキュメントを検証、構造化、変更する方法を学びます。TOCの管理やPDF/Aのチェックを含みます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFドキュメントを検証、再構築、フラット化します。
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントを操作する方法を説明します。PDF/A 準拠の検証、目次の追加とカスタマイズ、TOC ページ番号の非表示またはカスタマイズ、期限スクリプトの割り当て、インタラクティブ フォーム フィールドのフラッティングについて取り上げています。
---
Aspose.PDF for Java は単純なページ編集を超える文書構造操作を含みます。

## PDF/A-1a 準拠性の検証

ドキュメントが PDF/A-1a アーカイブ標準に適合しているか確認する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要な項目に対して検証を実行する [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) ターゲット。
1. 検証レポートを指定された出力パスに保存してください。

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## PDF/A-1b 準拠性の検証

このバリエーションは、同じソースドキュメントを PDF/A-1b 準拠レベルに対して検証します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 検証メソッドを呼び出す際に [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) PDF/A-1b の値。
1. 検証結果を出力レポートファイルに書き込む。

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## 目次の追加

ドキュメントに生成された目次ページを含め、コンテンツページへのリンクを設定したい場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 新しい目次を挿入する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そしてそれを構成する [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/)。
1. 作成 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 目的ページを指すエントリ。
1. 更新されたドキュメントを保存してください。

```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## TOCのレベルと書式設定をカスタマイズ

この例では、複数の目次レベルに異なるビジュアル設定を割り当てる方法を示しています。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 目次を追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして設定する [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) 配列をフォーマットしてください。
1. サンプルを作成 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 異なるレベルのエントリ。
1. フォーマット済みの目次を含むドキュメントを保存してください。

```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 目次のページ番号を非表示にする

目次にページ番号なしでエントリのタイトルを表示する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 目次を追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ページ番号を無効にする [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/)。
1. 必要なものを作成する [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) エントリを作成し、コンテンツページに追加してください。
1. 更新されたドキュメントを保存してください。

```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## TOCページ番号のプレフィックスをカスタマイズする

この例では、生成された目次に表示されるページ番号にカスタムプレフィックスを追加します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. TOC を挿入 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして、目的のページ番号プレフィックスを設定します [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/)。
1. 作成 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) 各ページを指すエントリ。
1. 更新されたドキュメントを保存してください。

```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## PDF の有効期限スクリプトの追加

ドキュメントを開いたときに JavaScript を実行し、特定の日付以降に有効期限の警告を表示する必要がある場合は、このアプローチを使用してください。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 必要なコンテンツをすべて追加してください。
1. 作成する [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) 有効期限ロジックと共に。
1. スクリプトを文書のオープン アクションに割り当て、出力ファイルを保存してください。

```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## 入力可能な PDF フォームをフラット化する

この例は、インタラクティブなフォームフィールドを静的なページコンテンツに変換するため、結果として得られるドキュメントはもうフォームとして編集できなくなります。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントにフォームウィジェットが含まれているか確認してください。
1. 各項目をフラット化 [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) aによって表される [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. フラット化されたドキュメントを保存してください。

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
