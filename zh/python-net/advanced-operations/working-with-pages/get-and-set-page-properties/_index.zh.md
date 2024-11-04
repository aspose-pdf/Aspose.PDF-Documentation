---
title: 使用 Python 获取和设置页面属性
linktitle: 获取和设置页面属性
type: docs
weight: 90
url: /python-net/get-and-set-page-properties/
description: 本节展示如何获取 PDF 文件中的页数，获取有关 PDF 页面属性（如颜色）的信息，并设置页面属性。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 获取和设置页面属性",
    "alternativeHeadline": "获取和设置 PDF 页面属性",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 获取页面属性, 设置页面属性",
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
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF for Python via .NET 允许您在 Python 应用程序中读取和设置 PDF 文件中页面的属性。本节展示了如何获取 PDF 文件的页数，获取有关 PDF 页面属性（例如颜色）的信息，并设置页面属性。给出的示例是用 Python 编写的。

## 获取 PDF 文件中的页数

在处理文档时，您通常想知道它们包含多少页。使用 Aspose.PDF，这不需要超过两行代码。

要获取 PDF 文件中的页数：

1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类打开 PDF 文件。
1. 然后使用 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合的 Count 属性（来自 Document 对象）来获取文档中的总页数。

以下代码片段展示了如何获取 PDF 文件的页数。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 获取页数
    print("页数:", str(len(document.pages)))
```


### 获取页面数量而不保存文档

有时我们会动态生成PDF文件，在创建PDF文件时，可能会遇到获取PDF文件页面数量的需求（例如创建目录等），而不在系统或流上保存文件。为了满足这一需求，Document类中引入了一个方法[process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)。请看下面的代码片段，展示了在不保存文档的情况下获取页面数量的步骤。

```python

    import aspose.pdf as ap

    # 实例化Document实例
    document = ap.Document()
    # 向PDF文件的页面集合中添加页面
    page = document.pages.add()
    # 创建循环实例
    for i in range(0, 300):
        # 向页面对象的段落集合中添加TextFragment
        page.paragraphs.add(ap.text.TextFragment("页面数量测试"))
    # 处理PDF文件中的段落以获取准确的页面数量
    document.process_paragraphs()
    # 打印文档中的页面数量
    print("文档中的页面数量 =", str(len(document.pages)))
```


## 获取页面属性

PDF 文件中的每个页面都有许多属性，例如宽度、高度、出血框、裁剪框和切割框。Aspose.PDF 允许您访问这些属性。

### **理解页面属性：Artbox、BleedBox、CropBox、MediaBox、TrimBox 和 Rect 属性之间的区别**

- **媒体框**：媒体框是最大的页面框。它对应于打印为 PostScript 或 PDF 时选择的页面大小（例如 A4、A5、美国信纸等）。换句话说，媒体框确定了显示或打印 PDF 文档的媒介的物理大小。
- **出血框**：如果文档有出血，PDF 也会有一个出血框。
 出血是指超出页面边缘的颜色（或艺术作品）的量。它用于确保当文档被打印和裁剪到尺寸（“修边”）时，油墨将一直延伸到页面的边缘。即使页面被误裁——稍微偏离修边标记切割——页面上也不会出现白色边缘。
- **修边框**: 修边框表示文档在打印和修边后的最终尺寸。
- **艺术框**: 艺术框是在文档页面的实际内容周围绘制的框。当在其他应用程序中导入PDF文档时，使用此页面框。
- **裁剪框**: 裁剪框是您的PDF文档在Adobe Acrobat中显示的“页面”尺寸。在正常视图中，Adobe Acrobat中仅显示裁剪框的内容。
  有关这些属性的详细描述，请阅读Adobe.Pdf规范，特别是10.10.1页面边界。
- **Page.Rect**: MediaBox和DropBox的交集（通常为可见矩形）。 下图说明了这些属性。

有关更多详细信息，请访问[此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

### **访问页面属性**

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)类提供了与特定PDF页面相关的所有属性。PDF文件的所有页面都包含在[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)对象的[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)集合中。

从那里，可以使用它们的索引访问单个Page对象，或者使用foreach循环遍历集合以获取所有页面。一旦访问了单个页面，我们就可以获取其属性。以下代码片段展示了如何获取页面属性。

```python

    import aspose.pdf as ap

    # 打开文件
    document = ap.Document(input_pdf)
    # 获取特定页面
    page = document.pages[1]
    # 获取页面属性
    print(
        "ArtBox : 高度={},宽度={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : 高度={},宽度={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : 高度={},宽度={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : 高度={},宽度={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : 高度={},宽度={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : 高度={},宽度={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("页面编号 :", page.number)
    print("旋转 :", page.rotate)
```

## 获取 PDF 文件的特定页面

Aspose.PDF for Python 允许您[将 PDF 拆分为单独的页面](/pdf/python-net/split-pdf-document/)并将其另存为 PDF 文件。在 PDF 文件中获取指定页面并将其另存为新的 PDF 是一个非常类似的操作：打开源文档，访问页面，创建一个新文档并将页面添加到该文档中。

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) 对象的 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection) 包含 PDF 文件中的页面。要从此集合中获取特定页面：

1. 使用 Pages 属性指定页面索引。
2. 创建一个新的 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
3. 将 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象添加到新的 Document 对象中。
4. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存输出。

以下代码片段演示了如何从 PDF 文件中获取特定页面并将其另存为新文件。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 获取特定页面
    page = document.pages[2]

    # 将页面保存为PDF文件
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## 确定页面颜色

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 类提供了与PDF文档中特定页面相关的属性，包括页面使用的颜色类型 - RGB、黑白、灰度或未定义。

PDF文件的所有页面都包含在 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合中。
 The [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 属性指定页面元素的颜色。要获取或确定特定 PDF 页面的颜色信息，请使用 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象的 [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 属性。

以下代码片段展示了如何遍历 PDF 文件的各个页面以获取颜色信息。

```python

    import aspose.pdf as ap

    # 打开源 PDF 文件
    document = ap.Document(input_pdf)
    # 遍历 PDF 文件的所有页面
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # 获取特定 PDF 页面的颜色类型信息
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("Page # " + str(page_number) + " is Black and white.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("Page # " + str(page_number) + " is Gray Scale.")

        if page_color_type == ap.ColorType.RGB:
            print("Page # " + str(page_number) + " is RGB.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("Page # " + str(page_number) + " Color is undefined.")
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
    "applicationCategory": "PDF 操作库用于 Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>