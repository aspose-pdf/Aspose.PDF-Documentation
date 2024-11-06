---
title: C++を使用してデフォルトフォント名を設定する
linktitle: デフォルトフォント名を設定する
type: docs
weight: 90
url: ja/cpp/set-default-font-name/
description: このセクションでは、C++ライブラリを使用してデフォルトフォント名を設定する方法について説明します。
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** APIを使用すると、ドキュメント内でフォントが利用できない場合にデフォルトフォント名を設定することができます。RenderingOptionsクラスのDefaultFontNameプロパティを使用してデフォルトフォント名を設定できます。DefaultFontNameが`nullptr`に設定されている場合、**Times New Roman**フォントが使用されます。以下のコードスニペットは、PDFを画像として保存する際にデフォルトフォント名を設定する方法を示しています。

```cpp
void WorkingWithImages::ExampleSetDefaultFontName()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    auto imageStream = System::IO::File::OpenWrite(_dataDir + u"SetDefaultFontName.png");

    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);
    auto pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    auto ro = MakeObject<RenderingOptions>();
    ro->set_DefaultFontName(u"Arial");
    pngDevice->set_RenderingOptions(ro);
    pngDevice->Process(document->get_Pages()->idx_get(1), imageStream);
}
```