---
title: Python で PDF ファイルを最適化する方法
linktitle: PDF を最適化
type: docs
weight: 30
url: /ja/python-net/optimize-pdf/
description: Aspose.PDF を使用して Python で PDF ファイルのサイズを最適化、圧縮、縮小する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ページを圧縮する
Abstract: この記事では、PDFファイルを最適化してWebページ、電子メール、ストレージシステムなどのさまざまなプラットフォームでサイズを縮小し、パフォーマンスを向上させるための包括的なガイドを提供します。最適化手法には、画像サイズの縮小、未使用リソースの削除、フォントの埋め込み解除などがあります。Aspose.PDF for Python の「最適化」メソッドと「リソース最適化」メソッドを利用して、Web 用に PDF を最適化し、ファイル全体のサイズを小さくする具体的な方法について説明します。最適化戦略は「OptimizationOptions」でカスタマイズでき、画像の圧縮、未使用のオブジェクトやストリームの削除、重複ストリームのリンク、フォントの埋め込み解除などの対象を絞ったアクションが可能になります。その他の方法としては、注釈のフラット化、フォームフィールドの削除、PDF ファイルを RGB からグレースケールに変換してサイズをさらに小さくする方法があります。また、FlateDecode圧縮を使用して画像を最適化することで、品質と機能を維持しながら効果的なPDFファイル管理を実現する方法についても取り上げています。
---

PDF 文書には追加のデータが含まれている場合があります。PDF ファイルのサイズを小さくすると、ネットワーク転送とストレージを最適化するのに役立ちます。これは、Web ページへの公開、ソーシャルネットワークでの共有、電子メールによる送信、またはストレージへのアーカイブに特に便利です。PDF を最適化するにはいくつかの手法を使用できます。

Web 配信、E メール共有、ストレージの節約、または印刷に適した出力のために、文書をゼロから再構築せずに PDF サイズを小さくする必要がある場合は、このページを使用してください。

- オンラインブラウジング用にページコンテンツを最適化する
- すべての画像を縮小または圧縮
- ページコンテンツの再利用を有効にする
- 重複ストリームをマージ
- フォントの埋め込み解除
- 未使用のオブジェクトを削除する
- フラットニングフォームフィールドを削除する
- 注釈を削除またはフラット化する

{{% alert color="primary" %}}

 最適化方法の詳細な説明は、最適化方法の概要ページにあります。

{{% /alert %}}

## PDF ドキュメントを Web 用に最適化

最適化、またはWebのリニアライゼーションとは、Webブラウザーを使用してオンラインブラウジングに適したPDFファイルを作成するプロセスを指します。ファイルを Web 表示用に最適化するには:

1. で入力ドキュメントを開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 対象。
1. を使う [最適化](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。
1. を使用して最適化されたドキュメントを保存します [保存 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

次のコードスニペットは、PDF ドキュメントを Web 用に最適化する方法を示しています。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## PDF のサイズを小さくする

ザの [リソースの最適化 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用すると、不要な情報を削除してドキュメントサイズを小さくすることができます。デフォルトでは、このメソッドは次のように機能します。

- ドキュメントページで使用されていないリソースは削除されます
- 等しいリソースが 1 つのオブジェクトに結合されます
- 未使用のオブジェクトは削除されます

以下のスニペットはその一例です。ただし、この方法では文書の圧縮は保証されないことに注意してください。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## 最適化戦略管理

最適化戦略をカスタマイズすることもできます。現在、 [リソースの最適化 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドは5つのテクニックを使用します。これらのテクニックは、OptimizeResources () メソッドを次のように使用して適用できます。 [最適化オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) パラメーター。

### すべての画像を縮小または圧縮する

画像の処理には、画質を下げる方法と、解像度を変更する方法の2つがあります。いずれにしても、 [画像圧縮オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) 適用する必要があります。次の例では、ImageQuality を 50 に下げて画像を縮小しています。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 未使用オブジェクトの削除

PDF 文書には、文書内の他のオブジェクトから参照されていない PDF オブジェクトが含まれている場合があります。たとえば、ページが文書ページツリーから削除されたが、ページオブジェクト自体は削除されていない場合などがこれに該当します。これらのオブジェクトを削除しても、文書は無効になるわけではなく、むしろ縮小されます。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 未使用のストリームの削除

ドキュメントに未使用のリソースストリームが含まれている場合があります。これらのストリームはページリソースディクショナリから参照されるため、「未使用オブジェクト」ではありません。したがって、「未使用オブジェクトの削除」メソッドを使用しても削除されません。しかし、これらのストリームはページコンテンツでは決して使用されません。これは、画像がページからは削除されているが、ページリソースからは削除されていない場合に発生する可能性があります。また、このような状況は、ページが文書から抽出され、文書ページに「共通の」リソース、つまり同じ Resources オブジェクトがある場合によく発生します。リソースストリームが使用されているかどうかを判断するために、ページの内容が分析されます。未使用のストリームは削除されます。文書サイズが小さくなることがあります。このテクニックの使用方法は前のステップと似ています。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 重複ストリームのリンク

ドキュメントによっては、同じリソースストリーム (画像など) が複数含まれている場合があります。これは、たとえば文書がそれ自体と連結されている場合などに起こる可能性があります。出力ドキュメントには、同じリソースストリームの独立したコピーが 2 つ含まれています。すべてのリソースストリームを分析して比較します。ストリームが重複している場合、それらはマージされます。つまり、コピーが 1 つだけ残ります。参照は適切に変更され、オブジェクトのコピーは削除されます。場合によっては、文書サイズを小さくすると役立つことがあります。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### フォントの埋め込み解除

文書が埋め込みフォントを使用している場合は、すべてのフォントデータが文書に保存されていることを意味します。その利点は、フォントがユーザーのマシンにインストールされているかどうかに関係なく、文書を表示できることです。しかし、フォントを埋め込むと文書が大きくなります。フォントの埋め込みを解除する方法では、埋め込まれたフォントがすべて削除されます。そのため、正しいフォントがインストールされていないと、文書のサイズは小さくなりますが、文書自体が読めなくなる可能性があります。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

最適化リソースはこれらのメソッドをドキュメントに適用します。これらの方法のいずれかを適用すると、文書のサイズは小さくなる可能性が高いです。これらの方法をどれも適用しなければ、文書サイズは変わりませんが、これは明らかです。

## PDF ドキュメントサイズを縮小するその他の方法

### 注釈の削除またはフラット化

注釈は不要になったら削除できます。必要であっても追加の編集が不要な場合は、フラット化できます。どちらの方法でもファイルサイズが小さくなります。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### フォームフィールドを削除する

PDF ドキュメントに AcroForms が含まれている場合は、フォームフィールドをフラット化してファイルサイズを小さくすることができます。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### PDF を RGB カラースペースからグレースケールに変換

PDFファイルは、テキスト、画像、添付ファイル、注釈、グラフ、およびその他のオブジェクトで構成されます。PDF ファイルの印刷時間を短縮するために、PDF を RGB カラースペースからグレースケールに変換しなければならない場合があります。また、ファイルをグレースケールに変換すると、文書サイズも小さくなりますが、文書の品質が低下する場合もあります。この機能は現在 Adobe Acrobat のプリフライト機能でサポートされていますが、Office オートメーションについて言えば、このような文書操作の活用を実現する究極のソリューションが Aspose.PDF です。この要件を満たすには、次のコードスニペットを使用できます。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### フラットデコード圧縮

.NET 経由の Python 用 Aspose.PDF は、PDF 最適化機能の FlateDecode 圧縮をサポートしています。以下のコードスニペットは、最適化のオプションを使用して **FlateDecode** 圧縮で画像を保存する方法を示しています。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## 関連ドキュメントトピック

- [Python で PDF ドキュメントを操作する](/pdf/ja/python-net/working-with-documents/)
- [Python で PDF ファイルをマージする](/pdf/ja/python-net/merge-pdf-documents/)
- [Python で PDF ファイルを分割する方法](/pdf/ja/python-net/split-document/)
- [Python で PDF ドキュメントを操作する方法](/pdf/ja/python-net/manipulate-pdf-document/)

