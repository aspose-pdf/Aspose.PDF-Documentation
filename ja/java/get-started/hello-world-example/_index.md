---
title: Java を使用した Hello World の例
linktitle: Hello World の例
type: docs
weight: 20
url: /ja/java/hello-world-example/
description: このサンプルは、Aspose.PDF for Java を使用してスタイル付き Hello World テキストでシンプルな PDF ドキュメントを作成する方法を示しています。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java 経由の Hello World の例
Abstract: この記事では、Aspose.PDF for Java の Hello World の例を提供します。この例では新しい PDF ドキュメントを作成し、ページを追加し、カスタム位置・フォント・カラーを持つ TextFragment を作成し、TextBuilder を使用してテキストをページに追加し、結果を PDF ファイルとして保存します。
---
「Hello World」例は、基本的な PDF 作成ワークフローを理解する最短の方法です。本記事では、例として新しい PDF を作成し、ページにスタイル付きテキストフラグメントを配置し、出力ファイルを保存します。

Java の例では、次の手順で PDF ドキュメントを作成します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. テキスト `Hello, world!` を含む [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を作成してください。
1. [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/) を設定し、フラグメントの [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) を使用してフォント、フォントサイズ、背景色、前景色を設定してください。
1. ページの [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) を作成してください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) に [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を追加してください。
1. PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

次の Java コードは `GetStartedExamples.java` に基づいています。

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```
