---
title: PDFに透かしを追加する
linktitle: 透かしを追加
type: docs
weight: 90
url: ja/java/add-watermarks/
description: この記事では、Javaを使用してプログラムでPDFにアーティファクトを追加し、透かしを取得する機能について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** は、PDFドキュメントにアーティファクトを使用して透かしを追加できます。このタスクを解決するためにこの記事を確認してください。

Adobe Acrobatで作成された透かしは、アーティファクトと呼ばれます（PDF仕様の14.8.2.2実際のコンテンツとアーティファクトに記載されています）。アーティファクトを扱うために、Aspose.PDFには2つのクラスがあります：[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) と [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection)。

特定のページ上のすべてのアーティファクトを取得するために、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) クラスにはArtifactsプロパティがあります。
 このトピックでは、PDFファイル内でアーティファクトを操作する方法について説明します。

## アーティファクトの操作

[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) クラスには次のプロパティが含まれています:

**Artifact.Type** – アーティファクトのタイプを取得します（Artifact.ArtifactType 列挙の値をサポートし、値には Background、Layout、Page、Pagination、Undefined が含まれます）。
**Artifact.Subtype** – アーティファクトのサブタイプを取得します（Artifact.ArtifactSubtype 列挙の値をサポートし、値には Background、Footer、Header、Undefined、Watermark が含まれます）。

{{% alert color="primary" %}}

Adobe Acrobat で作成された透かしは、タイプが Pagination でサブタイプが Watermark であることに注意してください。

{{% /alert %}}

**Artifact.Contents** – アーティファクトの内部オペレーターのコレクションを取得します。そのサポートされるタイプは System.Collections.ICollection です。
**Artifact.Form** – アーティファクトの XForm を取得します（XForm が使用されている場合）。透かし、ヘッダー、フッターのアーティファクトには、すべてのアーティファクト内容を示す XForm が含まれています。

**Artifact.Image** – アーティファクトの画像を取得します（画像が存在する場合、そうでなければ null）。**Artifact.Text** – アーティファクトのテキストを取得します。
**Artifact.Rectangle** – ページ上のアーティファクトの位置を取得します。
**Artifact.Rotation** – アーティファクトの回転を取得します（度単位、正の値は反時計回りの回転を示します）。
**Artifact.Opacity** – アーティファクトの不透明度を取得します。可能な値は0から1の範囲で、1は完全に不透明です。

## プログラミングサンプル: 透かしの取得

次のコードスニペットは、JavaでPDFファイルの最初のページにある各透かしを取得する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.EncodingType;
import com.aspose.pdf.facades.FontStyle;
import com.aspose.pdf.facades.FormattedText;

public class ExampleWatermark {
    // ドキュメントディレクトリへのパス。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {

        // ドキュメントを開く
        Document doc = new Document(_dataDir + "text.pdf");      
        FormattedText formattedText = new FormattedText("Watermark", java.awt.Color.BLUE,FontStyle.Courier, EncodingType.Identity_h, true, 72.0F);
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(formattedText);        
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }

}  
```