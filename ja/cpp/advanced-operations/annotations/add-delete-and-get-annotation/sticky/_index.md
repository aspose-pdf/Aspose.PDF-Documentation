---
title: PDF スティッキー注釈を C++ で使用
linktitle: スティッキー注釈
type: docs
weight: 50
url: ja/cpp/sticky-annotations/
description: このトピックでは、スティッキー注釈について説明します。例として、テキスト内の透かし注釈を示します。ページ上にグラフィックを表すために使用されます。このタスクを解決するためのコードスニペットを確認してください。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 透かし注釈を追加

透かし注釈は、印刷されるページのサイズに関係なく、ページ上の固定サイズと位置で印刷されるグラフィックを表すために使用されます。

PDF ページの特定の位置に [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/) を使用して透かしテキストを追加できます。透かしの不透明度は、不透明度プロパティを使用して制御することもできます。

以下のコードスニペットを確認して、WatermarkAnnotation を追加してください。

```cpp
 using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // PDF ファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // 注釈を作成する
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    // 注釈をページの注釈コレクションに追加する
    page->get_Annotations()->Add(wa);

    // フォント設定用の TextState を作成する
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    // 注釈テキストの不透明度レベルを設定する
    wa->set_Opacity(0.5);

    // 注釈にテキストを追加する
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    // ドキュメントを保存する
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## ウォーターマーク注釈を取得する

PDFドキュメントからウォーターマーク注釈を取得するために、次のコードスニペットを試してください。

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルをロードする
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // AnnotationSelectorを使用して注釈をフィルタリングする
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // 結果を出力する
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## ウォーターマーク注釈を削除する

PDFドキュメントからウォーターマーク注釈を削除するために、次のコードスニペットを試してください。

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // PDFファイルをロードする
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // AnnotationSelectorを使用して注釈をフィルタリングする
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // 注釈を削除する
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```