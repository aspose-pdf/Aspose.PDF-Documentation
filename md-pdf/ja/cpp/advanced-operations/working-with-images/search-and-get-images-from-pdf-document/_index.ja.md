---
title: C++を使用してPDFドキュメントから画像を検索および取得する
linktitle: 画像の検索と取得
type: docs
weight: 60
url: /cpp/search-and-get-images-from-pdf-document/
description: このセクションでは、Aspose.PDFライブラリを使用してPDFドキュメントから画像を検索および取得する方法を説明します。
lastmod: "2021-12-18"
---

ImagePlacementAbsorberを使用すると、PDFドキュメント内のすべてのページの画像を検索できます。

ドキュメント全体を画像で検索するには：

1. [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)コレクションの[Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f)メソッドを呼び出します。Acceptメソッドは[ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/)オブジェクトをパラメータとして取ります。これにより、ImagePlacementオブジェクトのコレクションが返されます。
1. ImagePlacementsオブジェクトをループして、そのプロパティ（画像、寸法、解像度など）を取得します。

次のコードスニペットは、ドキュメント内のすべての画像を検索する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // 画像配置検索を実行するためのImagePlacementAbsorberオブジェクトを作成
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // すべてのページに対してアブソーバを受け入れる
    document->get_Pages()->Accept(abs);

    // すべてのImagePlacementsをループし、画像とImagePlacementのプロパティを取得
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // ImagePlacementオブジェクトを使用して画像を取得
        auto image = imagePlacement->get_Image();

        // すべての配置について画像配置プロパティを表示
        Console::WriteLine(u"画像の幅: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"画像の高さ:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"画像のLLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"画像のLLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"画像の水平解像度:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"画像の垂直解像度:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```