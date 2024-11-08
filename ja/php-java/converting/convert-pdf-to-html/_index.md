---
title: PDFファイルをHTML形式に変換 
linktitle: PDFファイルをHTML形式に変換
type: docs
weight: 50
url: /ja/php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: このトピックでは、Aspose.PDFがPHPライブラリを使用してPDFファイルをHTML形式に変換する方法を示しています。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF for PHPは、さまざまなファイル形式をPDFドキュメントに変換し、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。この記事では、PDFファイルをHTML形式に変換し、PDFファイルの画像を特定のフォルダーに保存する方法について説明します。

{{% alert color="success" %}}
**PDFをHTMLにオンラインで変換してみる**

Aspose.PDF for PHPは、オンラインで無料で利用できるアプリケーション["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF 無料アプリでPDFからHTMLに変換](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

大きなPDFファイルを複数ページからHTML形式に変換すると、出力は単一のHTMLページとして表示されます。非常に長くなることがあります。ページサイズを制御するために、PDFからHTMLへの変換中に出力をいくつかのページに分割することが可能です。

## PDFページをHTMLに変換

Aspose.PDF for PHPは、さまざまなファイル形式をPDFドキュメントに変換し、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。この記事では、PDFファイルをHTML形式に変換し、PDFファイルからの画像を特定のフォルダーに保存する方法について説明します。

次のコードスニペットは、PDFをHTMLに変換するときに使用できるすべての可能なオプションを示しています。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルをロードします
$document = new Document($inputFile);

// 新しいHtmlSaveOptionsオブジェクトを作成して、HTMLとしてドキュメントを保存します
$saveOption = new HtmlSaveOptions();

// 指定された保存オプションを使用して、ドキュメントをHTMLとして保存します
$document->save($outputFile, $saveOption);
```


## PDFをHTMLに変換 - 出力をマルチページHTMLに分割

Aspose.PDF for PHPは、PDFドキュメントをHTMLを含むさまざまな出力形式に変換する機能をサポートしています。ただし、複数ページで構成される大きなPDFファイルを変換する場合、個々のPDFページを別々のHTMLファイルとして保存する必要があるかもしれません。

複数ページを含む大きなPDFファイルをHTML形式に変換する場合、出力は単一のHTMLページとして表示されます。それは非常に長くなる可能性があります。ページサイズを制御するために、PDFからHTMLへの変換中に出力を複数のページに分割することが可能です。以下のコードスニペットを試してください。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルをロードする
$document = new Document($inputFile);

// ドキュメントをHTMLとして保存するための新しいHtmlSaveOptionsオブジェクトを作成する
$saveOption = new HtmlSaveOptions();

// 出力を複数のページに分割するよう指定する
$saveOption->setSplitIntoPages(true);

// 指定された保存オプションを使用してドキュメントをHTMLとして保存する
$document->save($outputFile, $saveOption);
```

## PDFをHTMLに変換 - 画像をSVG形式で保存しないようにする


画像をPDFからHTMLに変換する際のデフォルトの保存形式はSVGです。変換中に、PDFからの一部の画像はSVGベクター画像に変換されます。これは遅くなる可能性があります。代わりに、画像をPNGに変換することができます。これを許可するために、Aspose.PDFはベクター用にSVGを使用するか、PNGを作成するオプションがあります。

PDFファイルをHTML形式に変換する際に画像をSVG形式としてレンダリングすることを完全に削除するには、次のコードスニペットを使用してみてください。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルを読み込む
$document = new Document($inputFile);

// ドキュメントをHTMLとして保存するための新しいHtmlSaveOptionsオブジェクトを作成
$saveOption = new HtmlSaveOptions();

// PDFからHTMLへの変換中にSVG画像が保存されるフォルダーを指定
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// 指定された保存オプションを使用してドキュメントをHTMLとして保存
$document->save($outputFile, $saveOption);
```

## 変換中のSVG画像の圧縮

PDFからHTMLへの変換中にSVG画像を圧縮するには、次のコードを使用してみてください。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルを読み込む
$document = new Document($inputFile);

// ドキュメントをHTMLとして保存するための新しいHtmlSaveOptionsオブジェクトを作成
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// 指定された保存オプションを使用してドキュメントをHTMLとして保存
$document->save($outputFile, $saveOptions);
```

## PDFをHTMLに変換 - 画像フォルダを指定

デフォルトでは、PDFファイルをHTMLに変換する際、PDF内の画像は出力HTMLが作成される同じディレクトリに作成された別のフォルダに保存されます。しかし、HTMLファイルを生成するときに画像を保存するための異なるフォルダを指定する必要がある場合があります。これを達成するために、[SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions)を導入しました。

[setSpecialFolderForAllImagesメソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-)は、画像を保存するターゲットフォルダを指定するために使用されます。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルをロードします
$document = new Document($inputFile);

// ドキュメントをHTMLとして保存するための新しいHtmlSaveOptionsオブジェクトを作成します
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// 指定された保存オプションを使用してドキュメントをHTMLとして保存します
$document->save($outputFile, $saveOptions);
```

## 透明テキストのレンダリング

ソース/入力PDFファイルに前景画像によって影付けされた透明テキストが含まれている場合、テキストのレンダリングに問題が生じる可能性があります。そのため、このようなシナリオに対応するために、SaveShadowedTextsAsTransparentTextsプロパティとSaveTransparentTextsプロパティを使用できます。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルをロードします
$document = new Document($inputFile);

// ドキュメントをHTMLとして保存するための新しいHtmlSaveOptionsオブジェクトを作成します
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// 指定された保存オプションを使用してドキュメントをHTMLとして保存します
$document->save($outputFile, $saveOptions);
```


## PDFドキュメントレイヤーのレンダリング

PDFをHTMLに変換する際に、PDFドキュメントのレイヤーを別のレイヤータイプ要素でレンダリングできます：

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルをロードします
$document = new Document($inputFile);

// ドキュメントをHTMLとして保存するための新しいHtmlSaveOptionsオブジェクトを作成します
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// 指定された保存オプションを使用してドキュメントをHTMLとして保存します
$document->save($outputFile, $saveOptions);
```

PDFからHTMLへの変換は、Aspose.PDFの最も人気のある機能の一つです。PDFドキュメントビューアを使用せずに、さまざまなプラットフォームでPDFファイルの内容を表示することが可能になるためです。出力HTMLはWWW標準に準拠しており、すべてのウェブブラウザで簡単に表示できます。この機能を使用することで、PDFファイルをハンドヘルドデバイスでも表示でき、PDF閲覧アプリケーションをインストールする必要がなく、シンプルなウェブブラウザを使用するだけで済みます。