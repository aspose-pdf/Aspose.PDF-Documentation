---
title: PythonでPDFをさまざまな画像形式に変換
linktitle: PDFを画像に変換
type: docs
weight: 70
url: /ja/python-net/convert-pdf-to-images-format/
lastmod: "2025-09-27"
description: Aspose.PDF for Python via .NET を使用して、PDF ページを PNG、JPEG、TIFF などの画像に変換する方法を探ります。
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: PythonでPDFを画像形式に変換する方法
Abstract: この記事では、Python と Aspose.PDF for Python ライブラリを使用して、PDF ファイルをさまざまな画像形式に変換する包括的なガイドを提供します。本文書では、TIFF、BMP、EMF、JPG、PNG、GIF、SVG などの画像形式への変換方法を概説します。主に 2 つの変換アプローチ、Device アプローチと SaveOption を取り上げます。Device アプローチでは、`DocumentDevice` や `ImageDevice` などのクラスを利用して、文書全体または特定ページの変換を行います。TIFF 用の `TiffDevice`、BMP 用の `BmpDevice`、EMF 用の `EmfDevice`、JPEG 用の `JpegDevice`、PNG 用の `PngDevice`、GIF 用の `GifDevice` など、各デバイスクラスの詳細な手順と Python コード例を示します。SVG 変換には `SvgSaveOptions` クラスを紹介します。また、これらの変換をオンラインで試すツールも紹介しています。
---

## PythonでPDFを画像に変換

**Aspose.PDF for Python** は PDF を画像に変換するためにいくつかのアプローチを提供します。一般的に、Device アプローチと SaveOption アプローチの 2 つを使用します。このセクションでは、これらのアプローチのいずれかを使用して、PDF 文書を BMP、JPEG、GIF、PNG、EMF、TIFF、SVG 形式の画像に変換する方法を示します。

ライブラリには、仮想デバイスを利用して画像を変換できる多数のクラスがあります。DocumentDevice は文書全体の変換を対象とし、ImageDevice は特定のページの変換を対象とします。

## DocumentDevice クラスを使用してPDFを変換

**Aspose.PDF for Python** は PDF ページを TIFF 画像に変換することを可能にします。

The [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (DocumentDevice に基づく) クラスは、PDF ページを TIFF 画像に変換できます。このクラスは [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) というメソッドを提供し、PDF ファイル内のすべてのページを単一の TIFF 画像に変換できます。

{{% alert color="success" %}}
**PDFをオンラインでTIFFに変換してみる**

Aspose.PDF for Python via .NET は、オンラインの無料アプリケーション [\"PDF to TIFF\"](https://products.aspose.app/pdf/conversion/pdf-to-tiff) を提供しており、機能と品質を調査することができます。

[![Aspose.PDF 変換 PDF to TIFF 無料アプリ](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDFページを1つのTIFF画像に変換

Aspose.PDF for Python は、PDF ファイル内のすべてのページを単一の TIFF 画像に変換する方法を説明しています。

手順: PythonでPDFをTIFFに変換

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのオブジェクトを作成します。
1. [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) と [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) のオブジェクトを作成します。
1. PDF 文書を TIFF に変換するために、[process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) メソッドを呼び出します。
1. 出力ファイルのプロパティを設定するには、[TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) クラスを使用します。

以下のコードスニペットは、すべての PDF ページを単一の TIFF 画像に変換する方法を示しています。

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    resolution = apdf.devices.Resolution(300)
    tiffSettings = apdf.devices.TiffSettings()
    tiffSettings.compression = apdf.devices.CompressionType.LZW
    tiffSettings.depth = apdf.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = apdf.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, path_outfile)

    print(infile + " converted into " + outfile)
```

## ImageDevice クラスを使用してPDFを変換

`ImageDevice` は `BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice`、`EmfDevice` の基底クラスです。

- The [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) クラスは、PDF ページを <abbr title="Bitmap Image File">BMP</abbr> 画像に変換できます。
- The [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) クラスは、PDF ページを <abbr title="Enhanced Meta File">EMF</abbr> 画像に変換できます。
- The [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) クラスは、PDF ページを JPEG 画像に変換できます。
- The [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) クラスは、PDF ページを <abbr title="Portable Network Graphics">PNG</abbr> 画像に変換できます。
- The [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) クラスは、PDF ページを <abbr title="Graphics Interchange Format">GIF</abbr> 画像に変換できます。

PDF ページを画像に変換する方法を見てみましょう。

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) クラスは、[process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) というメソッドを提供し、PDF ファイルの特定のページを BMP 画像形式に変換できます。他のクラスも同様のメソッドを持っています。したがって、PDF ページを画像に変換する必要がある場合は、必要なクラスのインスタンスを作成すれば済みます。

以下の手順と Python のコードスニペットは、この機能を示しています。

- [PythonでPDFをBMPに変換](#python-pdf-to-image)
- [PythonでPDFをEMFに変換](#python-pdf-to-image)
- [PythonでPDFをJPGに変換](#python-pdf-to-image)
- [PythonでPDFをPNGに変換](#python-pdf-to-image)
- [PythonでPDFをGIFに変換](#python-pdf-to-image)

手順: PythonでPDFを画像に変換 (BMP, EMF, JPG, PNG, GIF)

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用して PDF ファイルを読み込みます。
1. [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) のサブクラスのインスタンスを作成します。
* [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (PDF を BMP に変換するため)
* [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (PDF を Emf に変換するため)
* [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (PDF を JPG に変換するため)
* [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (PDF を PNG に変換するため)
* [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (PDF を GIF に変換するため)
1. [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) メソッドを呼び出して PDF から画像への変換を実行します。

### PDF を BMP に変換

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### PDF を EMF に変換

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### PDF を JPEG に変換

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```


### PDF を PNG に変換

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)

    device = apdf.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### デフォルトフォントで PDF を PNG に変換

```python

    from os import path
    import aspose.pdf as ap
    from io import FileIO


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### PDF を GIF に変換

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**PDF をオンラインで PNG に変換してみてください**

当社の無料アプリケーションの動作例として、次の機能をご確認ください。

Aspose.PDF for Python は、オンラインの無料アプリケーション["PDF を PNG に変換"](https://products.aspose.app/pdf/conversion/pdf-to-png) を提供しています。このアプリケーションで機能と品質をご確認いただけます。

[![無料アプリを使用して PDF を PNG に変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptions クラスを使用して PDF を変換

この記事のこの部分では、Python と SaveOptions クラスを使用して PDF を <abbr title="Scalable Vector Graphics">SVG</abbr> に変換する方法を示します。

{{% alert color="success" %}}
**PDF をオンラインで SVG に変換してみてください**

Aspose.PDF for Python via .NET は、オンラインの無料アプリケーション["PDF を SVG に変換"](https://products.aspose.app/pdf/conversion/pdf-to-svg) を提供しています。このアプリケーションで機能と品質をご確認いただけます。

[![無料アプリで Aspose.PDF の PDF を SVG に変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** は、2 次元ベクトルグラフィックス（静的および動的（インタラクティブまたはアニメーション））のための XML ベースのファイルフォーマットの仕様群です。SVG 仕様は、1999 年から World Wide Web Consortium（W3C）によって開発されているオープン標準です。

SVG 画像とその動作は XML テキストファイルで定義されています。つまり、検索、インデックス付け、スクリプト化、必要に応じて圧縮が可能です。XML ファイルであるため、SVG 画像は任意のテキストエディタで作成・編集できますが、Inkscape などの描画プログラムで作成する方が便利なことが多いです。

Aspose.PDF for Python は、SVG 画像を PDF 形式に変換する機能と、PDF ファイルを SVG 形式に変換する機能をサポートしています。この要件を実現するために、Aspose.PDF 名前空間に [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) クラスが導入されました。SvgSaveOptions のオブジェクトをインスタンス化し、[document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドの第2引数として渡します。

以下のコードスニペットは、Python で PDF ファイルを SVG 形式に変換する手順を示しています。

手順: Python で PDF を SVG に変換

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのオブジェクトを作成します。
1. 必要な設定を持つ [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) オブジェクトを作成します。
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出し、[SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) オブジェクトを渡して PDF ドキュメントを SVG に変換します。

### PDF を SVG に変換

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    save_options = apdf.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

