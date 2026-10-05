---
title: "Java 経由で PDF からフォントの抽出"
linktitle: "PDF からフォントの抽出"
type: docs
weight: 30
url: /ja/java/extract-fonts-from-pdf/
description: Aspose.PDF for Java を使用して、PDF ドキュメントで使用されているフォントを検査および抽出します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF からフォントを抽出する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントで使用されているフォントを検査する方法を説明します。PDF を開き、`getFontUtilities().getAllFonts()` を呼び出し、得られたフォントオブジェクトを反復処理して名前を読み取る方法を示します。
---
変換やアーカイブのワークフローの前に、文書のタイポグラフィを監査したり、埋め込みリソースを検査したり、フォント使用状況を検証したりする必要がある場合にフォント抽出を使用します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 呼び出す `document.getFontUtilities().getAllFonts()` すべてを集める [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 文書が参照しているリソース。
1. 抽出されたものを反復処理する [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) オブジェクトを取得し、フォントメタデータから各フォント名を読み取ります。
1. フォント名を出力して、ドキュメントのタイポグラフィを監査またはエクスポートできるようにしてください。

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
