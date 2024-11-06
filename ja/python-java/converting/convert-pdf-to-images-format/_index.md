---
title: PythonでPDFを異なる画像フォーマットに変換
linktitle: PDFを画像に変換
type: docs
weight: 70
url: ja/python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: このトピックでは、Aspose.PDF for Pythonを使用してPDFをTIFF、BMP、EMF、JPEG、PNG、GIF、SVGなどのさまざまな画像フォーマットに変換する方法を数行のコードで示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概要

この記事では、Pythonを使用してPDFを異なる画像フォーマットに変換する方法について説明します。以下のトピックをカバーしています。

_画像フォーマット_: **TIFF**
- [Python PDFをTIFFに](#python-pdf-to-tiff)
- [Python PDFをTIFFに変換](#python-pdf-to-tiff)
- [PythonでPDFの特定のページをTIFFに変換](#python-pdf-to-tiff-pages)

_画像フォーマット_: **BMP**
- [Python PDFをBMPに](#python-pdf-to-bmp)
- [Python PDFをBMPに変換](#python-pdf-to-bmp)
- [Python PDFをBMPコンバーター](#python-pdf-to-bmp)

_画像フォーマット_: **EMF**
- [Python PDFをEMFに](#python-pdf-to-emf)
- [Python PDFをEMFに変換](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_画像形式_: **JPG**
- [Python PDFをJPGに](#python-pdf-to-jpg)
- [PythonでPDFをJPGに変換](#python-pdf-to-jpg)
- [Python PDFからJPGコンバーター](#python-pdf-to-jpg)

_画像形式_: **PNG**
- [Python PDFをPNGに](#python-pdf-to-png)
- [PythonでPDFをPNGに変換](#python-pdf-to-png)
- [Python PDFからPNGコンバーター](#python-pdf-to-png)

_画像形式_: **GIF**
- [Python PDFをGIFに](#python-pdf-to-gif)
- [PythonでPDFをGIFに変換](#python-pdf-to-gif)
- [Python PDFからGIFコンバーター](#python-pdf-to-gif)

_画像形式_: **SVG**
- [Python PDFをSVGに](#python-pdf-to-svg)
- [PythonでPDFをSVGに変換](#python-pdf-to-svg)
- [Python PDFからSVGコンバーター](#python-pdf-to-svg)

## PythonでPDFを画像に変換

**Aspose.PDF for Python** は、PDFを画像に変換するためにいくつかのアプローチを使用します。
 一般的に、私たちは2つのアプローチを使用します: デバイスアプローチを使用した変換と、SaveOptionを使用した変換です。このセクションでは、これらのアプローチのいずれかを使用して、PDFドキュメントをBMP、JPEG、GIF、PNG、EMF、TIFF、およびSVG形式の画像に変換する方法を示します。

ライブラリには、仮想デバイスを使用して画像を変換するためのいくつかのクラスがあります。DocumentDeviceはドキュメント全体の変換を目的としており、ImageDeviceは特定のページ用です。

## DocumentDeviceクラスを使用してPDFを変換

**Aspose.PDF for Python**は、PDFページをTIFF画像に変換することを可能にします。

[TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/)（DocumentDeviceに基づく）クラスは、PDFページをTIFF画像に変換することを可能にします。このクラスは、PDFファイル内のすべてのページを単一のTIFF画像に変換することを可能にする[`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods)という名前のメソッドを提供します。

{{% alert color="success" %}}

**PDFをTIFFにオンラインで変換してみてください**
Aspose.PDF for Python via .NETは、オンラインの無料アプリケーション["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)を提供しており、機能性と品質を確認することができます。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDFページを1つのTIFF画像に変換

Aspose.PDF for Pythonは、PDFファイル内のすべてのページを1つのTIFF画像に変換する方法を説明します：

<a name="csharp-pdf-to-tiff"><strong>手順: PythonでPDFをTIFFに変換</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/)クラスのオブジェクトを作成します。
2. [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/)と[TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/)オブジェクトを作成します。

3. [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) メソッドを呼び出して、PDF ドキュメントを TIFF に変換します。
4. 出力ファイルのプロパティを設定するには、[TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) クラスを使用します。

次のコードスニペットは、すべての PDF ページを単一の TIFF 画像に変換する方法を示しています。

```python


from asposepdf import Api, Device

# ライセンスの初期化
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# PDF ドキュメントを開く
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# PDF ドキュメントを開く
document = Api.Document(input_pdf)
# Resolution オブジェクトを作成
resolution = Device.Resolution(300)

# TiffSettings オブジェクトを作成
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# TIFF デバイスを作成
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# 特定のページを変換し、画像をストリームに保存
tiffDevice.process(document, output_image)
```


## Convert PDF using ImageDevice class

`ImageDevice`は、`BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice`、および`EmfDevice`の祖先です。

- [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/)クラスを使用すると、PDFページを<abbr title="Bitmap Image File">BMP</abbr>画像に変換できます。
- [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/)クラスを使用すると、PDFページを<abbr title="Enhanced Meta File">EMF</abbr>画像に変換できます。
- [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/)クラスを使用すると、PDFページをJPEG画像に変換できます。
- [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/)クラスを使用すると、PDFページを<abbr title="Portable Network Graphics">PNG</abbr>画像に変換できます。

- [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/)クラスを使用すると、PDFページを<abbr title="Graphics Interchange Format">GIF</abbr>画像に変換できます。

以下は、PDFページを画像に変換する方法を見ていきます。

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) クラスは、PDFファイルの特定のページをBMP画像形式に変換することを可能にする、[Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) という名前のメソッドを提供しています。他のクラスも同じメソッドを持っています。したがって、PDFページを画像に変換する必要がある場合は、必要なクラスをインスタンス化するだけです。

次のステップとPythonのコードスニペットは、この可能性を示しています

- [PythonでPDFをBMPに変換](#python-pdf-to-image)
- [PythonでPDFをEMFに変換](#python-pdf-to-image)
- [PythonでPDFをJPGに変換](#python-pdf-to-image)
- [PythonでPDFをPNGに変換](#python-pdf-to-image)
- [PythonでPDFをGIFに変換](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>ステップ: PythonでPDFを画像に変換 (BMP, EMF, JPG, PNG, GIF)</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) クラスを使用してPDFファイルを読み込む。
2. [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/) のサブクラスのインスタンスを作成する。すなわち、
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) (PDFをBMPに変換するため)
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) (PDFをEmfに変換するため)
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) (PDFをJPGに変換するため)
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) (PDFをPNGに変換するため)
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) (PDFをGIFに変換するため)
3. PDFから画像への変換を実行するために、[ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods) メソッドを呼び出す。

### PDFをBMPに変換

```python
from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

# 解像度オブジェクトを作成
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # 保存するためのファイル名を作成
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # 特定のページを変換し、画像をファイルに保存
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### PDFをEMFに変換

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

# 解像度オブジェクトを作成
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # 保存するためのファイル名を作成
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # 特定のページを変換し、ファイルに画像を保存
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### PDFをJPEGに変換

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

# 解像度オブジェクトを作成
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # 保存するためのファイル名を作成
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # 特定のページを変換し、ファイルに画像を保存
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


### PDFをPNGに変換

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

# 解像度オブジェクトを作成
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # 保存用のファイル名を作成
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # 特定のページを変換し、画像をファイルに保存
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```

### PDFをGIFに変換

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

# 解像度オブジェクトを作成
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # 保存用のファイル名を作成
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # 特定のページを変換し、画像をファイルに保存
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


{{% alert color="success" %}}
**PDFをPNGにオンラインで変換してみてください**

無料アプリケーションの動作例として、次の機能を確認してください。

Aspose.PDF for Pythonは、オンライン無料アプリケーション「[PDF to PNG](https://products.aspose.app/pdf/conversion/pdf-to-png)」を提供しています。ここで機能と品質を確認してみてください。

[![無料アプリを使ってPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptionsクラスを使用してPDFを変換

この記事のこの部分では、PythonとSaveOptionsクラスを使用してPDFを<abbr title="Scalable Vector Graphics">SVG</abbr>に変換する方法を示します。

{{% alert color="success" %}}
**PDFをSVGにオンラインで変換してみてください**

Aspose.PDF for Python via .NETは、オンライン無料アプリケーション「[PDF to SVG](https://products.aspose.app/pdf/conversion/pdf-to-svg)」を提供しています。ここで機能と品質を確認してみてください。

[![無料アプリを使用してAspose.PDFでPDFをSVGに変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス (SVG)** は、二次元ベクターグラフィックスのためのXMLベースのファイル形式の仕様群であり、静的および動的（インタラクティブまたはアニメーション）なものです。SVG仕様は、1999年以来、ワールドワイドウェブコンソーシアム（W3C）によって開発されているオープン標準です。

SVG画像とその動作はXMLテキストファイルで定義されています。これは、検索、インデックス作成、スクリプト化、必要に応じて圧縮が可能であることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、通常はInkscapeなどの描画プログラムで作成する方が便利です。

Aspose.PDF for Pythonは、SVG画像をPDF形式に変換する機能をサポートしており、PDFファイルをSVG形式に変換する機能も提供しています。
 この要件を達成するために、[SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) クラスが Aspose.PDF 名前空間に導入されました。SvgSaveOptions のオブジェクトをインスタンス化し、それを [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドの第2引数として渡します。

以下のコードスニペットは、PythonでPDFファイルをSVG形式に変換する手順を示しています。

<a name="csharp-pdf-to-svg"><strong>手順: PythonでPDFをSVGに変換</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) クラスのオブジェクトを作成します。
2. 必要な設定で [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) オブジェクトを作成します。
3. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) メソッドを呼び出し、[SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) オブジェクトを渡してPDFドキュメントをSVGに変換します。

### PDFをSVGに変換

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```