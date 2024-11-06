---
title: C++を使用してPDFページを回転させる
linktitle: PDFページを回転させる
type: docs
weight: 50
url: ja/cpp/rotate-pages/
description: このトピックでは、既存のPDFファイルのページの向きをC++でプログラム的に回転させる方法について説明します。
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

このトピックでは、既存のPDFファイルのページの向きをC++でプログラム的に更新または変更する方法について説明します。

## ページの向きを変更する

Aspose.PDF for C++を使用すると、ページの向きを横向きから縦向きに、またその逆にも変更できます。ページの向きを変更するには、次のコードスニペットを使用してページのMediaBoxを設定します。また、Rotate()メソッドを使用して回転角度を設定することでもページの向きを変更できます。

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // ページのサイズ変更を補うためにページを上に移動する必要があります。
        // （ページの下端は0,0であり、情報は通常ページの上から配置されます。
        //  そのため、古い高さと新しい高さの差分だけ下端を上に移動します。）

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // オリジナルファイルにCropBoxが設定されている場合、CropBoxも設定する必要があります。
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // ページの回転角度を設定
        page->set_Rotate(Rotation::on90);
    }

    // 出力ファイルを保存
    document->Save(_dataDir + outputFileName);
}
```

## 新しいページの向きに合わせてページの内容を調整する

上記のコードスニペットを使用する際、ページの高さが減少するため、ドキュメントのコンテンツの一部が切り取られる可能性があることに注意してください。これを避けるためには、幅を比例的に広げ、高さをそのままにしておきます。計算の例:

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // 新しい高さは同じ
        double newHeight = r->get_Height();
        // 新しい幅は向きを横向きにするために比例的に拡張
        // （以前の向きが縦向きであると仮定します）
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

上記の方法に加えて、ページコンテンツにズームを適用できるPdfPageEditorファサードの使用を検討してください。

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDFの最初のページの長方形領域を取得
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // PdfPageEditorインスタンスを生成
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // ソースPDFをバインド
    ppe->BindPdf(_dataDir + inputFileName);
    // ズーム係数を設定
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // ページサイズを更新
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // 出力ファイルを保存
    document->Save(_dataDir + outputFileName);
}
```