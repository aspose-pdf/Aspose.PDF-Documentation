---
title: C++を使用した追加アノテーション
linktitle: 追加アノテーション
type: docs
weight: 60
url: ja/cpp/extra-annotations/
description: このセクションでは、PDFドキュメントに追加の種類のアノテーションを追加、取得、および削除する方法について説明します。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 既存のPDFファイルにキャレットアノテーションを追加する方法

キャレットアノテーションは、テキスト編集を示すシンボルです。キャレットアノテーションはマークアップアノテーションでもあるため、CaretクラスはMarkupクラスから派生し、キャレットアノテーションのプロパティを取得または設定する機能を提供し、キャレットアノテーションの表示の流れをリセットします。

キャレットアノテーションを作成する手順:

1. PDFファイルをロードする - 新しい[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. 新しい[キャレット注釈](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/)を作成し、キャレットのパラメータ（新しい長方形、タイトル、件名、フラグ、色、幅、StartingStyle、およびEndingStyle）を設定します。この注釈はテキストの挿入を示すために使用されます。  
1. 新しい[キャレット注釈](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/)を作成し、キャレットのパラメータ（新しい長方形、タイトル、件名、フラグ、色、幅、StartingStyle、およびEndingStyle）を設定します。この注釈はテキストの置換を示すために使用されます。  
1. 新しい[打ち消し線注釈](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/)を作成し、パラメータ（新しい長方形、タイトル、色、新しいQuadPointsと新しいポイント、件名、InReplyTo、ReplyType）を設定します。  
1. その後、ページに注釈を追加できます。

以下のコードスニペットは、キャレット注釈をPDFファイルに追加する方法を示しています：

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // PDFファイルをロード
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // この注釈はテキストの挿入を示すために使用されます
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Aspose User");
    caretAnnotation1->set_Subject(u"Inserted text 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // この注釈はテキストの置換を示すために使用されます
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Aspose User");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Inserted text 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416),
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Cross-out");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### キャレット注釈を取得する

以下のコードスニペットを使用してPDFドキュメントでキャレット注釈を取得してください

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDFファイルをロードする
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // AnnotationSelectorを使用して注釈をフィルターする
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // 結果を出力する
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### キャレット注釈を削除する

以下のコードスニペットはPDFファイルからキャレット注釈を削除する方法を示しています。

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDFファイルをロードする
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // AnnotationSelectorを使用して注釈をフィルターする
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // 注釈を削除する
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## リンク注釈を追加する方法

[リンク注釈](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation)は、ドキュメント内の別の場所への宛先または実行されるアクションへのハイパーテキストリンクです。

リンクはページ上の任意の場所に配置できる長方形の領域です。各リンクには、それに関連付けられた対応するPDFアクションがあります。このアクションは、ユーザーがこのリンクの領域をクリックしたときに実行されます。

次のコードスニペットは、電話番号の例を使用してPDFファイルにリンク注釈を追加する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);

    // TextFragmentAbsorberオブジェクトを作成して電話番号を見つける
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // 最初のページのみアブソーバーを適用
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // リンク注釈を作成し、アクションを電話番号に設定
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // ページに注釈を追加
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");
}
```

### リンク注釈を取得する

以下のコードスニペットを使用して、PDFドキュメントからLinkAnnotationを取得してみてください。

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // AnnotationSelectorを使用して注釈をフィルタリングする
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // 結果を出力
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // 各リンク注釈のURLを出力
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // ハイパーリンクに関連付けられたテキストを出力
        Console::WriteLine(extractedText);
    }
}
```

### リンク注釈の削除

以下のコードスニペットは、PDFファイルからリンク注釈を削除する方法を示しています。これには、1ページ目のすべてのリンク注釈を見つけて削除する必要があります。その後、注釈を削除したドキュメントを保存します。

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // AnnotationSelectorを使用して注釈をフィルタリング
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // 結果を出力
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // 注釈を削除したドキュメントを保存
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## Aspose.PDF for C++を使用して、特定のページ領域を編集注釈で編集する

Aspose.PDF for C++は、既存のPDFファイルに注釈を追加および操作する機能をサポートしています。最近、一部のお客様から、PDFドキュメントの特定のページ領域からテキスト、画像などの要素を削除する必要があると投稿されました。この要件を満たすために、RedactionAnnotationというクラスが提供されており、特定のページ領域を編集するために使用することができるか、既存のRedactionAnnotationsを操作してそれらを編集する（つまり、注釈をフラット化して、その下のテキストを削除する）ことができます。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // 特定のページ領域用にRedactionAnnotationインスタンスを作成
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // 編集注釈に印刷されるテキスト
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // 編集注釈に重ねてオーバーレイテキストを繰り返す
    annot->set_Repeat(true);

    // 最初のページの注釈コレクションに注釈を追加
    page->get_Annotations()->Add(annot);

    // 注釈をフラット化し、ページの内容を編集（つまり、編集された注釈の下のテキストと画像を削除）
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## Facadesアプローチ

Aspose.PDF.Facadesは、PDFファイル内の既存の注釈を操作する機能を提供する[PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/)クラスをサポートしています。

このクラスには、特定のページ領域を削除する機能を提供する[RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63)という名前のメソッドが含まれています。

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // 特定のページ領域を削除
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```