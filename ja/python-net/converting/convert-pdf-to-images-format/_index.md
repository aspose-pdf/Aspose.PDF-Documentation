---
title: PDFをPythonで異なる画像形式に変換する
linktitle: PDFを画像に変換
type: docs
weight: 70
url: ja/python-net/convert-pdf-to-images-format/
lastmod: "2022-12-23"
description: このトピックでは、Aspose.PDF for Pythonを使用してPDFをTIFF、BMP、EMF、JPEG、PNG、GIF、SVGなどのさまざまな画像形式に数行のコードで変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概要

この記事では、Pythonを使用してPDFを異なる画像形式に変換する方法を説明します。以下のトピックをカバーしています。

_画像形式_: **TIFF**
- [Python PDFをTIFFに変換](#python-pdf-to-tiff)
- [PythonでPDFをTIFFに変換](#python-pdf-to-tiff)
- [PythonでPDFの特定のページまたは単一ページをTIFFに変換](#python-pdf-to-tiff-pages)

_画像形式_: **BMP**
- [Python PDFをBMPに変換](#python-pdf-to-bmp)
- [PythonでPDFをBMPに変換](#python-pdf-to-bmp)
- [Python PDFをBMPに変換するコンバーター](#python-pdf-to-bmp)

_画像形式_: **EMF**
- [Python PDFをEMFに変換](#python-pdf-to-emf)
- [PythonでPDFをEMFに変換](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_画像形式_: **JPG**
- [Python PDFをJPGに変換](#python-pdf-to-jpg)
- [Python PDFからJPGへの変換](#python-pdf-to-jpg)
- [Python PDFをJPGに変換するコンバーター](#python-pdf-to-jpg)

_画像形式_: **PNG**
- [Python PDFをPNGに変換](#python-pdf-to-png)
- [Python PDFからPNGへの変換](#python-pdf-to-png)
- [Python PDFをPNGに変換するコンバーター](#python-pdf-to-png)

_画像形式_: **GIF**
- [Python PDFをGIFに変換](#python-pdf-to-gif)
- [Python PDFからGIFへの変換](#python-pdf-to-gif)
- [Python PDFをGIFに変換するコンバーター](#python-pdf-to-gif)

_画像形式_: **SVG**
- [Python PDFをSVGに変換](#python-pdf-to-svg)
- [Python PDFからSVGへの変換](#python-pdf-to-svg)
- [Python PDFをSVGに変換するコンバーター](#python-pdf-to-svg)

## PythonでPDFを画像に変換

**Aspose.PDF for Python** は、PDFを画像に変換するためにいくつかのアプローチを使用します。
 一般的に言って、私たちは2つのアプローチを使用します: Deviceアプローチを使用した変換とSaveOptionを使用した変換です。このセクションでは、これらのアプローチの1つを使用してPDFドキュメントをBMP、JPEG、GIF、PNG、EMF、TIFF、SVG形式の画像に変換する方法を示します。

ライブラリには、仮想デバイスを使用して画像を変換することを可能にするいくつかのクラスがあります。DocumentDeviceはドキュメント全体の変換を対象としていますが、ImageDeviceは特定のページ用です。

## DocumentDeviceクラスを使用してPDFを変換

**Aspose.PDF for Python** はPDFページをTIFF画像に変換することを可能にします。

[TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) （DocumentDeviceに基づく）クラスは、PDFページをTIFF画像に変換することを可能にします。このクラスは、PDFファイル内のすべてのページを単一のTIFF画像に変換することを可能にする[process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods)という名前のメソッドを提供します。

{{% alert color="success" %}}

**PDFをTIFFにオンラインで変換してみてください**
Aspose.PDF for Python via .NETは、オンラインで無料のアプリケーション["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDFページを1つのTIFF画像に変換

Aspose.PDF for Pythonは、PDFファイル内のすべてのページを単一のTIFF画像に変換する方法を説明します：

<a name="csharp-pdf-to-tiff"><strong>手順: PythonでPDFをTIFFに変換</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスのオブジェクトを作成します。
2. [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/)と[TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/)オブジェクトを作成します。

3. PDFドキュメントをTIFFに変換するために[process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods)メソッドを呼び出します。
4. 出力ファイルのプロパティを設定するために、[TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/)クラスを使用します。

以下のコードスニペットは、すべてのPDFページを単一のTIFF画像に変換する方法を示しています。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tiff.tiff"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # 解像度オブジェクトを作成
    resolution = ap.devices.Resolution(300)

    # TiffSettingsオブジェクトを作成
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    # TIFFデバイスを作成
    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)

    # 特定のページを変換し、画像をストリームに保存
    tiffDevice.process(document, output_pdf)
```


## ImageDeviceクラスを使用してPDFを変換する

`ImageDevice`は`BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice`、`EmfDevice`の祖先です。

- [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/)クラスを使用すると、PDFページを<abbr title="Bitmap Image File">BMP</abbr>画像に変換できます。
- [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/)クラスを使用すると、PDFページを<abbr title="Enhanced Meta File">EMF</abbr>画像に変換できます。
- [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/)クラスを使用すると、PDFページをJPEG画像に変換できます。
- [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/)クラスを使用すると、PDFページを<abbr title="Portable Network Graphics">PNG</abbr>画像に変換できます。

- [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/)クラスを使用すると、PDFページを<abbr title="Graphics Interchange Format">GIF</abbr>画像に変換できます。

以下は、PDFページを画像に変換する方法を見てみましょう。

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) クラスは、PDFファイルの特定のページをBMP画像形式に変換することを可能にする [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) という名前のメソッドを提供します。他のクラスも同じメソッドを持っています。したがって、PDFページを画像に変換する必要がある場合は、必要なクラスをインスタンス化するだけです。

以下の手順とPythonでのコードスニペットは、この可能性を示しています。

- [PythonでPDFをBMPに変換](#python-pdf-to-image)
- [PythonでPDFをEMFに変換](#python-pdf-to-image)
- [PythonでPDFをJPGに変換](#python-pdf-to-image)
- [PythonでPDFをPNGに変換](#python-pdf-to-image)
- [PythonでPDFをGIFに変換](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>手順: PythonでPDFを画像(BMP, EMF, JPG, PNG, GIF)に変換</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用してPDFファイルをロードします。
2. [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) のサブクラスのインスタンスを作成します。例えば、
   * [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (PDFをBMPに変換)
   * [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (PDFをEmfに変換)
   * [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (PDFをJPGに変換)
   * [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (PDFをPNGに変換)
   * [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (PDFをGIFに変換)
3. [ImageDevice.Process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) メソッドを呼び出して、PDFから画像への変換を実行します。

### PDFをBMPに変換

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_bmp"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # Resolutionオブジェクトを作成
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)

    for i in range(0, len(document.pages)):
        # 保存用のファイルを作成
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.bmp", 'x'
        )
        # 特定のページを変換し、画像をストリームに保存
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```


### PDFをEMFに変換

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_emf"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # 解像度オブジェクトを作成
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)

    for i in range(0, len(document.pages)):
        # 保存するファイルを作成
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.emf", 'x'
        )
        # 特定のページを変換し、画像をストリームに保存
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```  

### PDFをJPEGに変換

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_jpeg"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # 解像度オブジェクトを作成
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)

    for i in range(0, len(document.pages)):
        # 保存するファイルを作成
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.jpeg", "x"
        )
        # 特定のページを変換し、画像をストリームに保存
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()  
``` 


### PDFをPNGに変換

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_png"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # Resolutionオブジェクトを作成
    resolution = ap.devices.Resolution(300)
    device = ap.devices.PngDevice(resolution)

    for i in range(0, len(document.pages)):
        # 保存用のファイルを作成
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.png", 'x'
        )
        # 特定のページを変換し、ストリームに画像を保存
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
``` 

### PDFをGIFに変換

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_gif"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # Resolutionオブジェクトを作成
    resolution = ap.devices.Resolution(300)

    device = ap.devices.GifDevice(resolution)

    for i in range(0, len(document.pages)):
        # 保存用のファイルを作成
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.gif", 'x'
        )
        # 特定のページを変換し、ストリームに画像を保存
        device.process(document.pages[i + 1], imageStream)
        # ストリームを閉じる
        imageStream.close()  
``` 


{{% alert color="success" %}}
**PDFをPNGにオンラインで変換してみる**

無料アプリケーションの動作例として、次の機能を確認してください。

Aspose.PDF for Pythonは、オンライン無料アプリケーション["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)を提供しており、その機能や品質を調査することができます。

[![無料アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptionsクラスを使用してPDFを変換する

この記事のこの部分では、PythonとSaveOptionsクラスを使用してPDFを<abbr title="スケーラブル・ベクター・グラフィックス">SVG</abbr>に変換する方法を示します。

{{% alert color="success" %}}
**PDFをSVGにオンラインで変換してみる**

Aspose.PDF for Python via .NETは、オンライン無料アプリケーション["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)を提供しており、その機能や品質を調査することができます。

[![Aspose.PDF 無料アプリでPDFをSVGに変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス (SVG)** は、静的および動的（インタラクティブまたはアニメーション）の両方の二次元ベクターグラフィックのためのXMLベースのファイル形式の仕様ファミリーです。SVG仕様は、1999年以来World Wide Web Consortium (W3C)によって開発されているオープン標準です。

SVG画像とその動作はXMLテキストファイルで定義されています。これは、それらが検索、インデックス化、スクリプト化され、必要に応じて圧縮されることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeのような描画プログラムで作成する方が便利です。

Aspose.PDF for Pythonは、SVG画像をPDF形式に変換する機能をサポートしており、PDFファイルをSVG形式に変換する機能も提供しています。
 この要件を達成するために、[SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) クラスが Aspose.PDF 名前空間に導入されました。SvgSaveOptions のオブジェクトをインスタンス化し、それを [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドの第二引数として渡します。

以下のコードスニペットは、Python で PDF ファイルを SVG 形式に変換する手順を示しています。

<a name="csharp-pdf-to-svg"><strong>手順: Python で PDF を SVG に変換する</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのオブジェクトを作成します。
2. 必要な設定で [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) オブジェクトを作成します。
3. [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出し、[SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) オブジェクトを渡してPDF文書をSVGに変換します。

### PDFをSVGに変換する

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_svg.svg"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # SvgSaveOptionsのオブジェクトをインスタンス化する
    saveOptions = ap.SvgSaveOptions()

    # SVG画像をZipアーカイブに圧縮しない
    saveOptions.compress_output_to_zip_archive = False
    saveOptions.treat_target_file_name_as_directory = True

    # 出力をSVGファイルに保存する
    document.save(output_pdf, saveOptions)
```