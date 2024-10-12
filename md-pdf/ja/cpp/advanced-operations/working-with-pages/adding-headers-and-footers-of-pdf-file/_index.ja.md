---
title: PDFにヘッダーとフッターを追加
linktitle: PDFにヘッダーとフッターを追加
type: docs
weight: 70
url: /cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for C++を使用して、PDFファイルにヘッダーとフッターをTextStampクラスで追加できます。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++**を使用すると、既存のPDFファイルにヘッダーとフッターを追加できます。PDFドキュメントに画像やテキストを追加することができます。また、C++で1つのPDFファイルに異なるヘッダーを追加してみてください。

## PDFファイルのヘッダーにテキストを追加

[TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp)クラスを使用して、PDFファイルのヘッダーにテキストを追加できます。 TextStamp クラスは、フォントサイズ、フォントスタイル、フォントカラーなどのテキストベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーにテキストを追加するには、必要なプロパティを使用して Document オブジェクトと TextStamp オブジェクトを作成する必要があります。その後、Page の AddStamp メソッドを呼び出して、PDF のヘッダーにテキストを追加できます。

PDF のヘッダー領域にテキストが調整されるように TopMargin プロパティを設定する必要があります。また、HorizontalAlignment を Center に、VerticalAlignment を Top に設定する必要があります。

次のコードスニペットは、C++ で PDF ファイルのヘッダーにテキストを追加する方法を示しています。

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // ヘッダーを作成
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // スタンプのプロパティを設定
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // すべてのページにヘッダーを追加
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```
## PDFファイルのフッターにテキストを追加する

TextStampクラスを使用して、PDFファイルのフッターにテキストを追加することができます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。フッターにテキストを追加するには、Documentオブジェクトと必要なプロパティを使用してTextStampオブジェクトを作成する必要があります。その後、ページのAddStampメソッドを呼び出して、PDFのフッターにテキストを追加できます。

{{% alert color="primary" %}}

PDFのフッターエリアにテキストを調整するように、Bottom Marginプロパティを設定する必要があります。また、HorizontalAlignmentをCenterに設定し、VerticalAlignmentをBottomに設定する必要があります

{{% /alert %}}

次のコードスニペットは、C++でPDFファイルのフッターにテキストを追加する方法を示しています。

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // フッターを作成
    auto textStamp = MakeObject<TextStamp>(u"Footer Text");

    // スタンプのプロパティを設定
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Bottom);

    // すべてのページにフッターを追加
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## PDFファイルのヘッダーに画像を追加する

[ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp)クラスを使用して、PDFファイルのヘッダーに画像を追加できます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、画像ベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、PageのAddStampメソッドを呼び出して、PDFのヘッダーに画像を追加できます。

次のコードスニペットは、C++を使用してPDFファイルのヘッダーに画像を追加する方法を示しています。

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // ヘッダーを作成
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // スタンプのプロパティを設定
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // 全ページにヘッダーを追加
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## PDFファイルのフッターに画像を追加する

Image Stampクラスを使用して、PDFファイルのフッターに画像を追加することができます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、画像ベースのスタンプを作成するために必要なプロパティを提供します。フッターに画像を追加するためには、Documentオブジェクトと必要なプロパティを使用してImage Stampオブジェクトを作成する必要があります。その後、PageのAddStampメソッドを呼び出して、PDFのフッターに画像を追加することができます。

[BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173)プロパティを設定して、PDFのフッター領域に画像を調整するようにしてください。また、[HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9)を`Center`、[VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a)を`Bottom`に設定する必要があります。

以下のコードスニペットは、C++でPDFファイルのフッターに画像を追加する方法を示しています。

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // ヘッダーを作成
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // スタンプのプロパティを設定
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // すべてのページにヘッダーを追加
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## 1つのPDFファイルに異なるヘッダーを追加する

TopMarginまたはBottom Marginプロパティを使用してドキュメントのヘッダー/フッターセクションにTextStampを追加できることはわかっていますが、時には1つのPDFドキュメントに複数のヘッダー/フッターを追加する必要がある場合もあります。 **Aspose.PDF for C++** は、これを行う方法を説明します。

この要件を達成するために、個々の TextStamp オブジェクトを作成し（オブジェクトの数は必要なヘッダー/フッターの数に依存します）、それらを PDF ドキュメントに追加します。また、個々のスタンプオブジェクトに対して異なるフォーマット情報を指定することもできます。次の例では、Document オブジェクトと 3 つの TextStamp オブジェクトを作成し、[AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) メソッドを使用して PDF のヘッダーセクションにテキストを追加しています。次のコードスニペットは、Aspose.PDF for C++ を使用して PDF ファイルのフッターに画像を追加する方法を示しています。

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // ソースドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 3 つのスタンプを作成
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // スタンプの配置を設定（ページの上部、水平中央に配置）
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // フォントスタイルをボールドに指定
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // テキスト前景色情報を赤に設定
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // フォントサイズを 14 に指定
    stamp1->get_TextState()->set_FontSize(14);

    // 次に、2 番目のスタンプオブジェクトの垂直配置を上に設定する必要があります
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // スタンプの水平配置情報を中央揃えに設定
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // スタンプオブジェクトのズームファクターを設定
    stamp2->set_Zoom(10);

    // 3 番目のスタンプオブジェクトのフォーマットを設定
    // スタンプオブジェクトの垂直配置情報を上に指定
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // スタンプオブジェクトの水平配置情報を中央揃えに設定
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // スタンプオブジェクトの回転角度を設定
    stamp3->set_RotateAngle(35);
    // スタンプの背景色にピンクを設定
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // スタンプのフォントを Verdana に変更
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // 最初のスタンプは最初のページに追加されます;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // 2 番目のスタンプは 2 番目のページに追加されます;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // 3 番目のスタンプは 3 番目のページに追加されます。
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```