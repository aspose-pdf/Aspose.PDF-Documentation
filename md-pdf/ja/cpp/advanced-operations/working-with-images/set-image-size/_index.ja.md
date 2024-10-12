---
title: C++を使用して画像サイズを設定
linktitle: 画像サイズを設定
type: docs
weight: 80
url: /cpp/set-image-size/
description: このセクションでは、C++ライブラリを使用してPDFファイルの画像サイズを設定する方法について説明します。
lastmod: "2021-12-18"
---

PDFファイルに追加される画像のサイズを設定することが可能です。サイズを設定するには、[Aspose.Pdf.Image クラス](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image)の[FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e)プロパティと[FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa)プロパティを使用できます。

次のコードスニペットは、画像のサイズを設定する方法を示しています。

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>();
    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();
    // 画像インスタンスを作成
    auto img = MakeObject<Image>();
    // 画像の幅と高さをポイントで設定
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // 画像タイプをSVGとして設定
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // ソースファイルのパス
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // ページプロパティを設定
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // 結果のPDFファイルを保存
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```