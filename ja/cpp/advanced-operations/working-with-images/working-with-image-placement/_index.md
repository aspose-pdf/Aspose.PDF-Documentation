---
title: C++を使用した画像配置の操作
linktitle: 画像配置の操作
type: docs
weight: 50
url: /ja/cpp/working-with-image-placement/
description: このセクションでは、C++ライブラリを使用した画像配置PDFファイルの操作機能について説明します。
lastmod: "2021-12-18"
---

**Aspose.PDF for C++**は、PDFドキュメント内の画像の解像度と位置を取得するために、上記のクラスと同様の機能を提供する[ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement)、[ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber)、および[ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection)をサポートしています。

- ImagePlacementAbsorberは、ImagePlacementオブジェクトのコレクションとして画像使用の検索を実行します。
- ImagePlacementは、実際の画像配置の値を返すResolutionおよびRectangleのメンバーを提供します。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // ソースPDFドキュメントをロード
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // 最初のページのコンテンツをロード
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // 画像プロパティを取得
        Console::WriteLine(u"画像の幅: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"画像の高さ:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"画像のLLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"画像のLLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"画像の水平解像度:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"画像の垂直解像度:{0}", imagePlacement->get_Resolution()->get_Y());

        // 表示される寸法で画像を取得
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // リソースから画像を取得
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // 実際の寸法でビットマップを作成
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```