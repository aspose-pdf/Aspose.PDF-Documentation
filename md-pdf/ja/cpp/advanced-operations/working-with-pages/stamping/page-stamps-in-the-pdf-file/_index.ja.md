---
title: PDFにページスタンプを追加する
linktitle: PDFファイルのページスタンプ
type: docs
weight: 30
url: /cpp/page-stamps-in-the-pdf-file/
description: PdfPageStampクラスを使用して、C++でPDFファイルにページスタンプを追加します。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## C++でページスタンプを追加する

[PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp) は、グラフィックス、テキスト、テーブルを含む合成スタンプを適用する必要があるときに使用できます。次の例は、Adobe InDesign、Illustrator、Microsoft Wordを使用するような定型用紙を作成するためにスタンプを使用する方法を示しています。入力ドキュメントがあり、青色とプラム色の2種類の境界線を適用したいとします。

```cpp
void AddPageStamp()
{
    String _dataDir("C:\\Samples\\");

    String inputFileName ("sample-4pages.pdf");
    String outputFileName ("AddPageStamp_out.pdf");
    String pageStampFileName ("PageStamp.pdf");
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto bluePageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 1);
    bluePageStamp->set_Height(800);
    bluePageStamp->set_Background(true);

    auto plumPageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 2);
    plumPageStamp->set_Height(800);
    plumPageStamp->set_Background(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document->get_Pages()->idx_get(i)->AddStamp(bluePageStamp);
        else
            document->get_Pages()->idx_get(i)->AddStamp(plumPageStamp);
    }

    document->Save(_dataDir + outputFileName);
}
```