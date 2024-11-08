---
title: PDFにページスタンプを追加する
linktitle: PDFファイルのページスタンプ
type: docs
weight: 30
url: /ja/java/page-stamps-in-the-pdf-file/
description: JavaでPdfPageStampクラスを使用してPDFファイルにページスタンプを追加します。
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Javaでページスタンプを追加する

[PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) は、グラフィック、テキスト、テーブルを含む複合スタンプを適用する必要がある場合に使用できます。以下の例は、Adobe InDesign、Illustrator、Microsoft Wordを使用するように文房具を作成するためにスタンプを使用する方法を示しています。入力ドキュメントがあり、青色とプラム色の2種類の境界線を適用したいとします。

```java
public static void AddPageStamp()
{
    String inputFileName = "sample-4pages.pdf";
    String outputFileName = "AddPageStamp_out.pdf";
    String pageStampFileName = "PageStamp.pdf";
    Document document = new Document(_dataDir + inputFileName);

    PdfPageStamp bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1);
    bluePageStamp.setHeight(800);
    bluePageStamp.setBackground(true);

    PdfPageStamp plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2);
    plumPageStamp.setHeight(800);
    plumPageStamp.setBackground(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.getPages().get_Item(i).addStamp(bluePageStamp);
        else
            document.getPages().get_Item(i).addStamp(plumPageStamp);
    }

    document.save(_dataDir + outputFileName);
}
```