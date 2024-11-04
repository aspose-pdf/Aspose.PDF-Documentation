---
title: PDFドキュメントを操作する
linktitle: PDFドキュメントを操作する
type: docs
weight: 30
url: /cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: このセクションでは、PDF A標準に対するPDFドキュメントの検証、目次の操作、PDFの有効期限の設定、PDFファイル生成の進行状況の確認方法について説明します。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF A標準（A 1AおよびA 1B）のためのPDFドキュメントを検証する

PDF/A-1aまたはPDF/A-1bの互換性を検証するには、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスの[Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c)メソッドを使用します。このメソッドを使用すると、結果を保存するファイルの名前と必要な検証タイプ[PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763)列挙：PDF_A_1AまたはPDF_A_1Bを指定できます。

{{% alert color="primary" %}}

出力XML形式はカスタムAspose形式です。XMLにはProblemという名前のタグのコレクションが含まれており、それぞれのタグには特定の問題の詳細が含まれています。ProblemタグのObjectID属性は、この問題が関連する特定のオブジェクトのIDを表します。Clause属性はPDF仕様の対応するルールを表します。

{{% /alert %}}

次のコードスニペットは、PDF/A-1Aに対してPDFドキュメントを検証する方法を示します。

```cpp
void ExampleValidate01() {
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列。
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // PDF/A-1aに対してPDFを検証
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

次のコードスニペットは、PDF/A-1Bに対してPDFドキュメントを検証する方法を示します。

```cpp
void ExampleValidate02() {
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列。
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // PDF/A-1aに対してPDFを検証
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## TOCを使用する

### 既存のPDFにTOCを追加する

Aspose.PDF APIを使用すると、PDFを作成するとき、または既存のファイルに目次を追加することができます。

既存のPDFファイルにTOCを追加するには、Aspose.Pdf名前空間の[Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading)クラスを使用します。Aspose.Pdf名前空間を使用すると、新しいPDFファイルを作成したり、既存のPDFファイルを操作したりすることができます。既存のPDFにTOCを追加するには、Aspose.Pdf名前空間を使用してください。

次のコードスニペットは、既存のPDFファイル内に目次を作成する方法を示しています。

```cpp
void ExampleToc01() {
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // PDFファイルの最初のページにアクセス
    auto tocPage = document->get_Pages()->Insert(1);

    // TOC情報を表すオブジェクトを作成
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // TOCのタイトルを設定
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // TOC要素として使用される文字列オブジェクトを作成
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"First page", 0);
    titles->SetValue(u"Second page", 1);
    titles->SetValue(u"Third page", 2);
    titles->SetValue(u"Fourth page", 3);

    for (int i = 0; i < 2; i++)
    {
        // Headingオブジェクトを作成
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // Headingオブジェクトの宛先ページを指定

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // 宛先ページ
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // 宛先座標
        segment2->set_Text(titles[i]);

        // TOCを含むページに見出しを追加
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // 更新されたドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

### 異なるTOCレベルに異なるTabLeaderTypeを設定

Aspose.PDF for C++は、異なるTOCレベルに異なるTabLeaderTypeを設定することも可能です。FormatArrayのLineDashプロパティに適切なTabLeaderTypeの値を設定する必要があります。次に、PDFドキュメントのセクションのコレクションにリストセクションを追加します。その後、PDFドキュメントにセクションを作成し、PDFファイルを保存します。

```cpp
void ExampleToc02() {
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名の文字列。
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    // LeaderTypeを設定
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // TOC情報を表すオブジェクトを作成
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("目次");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // TOCのタイトルを設定
    tocInfo->set_Title(title);

    // リストセクションをPdfドキュメントのセクションコレクションに追加
    tocPage->set_TocInfo(tocInfo);

    // 左マージンを設定することによって4レベルリストのフォーマットを定義
    // および各レベルのテキストフォーマット設定

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Pdfドキュメントにセクションを作成
    auto page = document->get_Pages()->Add();

    // セクションに4つの見出しを追加
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"サンプル見出し" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    // 目次に見出しを追加。
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // Pdfを保存
    document->Save(_dataDir + outputFileName);
}
```

### TOCでページ番号を非表示にする

目次でタイトルと一緒にページ番号を非表示にしたい場合は、[TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) クラスの [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) プロパティを false に設定します。

以下のコードスニペットを確認して、目次でページ番号を非表示にする方法を確認してください:

```cpp
void ExampleToc03() {
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名の文字列。
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // 目次情報を表すオブジェクトを作成
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // TOCのタイトルを設定
    tocInfo->set_Title(title);

    // Pdfドキュメントのセクションコレクションにリストセクションを追加
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    // 左のマージンと各レベルのテキスト形式の設定を行うことで、4レベルリストのフォーマットを定義

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    // セクションに4つの見出しを追加
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"this is heading of level " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // Pdfを保存
    document->Save(_dataDir + outputFileName);
}
```

## PDFの有効期限を設定する方法

PDFファイルにアクセス権を適用して、特定のユーザーグループがPDFドキュメントの特定の機能/オブジェクトにアクセスできるようにします。PDFファイルのアクセスを制限するために、通常は暗号化を適用し、PDFファイルの有効期限を設定する必要がある場合があります。これにより、ドキュメントにアクセス/表示しているユーザーにPDFファイルの有効期限に関する有効なプロンプトが表示されます。

上記の要件を達成するために、[JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/)オブジェクトを使用できます。以下のコードスニペットを確認してください。

```cpp
void SetPDFexpiryDate() {

    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列。
    String outputFileName("SetExpiryDate_out.pdf");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    document->get_Pages()->Add();

    // ページオブジェクトの段落コレクションにテキストフラグメントを追加
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // PDFの有効期限を設定するためにJavaScriptオブジェクトを作成
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // JavaScriptをPDFのオープンアクションとして設定
    document->set_OpenAction(javaScript);

    // PDFドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## PDFファイル生成の進捗を判定する

顧客から、開発者がPDFファイル生成の進捗を判定できる機能を追加してほしいとの依頼がありました。そのリクエストに対する回答がこちらです。

[DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options)クラスの[CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb)フィールドを使用すると、PDF生成の進捗を判定することができます。

以下のコードスニペットは、[CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb)を使用する方法を示しています。

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Event type: {0}, Value: {1}, MaxValue: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列。
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // ドキュメントを開く
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## C++で入力可能なPDFをフラット化する

PDF ドキュメントには、多くの場合、ラジオボタン、チェックボックス、テキストボックス、リストなどのインタラクティブな入力可能なウィジェットを含むフォームが含まれています。さまざまなアプリケーション目的で編集できないようにするために、PDFファイルをフラット化する必要があります。 Aspose.PDF for C++ は、わずか数行のコードで C++ で PDF をフラット化する機能を提供します。

```cpp
void FlattenFillablePDF() {
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");
    // ファイル名のための文字列。
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 入力可能なPDFをフラット化する
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // 更新されたドキュメントを保存する
    document->Save(_dataDir + outputFileName);
}
```