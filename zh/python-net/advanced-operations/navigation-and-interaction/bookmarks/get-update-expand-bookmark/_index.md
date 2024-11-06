---
title: 获取、更新和展开书签使用Python
linktitle: 获取、更新和展开书签
type: docs
weight: 20
url: zh/python-net/get-update-and-expand-bookmark/
description: 本文描述了如何使用我们的Aspose.PDF for Python库在PDF文件中使用书签。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用Python获取、更新和展开书签",
    "alternativeHeadline": "如何从PDF文件中获取书签",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf文件生成",
    "keywords": "pdf, python, 获取书签",
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
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "本文描述了如何使用我们的Aspose.PDF for Python库在PDF文件中使用书签。"
}
</script>


## 获取书签

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合包含了 PDF 文件的所有书签。本文解释了如何从 PDF 文件中获取书签，以及如何获取特定书签所在的页面。

要获取书签，遍历 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合，并在 OutlineItemCollection 中获取每个书签。[OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 提供了对所有书签属性的访问。以下代码片段展示了如何从 PDF 文件中获取书签。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 遍历所有书签
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```


## 获取书签的页码

添加书签后，可以通过获取与书签对象关联的目标页码来找出它所在的页面。

```python

    import aspose.pdf as ap

    # 创建 PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # 打开 PDF 文件
    bookmarkEditor.bind_pdf(input_pdf)
    # 提取书签
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "标题:", bookmark.title)
        print(str_level_seprator, "页码:", bookmark.page_number)
        print(str_level_seprator, "页面操作:", bookmark.action)
```

## 从 PDF 文档获取子书签

书签可以组织成具有父子关系的层次结构。
 要获取所有书签，请遍历 Document 对象的 Outlines 集合。然而，要同时获取子书签，还需要遍历在第一次循环中获得的每个 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 对象中的所有书签。以下代码片段展示了如何从 PDF 文档中获取子书签。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 遍历所有书签
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("子书签")
            # 有子书签则也遍历它们
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## 更新 PDF 文档中的书签

要更新 PDF 文件中的书签，首先通过指定书签的索引，从 Document 对象的 OutlineColletion 集合中获取特定书签。一旦将书签检索到 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 对象中，就可以更新其属性，然后使用 Save 方法保存更新后的 PDF 文件。以下代码片段演示了如何在 PDF 文档中更新书签。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 获取书签对象
    outline = document.outlines[1]

    # 获取子书签对象
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # 保存输出
    document.save(output_pdf)
```

## 查看文档时展开书签

书签保存在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合中，该集合本身在 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。
 然而，我们可能需要在查看 PDF 文件时将所有书签展开。

为了实现这一要求，我们可以将每个大纲/书签项的打开状态设置为打开。以下代码段向您展示如何在 PDF 文档中将每个书签的打开状态设置为展开。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 设置页面查看模式，即显示缩略图，全屏，显示附件面板
    document.page_mode = ap.PageMode.USE_OUTLINES
    # 遍历 PDF 文件的大纲集合中的每个大纲项
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # 设置大纲项的打开状态
        item.open = True

    # 保存输出
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "applicationCategory": "PDF Manipulation Library for Python",
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