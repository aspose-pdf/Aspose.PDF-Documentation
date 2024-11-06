---
title: PDFに背景を追加するC++で
linktitle: 背景を追加
type: docs
weight: 110
url: ja/cpp/add-backgrounds/
descriptions: C++でPDFファイルに背景画像を追加します。BackgroundArtifactオブジェクトを使用します。
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFファイルに背景を追加することは、ドキュメントの全体的な読みやすさを向上させるのに役立ちます。PDFの内容はより魅力的になり、ドキュメントの外観が良ければ読者の注意を引くでしょう。背景はまた、PDFのハイライトを強調するためにも使用できます。

背景画像は、ウォーターマークや他の控えめなデザインをドキュメントに追加するために使用できます。Aspose.PDF for C++では、各PDFドキュメントはページの集合であり、各ページはアーティファクトの集合を含みます。[BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact)クラスは、ページオブジェクトに背景画像を追加するために使用できます。

次のコードスニペットは、C++でBackgroundArtifactオブジェクトを使用してPDFページに背景画像を追加する方法を示しています。

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // 新しいDocumentオブジェクトを作成する
    auto document = MakeObject<Document>();

    // ドキュメントオブジェクトに新しいページを追加する
    auto page = document->get_Pages()->Add();

    // 背景アーティファクトオブジェクトを作成する
    auto background = MakeObject<BackgroundArtifact>();

    // 背景アーティファクトオブジェクトの画像を指定する
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // アーティファクトコレクションに背景アーティファクトを追加する
    page->get_Artifacts()->Add(background);

    // ドキュメントを保存する
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```