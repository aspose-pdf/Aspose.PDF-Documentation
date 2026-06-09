---
title: Python でイメージフォーマットを PDF に変換する方法
linktitle: 画像を PDF に変換
type: docs
weight: 60
url: /ja/python-net/convert-images-format-to-pdf/
lastmod: "2026-06-09"
description: .NET 経由の Aspose.PDF for Python を使用して、BMP、CGM、DICOM、PNG、TIFF、EMF、SVG、その他の画像形式を Python で PDF に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python で画像を PDF に変換する方法
Abstract: この記事では、Python を使用してさまざまな画像形式を PDF に変換する方法、特に .NET 経由で Python 用 Aspose.PDF ライブラリを活用する方法に関する包括的なガイドを提供します。この記事では、BMP、CGM、DICOM、EMF、GIF、PNG、SVG、TIFF など、さまざまなイメージ形式について説明しています。各セクションでは、変換の実行に必要な手順を詳しく説明し、プロセスを説明するコードスニペットを提供しています。たとえば、BMP を PDF に変換するには、新しい PDF ドキュメントの作成、画像の配置の定義、画像の挿入、およびドキュメントの保存が必要です。同様に、CGM や DICOM などの形式の場合も、特定の読み込みオプションと処理手順が概説されています。この記事では、さまざまなエンコード方法をサポートしたり、シングルフレームイメージとマルチフレームイメージの両方を処理したりできることなど、このようなタスクに Aspose.PDF を使用する利点についても取り上げています。
---

## 関連コンバージョン

- [PDF を画像形式に変換](/pdf/ja/python-net/convert-pdf-to-images-format/) 逆のワークフローが必要なとき。
- [HTML ファイルを PDF に変換](/pdf/ja/python-net/convert-html-to-pdf/) Web コンテンツおよび MHTML ソース用。
- [他のファイル形式を PDF に変換](/pdf/ja/python-net/convert-other-files-to-pdf/) EPUB、XPS、テキスト、およびその他の非画像入力用。

## パイソン画像から PDF への変換

**.NET 経由の Python 用 Aspose.pdf ** を使用すると、さまざまな形式の画像を PDF ファイルに変換できます。このライブラリには、BMP、CGM、DICOM、EMF、JPG、PNG、SVG、TIFF 形式など、最も一般的な画像形式を変換するためのコードスニペットが紹介されています。

## BMP ファイルを PDF ファイルに変換します

.NET** ライブラリ経由で Python 用 **Aspose.pdf を使用して BMP ファイルを PDF ドキュメントに変換します。

<abbr title="Bitmap Image File">BMP</abbr> 画像は拡張子の付いたファイルです。BMP は、ビットマップデジタル画像の保存に使用されるビットマップ画像ファイルを表します。これらの画像はグラフィックアダプターに依存せず、デバイス独立ビットマップ (DIB) ファイル形式とも呼ばれます。

.NET API 経由で Aspose.PDF for Python を使用して BMP を PDF ファイルに変換できます。そのため、次の手順に従って BMP イメージを変換できます。

Python で BMP を PDF に変換する手順:

1. 空の PDF ドキュメントを作成します。
1. 必要なページを作成します。たとえば、A4を作成しましたが、独自の形式を指定できます。
1. 定義された長方形を使用して、（ファイル内の）画像をページ内に配置します。
1. 文書を PDF として保存します。

そのため、次のコードスニペットは次の手順に従い、Pythonを使用してBMPをPDFに変換する方法を示しています。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** BMPをオンラインでPDFに変換してみてください**

Asposeがオンライン申請書を提示します [「BMP から PDF へ」](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリを使用して BMP を PDF に変換](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGM ファイルを PDF に変換

.NET 経由で Aspose.PDF for Python を使用して CGM (コンピューターグラフィックスメタファイル) を PDF (またはサポートされている別の形式) に変換します。

<abbr title="Computer Graphics Metafile">CGM</abbr> は、CAD（コンピューター支援設計）およびプレゼンテーショングラフィックアプリケーションで一般的に使用されるコンピューターグラフィックスメタファイル形式のファイル拡張子です。CGM はベクターグラフィックス形式で、バイナリ (プログラムの読み取り速度に最適)、文字ベース (ファイルサイズが最小でデータ転送が速い)、クリアテキストエンコーディング (テキストエディタでファイルを読み込んだり変更したりできる) の 3 種類のエンコード方法をサポートしています。

CGM ファイルを PDF 形式に変換するには、次のコードスニペットを確認してください。

Python で CGM を PDF に変換する手順:

1. ファイルパスの定義
1. CGM のロードオプションを設定します。
1. CGM ファイルを PDF に変換
1. 変換メッセージを印刷

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## DICOM ファイルを PDF に変換

<abbr title="Digital Imaging and Communications in Medicine">ダイコム</abbr> フォーマットは、検査を受けた患者のデジタル医療画像および文書の作成、保存、送信、および視覚化に関する医療業界標準です。

**Aspose.pdf for Python**ではDICOM画像やSVG画像を変換できますが、画像を追加するには技術的な理由からPDFに追加するファイルの種類を指定する必要があります。

次のコードスニペットは、Aspose.PDF を使用して DICOM ファイルを PDF 形式に変換する方法を示しています。DICOM イメージをロードし、そのイメージを PDF ファイル内のページに配置して、出力を PDF として保存する必要があります。追加の pydicom ライブラリを使用してこの画像のサイズを設定します。ページ上に画像を配置したい場合は、このコードスニペットをスキップできます。

1. DICOM ファイルをロードします。
1. 画像のサイズを抽出します。
1. 印刷画像のサイズ。
1. 新しい PDF ドキュメントを作成します。
1. PDF 用の DICOM イメージを準備します。
1. PDF のページサイズと余白を設定します。
1. 画像をページに追加します。
1. PDF を保存します。
1. 変換メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**DICOMをオンラインでPDFに変換してみてください**

Asposeがオンライン申請書を提示します [「ダイコムから PDF へ」](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリを使って DICOM を PDF に変換](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF ファイルを PDF ファイルに変換します

<abbr title="Enhanced metafile format">EMF</abbr> グラフィカルイメージをデバイスに依存せずに保存します。EMF のメタファイルは時系列の可変長レコードで構成され、保存されたイメージを任意の出力デバイスで解析した後にレンダリングできます。

次のコードスニペットは、Python を使用して EMF を PDF に変換する方法を示しています。

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** EMFをオンラインでPDFに変換してみてください**

Asposeがオンライン申請書を提示します [「EMF から PDF へ」](https://products.aspose.app/pdf/conversion/emf-to-pdf/)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリを使用して EMF を PDF に変換](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## GIF ファイルを PDF に変換

.NET** ライブラリ経由で Python 用 **Aspose.pdf を使用して GIF ファイルを PDF ドキュメントに変換します。

<abbr title="Graphics Interchange Format">GIF</abbr> 品質を損なうことなく圧縮データを256色以下の形式で保存できます。ハードウェアに依存しない GIF 形式は、ネットワーク経由でビットマップ画像を転送するために CompuServe によって 1987 年に開発されました (GIF87a)。

そのため、次のコードスニペットは次の手順に従い、Pythonを使用してBMPをPDFに変換する方法を示しています。

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインでGIFをPDFに変換してみてください**

Asposeがオンライン申請書を提示します [「GIF ファイルから PDF へ」](https://products.aspose.app/pdf/conversion/gif-to-pdf/)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリを使って GIF を PDF に変換](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## PNG ファイルを PDF に変換

**.NET 経由の Python 用 Aspose.pdf ** サポート機能により、PNG 画像を PDF 形式に変換できます。次のコードスニペットを確認して、タスクを実行してください。

<abbr title="Portable Network Graphics">PNG</abbr> ロスレス圧縮を使用するラスターイメージファイル形式の一種を指し、ユーザーに人気があります。

以下の手順でPNGをPDF画像に変換できます。

1. 新しい PDF ドキュメントを作成します。
1. 画像の配置を定義します。
1. PDF を保存します。
1. 変換メッセージを印刷します。

さらに、以下のコードスニペットは、Pythonを使用してPNGをPDFに変換する方法を示しています。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインでPNGをPDFに変換してみてください**

Asposeがオンライン申請書を提示します [「PNG ファイルから PDF へ」](https://products.aspose.app/pdf/conversion/png-to-pdf/)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリを使用して PNG を PDF に変換](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVG ファイルを PDF に変換

**.NET 経由の Python 用 Aspose.pdf ** では、SVG 画像を PDF 形式に変換する方法と、ソース SVG ファイルのサイズを取得する方法について説明しています。

スケーラブルベクターグラフィックス（SVG）は、静的および動的（インタラクティブまたはアニメーション）の両方の2次元ベクターグラフィック用のXMLベースのファイル形式の仕様群です。SVG 仕様は 1999 年からワールド・ワイド・ウェブ・コンソーシアム (W3C) によって開発されてきたオープンスタンダードです。

<abbr title="Scalable Vector Graphics">SVG</abbr> イメージとその動作は XML テキストファイルで定義されます。つまり、画像を検索したり、索引を付けたり、スクリプトを作成したり、必要に応じて圧縮したりできるということです。SVG 画像は XML ファイルであるため、どのテキストエディターでも作成および編集できますが、多くの場合、Inkscape などの描画プログラムで作成したほうが便利です。

{{% alert color="success" %}}
**オンラインでSVG形式をPDFに変換してみてください**

.NET 経由の Python 用 Aspose.PDF を使用するとオンラインアプリケーションが表示されます [「SVG から PDF へ」](https://products.aspose.app/pdf/conversion/svg-to-pdf)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで SVG を PDF に変換](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

次のコードスニペットは、Aspose.PDF for Python を使用して SVG ファイルを PDF 形式に変換するプロセスを示しています。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## TIFF ファイルを PDF ファイルに変換します

**Aspose.pdf**ファイル形式がサポートされています。シングルフレームでもマルチフレームTIFF画像でもかまいません。つまり、TIFF 画像を PDF に変換できるということです。

TIFFまたはTIF（タグ付き画像ファイル形式）は、このファイル形式規格に準拠したさまざまなデバイスでの使用を目的としたラスター画像を表します。TIFF 画像には、異なる画像を含む複数のフレームを含めることができます。単一フレームでもマルチフレームの TIFF 画像でも Aspose.PDF ファイル形式がサポートされています。

他のラスターファイル形式のグラフィックと同じ方法で TIFF を PDF に変換できます。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## CDR ファイルを PDF に変換

次のコードスニペットは、CorelDRAW (CDR) ファイルをロードし、.NET 経由で Aspose.PDF for Python の 'cdrLoadOptions' を使用して PDF として保存する方法を示しています。

1. CDR ファイルのロード方法を設定するには、「CDRLoadOptions ()」を作成します。
1. CDR ファイルとロードオプションを使用して Document オブジェクトを初期化します。
1. 文書を PDF として保存します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## JPEG ファイルを PDF ファイルに変換します

この例は、.NET 経由で Aspose.PDF for Python を使用して JPEG ファイルを PDF ファイルに変換する方法を示しています。

1. 新しい PDF ドキュメントを作成します。
1. 新しいページを追加します。
1. 配置長方形を定義します (A4 サイズ:595x842 ポイント)。
1. 画像をページに挿入します。
1. PDF を保存します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
