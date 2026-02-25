---
title: PythonでPDFサイズを最適化、圧縮または削減
linktitle: PDFを最適化
type: docs
weight: 30
url: /ja/python-net/optimize-pdf/
description: Aspose.PDFを使用して、Webパフォーマンスの向上とファイルサイズの削減のために、PythonでPDFドキュメントを最適化する方法を学びます。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFページを圧縮
Abstract: 本記事では、PDFファイルのサイズを削減し、Webページ、メール、ストレージシステムなどのさまざまなプラットフォームでのパフォーマンスを向上させるための最適化方法を包括的に解説します。最適化手法には、画像サイズの縮小、未使用リソースの削除、フォントの埋め込み解除が含まれます。Web向けのPDF最適化や全体的なファイルサイズ削減の具体的な方法として、Aspose.PDF for Python の `Optimize` および `OptimizeResources` メソッドを利用します。`OptimizationOptions` を使用すれば、画像の圧縮、未使用オブジェクトやストリームの削除、重複ストリームのリンク、フォントの埋め込み解除といった対象を絞った最適化が可能です。追加の戦略として、アノテーションのフラット化、フォームフィールドの削除、PDF を RGB からグレースケールに変換してサイズをさらに減らす方法も紹介します。さらに、画像最適化のために FlateDecode 圧縮を使用することを強調し、品質と機能を保ちつつ効果的な PDF ファイル管理を実現します。
---

PDFドキュメントには時々余分なデータが含まれることがあります。ファイルサイズを削減すると、ネットワーク転送や保存の最適化に役立ちます。特にWebページへの掲載、ソーシャルネットワークでの共有、メールでの送信、またはストレージへのアーカイブに便利です。PDFを最適化するためにいくつかの手法を使用できます:

- オンライン閲覧向けにページコンテンツを最適化する
- すべての画像を縮小または圧縮する
- ページコンテンツの再利用を有効にする
- 重複ストリームをマージする
- フォントの埋め込み解除
- 未使用オブジェクトを削除する
- フラット化されたフォームフィールドを削除する
- アノテーションを削除またはフラット化する

{{% alert color="primary" %}}

最適化手法の詳細な説明は、Optimization Methods Overview ページにあります。

{{% /alert %}}

## Web向けPDFドキュメントの最適化

最適化（またはWeb用のリニアライズ）は、PDFファイルをウェブブラウザでのオンライン閲覧に適したものにするプロセスを指します。Web表示用にファイルを最適化するには、以下の手順を実行します:

1. 入力ドキュメントを [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトで開きます。
1. [最適化](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用します。
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して最適化されたドキュメントを保存します。

以下のコードスニペットは、Web向けにPDFドキュメントを最適化する方法を示しています。

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## PDFサイズの縮小

[OptimizeResources()] メソッドを使用すると、不要な情報を除去してドキュメントサイズを削減できます。デフォルトでは、このメソッドは以下のように動作します:

- ドキュメントページで使用されていないリソースが削除されます
- 同一のリソースが1つのオブジェクトに結合されます
- 未使用オブジェクトが削除されます

以下のスニペットは例です。ただし、このメソッドは必ずしも文書の縮小を保証するわけではありません。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## 最適化戦略の管理

最適化戦略をカスタマイズすることもできます。現在、[OptimizeResources()] メソッドは5つの手法を使用しています。これらの手法は、[OptimizationOptions] パラメータと共に OptimizeResources() メソッドを使用して適用できます。

### すべての画像の縮小または圧縮

画像を操作する方法は2つあります：画像品質を下げる、または解像度を変更することです。いずれの場合も [ImageCompressionOptions] を適用すべきです。以下の例では、ImageQuality を 50 に減らすことで画像を縮小しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 未使用オブジェクトの削除

PDFドキュメントには、文書内の他のオブジェクトから参照されていないPDFオブジェクトが含まれることがあります。例えば、ページが文書ページツリーから削除されたが、ページオブジェクト自体が削除されていない場合などです。これらのオブジェクトを削除しても文書が無効になるわけではなく、むしろサイズが縮小します。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 未使用ストリームの削除

文書には未使用のリソースストリームが含まれることがあります。これらのストリームはページリソース辞書から参照されているため、“未使用オブジェクト”ではありません。そのため、“未使用オブジェクトの削除”メソッドでは削除されませんが、ページコンテンツで使用されていないことがあります。例えば、ページから画像が削除されたがページリソースからは削除されていない場合などです。また、文書からページを抽出した際に、抽出されたページが同じResourcesオブジェクトという“共通”リソースを持つ場合にもこの状況がよく発生します。ページコンテンツを解析して、リソースストリームが使用されているかどうかを判断し、未使用のストリームを削除します。これにより文書サイズが減少することがあります。この手法の使用は前のステップと類似しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 重複ストリームのリンク

一部の文書には、同一のリソースストリーム（例えば画像）が複数含まれることがあります。例えば、文書を自分自身と連結した場合にこのような状況が起こります。出力文書には同じリソースストリームの独立したコピーが2つ存在します。すべてのリソースストリームを解析し比較します。ストリームが重複している場合、マージされ、1つのコピーだけが残ります。参照は適切に変更され、オブジェクトのコピーは削除されます。場合によっては、文書サイズの削減に効果があります。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### フォントの埋め込み解除

文書が埋め込みフォントを使用している場合、すべてのフォントデータが文書に保存されていることを意味します。これにより、ユーザーのマシンにフォントがインストールされていなくても文書を閲覧できるという利点があります。しかし、フォントを埋め込むことで文書は大きくなります。埋め込みフォント解除メソッドはすべての埋め込みフォントを削除します。その結果、文書サイズは縮小しますが、正しいフォントがインストールされていない場合、文書が読めなくなる可能性があります。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

最適化リソースはこれらの手法を文書に適用します。いずれかの手法が適用されれば、文書サイズはほぼ確実に減少します。何も適用しなければ、文書サイズは変わらないのは自明です。

## PDFドキュメントサイズを削減する追加の方法

### アノテーションの削除またはフラット化

不要な場合はアノテーションを削除できます。必要だが追加編集が不要な場合はフラット化できます。これらの手法はどちらもファイルサイズを削減します。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### フィールドの削除

PDFドキュメントにAcroFormsが含まれている場合、フォームフィールドをフラット化してファイルサイズを削減できます。

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### PDFをRGBカラースペースからグレースケールに変換

PDFファイルはテキスト、画像、添付ファイル、アノテーション、グラフ、その他のオブジェクトで構成されています。PDFをRGBカラースペースからグレースケールに変換する必要があるケースがあり、そうすることで印刷時に速度が向上します。また、ファイルをグレースケールに変換すると、文書サイズも縮小しますが、同時に品質が低下することもあります。この機能は現在、Adobe Acrobat のプレフライト機能でサポートされていますが、Office の自動化に関しては、Aspose.PDF が文書操作のための究極のソリューションを提供します。この要件を実現するには、以下のコードスニペットを使用できます。

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### FlateDecode 圧縮

.NET を介した Python 用 Aspose.PDF は、PDF 最適化機能に対する FlateDecode 圧縮のサポートを提供します。以下のコードスニペットは、最適化で画像を **FlateDecode** 圧縮で保存するオプションの使用方法を示しています。

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


