---
title: PythonでPDFをPowerPointに変換
linktitle: PDFをPowerPointに変換
type: docs
weight: 30
url: /ja/python-net/convert-pdf-to-powerpoint/
description: PythonでPDFをPowerPointに変換する方法を学びます。PDFからPPTXへの変換、スライドを画像として扱うこと、そしてAspose.PDFを使用したカスタム画像解像度を含みます。
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFをPPTX形式のPowerPointスライドに変換
Abstract: この記事では、Aspose.PDF for Python via .NET を使用して PDF ファイルを PowerPoint プレゼンテーションに変換する方法を示します。PDF から PPTX への変換、スライドを画像として変換する方法、およびプレゼンテーション出力の画像解像度設定について説明します。
---

## PythonでPDFをPowerPointに変換

**Aspose.PDF for Python via .NET** を使用すると、Python コードから PDF ファイルを PowerPoint PPTX プレゼンテーションに変換できます。

PDF レポート、スライドデッキ、パンフレット、ハンドアウトなどを PowerPoint ファイルとして再利用する必要がある場合に、このワークフローを使用してください。変換中に、個々の PDF ページが PPTX ファイル内の個別のスライドに変換されます。

PDF から PPTX への変換中、テキストは選択可能なテキストとしてレンダリングされ、PowerPoint で更新できます。PDF ファイルを PPTX 形式に変換するために、Aspose.PDF は [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラス。 a を渡す `PptxSaveOptions` オブジェクトを第2引数として [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッド。

## PythonでPDFをPPTXに変換する

PDFをPPTXに変換するには、以下のコード手順を使用します。

手順：PythonでPDFをPowerPointに変換する

1. インスタンスを作成する [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. インスタンスを作成する [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラス。
1. 呼び出す [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッド。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## スライドを画像として PDF を PPTX に変換

{{% alert color="success" %}}
**PDF をオンラインで PowerPoint に変換してみてください**

Aspose.PDF はオンラインで提供します ["PDF から PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) 変換品質をテストできるアプリケーションです。


[![Aspose.PDF コンバージョン PDF から PPTX へ アプリ](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

検索可能な PDF を選択可能なテキストではなく画像として PPTX に変換する必要がある場合、Aspose.PDF はその機能を via [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラス。これを実現するには、プロパティを設定します [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) の [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 以下のコード例に示すように、クラスを 'true' に設定します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## カスタム画像解像度で PDF を PPTX に変換

このメソッドは、PDF ドキュメントを PowerPoint (PPTX) ファイルに変換し、品質向上のためにカスタム画像解像度 (300 DPI) を設定します。

1. PDF を 'ap.Document' オブジェクトにロードします。
1. 'PptxSaveOptions' インスタンスを作成します。
1. 'image_resolution' プロパティを 300 DPI に設定し、高品質なレンダリングを行います。
1. 定義された保存オプションを使用して、PDFをPPTXファイルとして保存します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## 関連する変換

- [PDF を Word に変換](/pdf/ja/python-net/convert-pdf-to-word/) スライドではなく、編集可能なドキュメント出力用です。
- [PDF を Excel に変換](/pdf/ja/python-net/convert-pdf-to-excel/) 元の PDF に表が多く含まれるビジネスデータの場合。
- [PDF を HTML に変換](/pdf/ja/python-net/convert-pdf-to-html/) ブラウザ対応のパブリッシング ワークフロー向け。
