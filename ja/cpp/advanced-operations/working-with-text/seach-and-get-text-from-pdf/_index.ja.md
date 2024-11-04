---
title: PDFドキュメントのページからテキストを検索して取得する
linktitle: 検索とテキスト取得
type: docs
weight: 60
url: /cpp/search-and-get-text-from-pdf/
description: この記事では、さまざまなツールを使用してPDFドキュメントからテキストを検索して取得する方法を説明します。特定のページまたは全体のページから正規表現で検索できます。
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントのすべてのページからテキストを検索して取得する

[TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) クラスを使用すると、PDFドキュメントのすべてのページから特定のフレーズに一致するテキストを見つけることができます。ドキュメント全体からテキストを検索するには、[Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) コレクションのAcceptメソッドを呼び出す必要があります。'Accept' メソッドは、TextFragmentAbsorberオブジェクトをパラメータとして受け取り、TextFragmentオブジェクトのコレクションを返します。

次のコードスニペットは、すべてのページからテキストを検索する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // 入力検索フレーズのすべてのインスタンスを見つけるためにTextAbsorberオブジェクトを作成します
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("document");

    // すべてのページに対してアブソーバーを受け入れる
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 抽出されたテキストフラグメントをコレクションに取得
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // フラグメントをループする
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"テキスト :- {0}", textFragment->get_Text());
        Console::WriteLine(u"位置 :- {0}", textFragment->get_Position());
        Console::WriteLine(u"Xインデント :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"Yインデント :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"フォント - 名前 :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"フォント - アクセス可能か :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"フォント - 埋め込みか - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"フォント - サブセットか :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"フォントサイズ :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"前景色 :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## すべてのページから正規表現を使用してテキストを検索して取得する

TextFragmentAbsorberは、正規表現に基づいてすべてのページからテキストを検索して取得するのに役立ちます。 First, you need to pass a regular expression to [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) constructor as the phrase. After that, you have to set the [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) property of the TextFragmentAbsorber object. This property requires TextSearchOptions object and you need to pass true as a parameter to its constructor while creating new objects. As you want to retrieve matching text from all the pages, you need to call Accept method of Pages collection. [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) returns a TextFragmentCollection containing all the fragments matching the criteria specified by the regular expression. The following code snippet shows you how to search and get text from all the pages based on a regular expression.

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // like 1999-2000

    // Set text search option to specify regular expression usage
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Text :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Position :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Font - Name :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Font - IsAccessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Font - IsEmbedded - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Font - IsSubset :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Font Size :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Foreground Color :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

最初に、正規表現をフレーズとして[TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/)コンストラクターに渡す必要があります。その後、TextFragmentAbsorberオブジェクトの[TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/)プロパティを設定する必要があります。このプロパティにはTextSearchOptionsオブジェクトが必要で、新しいオブジェクトを作成する際には、コンストラクターのパラメーターとしてtrueを渡す必要があります。すべてのページから一致するテキストを取得したい場合は、PagesコレクションのAcceptメソッドを呼び出す必要があります。[TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/)は、正規表現で指定された基準に一致するすべてのフラグメントを含むTextFragmentCollectionを返します。以下のコードスニペットは、正規表現に基づいてすべてのページからテキストを検索して取得する方法を示しています。