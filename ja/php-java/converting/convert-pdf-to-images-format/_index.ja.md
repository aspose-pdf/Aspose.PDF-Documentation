---
title: PDFを画像形式に変換 
linktitle: PDFを画像に変換
type: docs
weight: 70
url: /php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: このトピックでは、Aspose.PDFがPDFをさまざまな画像形式に変換する方法を示します。PDFページを数行のコードでPNG、JPEG、BMP画像に変換します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for PHP**を使用すると、BMP、JPEG、GIF、PNG、EMF、TIFF、SVGなどの画像形式にPDFドキュメントを変換することができます。変換は`Device`を使用する方法と`SaveOption`を使用する方法の2つのアプローチで行われます。

ライブラリには、仮想デバイスを使用して画像を変換するためのいくつかのクラスがあります。`DocumentDevice`はドキュメント全体の変換を目的としていますが、`ImageDevice`は特定のページ用です。

## DocumentDeviceクラスを使用してPDFを変換

**Aspose.PDF for PHP**はPDFページをTIFF画像に変換することを可能にします。

[TiffDeviceクラス](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice)は、PDFページをTIFF画像に変換することができます。
 このクラスは、PDFファイル内のすべてのページを1つのTIFF画像に変換することを可能にするProcessという名前のメソッドを提供します。

### PDFページを1つのTIFF画像に変換する

Aspose.PDF for PHPは、PDFファイル内のすべてのページを1つのTIFF画像に変換する方法を説明します：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを作成します。
1. ドキュメントを変換するために[Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-)メソッドを呼び出します。
1. 出力ファイルのプロパティを設定するために[TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings)クラスを使用します。

次のコードスニペットは、すべてのPDFページを1つのTIFF画像に変換する方法を示しています。

```php
// PDFドキュメントを読み込む
$document = new Document($inputFile);

// 新しいTiffSettingsオブジェクトを作成
$tiffSettings = new devices_TiffSettings();

// TIFF設定をカスタマイズするには、以下の行のコメントを解除
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// TIFF画像の解像度を設定
$resolution = new devices_Resolution(300);

// 指定された解像度と設定で新しいTiffDeviceオブジェクトを作成
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// TiffDeviceを使用してPDFドキュメントをTIFFに変換
$tiffDevice->process($document, $outputFile);
```

### 単一ページをTIFF画像に変換

Aspose.PDF for PHPを使用すると、PDFファイルの特定のページをTIFF画像に変換することができます。ページ番号を引数として受け取るProcess(..)メソッドのオーバーロードバージョンを使用します。以下のコードスニペットは、PDFの最初のページをTIFF形式に変換する方法を示しています。

```php
// PDFドキュメントを読み込む
$document = new Document($inputFile);

// 新しいTiffSettingsオブジェクトを作成する
$tiffSettings = new devices_TiffSettings();

// TIFF設定をカスタマイズするために次の行のコメントを外す
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// TIFF画像の解像度を設定する
$resolution = new devices_Resolution(300);

// 指定された解像度と設定で新しいTiffDeviceオブジェクトを作成する
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// TiffDeviceを使用してPDFドキュメントをTIFFに変換する
$tiffDevice->process($document, 1, 1, $outputFile);
```


### 変換中にBradleyアルゴリズムを使用する

Aspose.PDF for PHPは、LZW圧縮を使用してPDFをTIFFに変換する機能をサポートしており、その後AForgeを使用して二値化を適用できます。しかし、ある顧客からの要求で、一部の画像についてはOtsuを使用してしきい値を取得する必要があるため、Bradleyも使用したいとのことです。

```php
// 新しいTiffSettingsオブジェクトを作成
$tiffSettings = new devices_TiffSettings();

// TIFF設定をカスタマイズするには、次の行のコメントを解除
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// TIFF画像の解像度を設定
$resolution = new devices_Resolution(300);

// 指定された解像度と設定で新しいTiffDeviceオブジェクトを作成
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// TiffDeviceを使用してPDFドキュメントをTIFFに変換
$tiffDevice->process($document, 1, 1, $outputFile);

// 出力画像を保存するためのストリームオブジェクトを作成
$inStream = new java("java.io.FileInputStream", $outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### PDFページをピクセル化されたTIFF画像に変換する

PDFファイルのすべてのページをピクセル化されたTIFF形式に変換するには、IndexedConversionTypeのPixelatedオプションを使用します。

```php
// 新しいTiffSettingsオブジェクトを作成する
$tiffSettings = new devices_TiffSettings();

// TIFF設定をカスタマイズするために以下の行をコメント解除
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// 画像の明るさを設定
$tiffSettings->setBrightness(0.5f);
// IndexedConversion Typeを設定、デフォルト値はsimple
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);


$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// TIFF画像の解像度を設定
$resolution = new devices_Resolution(300);

// 指定された解像度と設定で新しいTiffDeviceオブジェクトを作成
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// TiffDeviceを使用してPDFドキュメントをTIFFに変換
$tiffDevice->process($document, 1, 1, $outputFile);

// 出力画像を保存するためにストリームオブジェクトを作成
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}
**PDFをTIFFにオンラインで変換してみてください**

Aspose.PDF for PHPでは、オンライン無料アプリケーション["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## ImageDeviceクラスを使ってPDFを変換する

`ImageDevice`は`BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice`、`EmfDevice`の祖先です。

- [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice)クラスは、PDFページを<abbr title="ビットマップ画像ファイル">BMP</abbr>画像に変換することを可能にします。
- [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice)クラスは、PDFページを<abbr title="拡張メタファイル">EMF</abbr>画像に変換することを可能にします。

- [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice)クラスは、PDFページをJPEG画像に変換することを可能にします。
- [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) クラスは、PDF ページを <abbr title="Portable Network Graphics">PNG</abbr> 画像に変換することを可能にします。
- [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) クラスは、PDF ページを <abbr title="Graphics Interchange Format">GIF</abbr> 画像に変換することを可能にします。

PDF ページを画像に変換する方法を見てみましょう。

[BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) クラスは、PDF ファイルの特定のページを BMP 画像形式に変換することを可能にする [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) という名前のメソッドを提供します。他のクラスも同じメソッドを持っています。したがって、PDF ページを画像に変換する必要がある場合は、必要なクラスをインスタンス化するだけです。

次のコード スニペットは、この可能性を示しています:

```php
// PDF ドキュメントを読み込む
$document = new Document($inputFile);

// ドキュメント内のページのコレクションを取得する
$pages = $document->getPages();

// ドキュメント内のページの総数を取得する
$count = $pages->size();

// PNG 画像の解像度を設定する
$resolution = new devices_Resolution(300);

// 指定された解像度で新しい PNG デバイスを作成する
$imageDevice = new devices_PngDevice($resolution);

// ドキュメント内の各ページをループする
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // 現在のページの出力画像ファイル名を設定する
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // コレクションから現在のページを取得する
    $page = $document->getPages()->get_Item($pageCount);

    // 現在のページを処理して PNG 画像として保存する
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**PDFをPNGにオンラインで変換してみる**

私たちの無料アプリケーションの動作例として、次の機能を確認してください。

Aspose.PDF for PHPは、オンライン無料アプリケーション["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)を提供しており、その機能と品質を調査することができます。

[![無料アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptionsクラスを使用してPDFを変換する

この記事のこの部分では、JavaとSaveOptionsクラスを使用してPDFを<abbr title="Scalable Vector Graphics">SVG</abbr>に変換する方法を示します。

{{% alert color="success" %}}
**PDFをSVGにオンラインで変換してみる**

Aspose.PDF for PHPは、オンライン無料アプリケーション["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF 無料アプリでPDFをSVGに変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス (SVG)** は、XMLベースのファイル形式で、静的および動的（インタラクティブまたはアニメーション）な2次元ベクターグラフィックスの仕様のファミリーです。SVG仕様は、1999年からワールドワイドウェブコンソーシアム (W3C) によって開発されているオープンスタンダードです。

SVG画像とその動作はXMLテキストファイルで定義されています。これにより、検索、インデックス化、スクリプト化、必要に応じて圧縮することができます。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeのような描画プログラムを使用して作成する方が便利なことが多いです。

### PDFページをSVG画像に変換する

Aspose.PDF for PHPは、PDFファイルをSVG形式に変換する機能をサポートしています。
 この要件を達成するために、[SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) クラスが com.aspose.pdf パッケージに導入されました。[SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) のオブジェクトをインスタンス化し、それを [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) メソッドの第2引数として渡します。

次のコードスニペットは、PDFファイルをSVG形式に変換する手順を示しています。

```php
// PDFドキュメントを読み込む
$document = new Document($inputFile);

// SvgSaveOptionsクラスのインスタンスを作成する
$saveOption = new SvgSaveOptions();

// PDFドキュメントをSVGとして保存する
$document->save($outputFile, $saveOption);
```