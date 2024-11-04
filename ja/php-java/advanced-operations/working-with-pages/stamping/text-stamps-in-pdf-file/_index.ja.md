---
title: PDFにテキストスタンプをプログラムで追加
linktitle: PDFファイルのテキストスタンプ
type: docs
weight: 20
url: /php-java/text-stamps-in-the-pdf-file/
description: PHPを使用してTextStampクラスでPDFファイルにテキストスタンプを追加します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Javaでテキストスタンプを追加

Aspose.PDF for PHP via Javaは、PDFファイルにテキストスタンプを追加するための[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)クラスを提供します。
 The [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) クラスは、スタンプオブジェクトのフォントサイズ、フォントスタイル、フォントカラーなどを指定するための必要なメソッドを提供します。テキストスタンプを追加するには、まず必要なメソッドを使用して [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトと [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) オブジェクトを作成する必要があります。その後、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスの [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) メソッドを呼び出して、PDFドキュメントにスタンプを追加できます。

以下のコードスニペットは、PDFファイルにテキストスタンプを追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $colors = new Color();
    // テキストスタンプを作成
    $textStamp = new TextStamp("Sample Stamp");
    // スタンプが背景かどうかを設定
    $textStamp->setBackground(true);
    // 起点を設定
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // スタンプを回転
    $textStamp->setRotate((new Rotation())->On90);
    // テキストプロパティを設定
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // 特定のページにスタンプを追加
    $pages->get_Item(1)->addStamp($textStamp);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## TextStampオブジェクトの配置を定義する

PDFドキュメントに透かしを追加することは、頻繁に要求される機能の1つであり、Aspose.PDF for PHP via Javaは画像やテキストの透かしを追加することが完全に可能です。[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)クラスは、PDFファイルにテキストスタンプを追加する機能を提供します。最近では、[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)オブジェクトを使用する際に、テキストの配置を指定する機能をサポートする必要がありました。この要件を満たすために、[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)クラスにsetTextAlignment(..)メソッドを導入しました。このメソッドを使用することで、水平テキスト配置を指定できます。

次のコードスニペットは、既存のPDFドキュメントを読み込み、[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)を追加する例を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // サンプル文字列でFormattedTextオブジェクトをインスタンス化
    $text = new FormattedText("This");

    // FormattedTextに新しいテキスト行を追加
    $text->addNewLineText("is sample");
    $text->addNewLineText("Center Aligned");
    $text->addNewLineText("TextStamp");
    $text->addNewLineText("Object");
    
    // テキストスタンプを作成
    $textStamp = new TextStamp($text);

    // テキストスタンプの水平配置を中央揃えに指定
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // テキストスタンプの垂直配置を中央揃えに指定
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // TextStampのテキスト水平配置を中央揃えに指定
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // スタンプオブジェクトの上部余白を設定
    $textStamp->setTopMargin(20);
    
    // 特定のページにスタンプを追加
    $pages->get_Item(1)->addStamp($textStamp);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();  
```


## PDFファイルにスタンプとして塗りつぶしストロークテキストを追加

テキストの追加と編集のシナリオにおけるレンダリングモードの設定を実装しました。ストロークテキストをレンダリングするには、[TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState)オブジェクトを作成し、RenderingModeをTextRenderingMode.StrokeTextに設定し、またStrokingColorプロパティの色を選択します。その後、bindTextState()メソッドを使用してTextStateをスタンプにバインドします。

次のコードスニペットは、塗りつぶしストロークテキストを追加する方法を示しています。

```php

   // 高度なプロパティを転送するためのTextStateオブジェクトを作成します
    $ts = new TextState();
        
    // ストロークの色を設定します
    $ts->setStrokingColor((new Color())->getGray());

    // テキストレンダリングモードを設定します
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // 入力PDFドキュメントを読み込みます
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAID IN FULL",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // TextStateをバインドします
    $stamp->bindTextState($ts);
    
    // X,Yの原点を設定します
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // スタンプを追加します
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```