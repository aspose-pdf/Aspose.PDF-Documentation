---
title: C++を使用してPDFに画像を追加
linktitle: 画像を追加
type: docs
weight: 10
url: /ja/cpp/add-image-to-existing-pdf-file/
description: このセクションでは、C++ライブラリを使用して既存のPDFファイルに画像を追加する方法を説明します。
lastmod: "2021-12-18"
---

## 既存のPDFファイルに画像を追加

すべてのPDFページには、リソースとコンテンツのプロパティがあります。リソースは画像やフォームなど、コンテンツは一連のPDF演算子によって表されます。各演算子には名前と引数があります。この例では、演算子を使用してPDFファイルに画像を追加します。

既存のPDFファイルに画像を追加するには:

- [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) オブジェクトを作成し、入力PDFドキュメントを開きます。
- 画像を追加したいページを取得します。
- ページのリソースコレクションに画像を追加します。
- 演算子を使用してページに画像を配置します:
- 現在のグラフィカル状態を保存するために [GSave operator](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) を使用します。

- 画像を配置する位置を指定するために [ConcatenateMatrix operator](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96) を使用します。
- ページに画像を描画するために[Do演算子](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/)を使用します。  
- 最後に、更新されたグラフィカル状態を保存するために[GRestore演算子](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/)を使用します。  
- ファイルを保存します。  
次のコードスニペットは、PDFドキュメントに画像を追加する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // 座標を設定する
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // 画像を追加したいページを取得する
    auto page = document->get_Pages()->idx_get(1);

    // ストリームに画像を読み込む
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // ページリソースのImagesコレクションに画像を追加する
    page->get_Resources()->get_Images()->Add(imageStream);

    // GSave演算子の使用: この演算子は現在のグラフィック状態を保存します
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // RectangleとMatrixオブジェクトを作成する
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // ConcatenateMatrix（行列の連結）演算子の使用:
    // 画像をどのように配置するかを定義します
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // Do演算子の使用: この演算子は画像を描画します
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // GRestore演算子の使用: この演算子はグラフィック状態を復元します
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // 新しいPDFを保存する
    document->Save(_dataDir + u"updated_document.pdf");

    // 画像ストリームを閉じる
    imageStream->Close();
}
```

## PDFドキュメントで単一画像を複数回参照として追加する

場合によっては、同じ画像をPDFドキュメントに複数回使用する必要があります。新しいインスタンスを追加すると、結果のPDFドキュメントのサイズが増加します。[XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) メソッドは、元の画像と同じPDFオブジェクトへの参照を追加することにより、PDFドキュメントのサイズを最適化します。

```cpp
void WorkingWithImages::AddReferenceOfaSingleImageMultipleTimes() {

    String _dataDir("C:\\Samples\\");
    auto imageRectangle = MakeObject<Rectangle>(0, 0, 30, 15);

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    document->get_Pages()->Add();
    document->get_Pages()->Add();

    auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.png");

    SharedPtr<Aspose::Pdf::XImage> image;

    for (auto page : document->get_Pages()) {
        auto annotation = MakeObject<Aspose::Pdf::Annotations::WatermarkAnnotation>(page, page->get_Rect());
        auto form = annotation->get_Appearance()->idx_get(u"N");
        form->set_BBox(page->get_Rect());
        String name;
        if (image != nullptr) {
            name = form->get_Resources()->get_Images()->Add(imageStream);
            image = form->get_Resources()->get_Images()->idx_get(name);
        }
        else {
            form->get_Resources()->get_Images()->AddWithName(image);
        }
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
        form->get_Contents()->Add(
            MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(
                MakeObject<Matrix>(imageRectangle->get_Width(), 0, 0, imageRectangle->get_Height(), 0, 0)));

        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(name));
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
        page->get_Annotations()->Add(annotation, false);
        imageRectangle = MakeObject<Rectangle>(0, 0, imageRectangle->get_Width() * 1.01, imageRectangle->get_Height() * 1.01);
    }
    document->Save(_dataDir + u"AddReferenceOfaSingleImageMultipleTimes_out.pdf");
}
```

## ページに画像を配置しアスペクト比を維持する

画像の寸法がわからない場合、ページ上で画像が歪んでしまう可能性があります。次の例は、これを避ける方法の一つを示しています。

```cpp
void WorkingWithImages::AddingImageAndPreserveAspectRatioIntoPDF() {

    String _dataDir("C:\\Samples\\");

    auto bitmap = System::Drawing::Image::FromFile(_dataDir + u"3410492.jpg");

    int width;
    int height;

    width = bitmap->get_Width();
    height = bitmap->get_Height();

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page->AddImage(_dataDir + u"3410492.jpg", new Rectangle(10, 10, scaledWidth, scaledHeight));
    document->Save(_dataDir + u"sample_image.pdf");
}
```

## PDF内の画像がカラーか白黒かを識別する

画像のサイズを縮小するには、圧縮する必要があります。 
画像の圧縮タイプを決定する前に、それがカラーか白黒かを知る必要があります。

画像に適用される圧縮タイプは、元の画像のColorSpaceに依存します。つまり、画像がカラー（RGB）であればJPEG2000圧縮を使用し、白黒であればJBIG2 / JBIG2000圧縮を使用します。

PDFファイルには、テキスト、画像、グラフ、添付ファイル、注釈などの要素が含まれている場合があり、ソースPDFファイルに画像が含まれている場合、画像の色空間を決定し、画像に適切な圧縮を適用してPDFファイルのサイズを縮小することができます。

次のコードスニペットは、PDF内の画像がカラーか白黒かを識別する手順を示しています。

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // PDFファイルのすべてのページを反復処理
        for (auto page : document->get_Pages()) {
            // Image Placement Absorberインスタンスを作成
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* ColorType */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"グレースケール画像");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"カラー画像");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"ファイルの読み込みエラー = {0}", document->get_FileName());
    }
}
```
## 画像品質の制御

PDFファイルに追加される画像の品質を制御することが可能です。[XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) クラスのオーバーロードされた [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) メソッドを使用します。

以下のコードスニペットは、ドキュメント内のすべての画像を80%の品質で圧縮するJPEGに変換する方法を示しています。

```cpp
void WorkingWithImages::ControlImageQuality() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_with_images.pdf");

    for (auto page : document->get_Pages())
    {
        int idx = 1;
        for (auto image : page->get_Resources()->get_Images())
        {
            auto imageStream = MakeObject<System::IO::MemoryStream>();
            image->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Jpeg());
            page->get_Resources()->get_Images()->Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }

    document->Save(_dataDir + u"sample_with_images_out.pdf");
}
```