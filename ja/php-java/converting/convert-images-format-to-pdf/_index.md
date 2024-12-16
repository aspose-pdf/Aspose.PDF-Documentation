---
title: さまざまな画像形式をPDFに変換
linktitle: 画像をPDFに変換
type: docs
weight: 60
url: /ja/php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: このトピックでは、Aspose.PDF for PHPライブラリを使用して、さまざまな画像形式をPDFに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for PHP** は、さまざまな形式の画像をPDFファイルに変換することを可能にします。私たちのライブラリは、BMP、CGM、DMF、JPG、PNG、SVG、TIFF形式など、最も人気のある画像形式を変換するためのコードスニペットを示しています。

## BMPをPDFに変換

**Aspose.PDF for PHP** ライブラリを使用して、BMPファイルをPDFドキュメントに変換します。

<abbr title="Bitmap Image File">BMP</abbr> 画像は、.BMP拡張子を持つビットマップ画像ファイルを表し、ビットマップデジタル画像を保存するために使用されます。これらの画像はグラフィックスアダプタに依存せず、デバイス独立ビットマップ (DIB) ファイル形式とも呼ばれます。BMPをPDFに変換するには、Aspose.PDF for PHP APIを使用できます。
 以下の手順に従って、BMP画像を変換することができます：

1. 新しいDocumentオブジェクトを作成する
1. ドキュメントに新しいページを追加する
1. 必要に応じて、ページのマージンを0に設定する
1. 新しいImageオブジェクトを作成し、入力BMPファイルを設定する
1. ページに画像を追加する
1. ドキュメントを出力PDFファイルに保存する

次のコードスニペットはこれらの手順に従い、PHPを使用してBMPをPDFに変換する方法を示しています:

```php
// 新しいDocumentオブジェクトを作成する
$document = new Document();

// ドキュメントに新しいページを追加する
$page = $document->getPages()->add();

// ページのマージンを0に設定する
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 新しいImageオブジェクトを作成し、入力BMPファイルを設定する
$image = new Image();
$image->setFile($inputFile);

// ページに画像を追加する
$page->getParagraphs()->add($image);

// ドキュメントを出力PDFファイルに保存する
$document->save($outputFile);
```

## CGMをPDFに変換

<abbr title="Computer Graphics Metafile">CGM</abbr>は、グラフィックス情報の保存と取得のためのベクター形式の2D画像ファイル形式を提供するISO標準です。CGMはデバイスに依存しない形式です。CGMは、3つの異なるエンコーディング方法をサポートするベクターグラフィックス形式です: バイナリ（プログラムの読み取り速度に最適）、文字ベース（最小のファイルサイズを生成し、データ転送を高速化）、またはクリアテキストエンコーディング（ユーザーがテキストエディタでファイルを読み取り、変更できるようにする）

以下のコードスニペットは、Aspose.PDF for PHPを使用してCGMファイルをPDF形式に変換する方法を示しています。

1. CGMファイルをロードするための特定のオプションを指定するために、[CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/)のインスタンスを作成します。
1. ソースファイル名とオプションを指定して[Document](https://reference.aspose.com/page/java/com.aspose.page/Document)クラスのインスタンスを作成します。
1. 希望するファイル名でドキュメントを保存します。

```php
$options = new CgmLoadOptions();

// 指定されたオプションを使用してCGMファイルをロードし、Documentオブジェクトを作成します
$document = new Document($inputFile, $options);

// ドキュメントをPDFファイルとして保存します
$document->save($outputFile);
```


## DICOMをPDFに変換

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr>は、医用画像情報を扱い、保存し、印刷し、送信するための標準です。これには、ファイル形式の定義とネットワーク通信プロトコルが含まれています。

Aspsoe.PDF for PHPを使用すると、DICOMファイルをPDF形式に変換できます。次のコードスニペットを確認してください：

1. 新しいDocumentオブジェクトを作成する
1. ドキュメントに新しいページを追加する
1. 必要に応じて、ページの余白を0に設定する
1. 新しいImageオブジェクトを作成し、入力BMPファイルを設定する
1. 画像のソースファイルとしてDICOMファイルを設定する
1. 画像のファイルタイプをDICOMに設定する
1. 画像をページに追加する
1. ドキュメントを出力PDFファイルとして保存する

```php
// 新しいDocumentオブジェクトを作成する
$document = new Document();

// ドキュメントに新しいページを追加する
$page = $document->getPages()->add();

// ページの余白を0に設定する
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 新しいImageオブジェクトを作成する
$image = new Image();

// 画像のソースファイルとしてDICOMファイルを設定する
$image->setFile($inputFile);

// 画像のファイルタイプをDICOMに設定する
$image->setFileType(ImageFileType::$Dicom);

// 画像をページに追加する
$page->getParagraphs()->add($image);

// ドキュメントをPDFファイルとして保存する
$document->save($outputFile);
```


{{% alert color="success" %}}
**DICOMをPDFにオンラインで変換してみてください**

Asposeはオンラインで無料アプリケーション["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)を提供しており、そこで機能と品質を試すことができます。

[![Aspose.PDF Convertion DICOM to PDF using Free App](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMFをPDFに変換

拡張メタファイル形式（<abbr title="Enhanced metafile format">EMF</abbr>）は、デバイスに依存しないグラフィカル画像を保存します。EMFのメタファイルは、任意の出力デバイスで解析された後に保存された画像をレンダリングできるように、時系列で可変長のレコードで構成されます。

EMFをPDFに変換するためのいくつかのアプローチがあります。

## Imageクラスを使用

PDFドキュメントはページで構成され、各ページには1つ以上の段落オブジェクトが含まれます。段落は、テキスト、画像、表、フローティングボックス、グラフ、見出し、フォームフィールド、または添付ファイルである可能性があります。

画像ファイルをPDF形式に変換するには、それを段落に囲みます。

画像をローカルハードドライブ上の物理的な位置、ウェブURLで見つかる場所、またはStreamインスタンスで変換することが可能です。

画像を追加するには:

1. com.aspose.pdf.Imageクラスのオブジェクトを作成します。
1. ページインスタンスの[Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs)コレクションに画像を追加します。
1. 画像のパスまたはソースを指定します。
    - 画像がハードドライブ上の場所にある場合は、[Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image)メソッドを使用してパスの場所を指定します。
    - 画像がFileInputStreamに配置されている場合は、画像を保持するオブジェクトを[Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image)メソッドに渡します。

次のコードスニペットは、画像オブジェクトをロードし、ページマージンを設定し、ページに画像を配置し、出力をPDFとして保存する方法を示しています。

```php
$inputFile = "sample.emf";

// 新しいDocumentオブジェクトを作成
$document = new Document();

// ドキュメントに新しいページを追加
$page = $document->getPages()->add();

// ページのマージンを0に設定
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 新しいImageオブジェクトを作成し、入力ファイルを設定
$image = new Image();
$image->setFile($inputFile);

// ページに画像を追加
$page->getParagraphs()->add($image);

// ドキュメントをPDFファイルとして保存
$document->save($outputFile);
```


## JPGをPDFに変換

JPGをPDFに変換する方法に悩む必要はありません。Apose.PDF for PHPライブラリが最適なソリューションを提供します。

Aspose.PDF for PHPを使用して、次の手順でJPG画像を簡単にPDFに変換できます。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを初期化する
1. ドキュメントに新しいページを追加する
1. ページの余白を0に設定する
1. 新しいImageオブジェクトを作成し、入力ファイルを設定する
1. 出力PDFを保存する

以下のコードスニペットは、PHPを使用してJPG画像をPDFに変換する方法を示しています。

```php
$inputFile = "sample.jpg";

// 新しいDocumentオブジェクトを作成
$document = new Document();

// ドキュメントに新しいページを追加
$page = $document->getPages()->add();

// ページの余白を0に設定
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 新しいImageオブジェクトを作成し、入力ファイルを設定
$image = new Image();
$image->setFile($inputFile);

// ページに画像を追加
$page->getParagraphs()->add($image);

// ドキュメントをPDFファイルとして保存
$document->save($outputFile);
```


{{% alert color="success" %}}
**JPGをPDFにオンラインで変換してみてください**

Asposeは、オンラインで無料のアプリケーション["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion JPG to PDF using Free App](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## PNGをPDFに変換

**Aspose.PDF for PHP**は、PNG画像をPDF形式に変換する機能をサポートしています。次のコードスニペットを確認してタスクを実現してください。

<abbr title="Portable Network Graphics">PNG</abbr>は、非可逆圧縮を使用するラスター画像ファイル形式の一種を指し、それがユーザーの間で人気を集めています。

以下の手順でPNGをPDF画像に変換できます：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを初期化する
1. ドキュメントに新しいページを追加する
1. ページの余白を0に設定する
1. 新しいImageオブジェクトを作成し、入力ファイルを設定する
1. 出力PDFを保存する

さらに、以下のコードスニペットは、PHPアプリケーションでPNGをPDFに変換する方法を示しています：

```php
$inputFile = "sample.png";

// 新しいDocumentオブジェクトを作成
$document = new Document();

// ドキュメントに新しいページを追加
$page = $document->getPages()->add();

// ページのマージンを0に設定
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 新しいImageオブジェクトを作成し、入力ファイルを設定
$image = new Image();
$image->setFile($inputFile);

// ページに画像を追加
$page->getParagraphs()->add($image);

// ドキュメントをPDFファイルとして保存
$document->save($outputFile);
```

{{% alert color="success" %}}
**PNGをPDFにオンラインで変換してみてください**

Asposeは、機能と品質を調査できるオンライン無料アプリケーション["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)を提供しています。

[![Aspose.PDF Convertion PNG to PDF using Free App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## SVGをPDFに変換する

スケーラブルベクターグラフィックス（SVG）は、2次元のベクターグラフィックスのためのXMLベースのファイル形式の仕様ファミリーであり、静的および動的（インタラクティブまたはアニメーション）です。SVG仕様は、1999年以来、ワールドワイドウェブコンソーシアム（W3C）によって開発されているオープン標準です。

SVG画像とその動作はXMLテキストファイルで定義されています。これは、それらが検索、インデックス、スクリプト化され、必要に応じて圧縮されることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeなどの描画プログラムを使用して作成する方が便利です。

## SVGファイルをPDF形式に変換する方法

SVGファイルをPDFに変換するには、[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions)オブジェクトを初期化するために使用される[SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions)と呼ばれるクラスを使用します。
 後で、このオブジェクトは[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)オブジェクトの初期化中に引数として渡され、PDFレンダリングエンジンがソースドキュメントの入力形式を判断するのに役立ちます。

以下のコードスニペットは、SVGファイルをPDF形式に変換するプロセスを示しています。

```php
// 新しいSvgLoadOptionsオブジェクトを作成
$loadOption = new SvgLoadOptions();

// 新しいDocumentオブジェクトを作成し、SVGファイルを読み込む
$document = new Document($inputFile, $loadOption);

// ドキュメントをPDFファイルとして保存
$document->save($outputFile);
```

{{% alert color="success" %}}
**SVG形式をPDFにオンラインで変換してみてください**

Aspose.PDF for PHPはオンラインの無料アプリケーション["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)を提供しており、その機能と品質を試して調査することができます。

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## TIFFをPDFに変換

**Aspose.PDF for PHP** ファイル形式は、単一フレームまたはマルチフレームの <abbr title="Tag Image File Format">TIFF</abbr> 画像をサポートしています。つまり、Java アプリケーションで TIFF 画像を PDF に変換できます。

TIFF または TIF、Tagged Image File Format は、このファイル形式標準に準拠するさまざまなデバイスでの使用を目的としたラスター画像を表します。TIFF 画像は、異なる画像を持つ複数のフレームを含むことができます。Aspose.PDF ファイル形式もサポートされており、単一フレームまたはマルチフレームの TIFF 画像を扱うことができます。したがって、Java アプリケーションで TIFF 画像を PDF に変換できます。したがって、以下の手順でマルチページの TIFF 画像をマルチページの PDF ドキュメントに変換する例を考えます。

1. 新しい Document オブジェクトを作成します
1. ドキュメントに新しいページを追加します
1. ページの余白を 0 に設定します
1. 新しい Image オブジェクトを作成します
1. 入力 TIFF 画像のファイルパスを設定します
1. ページに画像を追加します
1. ドキュメントを PDF ファイルとして保存します

さらに、次のコードスニペットは、マルチページまたはマルチフレームの TIFF 画像を PDF に変換する方法を示しています。

```php
// 新しいDocumentオブジェクトを作成
$document = new Document();

// ドキュメントに新しいページを追加
$page = $document->getPages()->add();

// ページのマージンを0に設定
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 新しいImageオブジェクトを作成
$image = new Image();

// 入力TIFF画像のファイルパスを設定
$image->setFile($inputFile);

// ページに画像を追加
$page->getParagraphs()->add($image);

// ドキュメントをPDFファイルとして保存
$document->save($outputFile);
```