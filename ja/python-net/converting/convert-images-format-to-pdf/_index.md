---
title: Pythonでさまざまな画像フォーマットをPDFに変換
linktitle: 画像をPDFに変換
type: docs
weight: 60
url: /ja/python-net/convert-images-format-to-pdf/
lastmod: "2025-09-01"
description: Pythonを使用して、BMP、CGM、DICOM、PNG、TIFF、EMF、SVGなどのさまざまな画像フォーマットをPDFに変換します。
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Pythonで画像をPDFに変換する方法
Abstract: この記事では、Python（.NET経由の Aspose.PDF for Python ライブラリ）を使用してさまざまな画像フォーマットをPDFに変換する包括的なガイドを提供します。この記事では、BMP、CGM、DICOM、EMF、GIF、PNG、SVG、TIFF などの画像フォーマットを取り上げています。各セクションでは、変換に必要な手順を詳述し、プロセスを示すコードスニペットを提供しています。例えば、BMP を PDF に変換するには、新しい PDF ドキュメントを作成し、画像の配置を定義し、画像を挿入してドキュメントを保存します。同様に、CGM、DICOM などのフォーマットでは、特定のロードオプションと処理手順が示されています。この記事では、Aspose.PDF を使用する利点として、さまざまなエンコーディング方式への対応や、単一フレームおよびマルチフレーム画像の両方を処理できる点を強調しています。
---

## Python 画像を PDF に変換

**Aspose.PDF for Python via .NET** は、さまざまな画像フォーマットを PDF ファイルに変換できるようにします。当ライブラリは、BMP、CGM、DICOM、EMF、JPG、PNG、SVG、TIFF 形式など、最も一般的な画像フォーマットの変換コードスニペットを示しています。

## BMP を PDF に変換

**Aspose.PDF for Python via .NET** ライブラリを使用して BMP ファイルを PDF ドキュメントに変換します。

<abbr title="Bitmap Image File">BMP</abbr> 画像は拡張子を持つファイルです。BMP はビットマップ画像ファイルを表し、ビットマップデジタル画像の保存に使用されます。これらの画像はグラフィックアダプタに依存せず、デバイス非依存ビットマップ (DIB) ファイル形式とも呼ばれます。

Aspose.PDF for Python via .NET API を使用して BMP を PDF ファイルに変換できます。したがって、BMP 画像を変換するために次の手順に従うことができます。

Python で BMP を PDF に変換する手順:

1. 空の PDF ドキュメントを作成します。
1. 必要なページを作成します。例えば、A4 を作成しましたが、独自のフォーマットを指定することもできます。
1. 定義された矩形を使用して、ページ内に画像（infile から）を配置します。
1. ドキュメントを PDF として保存します。

以下のコードスニペットはこれらの手順に従い、Python を使用して BMP を PDF に変換する方法を示しています。

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインで BMP を PDF に変換してみる**

Aspose はオンラインの無料アプリケーション ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/) を提供しています。ここで機能と品質を確認できます。

[![Aspose.PDF 無料アプリで BMP を PDF に変換](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGM を PDF に変換

Aspose.PDF for Python via .NET を使用して、CGM（Computer Graphics Metafile）を PDF（または他のサポート形式）に変換します。

<abbr title="Computer Graphics Metafile">CGM</abbr> は、CAD（コンピュータ支援設計）やプレゼンテーション用グラフィックアプリケーションで一般的に使用される Computer Graphics Metafile 形式のファイル拡張子です。CGM はベクターグラフィック形式で、バイナリ（プログラムの読み取り速度に最適）、文字ベース（最小のファイルサイズを生成し、データ転送が高速）、クリアテキストエンコーディング（テキストエディタでファイルを読み書き可能）の 3 つのエンコード方式をサポートします。

次のコードスニペットを確認して、CGM ファイルを PDF 形式に変換してください。

Python で CGM を PDF に変換する手順:

1. ファイルパスを定義する
1. CGM のロードオプションを設定する。
1. CGM を PDF に変換する
1. 変換メッセージを出力する

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = apdf.CgmLoadOptions()

    # Open PDF document
    document = apdf.Document(path_infile, options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## DICOM を PDF に変換

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> フォーマットは、医療業界におけるデジタル医療画像や検査患者の文書の作成、保存、転送、可視化の標準です。

**Aspose.PDF for Python** は DICOM と SVG 画像の変換を可能にしますが、技術的な理由により画像を追加する際には PDF に追加するファイルのタイプを指定する必要があります。

以下のコードスニペットは、Aspose.PDF を使用して DICOM ファイルを PDF 形式に変換する方法を示しています。DICOM 画像を読み込み、PDF ファイルのページに画像を配置し、出力を PDF として保存する必要があります。画像のサイズを設定するために、追加の pydicom ライブラリを使用します。ページ上で画像の位置を指定したい場合は、このコードスニペットをスキップできます。

1. 新しい 'ap.Document()' を初期化し、ページを追加する
1. DICOM 画像を挿入する。apdf.Image() を作成し、タイプを DICOM に設定し、ファイルパスを割り当てる。
1. ページサイズを調整する。PDF ページの寸法を DICOM 画像サイズに合わせ、余白を削除する。
1. 画像をページに追加し、ドキュメントを出力ファイルに保存する。

1. DICOM ファイルを読み込む。
1. 画像の寸法を抽出する。
1. 画像サイズを出力する。
1. 新しい PDF ドキュメントを作成します。
1. PDF 用に DICOM 画像を準備します。
1. PDF のページサイズと余白を設定します。
1. 画像をページに追加します。
1. PDF を保存します。
1. 変換メッセージを表示します。

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    # Load the DICOM file
    dicom_file = pydicom.dcmread(path_infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = apdf.Document()
    page = document.pages.add()
    image = apdf.Image()
    image.file_type = apdf.ImageFileType.DICOM
    image.file = path_infile

    # Set page dimensions

    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインで DICOM を PDF に変換してみましょう**

Aspose はオンライン無料アプリケーション ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/) を提供しています。機能と品質を試すことができます。

[![Aspose.PDF の無料アプリを使用した DICOM から PDF への変換](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF を PDF に変換

<abbr title="Enhanced metafile format">EMF</abbr> はデバイスに依存しない形でグラフィック画像を保存します。EMF のメタファイルは可変長レコードで構成され、時系列順に並んでおり、任意の出力デバイスで解析後に画像をレンダリングできます。

以下のコードスニペットは、Python で EMF を PDF に変換する方法を示しています。

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(path_infile, rectangle)

    # Save the file into PDF format
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインで EMF を PDF に変換してみましょう**

Aspose はオンライン無料アプリケーション ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/) を提供しています。機能と品質を試すことができます。

[![Aspose.PDF の無料アプリを使用した EMF から PDF への変換](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## GIF を PDF に変換

**Aspose.PDF for Python via .NET** ライブラリを使用して GIF ファイルを PDF ドキュメントに変換します。

<abbr title="Graphics Interchange Format">GIF</abbr> は最大 256 色の形式で、品質を損なうことなく圧縮データを保存できます。ハードウェアに依存しない GIF 形式は、1987 年に CompuServe によってビットマップ画像をネットワークで送信するために開発されました。

以下のコードスニペットはこれらの手順に従い、Python を使用して BMP を PDF に変換する方法を示しています。

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインで GIF を PDF に変換してみましょう**

Aspose はオンライン無料アプリケーション ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/) を提供しています。機能と品質を試すことができます。

[![Aspose.PDF の無料アプリを使用した GIF から PDF への変換](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## PNG を PDF に変換

**Aspose.PDF for Python via .NET** は PNG 画像を PDF 形式に変換する機能をサポートしています。次のコードスニペットでタスクの実装方法をご確認ください。

<abbr title="Portable Network Graphics">PNG</abbr> は、ロスレス圧縮を使用するラスター画像ファイル形式で、ユーザーに人気があります。

以下の手順で PNG を PDF 画像に変換できます。

1. 新しい PDF ドキュメントを作成します。
1. 画像の配置を定義します。
1. PDF を保存します。
1. 変換メッセージを表示します。

さらに、以下のコードスニペットは Python で PNG を PDF に変換する方法を示しています。

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインで PNG を PDF に変換してみましょう**

Aspose はオンライン無料アプリケーション ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/) を提供しています。機能と品質を試すことができます。

[![Aspose.PDF の無料アプリを使用した PNG から PDF への変換](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVG を PDF に変換

**Aspose.PDF for Python via .NET** は、SVG 画像を PDF 形式に変換する方法と、元の SVG ファイルの寸法を取得する方法を解説しています。

Scalable Vector Graphics（SVG）は、2 次元ベクターグラフィックス（静的および動的（インタラクティブまたはアニメーション））のための XML ベースのファイル形式に関する仕様群です。SVG 仕様は、1999 年から World Wide Web Consortium（W3C）によって開発されているオープンスタンダードです。

<abbr title="Scalable Vector Graphics">SVG</abbr> 画像とその挙動は XML テキストファイルで定義されます。つまり、検索、インデックス付け、スクリプト実行、必要に応じて圧縮が可能です。XML ファイルであるため、任意のテキストエディタで作成・編集できますが、Inkscape などの描画プログラムで作成する方が便利な場合が多いです。

{{% alert color="success" %}}
**オンラインで SVG 形式を PDF に変換してみましょう**

Aspose.PDF for Python via .NET はオンライン無料アプリケーション ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf) を提供しています。機能と品質を試すことができます。

[![Aspose.PDF の無料アプリを使用した SVG から PDF への変換](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

以下のコードスニペットは、Aspose.PDF for Python を使用して SVG ファイルを PDF 形式に変換するプロセスを示しています。

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.SvgLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## TIFF を PDF に変換

**Aspose.PDF** ファイル形式がサポートされており、単一フレームでもマルチフレーム TIFF 画像でも対応しています。つまり、TIFF 画像を PDF に変換できるということです。

TIFF（または TIF）は Tagged Image File Format の略で、このファイル形式標準に準拠したさまざまなデバイスで使用されるラスタ画像を表します。TIFF 画像は異なる画像を含む複数のフレームを持つことができます。Aspose.PDF のファイル形式もサポートされており、単一フレームでもマルチフレーム TIFF 画像でも対応しています。

TIFF を PDF に変換するには、他のラスター画像形式と同様の方法で行うことができます:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## CDR を PDF に変換

以下のコードスニペットは、Aspose.PDF for Python via .NET で 'CdrLoadOptions' を使用して CorelDRAW（CDR）ファイルをロードし、PDF として保存する方法を示しています。

1. CDR ファイルのロード方法を設定するために 'CdrLoadOptions()' を作成します。
1. CDR ファイルとロードオプションを使用して Document オブジェクトを初期化します。
1. ドキュメントを PDF として保存します。

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.CdrLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## JPEG を PDF に変換

この例は、Aspose.PDF for Python via .NET を使用して JPEG を PDF ファイルに変換する方法を示しています。

1. 新しい PDF ドキュメントを作成します。
1. 新しいページを追加します。
1. 配置矩形を定義します（A4 サイズ：595×842 ポイント）。
1. 画像をページに挿入します。
1. PDF を保存します。

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

