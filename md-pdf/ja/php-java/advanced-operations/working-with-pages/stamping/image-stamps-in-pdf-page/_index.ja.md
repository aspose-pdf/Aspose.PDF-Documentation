---
title: PDFに画像スタンプをプログラムで追加 
linktitle: PDFファイルの画像スタンプ
type: docs
weight: 10
url: /php-java/image-stamps-in-pdf-page/
description: Aspose.PDF for PHP via Javaライブラリを使用して、ImageStampクラスを使用してPDFドキュメントに画像スタンプを追加します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルに画像スタンプを追加

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) クラスを使用して、PDFドキュメントに画像をスタンプとして追加できます。[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) クラスは、高さ、幅、不透明度などを指定するためのメソッドを提供します。

画像スタンプを追加するには:

1. 必要なプロパティを使用して[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトとImageStampオブジェクトを作成します。

1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスの [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) メソッドを呼び出して、PDF にスタンプを追加します。

以下のコードスニペットは、PDF ファイルに画像スタンプを追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // 画像スタンプを作成する
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // 特定のページにスタンプを追加
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close()
```

## スタンプ追加時の画像品質を制御する

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) クラスを使用すると、PDF ドキュメントに画像をスタンプとして追加できます。
 それにより、PDFファイルに画像を透かしとして追加する際に画像の品質を制御することもできます。これを可能にするために、[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) クラスに setQuality(...) という名前のメソッドが追加されました。同様のメソッドは、com.aspose.pdf.facades パッケージの [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) クラスにもあります。

次のコードスニペットは、PDFファイルにスタンプとして追加する際の画像品質を制御する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // 画像スタンプを作成
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();        
```

## フローティングボックスの背景としての画像スタンプ

Aspose.PDF APIを使用すると、フローティングボックスの背景として画像スタンプを追加できます。 FloatingBoxクラスのBackgroundImageプロパティを使用して、次のコードサンプルに示すようにフローティングボックスの背景画像スタンプを設定できます。

このコードスニペットは、PDFドキュメントを作成し、そこにFloatingBoxを追加するプロセスを示しています。FloatingBoxには、テキストフラグメント、ボーダー、背景画像、背景色が含まれています。結果として得られたドキュメントは、出力ファイルに保存されます。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // PDFドキュメントにページを追加
    $page = $pages->add();

    // FloatingBoxオブジェクトを作成
    $aBox = new FloatingBox(200, 100);

    // FloatingBoxの左位置を設定
    $aBox->setLeft(40);

    // FloatingBoxの上位置を設定
    $aBox->setTop(80);

    // FloatingBoxの水平位置を設定
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // テキストフラグメントをFloatingBoxの段落コレクションに追加
    $aBox->getParagraphs()->add(new TextFragment("main text"));

    // FloatingBoxのボーダーを設定
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // 背景画像を追加
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // FloatingBoxの背景色を設定
    $aBox->setBackgroundColor($colors->getYellow());

    // FloatingBoxをページオブジェクトの段落コレクションに追加
    $page->getParagraphs()->add($aBox);
    
    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```