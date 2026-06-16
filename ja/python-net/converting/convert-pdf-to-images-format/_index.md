---
title: Python でPDFをイメージフォーマットに変換する方法
linktitle: PDF を画像に変換
type: docs
weight: 70
url: /ja/python-net/convert-pdf-to-images-format/
lastmod: "2026-06-09"
description: .NET 経由の Aspose.PDF for Python を使用して、PDF ページを Python で TIFF、BMP、EMF、JPEG、PNG、GIF、SVG ファイルとしてレンダリングする方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python で PDF ページを TIFF、PNG、JPEG、GIF、BMP、EMF、SVG に変換
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルを一般的な画像形式に変換する方法について説明します。「TiffDevice」によるドキュメント全体の TIFF エクスポート、「BMPDevice」、「JpegDevice」、「PngDevice」、「PngDevice」、「GifDevice」などの「ImageDevice」サブクラスによるページごとのラスターイメージ生成、および「SVGSaveOptions」を使用した SVG へのベクターエクスポートについて説明します。各セクションには、PDF コンテンツを画像出力として保存するために必要なコアステップと Python の例が含まれています。
---

## パイソン PDF を画像に変換

**.NET 経由の Python 用 Aspose.PDF ** は、PDF コンテンツを画像に変換するいくつかの方法をサポートしています。実際には、ほとんどのワークフローでは次の 2 つのオプションのいずれかを使用します。

- PDF ページをラスターイメージ形式にレンダリングするためのデバイスアプローチ
- PDF コンテンツを SVG にエクスポートするための保存オプションアプローチ

この記事では、PDF ファイルを TIFF、BMP、EMF、JPEG、PNG、GIF、および SVG に変換する方法を説明します。

ライブラリには複数のレンダリングクラスが含まれています。 `DocumentDevice` 文書全体の変換用に設計されていますが、 `ImageDevice` 個々のページを対象としています。

## ドキュメントデバイスクラスを使用して PDF を変換

使用 `DocumentDevice` PDF 全体を 1 つの複数ページの TIFF ファイルにレンダリングする場合。

ザの [TIFF デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) クラスの基づき `DocumentDevice` そして、以下を提供します [処理する](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) PDF ファイル内のすべてのページを 1 つの TIFF 出力に変換する方法。

{{% alert color="success" %}}
**オンラインでPDFをTIFFに変換してみてください**

.NET 経由の Python 用 Aspose.PDF を使用するとオンラインアプリケーションが表示されます [「PDF から TIFF へ」](https://products.aspose.app/pdf/conversion/pdf-to-tiff)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF を TIFF に変換](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDF ページを 1 つの TIFF イメージに変換

.NET 経由の Python 用 Aspose.PDF では、PDF ファイル内のすべてのページを 1 つの TIFF イメージにレンダリングできます。

手順:Python で PDF を TIFF に変換する

1. を使用してソース PDF をロードします。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. 作成 [TIFF 設定](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) そして [TIFF デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) オブジェクト。
1. 圧縮、色深度、空白ページ処理などの TIFF オプションを設定します。
1. に電話してください [処理する](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) TIFF ファイルを書き込むメソッド。

次のコードスニペットは、すべての PDF ページを 1 つの TIFF 画像に変換する方法を示しています。

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_TIFF(infile, outfile):
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)
```

## イメージデバイスクラスを使用して PDF を変換する

使用 `ImageDevice` ラスターイメージ形式でページごとに出力する必要がある場合。

`ImageDevice` はの基本クラスです `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`、および `EmfDevice`.

- ザの [BMP デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) クラスを使用すると、PDF ページを BMP イメージに変換できます。
- ザの [EMF デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) クラスを使用すると、PDF ページを EMF イメージに変換できます。
- ザの [JPEG デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) クラスを使用すると、PDF ページを JPEG 画像に変換できます。
- ザの [PNG デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) クラスを使用すると、PDF ページを PNG 画像に変換できます。
- ザの [GIF デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) クラスでは、PDF ページを GIF 画像に変換できます。

ワークフローは各フォーマットで同じです。ドキュメントを読み込み、適切なデバイスを作成し、必要なページを処理します。

[BMP デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 公開する [処理する](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) 特定のページを BMP としてレンダリングするメソッド。他のイメージデバイスクラスも同じパターンに従うため、デバイスクラスを変更することでフォーマットを切り替えることができます。

次のリンクとコードサンプルは、PDF ページを一般的な画像形式にレンダリングする方法を示しています。

- [Python で PDF を BMP に変換](#convert-pdf-to-bmp)
- [Python で PDF を EMF に変換](#convert-pdf-to-emf)
- [Python で PDF を JPEG に変換](#convert-pdf-to-jpeg)
- [Python で PDF を PNG に変換](#convert-pdf-to-png)
- [Python で PDF を GIF に変換](#convert-pdf-to-gif)

手順:Python で PDF を画像 (BMP、EMF、JPG、PNG、GIF) に変換

1. を使用して PDF ファイルをロードします [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. 必要なインスタンスの作成 [イメージデバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) サブクラス:
    - [BMP デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (PDF ファイルを BMP に変換するには)
    - [EMF デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (PDF ファイルを EMF に変換するには)
    - [JPEG デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (PDFファイルをJPGに変換するには)
    - [PNG デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (PDF ファイルを PNG に変換するには)
    - [GIF デバイス](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (PDF を GIF に変換するには)
1. エクスポートしたいページをループ処理します。
1. に電話してください [イメージデバイス. プロセス ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) 各ページを画像として保存する方法。

### PDF ファイルを BMP ファイルに変換

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_BMP(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### PDF ファイルを EMF ファイルに変換

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_EMF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### PDF ファイルを JPEG ファイルに変換します

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_JPEG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### PDF ファイルを PNG ファイルに変換

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### PDF をデフォルトフォントで PNG に変換

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG_with_default_font(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### PDF ファイルを GIF 形式に変換

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_GIF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインでPDFをPNGに変換してみてください**

アプリケーションの動作例として、次の機能を確認してください。

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF ファイルから PNG へ」](https://products.aspose.app/pdf/conversion/pdf-to-png)ここで、機能や動作品質を調べてみるといいかもしれません。

[![アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 保存オプションクラスを使用して PDF を変換する

使用 `SaveOptions` PDF コンテンツを SVG にエクスポートする場合。

{{% alert color="success" %}}
**オンラインでPDFをSVGに変換してみてください**

.NET 経由の Python 用 Aspose.PDF を使用するとオンラインアプリケーションが表示されます [「PDF ファイルから SVG へ」](https://products.aspose.app/pdf/conversion/pdf-to-svg)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF を SVG に変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス（SVG）**は、2次元ベクターグラフィック用のXMLベースの形式です。SVG はベクターベースのままなので、Web、UI、デザインワークフローでスケーラブルな出力が必要な場合に役立ちます。

SVG ファイルはテキストベースで検索可能で、他のツールで簡単に後処理できます。

.NET 経由の Python 用 Aspose.PDF は、SVG を PDF に変換することも、PDF ページを SVG にエクスポートすることもできます。PDF から SVG への変換を行うには、以下を作成します。 [SVG 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) オブジェクトとそれを渡す [ドキュメント.save ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

以下の手順は、Python を使用して PDF ファイルを SVG に変換する方法を示しています。

手順:Python で PDF を SVG に変換する

1. を使用してソース PDF をロードします。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. を作成 [SVG 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) オブジェクトを作成し、必要なオプションを設定します。
1. に電話してください [ドキュメント.save ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使う `SvgSaveOptions` SVG 出力を書き込むためのインスタンス。

### PDF ファイルを SVG ファイルに変換します

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_SVG(infile, outfile):
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)
```

## 関連コンバージョン

- [画像形式を PDF に変換](/pdf/ja/python-net/convert-images-format-to-pdf/) JPG、PNG、TIFF、SVG、またはその他の画像ソースから PDF を再構築する必要がある場合。
- [PDF ファイルを HTML 形式に変換](/pdf/ja/python-net/convert-pdf-to-html/) ラスター画像の代わりにブラウザに優しい出力用。
- [PDF を他の形式に変換](/pdf/ja/python-net/convert-pdf-to-other-files/) EPUB、マークダウン、テキスト、XPS エクスポートワークフロー用。
