---
title: C++でのアーティファクトの操作
linktitle: アーティファクトの操作
type: docs
weight: 110
url: ja/cpp/artifacts/
description: このページでは、Aspose.PDF for C++ を使用してアーティファクトクラスを操作する方法について説明します。コードスニペットは、PDFページに背景画像を追加する方法と、PDFファイルの最初のページにある各ウォーターマークを取得する方法を示しています。
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFでウォーターマークを取得する方法

**PDFのアーティファクトとは何ですか？**

PDF / UA ISOリファレンスによると、重要ではない、または背景に表示されないコンテンツは、関連情報を運ばないため、支援技術がそれを無視できるようにアーティファクトとしてフラグを立てる必要があります。
アーティファクトがプログラムで作成できない場合、Aspose.PDF for C++ を使用して手動で行う必要があります。

[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) クラスには次のプロパティが含まれています：

- **Artifact.Type** – アーティファクトのタイプを取得します（値にはBackground, Layout, Page, Pagination, Undefinedを含むArtifact.ArtifactType列挙の値をサポートします）。
- **Artifact.Subtype** – アーティファクトのサブタイプを取得します（Artifact.ArtifactSubtype列挙の値をサポートし、値にはBackground、Footer、Header、Undefined、Watermarkが含まれます）。

{{% alert color="primary" %}}

Adobe Acrobatで作成された透かしには、タイプPaginationとサブタイプWatermarkがあります。

{{% /alert %}}

- **Artifact.Contents** – アーティファクト内部オペレーターのコレクションを取得します。サポートされる型はSystem.Collections.ICollectionです。
- **Artifact.Form** – アーティファクトのXFormを取得します（XFormが使用されている場合）。透かし、ヘッダー、およびフッターのアーティファクトには、すべてのアーティファクトの内容を示すXFormが含まれています。
- **Artifact.Image** – アーティファクトの画像を取得します（画像が存在する場合、存在しない場合はnull）。
- **Artifact.Text** – アーティファクトのテキストを取得します。
- **Artifact.Rectangle** – ページ上のアーティファクトの位置を取得します。
- **Artifact.Rotation** – アーティファクトの回転を取得します（度単位、正の値は反時計回りの回転を示します）。
- **Artifact.Opacity** – アーティファクトの不透明度を取得します。 可能な値は0から1の範囲で、1は完全に不透明です。

PDFファイルでアーティファクトを扱う例として、透かしを取り上げます。

Adobe Acrobatのサポートを受けて作成された透かしは、アーティファクトと呼ばれます（14.8.2.2 Present Content and PDF Specification Artifactsで説明されています）。アーティファクトを扱うためにAspose.PDFには2つのクラスがあります： [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) と [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection) です。

特定のページ上のすべてのアーティファクトを取得するために、[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) クラスにはArtifactsプロパティがあります。このトピックでは、PDFファイルで透かしアーティファクトを操作する方法を示します。

次のコードスニペットは、C++でPDFファイルの最初のページの各透かしを取得する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```
背景画像を使用して、PDFドキュメントに透かしや独自のデザインを追加できます。Aspose.PDF for C++は、[BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact)クラスを使用して、ページオブジェクトに背景画像を追加します。

次のコードスニペットは、BackgroundArtifactオブジェクトを使用してPDFページに背景画像を追加する方法を示しています。

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>();

    // ドキュメントオブジェクトにページを追加する
    auto page = pdfDocument->get_Pages()->Add();

    // 背景アーティファクトオブジェクトを作成する
    auto background = MakeObject<BackgroundArtifact>();

    // 背景アーティファクトオブジェクトの画像を指定する
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // ページのアーティファクトコレクションにBackgroundArtifactを追加する
    page->get_Artifacts()->Add(background);

    // 修正されたPDFを保存する
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### プログラミングサンプル: 透かしを取得する

次のコードスニペットは、PDFファイルの最初のページの各透かしを取得する方法を示しています。

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // サブタイプ、テキスト、およびアーティファクトの場所を反復処理して取得する
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### プログラミングサンプル: 特定のタイプのアーティファクトをカウントする

特定のタイプのアーティファクトの総数を計算するには（たとえば、透かしの総数）、次のコードを使用します。

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // アーティファクトのタイプが透かしの場合、カウンターを増加する
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"ページには {0} 個の透かしが含まれています", count);
}
```