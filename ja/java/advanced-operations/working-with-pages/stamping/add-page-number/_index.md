---
title: "Java での PDFにページ番号の追加"
linktitle: ページ番号の追加
type: docs
weight: 30
url: /ja/java/add-page-number/
description: JavaでPDFドキュメントにページ番号スタンプを追加する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFファイルにページ番号スタンプを追加する
Abstract: この記事では、Aspose.PDF for Java を使用してページ番号スタンプを追加する方法を説明します。カスタムフォントスタイルによる標準的なページ番号付けと、開始番号を設定可能なローマ数字のページ番号付けについて解説します。
---
## ページ番号スタンプの追加

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) オブジェクトを作成してください。
1. 必要なスタンプ配置と番号オプションを構成してください。
1. 必要なテキスト書式設定オプションを設定し、含める [FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) および [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/)。
1. 構成されたものを追加 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) 対象へ [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 更新された PDF を保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```
