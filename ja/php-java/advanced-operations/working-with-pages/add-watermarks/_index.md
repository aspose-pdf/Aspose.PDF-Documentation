---
title: PDFに透かしを追加する
linktitle: 透かしを追加
type: docs
weight: 90
url: ja/php-java/add-watermarks/
description: この記事では、PHPを使用してPDF内のアーティファクトを操作し、透かしを取得する機能について説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP via Java**は、アーティファクトを使用してPDFドキュメントに透かしを追加することができます。このタスクを解決するためにこの記事を確認してください。

Adobe Acrobatで作成された透かしは、アーティファクトと呼ばれます（PDF仕様の14.8.2.2 実際のコンテンツとアーティファクトで説明されています）。アーティファクトを操作するために、Aspose.PDFには2つのクラスがあります：[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact)と[ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection)です。

特定のページ上のすべてのアーティファクトを取得するために、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page)クラスにはArtifactsプロパティがあります。
 このトピックでは、PDFファイル内でのアーティファクトの操作方法について説明します。

## アーティファクトの操作

[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) クラスには以下のプロパティがあります：

**Artifact.Type** – アーティファクトのタイプを取得します（Artifact.ArtifactType 列挙の値をサポートしており、値には Background、Layout、Page、Pagination、Undefined が含まれます）。
**Artifact.Subtype** – アーティファクトのサブタイプを取得します（Artifact.ArtifactSubtype 列挙の値をサポートしており、値には Background、Footer、Header、Undefined、Watermark が含まれます）。

{{% alert color="primary" %}}

Adobe Acrobat で作成されたウォーターマークは、タイプが Pagination でサブタイプが Watermark であることに注意してください。

{{% /alert %}}

**Artifact.Contents** – アーティファクト内部オペレーターのコレクションを取得します。サポートされているタイプは System.Collections.ICollection です。
**Artifact.Form** – アーティファクトの XForm を取得します（XForm が使用されている場合）。ウォーターマーク、ヘッダー、およびフッターのアーティファクトは、すべてのアーティファクト内容を示す XForm を含んでいます。

**Artifact.Image** – アーティファクトの画像を取得します（画像が存在する場合、存在しない場合は null）。**Artifact.Text** – アーティファクトのテキストを取得します。  
**Artifact.Rectangle** – ページ上のアーティファクトの位置を取得します。  
**Artifact.Rotation** – アーティファクトの回転を取得します（度単位、正の値は反時計回りの回転を示します）。  
**Artifact.Opacity** – アーティファクトの不透明度を取得します。可能な値は0から1の範囲で、1は完全に不透明です。  

## プログラミングサンプル: 透かしの取得

次のコードスニペットは、PHPを使用してPDFファイルの最初のページにある各透かしを取得する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
            
    $formattedText = new FormattedText("Watermark", 
        (new Color())->getBlue()->getRgb(),
        (new facades_FontStyle())->getCourier(), 
        facades_EncodingType::$Identity_h, 
        true, 72.0);

    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    $artifact = new WatermarkArtifact();        
    $artifact->setText($formattedText);        
    $artifact->setArtifactHorizontalAlignment ($horizontalAlignment->getCenter());
    $artifact->setArtifactVerticalAlignment ($verticalAlignment->getCenter());
    $artifact->setRotation(45);
    $artifact->setOpacity(0.5);
    $artifact->setBackground(true);
    $document->getPages()->get_Item(1)->getArtifacts()->add($artifact);
    
    // 出力ドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```