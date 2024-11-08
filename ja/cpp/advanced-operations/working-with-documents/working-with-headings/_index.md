---
title: PDFでの見出しの操作
type: docs
weight: 90
url: /ja/cpp/working-with-headings/
lastmod: "2021-11-11"
description: C++を使用してPDFドキュメントの見出しに番号を作成します。Aspose.PDF for C++ はさまざまな種類の番号スタイルを示します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 見出しに番号スタイルを適用

ドキュメント内の任意のテキストは見出しから始まります。見出しは、スタイルやテーマに関係なく、コンテンツの不可欠な部分です。
見出しは、テキストへの注意を引き、ユーザーがドキュメント内で必要な情報を見つけるのに役立ち、可読性と視覚的な認識を向上させます。見出しスタイルを使用すると、目次を素早く作成し、ドキュメントの構造を変更することもできます。
それでは、Aspose.PDF for C++ ライブラリを使用してヘッダーを操作する方法を確認しましょう。

[Aspose.PDF for C++](/pdf/ja/cpp/) は多くの事前定義された番号スタイルを提供します。 これらの事前定義された番号スタイルは、列挙型NumberingStyleに格納されています。NumberingStyle列挙型の事前定義された値とその説明は以下の通りです：

|**見出しの種類**|**説明**|
| :- | :- |
|NumeralsArabic|アラビアタイプ、例えば、1,1.1,...|
|NumeralsRomanUppercase|ローマ大文字タイプ、例えば、I,I.II,...|
|NumeralsRomanLowercase|ローマ小文字タイプ、例えば、i,i.ii,...|
|LettersUppercase|英語大文字タイプ、例えば、A,A.B,...|
|LettersLowercase|英語小文字タイプ、例えば、a,a.b,...|
**Aspose.PDF.Heading**クラスの**Style**プロパティは、見出しの番号スタイルを設定するために使用されます。

|**図: 事前定義された番号スタイル**|
| :- |
上記の図に示されている出力を得るためのソースコードは、以下の例に示されています。

```cpp
void WorkingWithHeadingsInPDF() {
    // パス名の文字列
    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String outputFileName("ApplyNumberStyle_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top (72);
    document->get_PageInfo()->get_Margin()->set_Bottom (72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width (612.0);
    pdfPage->get_PageInfo()->set_Height (792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text (u"List 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList (true);
    heading2->set_StartNumber(13);
    heading2->set_Text (u"List 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList (true);
    heading3->set_StartNumber(1);
    heading3->set_Text (u"the value, as of the effective date of the plan, of property to be distributed under the plan onaccount of each allowed");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // 結合された出力ファイルを保存
    document->Save(_dataDir + outputFileName);
}
```