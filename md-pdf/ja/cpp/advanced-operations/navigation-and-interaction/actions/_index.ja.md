---
title: PDFでのアクションの操作
linktitle: アクション
type: docs
weight: 20
url: /cpp/actions/
description: このセクションでは、C++を使用してドキュメントやフォームフィールドにアクションをプログラムで追加する方法を説明します。
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルにハイパーリンクを追加する

PDFドキュメントは情報を共有するための素晴らしい方法です。読みやすく、編集しやすく、配布もしやすいです。しかし、PDFドキュメントにリンクを作成するのは難しい場合があります。方法をお見せしましょう。

PDFファイルにハイパーリンクを追加することが可能です。これは、読者がPDFの別の部分や外部コンテンツに移動できるようにするためです。

例えば、電子書籍にクリック可能な目次を追加したり、記事に外部リソースを引用したり、ウェブサイトの別のページに素早く移動してトピックに関する詳細情報を得たりすることができます。

数回クリックするだけでハイパーリンクを作成するには、次の簡単な手順に従ってください。

1.  [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスオブジェクトを作成します。
1. リンクを追加したい [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) クラスを取得します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) オブジェクトを Page と [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) オブジェクトを使用して作成します。矩形オブジェクトは、リンクを追加するページ上の位置を指定するために使用されます。
1. Action プロパティを [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) オブジェクトに設定し、リモート URI の位置を指定します。
1. ハイパーリンクテキストを表示するには、[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) オブジェクトが配置されている場所に類似した場所にテキスト文字列を追加します。
1. フリーテキストを追加するには:

- [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) オブジェクトをインスタンス化します。 It also accepts Page and Rectangle objects as argument, so it is possible to provide same values as specified against the LinkAnnotation constructor.  
- [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) オブジェクトの Contents プロパティを使用して、出力 PDF に表示される文字列を指定します。  
- オプションとして、PDF ドキュメントに表示されないように、[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) および FreeTextAnnotation オブジェクトの境界線の幅を 0 に設定します。  
- [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) および [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) オブジェクトが定義されたら、これらのリンクを [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) オブジェクトの Annotations コレクションに追加します。  

- 最後に、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトの Save メソッドを使用して更新された PDF を保存します。
以下のコードスニペットは、PDFファイルにハイパーリンクを追加する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// ドキュメントを開く

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// リンクを作成

auto page = document->get_Pages()->idx_get(1);

// リンク注釈オブジェクトを作成

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// LinkAnnotation用のボーダーオブジェクトを作成

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// ボーダーの幅を0に設定

border->set_Width(0);

// LinkAnnotationのボーダーを設定

link->set_Border(border);

// リンクタイプをリモートURIとして指定

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// PDFファイルの最初のページの注釈コレクションにリンク注釈を追加

page->get_Annotations()->Add(link);


// フリーテキスト注釈を作成

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// フリーテキストとして追加される文字列

textAnnotation->set_Contents(u"Link to Aspose website");

// フリーテキスト注釈のボーダーを設定

textAnnotation->set_Border(border);

// ドキュメントの最初のページの注釈コレクションにフリーテキスト注釈を追加

page->get_Annotations()->Add(textAnnotation);


// 更新されたドキュメントを保存

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## 同じPDF内のページにハイパーリンクを作成

Aspose.PDF for C++は、PDFの作成および操作に優れた機能を提供します。また、PDFページへのリンクを追加する機能も提供しており、リンクは別のPDFファイルのページ、ウェブURL、アプリケーションの起動リンク、さらには同じPDFファイル内のページへのリンクを指すことができます。同じPDFファイル内のページへのローカルハイパーリンクを追加するには、Aspose.PDF名前空間に[LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink)という名前のクラスが追加されており、このクラスにはTargetPageNumberというプロパティがあり、ハイパーリンクのターゲット/目的地のページを指定するために使用されます。

ローカルハイパーリンクを追加するには、テキストフラグメントを作成し、リンクをテキストフラグメントに関連付ける必要があります。 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) クラスには、LocalHyperlink インスタンスを関連付けるために使用される Hyperlink という名前のプロパティがあります。次のコードスニペットは、この要件を達成する手順を示しています。

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// Document インスタンスを作成

auto document = MakeObject<Document>();


// PDFファイルのページコレクションにページを追加

auto page = document->get_Pages()->Add();


// Text Fragment インスタンスを作成

auto text = MakeObject<TextFragment>(u"link page number test to page 2");


// ローカルハイパーリンクインスタンスを作成

auto link = MakeObject<LocalHyperlink>();


// リンクインスタンスのターゲットページを設定

link->set_TargetPageNumber(2);


// TextFragment のハイパーリンクを設定

text->set_Hyperlink(link);


// ページのパラグラフコレクションにテキストを追加

page->get_Paragraphs()->Add(text);


// 新しい TextFragment インスタンスを作成

text = new TextFragment(u"link page number test to page 1");


// TextFragment は新しいページに追加する必要があります

text->set_IsInNewPage(true);


// 別のローカルハイパーリンクインスタンスを作成

link = new LocalHyperlink();


// 2番目のハイパーリンクのターゲットページを設定

link->set_TargetPageNumber(1);


// 2番目の TextFragment のリンクを設定

text->set_Hyperlink(link);


// ページオブジェクトのパラグラフコレクションにテキストを追加

page->get_Paragraphs()->Add(text);


// 更新されたドキュメントを保存

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## PDF ハイパーリンク先（URL）を取得する

リンクはPDFファイル内で注釈として表され、追加、更新、削除が可能です。Aspose.PDF for C++は、PDFファイル内のハイパーリンクの宛先（URL）を取得することもサポートしています。

リンクのURLを取得するには：

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトを作成します。
1. リンクを抽出したい [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) を取得します。
1. 指定したページからすべての [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) オブジェクトを抽出するために [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) クラスを使用します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) オブジェクトを [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) オブジェクトの Accept メソッドに渡します。
1. すべての選択されたリンク注釈を [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) オブジェクトの Selected プロパティを使用して IList オブジェクトに取得します。
1. 最後に、LinkAnnotation アクションを GoToURIAction として抽出します。

次のコードスニペットは、PDF ファイルからハイパーリンクの宛先 (URL) を取得する方法を示しています。

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// アクションを抽出

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// リスト内の個々のアイテムを反復処理

if (list->get_Count() == 0)


Console::WriteLine(u"No Hyperlinks found...");

else {


// すべてのブックマークをループ処理


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// 宛先URLを出力




Console::WriteLine(u"Destination: " + action->get_URI());



}


}

} // else 終了
}
```
## ハイパーリンクテキストを取得する

ハイパーリンクには2つの部分があります: ドキュメントに表示されるテキストと、目的地のURLです。場合によっては、URLではなくテキストが必要です。

PDFファイル内のテキストと注釈/アクションは異なるエンティティで表されます。ページ上のテキストは単なる単語と文字の集合であり、注釈はハイパーリンクに内在するようなインタラクティブ性をもたらします。

URLの内容を見つけるには、注釈とテキストの両方を操作する必要があります。[Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation)オブジェクト自体にはテキストはありませんが、ページ上のテキストの下にあります。したがって、テキストを取得するには、AnnotationがURLの境界を提供し、TextオブジェクトがURLの内容を提供します。以下のコードスニペットをご覧ください。

```cpp
  void GetHyperlinkText() {

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");

// アクションを抽出する

auto page = document->get_Pages()->idx_get(1);

for (auto annot : page->get_Annotations()) {

auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);

if (la != nullptr) {

// 各リンク注釈のURLを出力する

auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());

Console::WriteLine(u"URI: " + action->get_URI());

auto absorber = MakeObject<TextAbsorber>();

absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());

page->Accept(absorber);

String extractedText = absorber->get_Text();

// ハイパーリンクに関連付けられたテキストを出力する

Console::WriteLine(extractedText);

}

}
}
```

## PDFファイルからドキュメントオープンアクションを削除する

[ドキュメントを表示する際にPDFページを指定する方法](#how-to-specify-pdf-page-when-viewing-document)では、ドキュメントを最初のページ以外のページで開くように指示する方法を説明しました。複数のドキュメントを連結し、1つ以上にGoToアクションが設定されている場合、それらを削除したいと思うでしょう。例えば、2つのドキュメントを結合し、2つ目のドキュメントに2ページ目に移動するGoToアクションがある場合、出力ドキュメントは結合されたドキュメントの1ページ目ではなく、2つ目のドキュメントの2ページ目で開きます。この動作を避けるために、オープンアクションコマンドを削除します。

オープンアクションを削除するには:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトの[OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e)プロパティをnullに設定します。
1. DocumentオブジェクトのSaveメソッドを使用して、更新されたPDFを保存します。

次のコードスニペットは、PDFファイルからドキュメントオープンアクションを削除する方法を示しています。

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// ドキュメントを開く

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// ドキュメントオープンアクションを削除

document->set_OpenAction(nullptr);


// 更新されたドキュメントを保存

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## ドキュメントを表示する際にPDFページを指定する方法 {#how-to-specify-pdf-page-when-viewing-document}

Adobe ReaderなどのPDFビューアでPDFファイルを表示する際、通常ファイルは最初のページに開きます。しかし、ファイルを別のページで開くように設定することも可能です。

'XYZExplicitDestination'クラスを使用すると、開きたいPDFファイルのページを指定することができます。[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスのOpenActionプロパティにGoToActionオブジェクトの値を渡すと、ドキュメントはXYZExplicitDestinationオブジェクトに対して指定されたページで開きます。以下のコードスニペットは、ドキュメントオープンアクションとしてページを指定する方法を示しています。

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// PDFファイルを読み込む

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// ドキュメントの2ページ目のインスタンスを取得

auto page2 = document->get_Pages()->idx_get(2);

// ターゲットページのズームファクターを設定するための変数を作成

double zoom = 1;

// GoToActionインスタンスを作成

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// 2ページに移動

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// ドキュメントオープンアクションを設定

document->set_OpenAction(action);

// 更新されたドキュメントを保存

document->Save(_dataDir + u"goto2page_out.pdf");
}
```