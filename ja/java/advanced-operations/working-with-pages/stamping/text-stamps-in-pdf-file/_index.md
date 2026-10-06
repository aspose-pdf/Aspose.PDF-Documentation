---
title: "Java での PDF へのテキストスタンプの追加"
linktitle: "PDF ファイルのテキストスタンプ"
type: docs
weight: 20
url: /ja/java/text-stamps-in-the-pdf-file/
description: "Java で PDF 文書にテキストスタンプを追加する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイルへのテキストスタンプの追加"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルにテキストスタンプを追加する方法を説明します。背景テキストスタンプの作成、位置指定、回転、そして Font、サイズ、スタイル、色のカスタマイズについてカバーしています。
---
PDF ページに目に見えるラベルやウォーターマークを追加する必要がある場合は、テキストスタンプを使用してください。

## テキストスタンプの追加

ページに回転したテキストスタンプをカスタムスタイルで表示する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) オブジェクトを作成し、配置とテキストの外観を設定してください。
1. スタンプを対象ページに追加し、ドキュメントを保存してください。

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
