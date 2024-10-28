---
title: C++を使用した演算子の操作
linktitle: 演算子の操作
type: docs
weight: 170
url: /cpp/operators/
description: このトピックでは、C++でAspose.PDFを使用して演算子をどのように使用するかを説明します。演算子クラスはPDF操作のための優れた機能を提供します。
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF演算子とその使用法の紹介

演算子は、ページ上にグラフィカルな形を描くなど、実行されるべきアクションを指定するPDFキーワードです。演算子キーワードは、名前付きオブジェクトとの区別として初期のスラッシュ文字（2Fh）がないことによって識別されます。演算子はコンテンツストリーム内でのみ意味があります。

コンテンツストリームは、ページ上に描画されるグラフィカル要素を説明する命令で構成されるPDFストリームオブジェクトです。PDF演算子の詳細については、[PDF仕様](https://opensource.adobe.com/dc-acrobat-sdk-docs/)をご覧ください。

### 実装の詳細

このトピックでは、Aspose.PDFを使用して演算子をどのように使用するかを説明します。 選択された例では、概念を説明するために画像をPDFファイルに追加します。PDFファイルに画像を追加するには、さまざまなオペレーターが必要です。この例では、[GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save)、[ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix)、[Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do)、および[GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore)を使用します。

- **GSave** オペレーターはPDFの現在のグラフィカル状態を保存します。
- **ConcatenateMatrix** （行列の連結）オペレーターは、画像をPDFページにどのように配置するかを定義するために使用されます。
- **Do** オペレーターはページに画像を描画します。
- **GRestore** オペレーターはグラフィカル状態を復元します。

PDFファイルに画像を追加するには：

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) オブジェクトを作成し、入力PDFドキュメントを開きます。 特定のページを取得し、画像を追加します。
1. ページのリソースコレクションに画像を追加します。
1. オペレーターを使用してページに画像を配置します:
   - まず、GSaveオペレーターを使用して現在のグラフィカル状態を保存します。
   - 次に、ConcatenateMatrixオペレーターを使用して画像を配置する場所を指定します。
   - Doオペレーターを使用してページに画像を描画します。
1. 最後に、GRestoreオペレーターを使用して更新されたグラフィカル状態を保存します。

以下のコードスニペットはPDFオペレーターの使用方法を示しています。

```cpp
void ExampleUsingOperators()
{
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // 座標を設定
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // 画像を追加するページを取得
    auto page = document->get_Pages()->idx_get(1);

    // ストリームに画像をロード
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // ページリソースの画像コレクションに画像を追加
    page->get_Resources()->get_Images()->Add(imageStream);

    // GSaveオペレーターを使用: このオペレーターは現在のグラフィックス状態を保存します
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Rectangle と Matrix オブジェクトを作成
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // ConcatenateMatrix（マトリックスを連結）オペレーターを使用: 画像の配置方法を定義
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // Doオペレーターを使用: このオペレーターは画像を描画します
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // GRestoreオペレーターを使用: このオペレーターはグラフィックス状態を復元します
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```
## ページにXFormを描画するための演算子の使用

このトピックでは、GSave/GRestore演算子、xFormを位置指定するためのContatenateMatrix演算子、およびページにxFormを描画するためのDo演算子の使用方法を示します。

以下のコードは、PDFファイルの既存の内容をGSave/GRestore演算子ペアでラップします。このアプローチは、既存の内容の最後に初期グラフィックス状態を取得するのに役立ちます。このアプローチがなければ、既存の演算子チェーンの最後に望ましくない変換が残る可能性があります。

```cpp
void DrawXFormOnPageUsingOperators() {
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // サンプルは以下を示します
    // GSave/GRestore演算子の使用
    // xFormを位置指定するためのContatenateMatrix演算子の使用
    // ページにxFormを描画するためのDo演算子の使用

    // 既存の内容をGSave/GRestore演算子ペアでラップする
    //        これは既存の内容の最後に初期グラフィックス状態を取得するため
    //        さもなければ、既存の演算子チェーンの最後に望ましくない変換が残るかもしれません
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // 新しいコマンドの後にグラフィックス状態を正しくクリアするためにグラフィックス状態演算子を保存する
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // xFormを作成

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // 画像の幅と高さを定義
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // 画像をストリームにロード
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // XFormリソースのImagesコレクションに画像を追加
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // Do演算子を使用: この演算子は画像を描画する
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // x=100 y=500の座標にフォームを配置
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // Do演算子でフォームを描画
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // x=100 y=300の座標にフォームを配置
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // Do演算子でフォームを描画
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // GSaveの後にGRestoreでグラフィックス状態を復元
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## 演算子クラスを使用してグラフィックオブジェクトを削除する

演算子クラスはPDF操作に優れた機能を提供します。PDFファイルに含まれるグラフィックが[PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor)クラスの[DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380)メソッドを使用して削除できない場合、演算子クラスを使用してそれらを削除することができます。

以下のコードスニペットは、グラフィックを削除する方法を示しています。PDFファイルにグラフィックのテキストラベルが含まれている場合、このアプローチを使用するとそれらはPDFファイルに残る可能性があることに注意してください。そのため、そのような画像を削除する代替方法を探すためにグラフィック演算子を検索してください。

```cpp
void RemoveGraphicsObjects() {
    // ドキュメントを開く
    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // 使用されたパス描画演算子
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```