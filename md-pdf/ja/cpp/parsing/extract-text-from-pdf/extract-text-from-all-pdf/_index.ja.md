---
title: C++を使用してすべてのPDFページからテキストを抽出する
linktitle: PDFからテキストを抽出する
type: docs
weight: 10
url: /cpp/extract-text-from-all-pdf/
description: この記事では、Aspose.PDFを使用してC++でPDFドキュメントからテキストを抽出するさまざまな方法について説明します。全ページから、特定の部分から、列に基づいてなど。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントのすべてのページからテキストを抽出する

PDFドキュメントからテキストを抽出することは一般的な要件です。 In this example, you’ll see how Aspose.PDF for C++ allows extracting text from all the pages of a PDF document. You need to create an object of the [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) class. After that, open the PDF using [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class and call the 'Accept' method of the [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)collection. The  [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) class absorbs the text from the document and returns in 'Text' property. The following code snippet shows you how to extract text from all pages of PDF document.

この例では、Aspose.PDF for C++ が PDF ドキュメントのすべてのページからテキストを抽出する方法を示します。[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) クラスのオブジェクトを作成する必要があります。その後、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスを使用して PDF を開き、[Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) コレクションの 'Accept' メソッドを呼び出します。[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) クラスはドキュメントからテキストを吸収し、'Text' プロパティで返します。次のコードスニペットは、PDF ドキュメントのすべてのページからテキストを抽出する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Create TextAbsorber object to extract text
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Accept the absorber for all the pages
    document->get_Pages()->Accept(textAbsorber);
    // Get the extracted text
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
特定のページのドキュメントオブジェクトで**Accept**メソッドを呼び出します。Indexは、テキストを抽出する必要がある特定のページ番号です。

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名の文字列
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // テキストを抽出するためのTextAbsorberオブジェクトを作成
    auto textAbsorber = MakeObject<TextAbsorber>();
    // 全ページに対してアブソーバーを受け入れる
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // 抽出されたテキストを取得
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## テキストデバイスを使用してページからテキストを抽出する

[TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/)クラスを使用して、PDFファイルからテキストを抽出できます。TextDeviceはその実装においてTextAbsorberを使用しています。したがって、実際には同じことをしていますが、TextDeviceはページから何かを抽出するための「デバイス」アプローチを統一するために実装されています。ImageDevice、PageDeviceなど。 TextAbsorberは、ページ、PDF全体、またはXFormからテキストを抽出することができ、このTextAbsorberはより汎用的です。

### すべてのページからテキストを抽出する

以下の手順とコードスニペットは、テキストデバイスを使用してPDFからテキストを抽出する方法を示しています。

1. 指定された入力PDFファイルでDocumentクラスのオブジェクトを作成する
1. TextDeviceクラスのオブジェクトを作成する
1. 抽出オプションを指定するためにTextExtractOptionsクラスのオブジェクトを使用する
1. TextDeviceクラスのProcessメソッドを使用して内容をテキストに変換する
1. テキストを出力ファイルに保存する

```cpp
void ExtractTextUsingTextDevice() {

    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名のための文字列
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto builder = MakeObject<System::Text::StringBuilder>();
    // 抽出されたテキストを保持するための文字列
    String extractedText;

    for (auto page : document->get_Pages()) {
        auto textStream = MakeObject<System::IO::MemoryStream>();
        // テキストデバイスを作成
        auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

        // テキスト抽出オプションを設定 - テキスト抽出モードを設定（RawまたはPure）
        auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

        textDevice->set_ExtractionOptions(textExtOptions);

        // 特定のページを変換し、テキストをストリームに保存
        textDevice->Process(page, textStream);

        // メモリストリームを閉じる
        textStream->Close();

        // メモリストリームからテキストを取得
        extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
        builder->Append(extractedText);

    }
    // 抽出されたテキストをテキストファイルに保存
    System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## 特定のページ領域からテキストを抽出する

[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) クラスは、PDFドキュメントの特定のページまたはすべてのページからテキストを抽出する機能を提供します。このクラスは抽出されたテキストを 'Text' プロパティで返します。しかし、特定のページ領域からテキストを抽出する必要がある場合は、[TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) の **Rectangle** プロパティを使用することができます。Rectangle プロパティは Rectangle オブジェクトを値として受け取り、このプロパティを使用して、テキストを抽出する必要があるページの領域を指定できます。

テキストを抽出するためにページの **Accept** メソッドが呼び出されます。 オブジェクトを作成します [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) および [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) クラス。個々のページ、**Page** インデックスとしての [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) オブジェクトで 'Accept' メソッドを呼び出します。**Index** はテキストを抽出する必要がある特定のページ番号です。 [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) クラスの 'Text' プロパティからテキストを取得できます。次のコードスニペットは、個々のページからテキストを抽出する方法を示しています。

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名のための文字列
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // テキストを抽出するための TextAbsorber オブジェクトを作成
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // すべてのページに対してアブソーバーを受け入れる
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // 抽出されたテキストを取得
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## 列に基づいてテキストを抽出する

PDFは非常に人気のあるフォーマットです。そしてその理由もあります。PDFを使用すると、異なるコンピューターで文書が同じように表示され、印刷されることをほぼ確実にすることができます。

しかし、PDF文書には通常、段落、表、図、ヘッダー/フッター情報などの内容が何であるかについての情報が欠けているという欠点があります。

Aspose.PDf for C++ - これは、列に基づいてテキストを抽出することを可能にする、使いやすいユーティリティです。

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名のための文字列
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // テキストを抽出するためのTextAbsorberオブジェクトを作成
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // 全ページに対してアブソーバーを適用
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // フォントサイズを少なくとも70％に減らす必要があります
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### 第二のアプローチ - ScaleFactorを使用

この新しいリリースでは、TextAbsorberおよび内部のテキストフォーマットメカニズムにいくつかの改善を導入しました。したがって、‘Pure’モードを使用してテキストを抽出する際に、[ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a)オプションを指定することができ、これは上記のアプローチに加えて、マルチカラムのPDFドキュメントからテキストを抽出する別のアプローチとなります。このスケールファクターは、テキスト抽出中の内部テキストフォーマットメカニズムに使用されるグリッドを調整するために設定できます。ScaleFactorの値を1から0.1（0.1を含む）の間に指定すると、フォント縮小と同じ効果があります。

ScaleFactorの値を0.1から-0.1の間に指定すると、ゼロ値として扱われますが、テキストを抽出する際に必要なスケールファクターを自動的に計算するためのアルゴリズムを機能させます。 ドキュメントのテキストはページ上で最も人気のあるフォントの平均グリフ幅に基づいて計算されますが、抽出されたテキストでは列の開始点が次の列の開始点に達しないことを保証できません。ScaleFactor値が指定されていない場合、デフォルト値の1.0が使用されることに注意してください。これはスケーリングが実行されないことを意味します。指定されたScaleFactor値が10より大きいか-0.1未満の場合、デフォルト値の1.0が使用されます。

大量のPDFファイルを処理してテキストコンテンツを抽出する際には、オートスケーリング（ScaleFactor = 0）の使用を提案します。もしくはグリッド幅の冗長な削減を手動で設定します（ScaleFactor = 0.5程度）。ただし、具体的なドキュメントに対してスケーリングが必要かどうかを判断してはいけません。ドキュメントに対してグリッド幅の冗長な削減を設定した場合（必要がない場合でも）、抽出されたテキストコンテンツは完全に適切なままです。以下のコードスニペットをご覧ください。
## PDFドキュメントからハイライトされたテキストを抽出する

PDFドキュメントからテキストを抽出するさまざまなシナリオで、PDFドキュメントからハイライトされたテキストのみを抽出する必要が生じることがあります。この機能を実装するために、APIにTextMarkupAnnotation.GetMarkedText()およびTextMarkupAnnotation.GetMarkedTextFragments()メソッドを追加しました。TextMarkupAnnotationをフィルタリングし、前述のメソッドを使用して、PDFドキュメントからハイライトされたテキストを抽出することができます。次のコードスニペットは、PDFドキュメントからハイライトされたテキストを抽出する方法を示しています。

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名の文字列
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // すべての注釈をループする
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // TextMarkupAnnotationをフィルタリングする
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // ハイライトされたテキストフラグメントを取得する
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // ハイライトされたテキストを表示する
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## XMLからテキストフラグメントとセグメント要素にアクセスする

時々、XMLから生成されたPDFドキュメントを処理する際に、TextFragmentやTextSegmentアイテムにアクセスする必要があります。Aspose.PDF for C++は名前でそのようなアイテムにアクセスすることを提供します。以下のコードスニペットは、この機能を使用する方法を示しています。

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Parsing\\");

    // ファイル名のための文字列
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // ページに対していくつかの操作を行う
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // セグメントに対していくつかの操作を行う
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```