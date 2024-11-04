---
title: PDFでのテキスト置換をC++で行う
linktitle: PDFでのテキスト置換
type: docs
weight: 40
url: /cpp/replace-text-in-pdf/
description: PDFからテキストを置換および削除するさまざまな方法について学びます。Aspose.PDFは特定の領域や正規表現でテキストを置換することができます。
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDFドキュメント内のテキストを修正または置換する必要がある場合があります。それを手動で行おうとすると骨の折れる作業になりますので、その問題の解決策をここに示します。

正直なところ、PDFファイルを編集することは簡単な作業ではありません。PDFファイルを編集する際に、ある単語を別の単語に置き換える必要がある状況は非常に困難であり、それを行うのに長い時間がかかります。さらに、フォーマットやフォントの破損など、出力に多くの問題が発生する可能性があります。PDFファイル内のテキストを簡単に検索して置換したい場合は、Aspose.Pdfライブラリソフトウェアを使用することをお勧めします。これにより、数分で作業が完了します。

この記事では、Aspose.PDF for C++を使用してPDFファイル内のテキストを正常に検索し、置換する方法を紹介します。

## PDFドキュメントの全ページでテキストを置換する

{{% alert color="primary" %}}

Aspose.PDFを使用してドキュメント内のテキストを置換し、この[リンク](https://products.aspose.app/pdf/redaction)でオンラインで結果を得ることができます。

{{% /alert %}}

PDFドキュメントの全ページでテキストを置換するには、まずTextFragmentAbsorberを使用して置換したい特定のフレーズを見つける必要があります。その後、すべてのTextFragmentを通過してテキストを置換し、他の属性を変更する必要があります。その作業が完了したら、DocumentオブジェクトのSaveメソッドを使用して出力PDFを保存するだけです。以下のコードスニペットは、PDFドキュメントの全ページでテキストを置換する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 入力された検索フレーズのすべてのインスタンスを見つけるためにTextFragmentAbsorberオブジェクトを作成
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // ドキュメントの最初のページに対してアブソーバーを適用
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 抽出されたテキストフラグメントをコレクションに取得
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // フラグメントをループ
    for (auto textFragment : textFragmentCollection) {
        // テキストとその他のプロパティを更新
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // 更新されたPDFファイルを保存
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 特定のページ領域でテキストを置換する

特定のページ領域でテキストを置換するには、まずTextFragmentAbsorberオブジェクトをインスタンス化し、TextSearchOptions.Rectangleプロパティを使用してページ領域を指定し、すべてのTextFragmentを反復してテキストを置換する必要があります。これらの操作が完了したら、DocumentオブジェクトのSaveメソッドを使用して出力PDFを保存するだけです。次のコードスニペットは、PDFドキュメントのすべてのページでテキストを置換する方法を示しています。

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // TextFragment Absorberオブジェクトをインスタンス化
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // ページ境界内でテキストを検索
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // TextSearch Optionsのページ領域を指定
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // PDFファイルの最初のページからテキストを検索
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // 個々のTextFragmentを反復
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // テキストを "---" に置換
        tf->set_Text(u"---");
    }

    // 更新されたPDFファイルを保存
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 正規表現に基づいてテキストを置換する

正規表現に基づいていくつかのフレーズを置換したい場合、まずTextFragmentAbsorberを使用してその特定の正規表現に一致するすべてのフレーズを見つける必要があります。正規表現をTextFragmentAbsorberのコンストラクターにパラメーターとして渡す必要があります。また、正規表現が使用されているかどうかを指定するTextSearchOptionsオブジェクトを作成する必要があります。TextFragmentsで一致するフレーズを取得したら、それらすべてをループして必要に応じて更新します。最後に、DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存する必要があります。以下のコードスニペットは、正規表現に基づいてテキストを置換する方法を示しています。

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルをロード
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // 入力検索フレーズのすべてのインスタンスを見つけるためのTextAbsorberオブジェクトを作成
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // 例: 1999-2000

    // 正規表現の使用を指定するためにテキスト検索オプションを設定
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // ドキュメントの最初のページに対してアブソーバを受け入れる
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 抽出されたテキストフラグメントをコレクションに取得
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // フラグメントをループ
    for (auto textFragment : textFragmentCollection) {
        // テキストやその他のプロパティを更新
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // 更新されたPDFファイルを保存
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 既存のPDFファイルのフォントを置き換える

Aspose.PDF for C++は、PDFドキュメント内のテキストを置き換える機能をサポートしています。しかし、PDFドキュメント内で使用されているフォントのみを置き換える必要がある場合があります。この場合、テキストを置き換えるのではなく、使用されているフォントのみが置き換えられます。TextFragmentAbsorberコンストラクタのオーバーロードの1つは、TextEditOptionsオブジェクトを引数として受け取り、TextEditOptions.FontReplace列挙からRemoveUnusedFontsの値を使用して、要求を達成できます。次のコードスニペットは、PDFドキュメント内のフォントを置き換える方法を示しています。

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // テキストフラグメントを検索し、編集オプションを未使用フォントの削除に設定
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // ドキュメントのすべてのページにアブソーバーを適用
    document->get_Pages()->Accept(textFragmentAbsorber);

    // すべてのTextFragmentを巡回
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // フォント名がArialMTの場合、フォント名をArialに置き換える
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // 更新されたPDFファイルを保存
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

次のコードスニペットでは、テキストを置換する際に非英語フォントを使用する方法を示します。

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // すべての"PDF"という単語を特定のフォントである日本語テキストに変更します
    // OSにインストールされている可能性があるMSGothic
    // また、別のフォントでヒエログリフをサポートしているものかもしれません
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // テキスト検索オプションのインスタンスを作成
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // ドキュメントのすべてのページにアブソーバーを適用
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 抽出されたテキストフラグメントをコレクションに取得
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // フラグメントをループ
    for (auto textFragment : textFragmentCollection) {
        // テキストとその他のプロパティを更新
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## テキスト置換がページコンテンツを自動的に再配置する必要があります

Aspose.PDF for C++は、PDFファイル内のテキストの検索と置換をサポートしています。しかし最近、一部のクライアントがテキストを置換する際に問題に直面しました。特定のTextFragmentが小さいコンテンツで置換されると、生成されたPDFに余分な空白が表示されたり、TextFragmentが長い文字列で置換されると、単語が既存のページコンテンツと重なったりします。したがって、PDFドキュメント内のテキストを置換した後にコンテンツを再配置するメカニズムを導入する必要がありました。

上記のシナリオに対応するために、Aspose.PDF for C++が改善され、PDFファイル内のテキストを置換する際にそのような問題が発生しないようになりました。次のコードスニペットは、PDFファイル内のテキストを置換し、ページコンテンツが自動的に再配置されることを示しています。

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Documentオブジェクトをインスタンス化
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 正規表現を使ってTextFragment Absorberオブジェクトを作成
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // ReplaceAdjustment.WholeWordsHyphenationオプションを指定して、
    // 現在の行が置換後に長すぎたり短すぎたりした場合に、次の行または現在の行でテキストを折り返すこともできます：
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // ドキュメントのすべてのページに対してabsorberを適用
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 抽出されたテキストフラグメントをコレクションに取得
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 各TextFragmentを置換
    for (auto textFragment : textFragmentCollection) {
        // 置換するテキストフラグメントのフォントを設定
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // フォントサイズを設定
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // プレースホルダーよりも大きな文字列でテキストを置換
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // 結果のPDFを保存
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## PDF作成中の置換可能なシンボルのレンダリング

置換可能なシンボルは、実行時に対応するコンテンツに置き換えられるテキスト文字列内の特別なシンボルです。現在、新しいAspose.PDF名前空間のDocument Object Modelでサポートされている置換可能なシンボルは、`$P`、`$p`、`\n`、`\r`です。`$p`と`$P`は、実行時のページ番号を扱うために使用されます。`$p`は現在のParagraphクラスが存在するページの番号に置き換えられます。`$P`はドキュメント内の総ページ数に置き換えられます。PDFドキュメントの段落コレクションに`TextFragment`を追加する際、テキスト内での改行をサポートしていません。しかし、改行を含むテキストを追加するためには、`TextParagraph`で`TextFragment`を使用してください：

- 単一の"\n"の代わりに`TextFragment`で"\r\n"またはEnvironment.NewLineを使用します。
- TextParagraphオブジェクトを作成します。これにより、テキストが分割されて追加されます。
- TextParagraph.AppendLineでTextFragmentを追加します。
- TextBuilder.AppendParagraphでTextParagraphを追加します。

```cpp
void RenderingReplaceableSymbols() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->Add();

    // 改行マーカーを含むテキストで新しいTextFragmentを初期化
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // 必要に応じてテキストフラグメントのプロパティを設定
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // TextParagraphオブジェクトを作成
    auto par = MakeObject<TextParagraph>();

    // 段落に新しいTextFragmentを追加
    par->AppendLine(textFragment);

    // 段落の位置を設定
    par->set_Position(MakeObject<Position>(100, 600));

    // TextBuilderオブジェクトを作成
    auto textBuilder = MakeObject<TextBuilder>(page);

    // TextBuilderを使用してTextParagraphを追加
    textBuilder->AppendParagraph(par);

    document->Save(_dataDir + u"RenderingReplaceableSymbols_out.pdf");
}
```

## ヘッダー/フッター領域の置換可能なシンボル

置換可能なシンボルは、PDFファイルのヘッダー/フッターセクション内にも配置できます。フッターセクションに置換可能なシンボルを追加する方法を確認するには、次のコードスニペットをレビューしてください。

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // MarginInfo インスタンスを PageInfo の Margin プロパティに割り当てる
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // ヘッダーとして表示する内容を格納するテキスト段落をインスタンス化する
    auto t1 = MakeObject<TextFragment>("report title");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("Report_Name");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // セクション用の HeaderFooter オブジェクトを作成する
    auto hfFoot = MakeObject<HeaderFooter>();

    // HeaderFooter オブジェクトを奇数および偶数フッターに設定する
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // 現在のページ番号と総ページ数を含むテキスト段落を追加する
    auto t3 = MakeObject<TextFragment>("Generated on test date");
    auto t4 = MakeObject<TextFragment>("report name ");
    auto t5 = MakeObject<TextFragment>("Page $p of $P");

    // テーブルオブジェクトをインスタンス化する
    auto tab2 = MakeObject<Table>();

    // 希望するセクションの段落コレクションにテーブルを追加する
    hfFoot->get_Paragraphs()->Add(tab2);

    // テーブルの列幅を設定する
    tab2->set_ColumnWidths(u"165 172 165");

    // テーブル内に行を作成し、その行にセルを作成する
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // テキストの垂直方向の配置を中央揃えに設定する
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // 希望するセクションの段落コレクションにテーブルを追加する
    page.getParagraphs().add(table);

    // BorderInfo オブジェクトを使ってデフォルトのセル境界を設定する
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // 別のカスタマイズされた BorderInfo オブジェクトを使ってテーブル境界を設定する
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // テーブル内に行を作成し、その行にセルを作成する
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total for C++ is a compilation of every Java component offered by Aspose. It is compiled on a"
                    + CRLF
                    + u"daily basis to ensure it contains the most up to date versions of each of our Java components. "
                    + CRLF
                    + u"daily basis to ensure it contains the most up to date versions of each of our Java components. "
                    + CRLF
                    + u"Using Aspose.Total for C++ developers can create a wide range of applications.");
            else
                c1 = row->get_Cells()->Add(u"item1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## PDFドキュメントからすべてのテキストを削除

### 演算子を使用してすべてのテキストを削除

いくつかのテキスト操作では、PDFドキュメントからすべてのテキストを削除する必要があり、そのためには通常、見つかったテキストを空の文字列値として設定する必要があります。 テキストの断片セットのテキストを変更すると、テキストの位置を確認および調整するための多くの操作が必要になります。 それらはテキスト編集スクリプトで必要です。 難しさは、ループで処理されるスクリプトで削除されるテキストのチャンク数を決定できないことにあります。

したがって、PDFページからすべてのテキストを削除するシナリオには、別のアプローチを使用することをお勧めします。

次のコードスニペットは、このタスクを迅速に解決する方法を示しています。

```cpp
void RemoveAllTextUsingOperators() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // PDFドキュメントのすべてのページをループする
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // ページ上のすべてのテキストを選択
        page->get_Contents()->Accept(operatorSelector);
        // すべてのテキストを削除
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // ドキュメントを保存
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```