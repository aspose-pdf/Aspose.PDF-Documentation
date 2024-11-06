---
title: C++を使用してPDFにテキストを追加する
linktitle: PDFにテキストを追加
type: docs
weight: 10
url: ja/cpp/add-text-to-pdf-file/
description: この記事では、Aspose.PDFでのテキスト操作のさまざまな側面について説明します。PDFにテキストを追加したり、HTMLフラグメントを追加したり、カスタムOTFフォントを使用する方法を学びます。
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## テキストの追加

既存のPDFファイルにテキストを追加するには:

1. Documentオブジェクトを使用して入力PDFを開きます。
2. テキストを追加したい特定のページを取得します。
3. 入力テキストと他のテキストプロパティと共にTextFragmentオブジェクトを作成します。特定のページから作成されたTextBuilderオブジェクトは、AppendTextメソッドを使用してTextFragmentオブジェクトをページに追加することができます。
4. DocumentオブジェクトのSaveメソッドを呼び出し、出力PDFファイルを保存します。

次のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");
    // String for output file name
    String outputFileName("AddingText_out.pdf");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // get particular page
    auto pdfPage = document->get_Pages()->idx_get(1);

    // create text fragment
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // set text properties
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## ストリームからフォントを読み込む

次のコードスニペットは、PDFドキュメントにテキストを追加するときにストリームオブジェクトからフォントを読み込む方法を示しています。

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // 入力PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // ドキュメントの最初のページ用のテキストビルダーオブジェクトを作成
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // サンプル文字列でテキストフラグメントを作成
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // TrueTypeフォントをストリームオブジェクトに読み込む
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // テキスト文字列のフォント名を設定
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // テキストフラグメントの位置を指定
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // PDFファイル上に配置できるようにテキストをTextBuilderに追加
        textBuilder->AppendText(textFragment);

        // 結果のPDFドキュメントを保存
        document->Save(_dataDir + outputFileName);
    }
}
```

## TextParagraphを使用してテキストを追加

次のコードスニペットは、[TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph)クラスを使用してPDFドキュメントにテキストを追加する方法を示しています。

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // Documentオブジェクトのページコレクションにページを追加
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // テキストパラグラフを作成
    auto paragraph = MakeObject<TextParagraph>();

    // 続く行のインデントを設定
    paragraph->set_SubsequentLinesIndent(20);

    // TextParagraphを追加する場所を指定
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // 単語の折り返しモードを指定
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // テキストフラグメントを作成
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // フラグメントをパラグラフに追加
    paragraph->AppendLine(fragment1);
    // パラグラフを追加
    builder->AppendParagraph(paragraph);

    // 結果のPDFドキュメントを保存
    document->Save(_dataDir + outputFileName);
}

```

## テキストセグメントにハイパーリンクを追加

PDFページは、1つ以上のTextFragmentオブジェクトで構成されることがあり、それぞれのTextFragmentオブジェクトは1つ以上のTextSegmentインスタンスを持つことができます。TextSegmentにハイパーリンクを設定するには、Aspose.Pdf.WebHyperlinkインスタンスのオブジェクトを提供しながら、[TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment)クラスのHyperlinkプロパティを使用できます。この要件を達成するには、以下のコードスニペットを試してください。

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // ドキュメントインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page1 = document->get_Pages()->Add();

    // TextFragmentインスタンスを作成
    auto tf = MakeObject<TextFragment>("Sample Text Fragment");
    // TextFragmentの水平配置を設定
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // サンプルテキストでテキストセグメントを作成
    auto segment = MakeObject<TextSegment>(" ... Text Segment 1...");
    // TextFragmentのセグメントコレクションにセグメントを追加
    tf->get_Segments()->Add(segment);

    // 新しいTextSegmentを作成
    segment = MakeObject<TextSegment>("Link to Google");
    // TextFragmentのセグメントコレクションにセグメントを追加

    tf->get_Segments()->Add(segment);

    // TextSegmentにハイパーリンクを設定
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // テキストセグメントの前景色を設定
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // テキストフォーマットをイタリックに設定
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // 別のTextSegmentオブジェクトを作成
    segment = MakeObject<TextSegment>(u"TextSegment without hyperlink");

    // TextFragmentのセグメントコレクションにセグメントを追加
    tf->get_Segments()->Add(segment);

    // ページオブジェクトの段落コレクションにTextFragmentを追加
    page1->get_Paragraphs()->Add(tf);

    // 結果のPDFドキュメントを保存
    document->Save(_dataDir + outputFileName);

}
```

## OTFフォントを使用する

Aspose.PDF for C++ は、PDFファイルの内容を作成/操作する際にカスタム/TrueTypeフォントを使用する機能を提供し、ファイル内容がデフォルトのシステムフォント以外で表示されるようにします。

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // 新しいドキュメントインスタンスを作成する
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加する
    auto page = document->get_Pages()->Add();

    // サンプルテキストでTextFragmentインスタンスを作成する
    auto fragment = MakeObject<TextFragment>("OTFフォントのサンプルテキスト");

    // または、システムディレクトリ内のOTFフォントのパスを指定することもできます
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // PDFファイル内にフォントを埋め込むよう指定し、適切に表示されるようにします。
    // 特定のフォントがターゲットマシンにインストールされていない場合でも
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // TextFragmentをページインスタンスの段落コレクションに追加する
    page->get_Paragraphs()->Add(fragment);
    // 結果として得られるPDFドキュメントを保存する。
    document->Save(_dataDir + outputFileName);
}
```

## DOMを使用してHTML文字列を追加する

Aspose.Pdf.Generator.TextクラスにはIsHtmlTagSupportedというプロパティがあり、これによりHTMLタグ/コンテンツをPDFファイルに追加することが可能です。追加されたコンテンツは、単なるテキスト文字列としてではなく、ネイティブHTMLタグとしてレンダリングされます。Aspose.Pdf名前空間の新しいドキュメントオブジェクトモデル（DOM）に同様の機能をサポートするために、HtmlFragmentクラスが導入されました。

[HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) インスタンスを使用して、PDFファイル内に配置するHTMLコンテンツを指定できます。TextFragmentと同様に、HtmlFragmentは段落レベルのオブジェクトであり、Pageオブジェクトの段落コレクションに追加できます。以下のコードスニペットは、DOMアプローチを使用してPDFファイル内にHTMLコンテンツを配置する手順を示しています。

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");

    // String for output file name
    String outputFileName("sample_html_out.pdf");

    // create Document instance
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Add a page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Instantiate HtmlFragment with HTML contents
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // set MarginInfo for margin details
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // Set margin information
    title->set_Margin(margin);

    // Add HTML Fragment to paragraphs collection of page
    page->get_Paragraphs()->Add(title);
    // Save PDF file
    document->Save(_dataDir + outputFileName);
}
```

以下のコードスニペットは、HTMLの順序付きリストをドキュメントに追加する手順を示しています：

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>();

    // 対応するHTMLフラグメントでHtmlFragmentオブジェクトをインスタンス化
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // ページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // ページ内にHtmlFragmentを追加
    page->get_Paragraphs()->Add(htmlFragment);

    // 結果のPDFファイルを保存
    document->Save(_dataDir + outputFileName);
}
```

TextStateオブジェクトを使用してHTML文字列のフォーマットを設定することもできます：

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("sample_html_out.pdf");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>();

    // ページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // HTMLコンテンツでHtmlFragmentをインスタンス化
    auto title = MakeObject<HtmlFragment>("<h1><strong>HTML String Demo</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // ページの段落コレクションにHTMLフラグメントを追加
    page->get_Paragraphs()->Add(title);
    // PDFファイルを保存
    document->Save(_dataDir + outputFileName);
}

```

ドキュメント内でいくつかのテキスト属性値をHTMLマークアップを通じて設定し、その後で同じ値をTextStateプロパティで提供した場合、それらはTextStateインスタンスのプロパティによってHTMLパラメータを上書きします。次のコードスニペットは、説明した動作を示しています。

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // 出力ファイル名用の文字列
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>();

    // ページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // HTMLコンテンツでHtmlFragmentをインスタンス化
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>表はテキストを含みます</i></b></p>");

    // フォントファミリーは 'Verdana' から 'Arial' にリセットされます
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // 下のマージン情報を設定
    title->get_Margin()->set_Bottom(10);
    // 上のマージン情報を設定
    title->get_Margin()->set_Top(400);
    // ページの段落コレクションにHTMLフラグメントを追加
    page->get_Paragraphs()->Add(title);
    // PDFファイルを保存
    document->Save(_dataDir + outputFileName);
}
```

## フットノートとエンドノート (DOM)

フットノートは、連続した上付き数字を使用して、論文のテキスト内の注釈を示します。実際の注釈はインデントされ、ページの下部にフットノートとして表示されることがあります。

### フットノートの追加

フットノート参照システムでは、参照を次のように示します：

- ソース資料に続く行の上に小さな数字を置きます。この数字はノート識別子と呼ばれ、テキスト行のやや上に配置されます。
- 同じ番号を、その後にソースの引用を付けて、ページの下部に置きます。フットノートは数値的かつ年代順であるべきです：最初の参照は1、2番目は2、というように続きます。

フットノートの利点は、読者が興味のある参照のソースを簡単にページを下に見て確認できることです。

次のステップに従ってください：

- [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) インスタンスを作成
- [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) オブジェクトを作成

- [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) オブジェクトを作成
- Noteインスタンスを作成し、その値をTextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219)プロパティに渡します
- TextFragmentをページインスタンスの段落コレクションに追加します

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名のための文字列
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Pagesコレクションにページを追加
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // TextFragmentインスタンスを作成
    auto text = MakeObject<TextFragment>("Hello World");
    // TextFragmentのFootNote値を設定
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page->get_Paragraphs()->Add(text);
    // 二つ目のTextFragmentを作成
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // 二つ目のテキストフラグメントのFootNoteを設定
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // 二つ目のテキストフラグメントをPDFファイルの段落コレクションに追加
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### フットノートのカスタムラインスタイル

次の例は、PDFページの下部にフットノートを追加し、カスタムラインスタイルを定義する方法を示しています。

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("customFootNote_Line.pdf");

    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFのページコレクションにページを追加
    auto page = document->get_Pages()->Add();
    
    // GraphInfoオブジェクトを作成
    auto graph = MakeObject<GraphInfo>();
    // 線幅を2に設定
    graph->set_LineWidth(2);
    // グラフオブジェクトの色を設定
    graph->set_Color(Color::get_Red());
    // 破線配列の値を3に設定
    graph->set_DashArray(MakeArray<int>(3));
    // 破線位相の値を1に設定
    graph->set_DashPhase(1);
    // ページのフットノートラインスタイルをグラフとして設定
    page->set_NoteLineStyle(graph);

    // TextFragmentインスタンスを作成
    auto text = MakeObject<TextFragment>("Hello World");
    // TextFragmentにフットノートの値を設定
    text->set_FootNote(MakeObject<Note>("テストテキスト1のフットノート"));
    // 文書の最初のページの段落コレクションにTextFragmentを追加
    page->get_Paragraphs()->Add(text);
    // 2番目のTextFragmentを作成
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // 2番目のテキストフラグメントにフットノートを設定
    text->set_FootNote(MakeObject<Note>("テストテキスト2のフットノート"));
    // PDFファイルの段落コレクションに2番目のテキストフラグメントを追加
    page->get_Paragraphs()->Add(text);
    // PDFファイルを保存
    document->Save(_dataDir + outputFileName);
}
```

以下のようにTextStateオブジェクトを使用して脚注ラベル（ノート識別子）のフォーマットを設定できます。

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("sample.pdf");

    // 出力ファイル名の文字列
    String outputFileName("sample_footnote.pdf");

    // Documentインスタンスを作成
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // TextFragmentインスタンスを作成
    auto text = MakeObject<TextFragment>("Hello World");
    // TextFragmentに対する脚注の値を設定
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page->get_Paragraphs()->Add(text);
    // 2番目のTextFragmentを作成
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // 2番目のテキストフラグメントに脚注を設定
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // 2番目のテキストフラグメントをPDFファイルの段落コレクションに追加
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### フットノートラベルのカスタマイズ

デフォルトでは、フットノート番号は1から始まる連番です。しかし、カスタムフットノートラベルを設定する必要がある場合があります。この要件を達成するために、次のコードスニペットを試してください。

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // 出力ファイル名の文字列    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // GraphInfoオブジェクトを作成
    auto graph = MakeObject<GraphInfo>();

    // 線幅を2に設定
    graph->set_LineWidth(2);

    // グラフオブジェクトの色を設定
    graph->set_Color(Color::get_Red());

    // ダッシュ配列値を3に設定
    graph->set_DashArray(MakeArray<int>(3));

    // ダッシュ位相値を1に設定
    graph->set_DashPhase(1);

    // ページのフットノート線スタイルをグラフに設定
    page->set_NoteLineStyle(graph);

    // TextFragmentインスタンスを作成
    auto text = MakeObject<TextFragment>("Hello World");
    // TextFragmentのフットノート値を設定
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // フットノートのカスタムラベルを指定
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## 画像と表を脚注に追加する

次のコードスニペットは、[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)オブジェクトに[Footnote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722)を追加し、次に画像と表オブジェクトを脚注セクションの段落コレクションに追加する手順を示しています。

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Documentインスタンスを作成
    auto document = new Document();
    // PDFのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // TextFragmentインスタンスを作成
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("footnote text");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Row 1 Cell 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## EndNotesの作成方法

EndNoteは、論文の最後にある特定の場所を読者に示し、論文で引用または言及された情報や言葉の出典を明らかにするための出典引用です。エンドノートを使用する場合、引用またはパラフレーズされた文や要約された材料の後に上付きの数字が続きます。

以下の例は、PDFページにEndNoteを追加する方法を示しています。

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名のための文字列
    String outputFileName("endNote_out.pdf");

    // Documentインスタンスを作成
    auto document = new Document();
    // PDFのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // TextFragmentインスタンスを作成
    auto text = MakeObject<TextFragment>("Hello World");

    // TextFragmentに対してEndNoteの値を設定
    text->set_EndNote(MakeObject<Note>("サンプルのエンドノート"));

    // FootNoteのカスタムラベルを指定
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // ドキュメントの最初のページの段落コレクションにTextFragmentを追加
    page->get_Paragraphs()->Add(text);
    // PDFファイルを保存
    document->Save(_dataDir + outputFileName);
}
```

## テキストと画像をインライン段落として

PDFファイルのデフォルトのレイアウトはフローレイアウト（左上から右下）です。したがって、PDFファイルに新しい要素が追加されるたびに、右下のフローに追加されます。ただし、画像とテキストなどのさまざまなページ要素を同じレベル（一つの後にもう一つ）で表示する必要がある場合があります。一つのアプローチとして、テーブルインスタンスを作成し、両方の要素を個々のセルオブジェクトに追加することができます。しかし、別のアプローチとしてインライン段落を使用することもできます。画像とテキストのIsInLineParagraphプロパティをtrueに設定することで、これらの段落は他のページ要素とインラインで表示されます。

次のコードスニペットは、PDFファイルにテキストと画像をインライン段落として追加する方法を示しています。

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Documentインスタンスをインスタンス化
    auto document = MakeObject<Document>();

    // Documentインスタンスのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // TextFragmentを作成
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // ページオブジェクトの段落コレクションにテキストフラグメントを追加
    page->get_Paragraphs()->Add(text);

    // 画像インスタンスを作成
    auto image = MakeObject<Image>();

    // 画像をインライン段落として設定し、前の段落オブジェクト（TextFragment）の直後に表示
    image->set_IsInLineParagraph(true);

    // 画像ファイルのパスを指定
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // 画像の高さを設定（オプション）
    image->set_FixHeight(30);
    // 画像の幅を設定（オプション）
    image->set_FixWidth(100);
    // ページオブジェクトの段落コレクションに画像を追加
    page->get_Paragraphs()->Add(image);
    // 異なる内容でTextFragmentオブジェクトを再初期化
    text = MakeObject<TextFragment>(" Hello Again..");
    // TextFragmentをインライン段落として設定
    text->set_IsInLineParagraph(true);
    // 新たに作成したTextFragmentをページの段落コレクションに追加
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## テキストを追加する際の文字間隔の指定

テキストは、TextFragment インスタンスまたは TextParagraph オブジェクトを使用して PDF の段落コレクションに追加することができます。また、TextStamp クラスを使用して PDF 内にテキストをスタンプすることもできます。テキストを追加する際には、テキストオブジェクトの文字間隔を指定する必要がある場合があります。この要件を満たすために、Property CharacterSpacing という新しいプロパティが導入されました。

この要件を満たすための次のアプローチを考慮してください。

以下のアプローチは、PDF ドキュメント内にテキストを追加する際に文字間隔を指定する手順を示しています。

### TextBuilder と TextFragment の使用

```cpp
// TextBuilder と TextFragment を使用してテキストを追加する際の文字間隔の指定
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Document インスタンスを作成
    auto document = MakeObject<Document>();
    // Document のページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // TextBuilder インスタンスを作成
    auto builder = MakeObject<TextBuilder>(page);

    // サンプル内容を持つテキストフラグメントインスタンスを作成
    auto wideFragment = MakeObject<TextFragment>("Text with increased character spacing");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // TextFragment の文字間隔を指定
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // TextFragment の位置を指定
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // TextBuilder インスタンスに TextFragment を追加
    builder->AppendText(wideFragment);

    // 結果の PDF ドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

### Using TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // ページをDocumentのページコレクションに追加
    auto page = document->get_Pages()->Add();

    // TextBuilderインスタンスを作成
    auto builder = MakeObject<TextBuilder>(page);

    // TextParagraphインスタンスを作成
    auto paragraph = MakeObject<TextParagraph>();

    // フォント名とサイズを指定するためにTextStateインスタンスを作成
    auto state = MakeObject<TextState>("Arial", 12);

    // 文字間隔を指定
    state->set_CharacterSpacing(1.5f);

    // テキストをTextParagraphオブジェクトに追加
    paragraph->AppendLine(u"This is paragraph with character spacing", state);

    // TextParagraphの位置を指定
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // TextParagraphをTextBuilderインスタンスに追加
    builder->AppendParagraph(paragraph);

    // 結果のPDFドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

### テキストスタンプの使用

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // Documentのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // サンプルテキストでTextStampインスタンスを作成
    auto stamp = MakeObject<TextStamp>("これは文字間隔を設定したテキストスタンプです");

    // Stampオブジェクトのフォント名を指定
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // TextStampのフォントサイズを指定
    stamp->get_TextState()->set_FontSize(12);
    // 文字間隔を1fとして指定
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // スタンプのXインデントを設定
    stamp->set_XIndent(100);
    // スタンプのYインデントを設定
    stamp->set_YIndent(500);
    // ページインスタンスにテキストスタンプを追加
    stamp->Put(page);
    // 結果として得られるPDFドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## マルチカラムPDFドキュメントを作成する

このトピックでは、Aspose.Pdf for C++を使用してマルチカラムのPDFを作成する方法を示します。

今日では、本の中で段落が左から右に印刷されているのではなく、別々のページに複数のカラムで表示されるニュースをよく目にします。Microsoft WordやAdobe Acrobat Writerなどの多くの文書処理アプリケーションでは、ユーザーが単一のページに複数のカラムを作成し、それにデータを追加することができます。

Aspose.Pdf for C++もまた、PDFドキュメントページに複数のカラムを作成する機能を提供します。複数のカラムを持つPDFを作成するには、[Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box)クラスを使用できます。このクラスはFloatingBox内のカラム数を指定するColumnInfo.ColumnCountプロパティを提供しており、ColumnInfo.ColumnSpacingとColumnInfo.ColumnWidthsを使用してカラム間隔とカラム幅を指定することもできます。

以下に、Graphオブジェクト（Line）を使用して2つのカラムを作成し、それらをFloatingBoxの段落コレクションに追加し、さらにPageインスタンスの段落コレクションに追加する例を示します。

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // 新しいドキュメントインスタンスを作成する
    auto document = MakeObject<Document>();

    // PDFファイルの左マージン情報を指定する
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // PDFファイルの右マージン情報を指定する
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // ページをPDFファイルのページコレクションに追加する
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // セクションオブジェクトの段落コレクションに線を追加する
    page->get_Paragraphs()->Add(graph1);

    // 線の座標を指定する
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // HTMLタグを含むテキストで文字列変数を作成する
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> 金銭詐欺を避ける方法</<strong> </span>");

    // HTMLテキストを含むテキスト段落を作成する

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // セクションに4つの列を追加する
    box->get_ColumnInfo()->set_ColumnCount(2);
    // 列間のスペースを設定する
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("By A Googler (The Official Google Blog)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // 線を描画するためのグラフオブジェクトを作成する
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // 線の座標を指定する
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // セクションオブジェクトの段落コレクションに線を追加する
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // PDFファイルを保存する
    document->Save(_dataDir + outputFileName);
}
```

## カスタムタブストップの操作

タブストップは、タブの停止点です。ワードプロセッシングでは、各行に一定間隔で配置された複数のタブストップが含まれています（例えば、半インチごと）。ただし、ほとんどのワードプロセッサではタブストップを自由に設定できるため、変更することができます。Tabキーを押すと、カーソルまたは挿入ポイントが次のタブストップまで移動しますが、それ自体は見えません。タブストップはテキストファイル内に存在しませんが、ワードプロセッサはそれらを追跡して、Tabキーに正しく反応できるようにします。

ここでは、カスタムTABストップを設定する方法の例を示します。

## PDFに透明なテキストを追加する方法

PDF 1.4（Acrobat 5でサポートされているファイル形式）は、透明性をサポートする最初のPDFバージョンでした。このPDFは、Adobe Illustrator 9とほぼ同時期に市場に出ました。

PDFファイルには、画像、テキスト、グラフ、添付ファイル、注釈オブジェクトが含まれており、TextFragmentを作成する際に、前景色、背景色情報、およびテキストの書式設定を設定できます。Aspose.PDF for C++は、アルファカラーチャネルを使用してテキストを追加する機能をサポートしています。以下のコードスニペットは、透明な色でテキストを追加する方法を示しています。

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // Create Document instance
    auto document = MakeObject<Document>();    
    // Create page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Create Graph object
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // Create rectangle instance with certain dimensions
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // Create color object from Alpha color channel
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Add rectanlge to shapes collection of Graph object
    canvas->get_Shapes()->Add(rect);

    // Add graph object to paragraphs collection of page object
    page->get_Paragraphs()->Add(canvas);

    // Set value to not change position for graph object
    canvas->set_IsChangePosition(false);

    // Create TextFragment instance with sample value
    auto text = MakeObject<TextFragment>(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
    // Create color object from Alpha channel
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // Set color information for text instance
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // Add text to paragraphs collection of page instance
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## フォントの行間を指定する

[Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) クラスには、特定のフォント、例えば入力フォント "HPSimplified.ttf" に対して設計された列挙型 [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91) があります。また、クラス [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) には、LineSpacingMode の型のプロパティ [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf) があります。LineSpacing を LineSpacingMode.FullSize に設定するだけです。フォントを正しく表示するためのコードスニペットは次のようになります:

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // 入力PDFファイルを読み込む
    auto document = MakeObject<Document>();
    
    // LineSpacingMode.FullSizeを使用してTextFormattingOptionsを作成
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // サンプル文字列でテキストフラグメントを作成
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // TrueTypeフォントをストリームオブジェクトに読み込む
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // テキスト文字列のフォント名を設定
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // テキストフラグメントの位置を指定
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // 現在のフラグメントのTextFormattingOptionsを事前に定義されたものに設定（LineSpacingMode.FullSizeを指す）
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // テキストをPDFファイル上に配置するためにTextBuilderに追加    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // 結果のPDFドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## テキスト幅を動的に取得する

[Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) クラスは、PDFドキュメント内でテキスト幅を動的に取得する方法を示します。

場合によっては、テキスト幅を動的に取得する必要があります。Aspose.PDF for C++ には、文字列の幅を測定するための2つのメソッドが含まれています。[MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) メソッドを Aspose.Pdf.Text.Font または Aspose.Pdf.Text.TextState クラス（またはその両方）から呼び出すことができます。以下のコードスニペットは、この機能を使用する方法を示しています。

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"Font and state string measuring doesn't match!");
    }
}
```