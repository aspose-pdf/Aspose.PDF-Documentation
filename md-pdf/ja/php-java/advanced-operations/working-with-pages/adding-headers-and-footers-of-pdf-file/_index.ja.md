---
title: PDFのヘッダーとフッターを追加
linktitle: PDFのヘッダーとフッターを追加
type: docs
weight: 70
url: /php-java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for PHP via Javaは、TextStampクラスを使用してPDFファイルにヘッダーとフッターを追加することができます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFスタンプは、契約書、レポート、機密資料などで、文書がレビューされ、「既読」、「認定済み」、「機密」などとマークされていることを証明するためによく使用されます。この記事では、**Aspose.PDF for PHP via Java**を使用してPDF文書に画像スタンプとテキストスタンプを追加する方法を紹介します。

上記のコードスニペットを一行一行読むと、文法とコードロジックが非常に理解しやすいことがわかります。

## PDFファイルのヘッダーにテキストを追加

[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)クラスを使用して、PDFファイルのヘッダーにテキストを追加することができます。
 TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーにテキストを追加するには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、PageのAddStampメソッドを呼び出して、PDFのヘッダーにテキストを追加できます。

PDFのヘッダー領域にテキストを調整するように、TopMarginプロパティを設定する必要があります。また、HorizontalAlignmentをCenterに、VerticalAlignmentをTopに設定する必要があります。

次のコードスニペットは、PHPでPDFファイルのヘッダーにテキストを追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ヘッダーを作成
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // スタンプのプロパティを設定
    $textStamp->setTopMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // 1ページ目にフッターを追加
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## PDFファイルのフッターにテキストを追加する

TextStampクラスを使用して、PDFファイルのフッターにテキストを追加することができます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなどのテキストベースのスタンプを作成するために必要なプロパティを提供します。フッターにテキストを追加するには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、PageのaddStampメソッドを呼び出して、PDFのフッターにテキストを追加することができます。

以下のコードスニペットは、PHPを使用してPDFファイルのフッターにテキストを追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ヘッダーを作成
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // スタンプのプロパティを設定
    $textStamp->setBottomMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // 1ページ目にフッターを追加
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```


## PDFファイルのヘッダーに画像を追加する

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp)クラスを使用して、PDFファイルのヘッダーに画像を追加できます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなどの画像ベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、Pageの[addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp)メソッドを呼び出して、PDFのヘッダーに画像を追加できます。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // フッターを作成
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // スタンプのプロパティを設定
    $imageStamp->setTopMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // 1ページ目にフッターを追加
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```


以下のコードスニペットは、PHPを使用してPDFファイルのヘッダーに画像を追加する方法を示しています。

## PDFファイルのフッターに画像を追加

画像スタンプクラスを使用して、PDFファイルのフッターに画像を追加できます。画像スタンプクラスは、フォントサイズ、フォントスタイル、フォント色など、画像ベースのスタンプを作成するために必要なプロパティを提供します。フッターに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、PageのAddStampメソッドを呼び出して、PDFのフッターに画像を追加できます。

{{% alert color="primary" %}}

PDFのフッターエリアに画像を調整するように、BottomMarginプロパティを設定する必要があります。また、[HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment)を`Center`に、[VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment)を`Bottom`に設定する必要があります。

{{% /alert %}}

以下のコードスニペットは、PHPを使用してPDFファイルのフッターに画像を追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // フッターを作成
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // スタンプのプロパティを設定
    $imageStamp->setBottomMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // 1ページ目にフッターを追加
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## 1つのPDFファイルに異なるヘッダーを追加

ドキュメントのヘッダー/フッターセクションにTopMarginまたはBottom Marginプロパティを使用してTextStampを追加できることはわかっていますが、時には1つのPDFドキュメントに複数のヘッダー/フッターを追加する必要がある場合があります。**Aspose.PDF for PHP via Java**はこれを行う方法を説明しています。

この要件を達成するために、個々の[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)オブジェクトを作成し（必要なヘッダー/フッターの数に応じてオブジェクトの数が決まります）、それらをPDFドキュメントに追加します。
 個々のスタンプオブジェクトに対して異なるフォーマット情報を指定することもできます。次の例では、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトと3つの [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) オブジェクトを作成し、[addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) メソッドを使用してPDFのヘッダーセクションにテキストを追加しました。次のコードスニペットは、Aspose.PDF for PHP via Javaを使用してPDFファイルのフッターに画像を追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // 3つのスタンプを作成
    $stamp1 = new TextStamp("Header 1");
    $stamp2 = new TextStamp("Header 2");
    $stamp3 = new TextStamp("Header 3");
    
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();
    $fontStyles = new FontStyles();

    // スタンプの配置を設定（ページの上部に配置し、水平に中央揃え）
    $stamp1->setVerticalAlignment ($verticalAlignment->Top);
    $stamp1->setHorizontalAlignment($horizontalAlignment->Center);

    // フォントスタイルを太字に指定
    $stamp1->getTextState()->setFontStyle($fontStyles->Bold);
    // テキストの前景色を赤に設定
    $stamp1->getTextState()->setForegroundColor((new Color())->getRed());
    // フォントサイズを14に指定
    $stamp1->getTextState()->setFontSize(14);

    // 2番目のスタンプオブジェクトの垂直配置を上に設定
    $stamp2->setVerticalAlignment($verticalAlignment->Top);
    // スタンプの水平配置を中央揃えに設定
    $stamp2->setHorizontalAlignment($horizontalAlignment->Center);
    // スタンプオブジェクトのズーム係数を設定
    $stamp2->setZoom(10);

    // 3番目のスタンプオブジェクトのフォーマットを設定
    // スタンプオブジェクトの垂直配置情報を上に指定
    $stamp3->setVerticalAlignment($verticalAlignment->Top);
    // スタンプオブジェクトの水平配置情報を中央揃えに設定
    $stamp3->setHorizontalAlignment ($horizontalAlignment->Center);
    // スタンプオブジェクトの回転角度を設定
    $stamp3->setRotateAngle(35);
    // スタンプの背景色をピンクに設定
    $stamp3->getTextState()->setBackgroundColor ((new Color())->getPink());  
    // スタンプのフォントフェイス情報をVerdanaに変更
    $stamp3->getTextState()->setFont ((new FontRepository())->findFont("Verdana"));

    // 最初のスタンプを最初のページに追加
    $document->getPages()->get_Item(1)->addStamp($stamp1);
    // 2番目のスタンプを2番目のページに追加
    $document->getPages()->get_Item(2)->addStamp($stamp2);
    // 3番目のスタンプを3番目のページに追加
    $document->getPages()->get_Item(3)->addStamp($stamp3);
    
    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```