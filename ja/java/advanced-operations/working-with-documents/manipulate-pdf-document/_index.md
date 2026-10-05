---
title: "Java での PDF ドキュメントの操作"
linktitle: "PDF ドキュメントの操作"
type: docs
weight: 20
url: /ja/java/manipulate-pdf-document/
description: "Java で PDF ドキュメントを検証、構造化、変更する方法を学習します。TOC の管理や PDF/A 検証を含みます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ドキュメントの検証、再構築、およびフラット化"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ドキュメントを操作する方法を説明します。PDF/A 準拠の検証、目次の追加とカスタマイズ、TOC ページ番号の非表示またはカスタマイズ、有効期限スクリプトの割り当て、インタラクティブフォームフィールドのフラット化について取り上げています。"
---
Aspose.PDF for Java は、単純なページ編集を超えたドキュメント構造操作をサポートしています。

## PDF/A-1a 準拠性の検証

ドキュメントが PDF/A-1a アーカイブ標準に適合しているかを確認する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要な [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) を対象に検証を実行してください。
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
1. 検証メソッドを呼び出す際に [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) の PDF/A-1b の値を指定してください。
1. 検証結果を出力レポートファイルに書き込んでください。

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
1. 新しい目次を挿入する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を作成し、その [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) を設定してください。
1. 目的のページを指す [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) エントリを作成してください。
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

## TOC のレベルと書式設定のカスタマイズ

この例では、複数の目次レベルに異なるビジュアル設定を割り当てる方法を示しています。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 目次用の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、[TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) の書式設定配列を設定してください。
1. 異なるレベルの [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) エントリのサンプルを作成してください。
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

## 目次のページ番号の非表示

目次にページ番号なしでエントリのタイトルを表示する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 目次用の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、[TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) でページ番号を無効にしてください。
1. 必要な [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) エントリを作成し、コンテンツページに追加してください。
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

## TOC ページ番号のプレフィックスのカスタマイズ

この例では、生成された目次に表示されるページ番号にカスタムプレフィックスを追加します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. TOC を [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) に挿入し、目的のページ番号プレフィックスを [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) に設定してください。
1. 各ページを指す [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) エントリを作成してください。
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

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で開き、必要なコンテンツをすべて追加してください。
1. 有効期限ロジックを含む [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) を作成してください。
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

## 入力可能な PDF フォームのフラット化

この例では、インタラクティブなフォームフィールドを静的なページ コンテンツに変換します。そのため、変換後のドキュメントはフォームとして編集できなくなります。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントにフォームウィジェットが含まれているか確認してください。
1. 各 [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) を、[WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/) で表されるものとしてフラット化してください。
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
