---
title: Python で PDF をパワーポイントに変換
linktitle: PDF をパワーポイントに変換
type: docs
weight: 30
url: /ja/python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF を使って PDF を PowerPoint に変換する方法 (PDF から PPTX へ、スライドを画像に変換する方法、カスタム画像解像度など) を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF を PPTX パワーポイントスライドに変換
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルを PowerPoint プレゼンテーションに変換する方法を説明します。PDF から PPTX への変換、スライドを画像として変換、およびプレゼンテーション出力用の画像解像度の設定について説明します。
---

## Python で PDF をパワーポイントに変換

**.NET 経由の Python 用 Aspose.pdf ** を使用すると、PDF ファイルを Python コードから PowerPoint PPTX プレゼンテーションに変換できます。

このワークフローは、PDF レポート、スライドデッキ、パンフレット、または配布資料を PowerPoint ファイルとして再利用する必要がある場合に使用します。変換中、個々の PDF ページは PPTX ファイル内の個別のスライドに変換されます。

PDF から PPTX への変換中に、テキストを PowerPoint で更新できる選択可能なテキストとしてレンダリングできます。PDF ファイルを PPTX 形式に変換するために、Aspose.PDF は次の機能を提供しています。 [PPTX 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラス。パス a `PptxSaveOptions` の 2 番目の引数としてのオブジェクト [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

## Python で PDF を PPTX に変換

PDF を PPTX に変換するには、次のコードステップを使用します。

手順:Python で PDF をパワーポイントに変換

1. のインスタンスを作成 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. のインスタンスを作成 [PPTX 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラス。
1. に電話してください [ドキュメント.save ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## スライドを画像としてPDFをPPTXに変換

{{% alert color="success" %}}
**オンラインでPDFをパワーポイントに変換してみてください**

Aspose.PDF はオンラインで提供します [「PDF から PPTX へ」](https://products.aspose.app/pdf/conversion/pdf-to-pptx) 変換品質をテストできるアプリケーション。


[![Aspose.PDF アプリで PDF から PPTX に変換](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

検索可能な PDF を、選択可能なテキストではなく画像として PPTX に変換する必要がある場合に備えて、Aspose.PDF は次のような機能を提供します。 [PPTX 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラス。これを実現するには、プロパティを設定します。 [slides_as](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) の [PPTX 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) 次のコードサンプルに示すように、クラスを 'true' に設定します。

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

## カスタム画像解像度でPDFをPPTXに変換

この方法では、品質を向上させるためにカスタム画像解像度（300 DPI）を設定しながら、PDF ドキュメントを PowerPoint（PPTX）ファイルに変換します。

1. PDF を「AP.Document」オブジェクトに読み込みます。
1. 「PPTXSaveOptions」インスタンスを作成します。
1. 高品質のレンダリングを行うには、「image_resolution」プロパティを 300 DPI に設定します。
1. 定義した保存オプションを使用して PDF を PPTX ファイルとして保存します。

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

## 関連コンバージョン

- [PDF をワードに変換](/pdf/ja/python-net/convert-pdf-to-word/) スライドの代わりに編集可能なドキュメント出力用。
- [PDF をエクセルに変換](/pdf/ja/python-net/convert-pdf-to-excel/) ソース PDF に表形式のビジネスデータが含まれている場合。
- [PDF ファイルを HTML 形式に変換](/pdf/ja/python-net/convert-pdf-to-html/) ブラウザ対応のパブリッシングワークフロー用。
