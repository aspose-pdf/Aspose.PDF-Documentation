---
title: PDFファイルからリンクを抽出する
linktitle: リンクを抽出する
type: docs
weight: 30
url: /ja/cpp/extract-links/
description: C#を使用してPDFからリンクを抽出します。このトピックでは、AnnotationSelectorクラスを使用してリンクを抽出する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルからリンクを抽出する

リンクはPDFファイル内で注釈として表現されるため、リンクを抽出するには、すべての[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)オブジェクトを抽出します。

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトを作成します。
1. リンクを抽出したい[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)を取得します。
1. Use the [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) クラスを使用して、指定されたページからすべての [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) オブジェクトを抽出します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) オブジェクトを Page オブジェクトの Accept メソッドに渡します。
1. [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) オブジェクトの Selected プロパティを使用して、選択されたすべてのリンク注釈を IList オブジェクトに取得します。

次のコードスニペットは、PDFファイルからリンクを抽出する方法を示しています。

```cpp
void ExtractLinksFromThePDFFile() {
   
    // PDFファイルを読み込む
    String _dataDir("C:\\Samples\\");

    // Documentインスタンスを作成
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Annotation located: {0}", annot->get_Rect());
    }
}
```