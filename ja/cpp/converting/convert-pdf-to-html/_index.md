---
title: PDFファイルをHTML形式に変換
linktitle: PDFファイルをHTML形式に変換
type: docs
weight: 50
url: ja/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFを使用してC++ライブラリでPDFファイルをHTML形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** は、さまざまなファイル形式をPDFドキュメントに変換したり、PDFファイルをさまざまな出力形式に変換したりするための多くの機能を提供します。この記事では、PDFファイルを<abbr title="HyperText Markup Language">HTML</abbr>に変換する方法について説明します。Aspose.PDF for C++は、InLineHtmlアプローチを使用してHTMLファイルをPDF形式に変換する機能を提供します。PDFファイルをHTML形式に変換する機能を求める多くのリクエストがあり、この機能を提供しました。この機能はXHTML 1.0もサポートしていることに注意してください。

**Aspose.PDF for C++** は、PDFファイルをHTMLに変換する機能をサポートしています。 Aspose.PDFライブラリで実行できる主なタスクは次のとおりです：

- PDFをHTMLに変換する;
- 出力を複数ページのHTMLに分割する;
- SVGファイルを保存するフォルダーを指定する;
- 変換中にSVG画像を圧縮する;
- 画像フォルダーを指定する;
- 本文コンテンツのみの続きファイルを作成する;
- 透明テキストのレンダリング;
- PDFドキュメントレイヤーのレンダリング。

Aspose.PDF for C++は、ソースPDFファイルをHTMLに変換するための2行のコードを提供します。`SaveFormat列挙`にはHtmlという値が含まれており、これによりソースファイルをHTMLに保存できます。次のコードスニペットは、PDFファイルをHTMLに変換するプロセスを示しています。

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名用の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名用の文字列
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // 出力をHTML形式で保存する
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**PDFをHTMLにオンラインで変換してみる**

Aspose.PDF for C++は、オンライン無料アプリケーション「[PDF to HTML](https://products.aspose.app/pdf/conversion/pdf-to-html)」を提供しており、その機能性と品質を試すことができます。

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## 出力をマルチページHTMLに分割する

複数ページを含む大きなPDFファイルをHTML形式に変換する際、出力は単一のHTMLページとして表示されます。非常に長くなることがあります。ページサイズを制御するために、PDFからHTMLへの変換中に出力を複数のページに分割することが可能です。以下のコードスニペットを使用してみてください。

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名用の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名用の文字列
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML保存オプションオブジェクトをインスタンス化
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // 出力を複数のページに分割するように指定
    htmlOptions->set_SplitIntoPages(true);

    try {
    // 出力をHTML形式で保存
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## SVGファイルを保存するフォルダーを指定

PDFからHTMLへの変換中に、SVG画像を保存するフォルダーを指定することが可能です。[`HtmlSaveOptionクラス`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options)の[`SpecialFolderForSvgImagesプロパティ`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f)を使用して、特定のSVG画像ディレクトリを指定します。このプロパティは、変換中に遭遇したSVG画像を保存するディレクトリへのパスを取得または設定します。このパラメーターが空またはnullの場合、SVGファイルは他の画像ファイルと一緒に保存されます。

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML保存オプションオブジェクトをインスタンス化
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // PDFからHTMLへの変換中にSVG画像が保存されるフォルダーを指定
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // 出力をHTML形式で保存
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFからHTMLへの変換中にSVG画像を圧縮

PDFからHTMLへの変換中にSVG画像を圧縮するには、次のコードを試してください:

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名のための文字列
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML保存オプションオブジェクトをインスタンス化する
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // PDFからHTMLへの変換中にSVG画像が保存されるフォルダを指定する
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // HTML形式で出力を保存する
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 画像フォルダの指定

PDFからHTMLへの変換中に画像が保存されるフォルダも指定できます:

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": 開始" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名のための文字列
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML保存オプションオブジェクトをインスタンス化
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // PDFからHTMLへの変換中にすべての画像が保存されるフォルダを指定
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // 出力をHTML形式で保存
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": 終了" << std::endl;
}
```

## Create Subsequent Files with Body Contents Only

最近、PDFファイルをHTMLに変換し、ユーザーが各ページの`<body>`タグの内容のみを取得できる機能を導入するよう依頼されました。 このコードは、CSS、`<html>`, `<head>` の詳細を含む1つのファイルと、他のファイルに `<body>` の内容だけを含むすべてのページを生成します。

この要件を満たすために、新しいプロパティ HtmlMarkupGenerationMode が [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) クラスに導入されました。

以下の単純なコードスニペットを使用すると、出力HTMLをページごとに分割できます。出力ページでは、すべてのHTMLオブジェクトが現在の位置に正確に配置される必要があります（フォントの処理と出力、CSSの作成と出力、画像の作成と出力）が、出力HTMLは現在タグ内に配置されている内容を含むことになります（現在の「body」タグは省略されます）。ただし、このアプローチを使用する場合、CSSへのリンクはコードの責任になります。これはのようなものが削除されるためです。この目的のために、CSSを File.ReadAllText() で読み取り、AJAXを介してWebページに送信し、jQueryによって適用されるようにすることができます。

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名用の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名用の文字列
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML保存オプションオブジェクトをインスタンス化
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // 出力をHTML形式で保存
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## 透明なテキストのレンダリング

ソース/入力PDFファイルに前景画像によって影がつけられた透明なテキストが含まれている場合、テキストのレンダリングに問題が生じる可能性があります。そのようなシナリオに対応するために、[SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) と SaveTransparentTexts プロパティを使用できます。

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML保存オプションオブジェクトをインスタンス化
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // 出力をHTML形式で保存
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFドキュメントのレイヤー描画

PDFからHTMLへの変換中に、PDFドキュメントのレイヤーを別々のレイヤータイプ要素でレンダリングできます:

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名のための文字列
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // HTML保存オプションオブジェクトをインスタンス化
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // 出力HTMLでPDFドキュメントのレイヤーを別々にレンダリングするように指定
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // HTML形式で出力を保存
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```