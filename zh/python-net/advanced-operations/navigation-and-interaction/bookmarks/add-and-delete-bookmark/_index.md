---
title: 使用 Python 添加和删除书签
linktitle: 添加和删除书签
type: docs
weight: 10
url: /zh/python-net/add-and-delete-bookmark/
description: 你可以使用 Python 向 PDF 文档添加书签。可以从 PDF 文档中删除所有或特定书签。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "添加和删除书签",
    "alternativeHeadline": "如何从 PDF 添加和删除书签",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 删除书签, 添加书签",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "你可以使用 Python 向 PDF 文档添加书签。可以从 PDF 文档中删除所有或特定书签。"
}
</script>


## 将书签添加到 PDF 文档

书签保存在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合中，它本身在 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。

要向 PDF 添加书签：

1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象打开 PDF 文档。
1. 创建书签并定义其属性。
1. 将 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 集合添加到大纲集合中。

以下代码片段向您展示了如何在 PDF 文档中添加书签。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 创建书签对象
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "测试书签"
    outline.italic = True
    outline.bold = True
    # 设置目标页码
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # 在文档的大纲集合中添加书签。
    document.outlines.append(outline)

    # 保存输出
    document.save(output_pdf)
```


## 向 PDF 文档添加子书签

书签可以嵌套，表示与父书签和子书签的层次关系。本文解释了如何向 PDF 添加子书签，即二级书签。

要向 PDF 文件添加子书签，首先添加父书签：

1. 打开文档。
1. 向 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 添加书签，定义其属性。
1. 将 OutlineItemCollection 添加到 Document 对象的 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。

子书签的创建方式与上述父书签相同，但被添加到父书签的 Outlines 集合中。

以下代码片段展示了如何向 PDF 文档添加子书签。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 创建一个父书签对象
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # 创建一个子书签对象
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # 在父书签的集合中添加子书签
    outline.append(childOutline)
    # 在文档的大纲集合中添加父书签。
    document.outlines.append(outline)

    # 保存输出
    document.save(output_pdf)
```


## 从 PDF 文档中删除所有书签

PDF 中的所有书签都保存在 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合中。本文解释了如何从 PDF 文件中删除所有书签。

要从 PDF 文件中删除所有书签：

1. 调用 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合的 Delete 方法。
1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存修改后的文件。

以下代码片段展示了如何从 PDF 文档中删除所有书签。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 删除所有书签
    document.outlines.delete()

    # 保存更新后的文件
    document.save(output_pdf)

```

## 从 PDF 文档中删除特定书签

要从 PDF 文件中删除特定书签：

1. 将书签的标题作为参数传递给 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合的 Delete 方法。
1. 然后使用 Document 对象的 Save 方法保存更新后的文件。

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类提供了 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 集合。[delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) 方法删除传递给该方法的标题的任何书签。

以下代码片段展示了如何从 PDF 文档中删除特定书签。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 按标题删除特定大纲
    document.outlines.delete("Child Outline")

    # 保存更新后的文件
    document.save(output_pdf)