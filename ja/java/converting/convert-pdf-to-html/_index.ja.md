---
title: PDFファイルをHTML形式に変換する 
linktitle: PDFファイルをHTML形式に変換する 
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFがJavaライブラリを使用してPDFファイルをHTML形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF for Javaは、さまざまなファイル形式をPDFドキュメントに変換したり、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。この記事では、PDFファイルをHTML形式に変換し、PDFファイルの画像を特定のフォルダーに保存する方法について説明します。

{{% alert color="success" %}}
**PDFをHTMLにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンラインで無料のアプリケーション["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

大きなページ数のあるPDFファイルをHTML形式に変換すると、出力は単一のHTMLページとして表示されます。非常に長くなる可能性があります。ページサイズを制御するために、PDFからHTMLへの変換中に出力を複数ページに分割することが可能です。

## PDFページをHTMLに変換

Aspose.PDF for Javaは、さまざまなファイル形式をPDFドキュメントに変換し、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。この記事では、PDFファイルをHTML形式に変換し、PDFファイルからの画像を特定のフォルダーに保存する方法について説明します。

以下のコードスニペットは、PDFをHTMLに変換する際に使用できるすべてのオプションを示しています。

```java
// ソースPDFドキュメントを開く
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// ファイルをMSドキュメント形式で保存
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## PDFをHTMLに変換 - 出力をマルチページHTMLに分割

Aspose.PDF for Javaは、PDFドキュメントをHTMLを含むさまざまな出力形式に変換する機能をサポートしています。
 大きなPDFファイル（複数ページで構成されている）を変換する際、個々のPDFページを別々のHTMLファイルとして保存する必要がある場合があります。

複数ページの大きなPDFファイルをHTML形式に変換すると、出力が単一のHTMLページとして表示されます。それは非常に長くなる可能性があります。ページサイズを制御するために、PDFをHTMLに変換する際に出力を複数のページに分割することが可能です。以下のコードスニペットを使用してみてください。

```java
// ソースPDFドキュメントを開く
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// HTML SaveOptionsオブジェクトをインスタンス化する
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 出力を複数のページに分割することを指定する
htmlOptions.setSplitIntoPages(true);

// ドキュメントを保存する
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## PDFをHTMLに変換 - 画像をSVG形式で保存しないようにする

PDFからHTMLに変換する際のデフォルトの画像保存形式はSVGです。 PDFの変換中に、一部の画像がSVGベクター画像に変換されます。これは遅くなる可能性があります。代わりに、画像をPNGに変換することができます。これを可能にするために、Aspose.PDFはベクターにSVGを使用するか、PNGを作成するオプションがあります。

PDFファイルをHTML形式に変換する際に、画像のレンダリングを完全にSVG形式として削除するには、次のコードスニペットを試してください。

```java
 // PDFファイルをロード
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// HTML保存オプションオブジェクトのインスタンス化
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// PDFからHTMLへの変換中にSVG画像が保存されるフォルダを指定
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// 出力ファイルを保存
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## 変換中にSVG画像を圧縮する

PDFからHTMLへの変換中にSVG画像を圧縮するには、次のコードを試してください。

```java
// PDFファイルをロード
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// テストされた機能を持つHtmlSaveOptionを作成
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// もしあればSVG画像を圧縮
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## PDFをHTMLに変換 - 画像フォルダーを指定

デフォルトでは、PDFファイルをHTMLに変換する際、PDF内の画像は出力HTMLが作成される同じディレクトリに作成された別のフォルダーに保存されます。しかし、HTMLファイルを生成する際に画像を保存する別のフォルダーを指定する必要がある場合もあります。これを達成するために、[SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions)を導入しました。[SpecialFolderForAllImagesメソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-)は、画像を保存するターゲットフォルダーを指定するために使用されます。

```java
// PDFファイルを読み込む
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// 画像を保存する別のフォルダーを指定する
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## 本文内容のみの後続ファイルを作成する

以下のシンプルなコードスニペットを使用すると、出力HTMLをページに分割することができます。出力ページでは、すべてのHTMLオブジェクトは現在の位置にそのまま配置されなければなりません（フォントの処理と出力、CSSの作成と出力、画像の作成と出力）。ただし、出力HTMLには現在タグ内に配置されているコンテンツが含まれます（現在の「body」タグは省略されます）。

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## 透明なテキストのレンダリング

ソース/入力PDFファイルに前景画像で覆われた透明なテキストが含まれている場合、テキストのレンダリングに問題が生じる可能性があります。そのため、このようなシナリオに対応するために、`setSaveShadowedTextsAsTransparentTexts` および `setSaveTransparentTexts` メソッドを使用することができます。

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// HTML SaveOptionsオブジェクトをインスタンス化
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// ドキュメントを保存
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## PDFドキュメントレイヤーのレンダリング

PDFをHTMLに変換する際に、PDFドキュメントレイヤーを別々のレイヤータイプ要素でレンダリングできます。

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// HTML SaveOptionsオブジェクトをインスタンス化

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// 出力HTMLでPDFドキュメントレイヤーを個別にレンダリングするよう指定
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// ドキュメントを保存
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

PDFからHTMLへの変換は、Aspose.PDFの最も人気のある機能の1つです。これにより、PDFドキュメントビューアを使用せずにさまざまなプラットフォームでPDFファイルの内容を表示することが可能になります。出力HTMLはWWW標準に準拠しており、すべてのウェブブラウザで簡単に表示できます。この機能を使用することで、手持ちのデバイス上でPDFファイルを表示することが可能になります。PDF閲覧アプリケーションをインストールする必要がなく、単純なウェブブラウザを使用するだけで済みます。


## PDFからHTMLへの変換 - フォントリソースの除外

PDFをHTMLに変換する際に、すべてまたは一部のフォントリソースを除外することを意図している場合、Aspose.PDF for Java APIを使用して、HtmlSaveOptionsクラスを利用することでこれを実現できます。この目的のために、APIは2つのオプションを提供しています。

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - すべてのフォントのエクスポートを防ぐ
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - 特定のフォントのエクスポートを防ぐ（ハッシュを付けずにフォント名を指定）

フォントリソースを除外してPDFをHTMLに変換するには、次の手順を使用します。

1. HtmlSaveOptionsクラスの新しいオブジェクトを定義する
1. HtmlSaveOptions.ExcludeFontNameListでエクスポートを防ぐフォント名を定義して設定する
1. saveメソッドを使用してPDFをHTMLに変換する

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```