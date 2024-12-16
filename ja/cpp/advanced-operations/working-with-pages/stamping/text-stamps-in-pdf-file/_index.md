---
title: PDFファイルにテキストスタンプを追加
linktitle: PDFファイルにテキストスタンプ
type: docs
weight: 20
url: /ja/cpp/text-stamps-in-the-pdf-file/
description: C++を使用してTextStampクラスでPDFファイルにテキストスタンプを追加します。
lastmod: "2021-12-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## C++でテキストスタンプを追加

[TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp)クラスを使用してPDFファイルにテキストスタンプを追加できます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。テキストスタンプを追加するには、Documentオブジェクトと必要なプロパティを使用してTextStampオブジェクトを作成する必要があります。その後、PageのAddStampメソッドを呼び出して、PDFにスタンプを追加できます。次のコードスニペットは、PDFファイルにテキストスタンプを追加する方法を示しています。

```cpp
void AddTextStampToPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create text stamp
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // Set whether stamp is background
    textStamp->set_Background(true);
    // Set origin
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // Rotate stamp
    textStamp->set_Rotate(Rotation::on90);

    // Set text properties
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // Add stamp to particular page
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // Save output document
    document->Save(_dataDir + outputFileName);
}
```

## TextStampオブジェクトの配置を定義する

PDFドキュメントに透かしを追加することは、頻繁に要求される機能の一つであり、Aspose.PDF for C++は画像やテキストの透かしを追加することが完全に可能です。[TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp)という名前のクラスがあり、PDFファイルにテキストスタンプを追加する機能を提供します。最近、TextStampオブジェクトを使用する際にテキストの配置を指定する機能をサポートする必要がありました。この要件を満たすために、TextStampクラスにTextAlignmentプロパティを導入しました。このプロパティを使用することで、水平テキスト配置を指定できます。

次のコードスニペットは、既存のPDFドキュメントを読み込み、それにTextStampを追加する方法の例を示しています。

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // サンプル文字列でFormattedTextオブジェクトをインスタンス化
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // FormattedTextに新しいテキスト行を追加
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // FormattedTextを使用してTextStampオブジェクトを作成
    auto stamp = MakeObject<TextStamp>(text);
    // テキストスタンプの水平配置を中央揃えに指定
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // テキストスタンプの垂直配置を中央揃えに指定
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // TextStampのテキスト水平配置を中央揃えに指定
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // スタンプオブジェクトの上部余白を設定
    stamp->set_TopMargin(20);
    // PDFファイルのすべてのページにスタンプを追加
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // 出力ドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## PDFファイルにスタンプとして塗りつぶし輪郭テキストを追加する

テキストの追加と編集のシナリオに対してレンダリングモードを設定する機能を実装しました。輪郭テキストをレンダリングするには、TextStateオブジェクトを作成し、RenderingModeをTextRenderingMode.StrokeTextに設定し、さらにStrokingColorプロパティの色を選択します。その後、BindTextState()メソッドを使用してスタンプにTextStateをバインドします。

以下のコードスニペットは、塗りつぶし輪郭テキストを追加する方法を示しています。

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // 高度なプロパティを転送するためのTextStateオブジェクトを作成
    auto ts = MakeObject<TextState>();

    // 輪郭の色を設定
    ts->set_StrokingColor(Color::get_Gray());

    // テキストレンダリングモードを設定
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // 入力PDFドキュメントをロード
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // TextStateをバインド
    stamp->BindTextState(ts);

    // X,Y原点を設定
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // スタンプを追加
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```