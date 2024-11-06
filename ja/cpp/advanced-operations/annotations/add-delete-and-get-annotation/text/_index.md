---
title: PDFテキスト注釈
Texttitle: テキスト注釈
type: docs
weight: 10
url: ja/cpp/text-annotation/
description: Aspose.PDF for C++は、PDFドキュメントにテキスト注釈を追加、取得、削除することを可能にします。
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 既存のPDFファイルにテキスト注釈を追加する方法

テキスト注釈は、PDFドキュメント内の特定の位置に添付された注釈です。閉じている場合、注釈はアイコンとして表示され、開いている場合は、読者が選んだフォントとサイズでノートテキストを含むポップアップウィンドウを表示する必要があります。

注釈は特定のページの[Annotations](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation)コレクションによって含まれています。このコレクションには、その個々のページの注釈のみが含まれており、すべてのページには独自のAnnotationsコレクションがあります。

特定のページに注釈を追加するには、そのページのAnnotationsコレクションに[Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_collection#a1f7bf6c38fe2f97904a3575f5241d6c9)メソッドを使用して追加します。

1. 初めに、PDFに追加したい注釈を作成します。
1. 次に、入力PDFを開きます。
1. [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)オブジェクトのAnnotationsコレクションに注釈を追加します。

次のコードスニペットは、PDFページに注釈を追加する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // PDFファイルを読み込みます
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);
    auto rect = MakeObject<Rectangle>(200, 750, 400, 790);
    auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::TextAnnotation>(page, rect);

    textAnnotation->set_Title(u"Aspose User");
    textAnnotation->set_Subject(u"Sample Subject");
    textAnnotation->set_State(Aspose::Pdf::Annotations::AnnotationState::Accepted);
    textAnnotation->set_Contents(u"Sample contents for the annotation");
    textAnnotation->set_Open(true);
    textAnnotation->set_Icon(Aspose::Pdf::Annotations::TextIcon::Circle);

    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textAnnotation);
    border->set_Width(5);
    border->set_Dash(MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textAnnotation->set_Border(border);
    textAnnotation->set_Rect(rect);

    page->get_Annotations()->Add(textAnnotation);
    document->Save(_dataDir + u"sample_textannot.pdf");
}
```

## テキスト注釈を取得

PDFドキュメントでテキスト注釈を取得するには、次のコードスニペットを使用してください。

```cpp
void GetTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // AnnotationSelectorを使用して注釈をフィルタリング
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // 結果を出力
    for (auto fa : textAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

## PDFファイルからテキスト注釈を削除

以下のコードスニペットは、PDFファイルからテキスト注釈を削除する方法を示しています。

```cpp
void DeleteTextAnnotation() {

    String _dataDir("C:\\Samples\\");
    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // AnnotationSelectorを使用して注釈をフィルタリング
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // 注釈を削除
    for (auto fa : textAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_textannot_del.pdf");
}
```

## 新しいフリーテキスト注釈を追加（または作成）する方法

フリーテキスト注釈は、ページ上に直接テキストを表示します。以下のスニペットでは、文字列の最初の出現箇所の上にフリーテキスト注釈を追加します。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void FreeTextAnnotations::AddFreeTextAnnotationDemo()
{
    String _dataDir("C:\\Samples\\");

    // PDFファイルをロード
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto defaultAppearance = MakeObject<DefaultAppearance>();
    defaultAppearance->set_FontName(u"Helvetica");
    defaultAppearance->set_FontSize(12);
    defaultAppearance->set_TextColor(System::Drawing::Color::get_Blue());

    auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

    freeTextAnnotation->set_RichText(u"Free Text Demo");
    page->get_Annotations()->Add(freeTextAnnotation);
    document->Save(_dataDir + u"sample_freetext.pdf");
}
```

## フリーテキスト注釈を取得する

PDFドキュメントでテキスト注釈を取得するには、以下のコードスニペットを試してください：

```cpp
void FreeTextAnnotations::GetFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルをロードする
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // AnnotationSelectorを使用して注釈をフィルターする
    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // 結果を出力する
    for (auto fa : freeTextAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

### フリーテキスト注釈を非表示にする

場合によっては、ドキュメントを表示するときには見えないが、印刷するときには見える透かしを作成する必要があります。 Use annotation flags for this purpose. The following code snippet shows how.

```cpp
void FreeTextAnnotations::MakeFreeTextAnnotationInvisble() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto doc = MakeObject<Document>(_dataDir + u"input.pdf");

    auto annotation = new FreeTextAnnotation(doc->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(50, 600, 250, 650),
        MakeObject<DefaultAppearance>(u"Helvetica", 16,
            System::Drawing::Color::get_Red()));
    annotation->set_Contents(u"ABCDEFG");
    annotation->get_Characteristics()->set_Border(System::Drawing::Color::get_Red());
    annotation->set_Flags (AnnotationFlags::Print | AnnotationFlags::NoView);
    doc->get_Pages()->idx_get(1)->get_Annotations()->Add(annotation);

    // 出力ファイルを保存
    doc->Save(_dataDir + u"InvisibleAnnotation_out.pdf");
}
```

## Delete FreeText Annotation

The following code snippet shows how Delete FreeText Annotation from a PDF file.

```cpp
void FreeTextAnnotations::DeleteFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");

    // AnnotationSelectorを使用して注釈をフィルターする
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // 注釈を削除する
    for (auto fa : freeTextAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_freetext_del.pdf");
}
```