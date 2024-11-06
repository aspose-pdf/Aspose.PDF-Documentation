---
title: C++を使用してPDFファイルから画像を抽出する
linktitle: 画像を抽出する
type: docs
weight: 30
url: ja/cpp/extract-images-from-pdf-file/
description: このセクションでは、C++ライブラリを使用してPDFファイルから画像を抽出する方法を示します。
lastmod: "2021-12-18"
---

Aspose.PDF for C++を使用して、PDFドキュメントからすべての画像を抽出し、他のプログラムで再利用できる個別のファイルにすることができます。

画像は各ページのResourcesコレクションのImagesコレクションに保持されています。特定のページを抽出するには、画像の特定のインデックスを使用してImagesコレクションから画像を取得します。

画像のインデックスは[XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image)オブジェクトを返します。このオブジェクトは、抽出された画像を保存するために使用できるSaveメソッドを提供します。

次のコードスニペットは、PDFファイルから画像を抽出する方法を示しています。

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // 特定の画像を抽出
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // 出力画像を保存
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // 更新されたPDFファイルを保存
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```