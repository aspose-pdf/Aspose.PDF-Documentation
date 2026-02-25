---
title: PythonでPDFをPowerPointに変換
linktitle: PDFをPowerPointに変換
type: docs
weight: 30
url: /ja/python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF for Python via .NET を使用して、PDF を PowerPoint プレゼンテーションに簡単に変換する方法を学びます。シームレスな PDF から PPTX への変換のためのステップバイステップ ガイドです。
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFをPowerPointに変換する方法
Abstract: この記事では、Python を使用して PDF ファイルを PowerPoint プレゼンテーション（特に PPTX 形式）に変換する包括的なガイドを提供します。Aspose.PDF for Python via .NET の使用を紹介し、PDF ページを PPTX ファイル内の個別スライドに変換できることで、変換プロセスを容易にします。記事では、Document クラスと PptxSaveOptions クラスのインスタンス作成や Save メソッドの利用など、変換に必要な手順を概説しています。また、PptxSaveOptions の特定のプロパティを設定することで、PDF を画像スライドとして PPTX に変換する機能も強調しています。変換プロセスを示すコードスニペットも掲載しています。さらに、PDF から PPTX への変換機能をテストできるオンラインアプリケーションへの参照を提供し、ユーザーが実際に体験できるようにしています。このほか、関連するさまざまなトピックや機能も列挙し、Python を用いた PDF から PowerPoint への変換の多様性とプログラマティックなアプローチを強調しています。
---

## PythonでPDFをPowerPointおよびPPTXに変換

**Aspose.PDF for Python via .NET** は PDF から PPTX への変換進行状況を追跡できます。

Aspose.Slides という API があり、PPT/PPTX プレゼンテーションの作成と操作機能を提供します。この API は <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> ファイルを PDF 形式に変換する機能も提供します。この変換では、PDF ファイルの各ページが PPTX ファイルの個別スライドに変換されます。

PDF から PPTX への変換では、テキストは選択/更新できる Text としてレンダリングされます。PDF ファイルを PPTX 形式に変換するには、Aspose.PDF が提供する [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラスを使用する必要があることに注意してください。PptxSaveOptions クラスのオブジェクトは、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) の第二引数として渡されます。以下のコードスニペットは、PDF ファイルを PPTX 形式に変換するプロセスを示しています。

## Python と Aspose.PDF for Python via .NET を使用したシンプルな PDF から PowerPoint への変換

PDF を PPTX に変換するには、Aspose.PDF for Python が以下のコード手順の使用を推奨します。

手順: PythonでPDFをPowerPointに変換

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのインスタンスを作成します。
1. [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラスのインスタンスを作成します。
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## スライドを画像として PDF を PPTX に変換

{{% alert color="success" %}}
**オンラインで PDF を PowerPoint に変換してみる**

Aspose.PDF はオンラインの無料アプリケーション ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) を提供しており、機能と品質を試すことができます。


[![Aspose.PDF 無料アプリによる PDF から PPTX への変換](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

検索可能な PDF を選択可能なテキストではなく画像として PPTX に変換する必要がある場合、Aspose.PDF は [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラスを介してその機能を提供します。これを実現するには、以下のコードサンプルに示すように、[PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラスのプロパティ [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) を 'true' に設定します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## カスタム画像解像度で PDF を PPTX に変換

このメソッドは、PDF ドキュメントを PowerPoint (PPTX) ファイルに変換し、品質向上のためにカスタム画像解像度（300 DPI）を設定します。

1. PDF を 'ap.Document' オブジェクトにロードします。
1. 'PptxSaveOptions' のインスタンスを作成します。
1. 高品質なレンダリングのために 'image_resolution' プロパティを 300 DPI に設定します。
1. 定義した保存オプションを使用して PDF を PPTX ファイルとして保存します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

