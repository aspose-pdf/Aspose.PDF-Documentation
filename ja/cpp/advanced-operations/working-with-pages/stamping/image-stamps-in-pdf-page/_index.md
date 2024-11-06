---
title: PDFに画像スタンプをプログラムで追加する
linktitle: PDFファイルに画像スタンプ
type: docs
weight: 10
url: ja/cpp/image-stamps-in-pdf-page/
description: Aspose.PDF for C++ライブラリを使用して、ImageStampクラスでPDFドキュメントに画像スタンプを追加します。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルに画像スタンプを追加する

ImageStampクラスを使用して、PDFファイルに画像スタンプを追加できます。ImageStampクラスは、高さ、幅、不透明度などの画像ベースのスタンプを作成するために必要なプロパティを提供します。

画像スタンプを追加するには:

1. 必要なプロパティを使用して[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトとImageStampオブジェクトを作成します。
1. [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)クラスの[AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02)メソッドを呼び出して、PDFにスタンプを追加します。

次のコードスニペットは、PDFファイルに画像スタンプを追加する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 画像スタンプを作成
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // 特定のページにスタンプを追加
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // 出力ドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## スタンプを追加するときの画像品質の制御

画像をスタンプオブジェクトとして追加する際、画像の品質を制御できます。 The Quality プロパティは、[ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) クラスのプロパティで、この目的のために使用されます。これは、画像の品質をパーセントで示します（有効な値は0から100です）。

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名のための文字列
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 画像スタンプを作成
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## 浮動ボックス内の背景としての画像スタンプ

Aspose.PDF API を使用すると、浮動ボックス内の背景として画像スタンプを追加できます。 FloatingBox クラスの BackgroundImage プロパティは、次のコードサンプルに示すように、フローティングボックスの背景画像スタンプを設定するために使用できます。

```cpp
void ImageStampAsBackgroundInFloatingBox() {
    
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // Document オブジェクトをインスタンス化
    auto document = MakeObject<Document>();

    // PDF ドキュメントにページを追加
    auto page = document->get_Pages()->Add();

    // FloatingBox オブジェクトを作成
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // FloatingBox の左位置を設定
    aBox->set_Left(40);
    // FloatingBox の上位置を設定
    aBox->set_Top(80);
    // FloatingBox の水平方向の配置を設定
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // FloatingBox の段落コレクションにテキストフラグメントを追加
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // FloatingBox の境界を設定
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // 背景画像を追加
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // FloatingBox の背景色を設定
    aBox->set_BackgroundColor(Color::get_Yellow());

    // ページオブジェクトの段落コレクションに FloatingBox を追加
    page->get_Paragraphs()->Add(aBox);
    // PDF ドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```