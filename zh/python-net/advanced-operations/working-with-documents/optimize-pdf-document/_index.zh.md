---
title: 优化、压缩或减少 PDF 大小在 Python 中
linktitle: 优化 PDF
type: docs
weight: 30
url: /python-net/optimize-pdf/
keywords: "优化 pdf python"
description: 优化 PDF 文件，缩小所有图像，减少 PDF 大小，取消嵌入字体，使用 Python 删除未使用的对象。
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 优化 PDF",
    "alternativeHeadline": "如何使用 Python 优化 PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 优化 pdf",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 文档团队",
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
    "description": "优化 PDF 文件，缩小所有图像，减少 PDF 大小，取消嵌入字体，使用 Python 删除未使用的对象。"
}
</script>


一个 PDF 文档有时可能包含额外的数据。减小 PDF 文件的大小将帮助您优化网络传输和存储。这在网页发布、社交网络分享、通过电子邮件发送或存储归档时尤其方便。我们可以使用几种技术来优化 PDF：

- 优化页面内容以便在线浏览
- 缩小或压缩所有图像
- 启用页面内容重用
- 合并重复的流
- 去除嵌入字体
- 删除未使用的对象
- 移除平坦化表单字段
- 移除或平坦化注释

{{% alert color="primary" %}}

优化方法的详细解释可以在优化方法概述页面中找到。

{{% /alert %}}

## 为网络优化 PDF 文档

Web 的优化或线性化是指使 PDF 文件适合使用网络浏览器在线浏览的过程。要优化文件以便网页展示：

1. 在 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象中打开输入文档。
1. 使用 [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。
1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存优化后的文档。

以下代码片段展示了如何为网络优化 PDF 文档。

```python 

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 为网络优化
    document.optimize()

    # 保存输出文档
    document.save(output_pdf)
```

## 减小 PDF 大小

[OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法允许通过剔除不必要的信息来减少文档大小。默认情况下，该方法的工作方式如下：

- 移除未在文档页面上使用的资源
- 相同的资源合并为一个对象

- 删除未使用的对象

下面的代码片段是一个示例。但是，请注意这种方法不能保证文档缩小。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 优化 PDF 文档。但是，请注意这种方法不能保证文档缩小
    document.optimize_resources()
    # 保存更新后的文档
    document.save(output_pdf)
```

## 优化策略管理

我们还可以自定义优化策略。目前，[OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法使用 5 种技术。这些技术可以通过使用 [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) 参数的 OptimizeResources() 方法来应用。

### 缩小或压缩所有图像

我们有两种处理图像的方式：降低图像质量和/或改变其分辨率。
 在任何情况下，都应应用 [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/)。在下面的示例中，我们通过将 ImageQuality 降低到 50 来缩小图像。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 初始化 OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # 设置 CompressImages 选项
    optimizeOptions.image_compression_options.compress_images = True
    # 设置 ImageQuality 选项
    optimizeOptions.image_compression_options.image_quality = 50
    # 使用 OptimizationOptions 优化 PDF 文档
    document.optimize_resources(optimizeOptions)
    # 保存更新后的文档
    document.save(output_pdf)
```

### 移除未使用的对象

PDF 文档有时包含未被文档中任何其他对象引用的 PDF 对象。 这种情况可能发生在，例如，一个页面从文档页面树中移除，但页面对象本身并未被移除。移除这些对象不会使文档无效，而是缩小了它。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 设置 RemoveUsedObject 选项
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # 使用 OptimizationOptions 优化 PDF 文档
    document.optimize_resources(optimizeOptions)
    # 保存更新后的文档
    document.save(output_pdf)
```

### 移除未使用的流

有时文档中包含未使用的资源流。 这些流不是“未使用的对象”，因为它们被引用自页面资源字典。因此，它们不会被“移除未使用的对象”方法移除。但是，这些流从未与页面内容一起使用。当图像被从页面上移除但没有从页面资源中移除时，可能会发生这种情况。此外，当从文档中提取页面且文档页面具有“公共”资源（即相同的Resources对象）时，这种情况经常发生。分析页面内容以确定资源流是否被使用。未使用的流将被移除。这有时会减少文档的大小。使用这种技术与前一步类似：

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 设置 RemoveUsedStreams 选项
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # 使用 OptimizationOptions 优化 PDF 文档
    document.optimize_resources(optimizeOptions)
    # 保存更新的文档
    document.save(output_pdf)
```

### 链接重复的流

有些文档可能包含多个相同的资源流（例如，图像）。这种情况可能发生在文档与自身连接时。输出文档包含同一资源流的两个独立副本。我们分析所有资源流并进行比较。如果流是重复的，它们将被合并，也就是说，仅保留一个副本。引用会相应地更改，并且对象的副本会被删除。在某些情况下，这有助于减少文档的大小。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 设置 LinkDuplcateStreams 选项
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # 使用 OptimizationOptions 优化 PDF 文档
    document.optimize_resources(optimizeOptions)
    # 保存更新后的文档
    document.save(output_pdf)
```

### 移除嵌入字体

如果文档使用嵌入字体，则意味着所有字体数据都存储在文档中。
 文档的优点是，无论字体是否安装在用户的机器上都可以查看。但是嵌入字体会使文档变大。非嵌入字体的方法会移除所有嵌入的字体。因此，文档的大小会减小，但如果没有安装正确的字体，文档本身可能会变得不可读。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 设置 UnembedFonts 选项
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # 使用 OptimizationOptions 优化 PDF 文档
    document.optimize_resources(optimizeOptions)
    # 保存更新后的文档
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "原始文件大小: {}. 减少后的文件大小: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

优化资源将这些方法应用于文档。 如果应用了这些方法，文档大小很可能会减少。如果没有应用这些方法，文档大小不会改变，这是显而易见的。

## 其他减少 PDF 文档大小的方法

### 删除或扁平化注释

当注释不必要时，可以删除它们。当它们需要但不需要额外编辑时，可以将它们扁平化。这两种技术都会减少文件大小。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    # 扁平化注释
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # 保存更新的文档
    document.save(output_pdf)
```

### 删除表单字段

如果 PDF 文档包含 AcroForms，我们可以尝试通过扁平化表单字段来减少文件大小。

```python

    import aspose.pdf as ap

    # 加载源 PDF 表单
    doc = ap.Document(input_pdf)

    # 扁平化表单
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # 保存更新的文档
    doc.save(output_pdf)
```

### 将 PDF 从 RGB 颜色空间转换为灰度

PDF 文件包含文本、图像、附件、注释、图表和其他对象。您可能会遇到将 PDF 从 RGB 颜色空间转换为灰度的需求，以便在打印这些 PDF 文件时速度更快。此外，当文件转换为灰度时，文档大小也会减少，但这也可能导致文档质量下降。此功能目前由 Adobe Acrobat 的预检功能支持，但在谈到办公自动化时，Aspose.PDF 是一个提供此类文档操作的终极解决方案。为了实现此需求，可以使用以下代码片段。

```python

    import aspose.pdf as ap

    # 加载源 PDF 文件
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # 将 RGB 颜色空间图像转换为灰度颜色空间
        strategy.convert(page)

    # 保存结果文件
    document.save(output_pdf)
```


### FlateDecode 压缩

Aspose.PDF for Python via .NET 支持 PDF 优化功能的 FlateDecode 压缩。下面的代码片段展示了如何在优化中使用该选项以 **FlateDecode** 压缩存储图像：

```python

    import aspose.pdf as ap

    # 打开文档
    doc = ap.Document(input_pdf)
    # 初始化 OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # 为了使用 FlateDecode 压缩优化图像，设置优化选项为 Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # 设置优化选项
    doc.optimize_resources(optimizationOptions)
    # 保存文档
    doc.save(output_pdf)