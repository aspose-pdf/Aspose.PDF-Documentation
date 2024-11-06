---
title: PDFに透かしを追加する方法 C++を使用
linktitle: 透かしを追加
type: docs
weight: 90
url: ja/cpp/add-watermarks/
description: この記事では、プログラムでC++を使用してPDFにおけるアーティファクトの操作と透かしの取得に関する機能を説明します。
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

透かしは通常、文書や画像を作成した人物を識別するためのロゴや印章を含む半透明の画像です。

**Aspose.PDF for C++**は、Artifactクラスを使用してPDF文書に透かしを追加することができます。このタスクを解決するためにこの記事を確認してください。

Adobe Acrobatで作成された透かしは、PDF仕様の14.8.2.2「実際のコンテンツとアーティファクト」で説明されているように、アーティファクトと呼ばれます。アーティファクトを操作するために、Aspose.PDFには2つのクラスがあります：[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact)と[ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection)です。

特定のページ上のすべてのアーティファクトを取得するために、[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)クラスはArtifactsプロパティを持っています。 このトピックでは、PDFファイルでアーティファクトを扱う方法について説明します。

## アーティファクトの操作

[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) クラスは次のプロパティを含んでいます:

**Artifact.Type** – アーティファクトのタイプを取得します（Artifact.ArtifactType 列挙の値をサポートしており、Background、Layout、Page、Pagination、Undefined が含まれます）。
**Artifact.Subtype** – アーティファクトのサブタイプを取得します（Artifact.ArtifactSubtype 列挙の値をサポートしており、Background、Footer、Header、Undefined、Watermark が含まれます）。

{{% alert color="primary" %}}

Adobe Acrobat で作成されたウォーターマークは、タイプが Pagination でサブタイプが Watermark であることに注意してください。

{{% /alert %}}

**Artifact.Contents** – アーティファクト内部オペレーターのコレクションを取得します。そのサポートされるタイプは System.Collections.ICollection です。
**Artifact.Form** – アーティファクトの XForm を取得します（XForm が使用されている場合）。ウォーターマーク、ヘッダー、フッターのアーティファクトには、すべてのアーティファクト内容を表示する XForm が含まれています。

**Artifact.Image** – アーティファクトの画像を取得します（画像が存在する場合、それ以外は null）。**Artifact.Text** – アーティファクトのテキストを取得します。  
**Artifact.Rectangle** – ページ上のアーティファクトの位置を取得します。  
**Artifact.Rotation** – アーティファクトの回転を取得します（度単位、正の値は反時計回りの回転を示します）。  
**Artifact.Opacity** – アーティファクトの不透明度を取得します。可能な値は0から1の範囲で、1は完全に不透明です。

## プログラミングサンプル: PDFファイルに透かしを追加する方法

次のコードスニペットは、C++を使用してPDFファイルの最初のページに各透かしを取得する方法を示しています。

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```