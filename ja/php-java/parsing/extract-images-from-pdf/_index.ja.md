---
title: PDFから画像を抽出する
linktitle: 画像を抽出
type: docs
weight: 20
url: /php-java/extract-images-from-the-pdf-file/
description: Aspose.PDF for PHPを使用してPDFから画像の一部を抽出する方法
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDFドキュメントの各ページにはリソース（画像、フォーム、フォント）が含まれています。これらのリソースには、[getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) メソッドを呼び出すことでアクセスできます。[Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) クラスには [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) が含まれており、[getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) メソッドを呼び出すことで画像のリストを取得できます。

したがって、ページから画像を抽出するには、ページへの参照を取得し、次にページリソース、最後に画像コレクションへのアクセスが必要です。
特定の画像は、例えばインデックスで抽出できます。

画像のインデックスは、[XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) オブジェクトを返します。
This object provides a [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

 ```php
 
    // PDFドキュメントを読み込む
    $document = new Document($inputFile);

    // ドキュメントの最初のページを取得する
    $page = $document->getPages()->get_Item(1);

    // ページ上の画像のコレクションを取得する
    $xImageCollection = $page->getResources()->getImages();

    // コレクションから最初の画像を取得する
    $xImage = $xImageCollection->get_Item(1);

    // 画像を保存するための新しいFileOutputStreamオブジェクトを作成する
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // 画像を出力ファイルに保存する
    $xImage->save($outputImage);

    // 出力画像ファイルを閉じる
    $outputImage->close();
```