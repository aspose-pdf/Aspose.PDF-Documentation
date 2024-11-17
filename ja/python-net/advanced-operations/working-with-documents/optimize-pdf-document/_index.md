---
title: PythonでPDFサイズを最適化、圧縮または縮小
linktitle: PDFを最適化
type: docs
weight: 30
url: /ja/python-net/optimize-pdf/
description: PDFファイルを最適化し、すべての画像を縮小し、PDFサイズを減らし、埋め込みフォントを削除し、Pythonで未使用のオブジェクトを除去します。
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFを最適化",
    "alternativeHeadline": "PythonでPDFを最適化する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, optimize pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "PDFファイルを最適化し、すべての画像を縮小し、PDFサイズを減らし、埋め込みフォントを削除し、Pythonで未使用のオブジェクトを除去します。"
}
</script>


PDFドキュメントには時々追加のデータが含まれることがあります。PDFファイルのサイズを縮小することで、ネットワークの転送とストレージを最適化するのに役立ちます。これは、ウェブページでの公開、ソーシャルネットワークでの共有、電子メールでの送信、またはストレージでのアーカイブに特に便利です。PDFを最適化するためにいくつかの技術を使用できます：

- オンライン閲覧のためにページコンテンツを最適化する
- すべての画像を縮小または圧縮する
- ページコンテンツの再利用を有効にする
- 重複するストリームをマージする
- フォントの埋め込みを解除する
- 使用されていないオブジェクトを削除する
- フォームフィールドのフラット化を削除する
- 注釈を削除またはフラット化する

{{% alert color="primary" %}}

最適化方法の詳細な説明は、最適化方法概要ページで確認できます。

{{% /alert %}}

## Web用のPDFドキュメントを最適化する

Web用の最適化、または線形化とは、PDFファイルをウェブブラウザを使用してオンライン閲覧に適した状態にするプロセスを指します。ウェブ表示用にファイルを最適化するには：

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトで入力ドキュメントを開きます。
1. [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用します。
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用して最適化されたドキュメントを保存します。

次のコードスニペットは、PDFドキュメントをWeb用に最適化する方法を示しています。

```python 

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # Web用に最適化
    document.optimize()

    # 出力ドキュメントを保存
    document.save(output_pdf)
```

## PDFサイズの縮小

[OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドは、不必要な情報を除去することでドキュメントサイズを縮小することを可能にします。デフォルトでは、このメソッドは以下のように機能します：

- ドキュメントページで使用されていないリソースが削除されます
- 同一のリソースが1つのオブジェクトに結合されます

- 未使用のオブジェクトが削除されます

スニペット以下は一例です。ただし、この方法ではドキュメントの縮小を保証できないことに注意してください。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # PDFドキュメントを最適化する。ただし、この方法ではドキュメントの縮小を保証できないことに注意してください
    document.optimize_resources()
    # 更新されたドキュメントを保存
    document.save(output_pdf)
```

## 最適化戦略管理

最適化戦略をカスタマイズすることもできます。現在、[OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドは5つの技術を使用しています。これらの技術は [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) パラメーターを使用して OptimizeResources() メソッドで適用できます。

### すべての画像の縮小または圧縮

画像を扱う方法は2つあります：画像の品質を下げること、または解像度を変更することです。
 いずれにせよ、[ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) を適用する必要があります。以下の例では、ImageQuality を 50 に減らすことで画像を縮小します。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # OptimizationOptions を初期化
    optimizeOptions = ap.optimization.OptimizationOptions()
    # CompressImages オプションを設定
    optimizeOptions.image_compression_options.compress_images = True
    # ImageQuality オプションを設定
    optimizeOptions.image_compression_options.image_quality = 50
    # OptimizationOptions を使用して PDF ドキュメントを最適化
    document.optimize_resources(optimizeOptions)
    # 更新されたドキュメントを保存
    document.save(output_pdf)
```

### 未使用オブジェクトの削除

PDF ドキュメントには、ドキュメント内の他のオブジェクトから参照されていない PDF オブジェクトが含まれていることがあります。 この現象は、例えばページがドキュメントのページツリーから削除されたが、ページオブジェクト自体は削除されていない場合に起こります。これらのオブジェクトを削除してもドキュメントが無効になることはなく、むしろ縮小されます。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # RemoveUsedObjectオプションを設定する
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # OptimizationOptionsを使用してPDFドキュメントを最適化する
    document.optimize_resources(optimizeOptions)
    # 更新されたドキュメントを保存する
    document.save(output_pdf)
```

### 未使用ストリームの削除

時々、ドキュメントには未使用のリソースストリームが含まれています。 これらのストリームはページリソース辞書から参照されているため、「未使用オブジェクト」ではありません。したがって、「未使用オブジェクトを削除」する方法では削除されません。しかし、これらのストリームはページの内容で使用されることはありません。これは、画像がページから削除されたが、ページリソースから削除されていない場合に発生する可能性があります。また、ドキュメントからページが抽出され、ドキュメントページが「共通」のリソース、つまり同じResourcesオブジェクトを持っている場合にも、この状況がよく発生します。リソースストリームが使用されているかどうかを判断するためにページ内容が分析されます。未使用のストリームは削除されます。これにより、ドキュメントサイズが減少することがあります。この技術の使用は前のステップと似ています：

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # RemoveUsedStreamsオプションを設定
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # OptimizationOptionsを使用してPDFドキュメントを最適化
    document.optimize_resources(optimizeOptions)
    # 更新されたドキュメントを保存
    document.save(output_pdf)
```

### 重複ストリームのリンク

一部の文書には、いくつかの同一のリソースストリーム（例えば画像）が含まれることがあります。これは、例えば文書がそれ自体と連結された場合に発生することがあります。出力文書には、同じリソースストリームの2つの独立したコピーが含まれています。すべてのリソースストリームを分析し、それらを比較します。ストリームが重複している場合、それらは統合され、つまり1つのコピーだけが残されます。参照が適切に変更され、オブジェクトのコピーが削除されます。場合によっては、文書のサイズを減らすのに役立ちます。

```python

    import aspose.pdf as ap

    # 文書を開く
    document = ap.Document(input_pdf)
    # LinkDuplcateStreams オプションを設定
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # OptimizationOptions を使用してPDF文書を最適化
    document.optimize_resources(optimizeOptions)
    # 更新された文書を保存
    document.save(output_pdf)
```

### フォントの埋め込み解除

文書が埋め込みフォントを使用している場合、すべてのフォントデータが文書に保存されていることを意味します。
 ドキュメントの利点は、フォントがユーザーのマシンにインストールされているかどうかに関係なく表示可能であることです。しかし、フォントを埋め込むとドキュメントのサイズが大きくなります。フォントの埋め込み解除方法は、すべての埋め込みフォントを削除します。そのため、ドキュメントサイズは小さくなりますが、正しいフォントがインストールされていない場合、ドキュメント自体が読めなくなる可能性があります。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # UnembedFontsオプションを設定
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # OptimizationOptionsを使用してPDFドキュメントを最適化
    document.optimize_resources(optimizeOptions)
    # 更新されたドキュメントを保存
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "元のファイルサイズ: {}. 削減されたファイルサイズ: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

最適化リソースは、これらの方法をドキュメントに適用します。 これらの方法のいずれかが適用されると、文書のサイズはおそらく減少します。これらの方法のいずれも適用されない場合、文書のサイズは変わらないのは明らかです。

## PDF文書サイズを減らすための追加の方法

### 注釈の削除またはフラット化

注釈が不要な場合は削除できます。必要な場合でも追加の編集が不要な場合は、フラット化できます。どちらの技術もファイルサイズを削減します。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)
    # 注釈をフラット化
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # 更新されたドキュメントを保存
    document.save(output_pdf)
```

### フォームフィールドの削除

PDF文書にAcroFormsが含まれている場合、フォームフィールドをフラット化することでファイルサイズを減らすことができます。

```python

    import aspose.pdf as ap

    # ソースPDFフォームを読み込む
    doc = ap.Document(input_pdf)

    # フォームをフラット化
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # 更新されたドキュメントを保存
    doc.save(output_pdf)
```

### RGBカラースペースからグレースケールにPDFを変換する

PDFファイルは、テキスト、画像、添付ファイル、注釈、グラフ、その他のオブジェクトで構成されています。PDFをRGBカラースペースからグレースケールに変換する必要がある場合があります。こうすることで、PDFファイルを印刷する際により速くなります。また、ファイルがグレースケールに変換されると、ドキュメントのサイズも縮小されますが、品質が低下する可能性もあります。この機能は現在Adobe Acrobatのプリフライト機能でサポートされていますが、オフィスの自動化に関しては、Aspose.PDFがドキュメント操作のための最適なソリューションを提供します。この要件を達成するために、以下のコードスニペットを使用できます。

```python

    import aspose.pdf as ap

    # ソースPDFファイルをロード
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # RGBカラースペース画像をグレースケールカラースペースに変換
        strategy.convert(page)

    # 結果ファイルを保存
    document.save(output_pdf)
```


### FlateDecode 圧縮

Aspose.PDF for Python via .NETは、PDF最適化機能のためのFlateDecode圧縮のサポートを提供します。以下のコードスニペットは、**FlateDecode**圧縮を使用して画像を保存するための最適化オプションの使用方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    doc = ap.Document(input_pdf)
    # OptimizationOptionsを初期化する
    optimizationOptions = ap.optimization.OptimizationOptions()
    # FlateDecode圧縮を使用して画像を最適化するために最適化オプションをFlateに設定する
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # 最適化オプションを設定する
    doc.optimize_resources(optimizationOptions)
    # ドキュメントを保存する
    doc.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>