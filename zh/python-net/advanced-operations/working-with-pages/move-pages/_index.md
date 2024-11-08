---
title: 使用Python编程移动PDF页面
linktitle: 移动PDF页面
type: docs
weight: 100
url: /zh/python-net/move-pages/
description: 尝试使用Aspose.PDF for Python via .NET在PDF文件中将页面移动到所需位置或文件末尾。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用Python编程移动PDF页面",
    "alternativeHeadline": "如何使用Python移动PDF页面",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf文档生成",
    "keywords": "pdf, python, 移动pdf页面",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF文档团队",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "尝试使用Aspose.PDF for Python via .NET在PDF文件中将页面移动到所需位置或文件末尾。"
}
</script>


## 将页面从一个 PDF 文档移动到另一个

本主题解释了如何使用 Python 将页面从一个 PDF 文档移动到另一个文档的末尾。
要移动页面，我们应该：

1. 使用源 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类对象。
1. 使用目标 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类对象。
1. 从 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合中获取页面。
1. 将页面 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 到目标文档。
1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存输出 PDF。
1. 在源文档中 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 页面。

1. 使用[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)方法保存源PDF。

以下代码片段展示了如何移动一页。

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # 保存输出文件
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## 从一个PDF文档移动一组页面到另一个

1. 使用源PDF文件创建一个[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)类对象。
1. 使用目标PDF文件创建一个[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)类对象。
1. 定义一个数组，包含要移动的页面编号。
1. 循环遍历数组：

1. 从 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合中获取页面。
1. 将页面[添加](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)到目标文档。
1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存输出 PDF。
1. 使用数组在源文档中[删除](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods)页面。
1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存源 PDF。

以下代码片段展示了如何在 PDF 文件的末尾插入一个空白页面。

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # 保存输出文件
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## 在当前 PDF 文档中移动页面到新位置

1. 使用源 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类对象。
1. 从 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合中获取页面。
1. 将页面 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 到新位置（例如末尾）。
1. 在先前位置 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) 页面。
1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存输出 PDF。

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # 保存输出文件
    srcDocument.save(output_pdf)