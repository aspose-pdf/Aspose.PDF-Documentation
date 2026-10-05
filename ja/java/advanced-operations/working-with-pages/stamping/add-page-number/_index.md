---
title: "Java での PDF へのページ番号追加"
linktitle: ページ番号の追加
type: docs
weight: 30
url: /ja/java/add-page-number/
description: "Java で PDF ドキュメントにページ番号スタンプを追加する方法を学習します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイルへのページ番号スタンプの追加"
Abstract: この記事では、Aspose.PDF for Java を使用してページ番号スタンプを追加する方法を説明します。カスタムフォントスタイルによる標準的なページ番号付けと、開始番号を設定可能なローマ数字のページ番号付けについて解説します。
---
## ページ番号スタンプの追加

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) オブジェクトを作成してください。
1. 必要なスタンプの配置と番号オプションを構成してください。
1. 必要なテキスト書式設定オプションを設定し、[FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) および [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) を含めてください。
1. 構成した [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) を対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) に追加してください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

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
