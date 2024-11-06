---
title: PDFに背景を追加 
linktitle: 背景を追加
type: docs
weight: 110
url: ja/php-java/add-backgrounds/
descriptions: PHPを使用してPDFファイルに背景画像を追加します。BackgroundArtifactオブジェクトを使用します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

背景画像は、透かしやその他の控えめなデザインを文書に追加するために使用できます。Aspose.PDF for PHP via Javaでは、各PDF文書はページのコレクションであり、各ページはアーティファクトのコレクションを含んでいます。[BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact)クラスを使用して、ページオブジェクトに背景画像を追加できます。

以下のコードスニペットは、BackgroundArtifactオブジェクトを使用してPDFページに背景画像を追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントオブジェクトに新しいページを追加
    $page = $document->getPages()->add();

    // BackgroundArtifactオブジェクトを作成    
    $background = new BackgroundArtifact();

    // backgroundArtifactオブジェクトの画像を指定
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // ページのアーティファクトコレクションにbackgroundArtifactを追加
    $page->getArtifacts()->add($background);

    // 更新されたPDFファイルを保存
    $document->save($outputFile);
    $document->close();
```