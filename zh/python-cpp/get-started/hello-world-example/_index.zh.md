---
title: 使用 Python 语言的 Hello World 示例
linktitle: Hello World 示例
type: docs
weight: 20
url: /python-cpp/hello-world-example/
description: 此示例演示如何使用 Aspose.PDF for Python 创建一个简单的 PDF "Hello, World!" 文档
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 语言的 Hello World 示例",
    "alternativeHeadline": "Aspose.PDF Python（通过 C++）示例",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, Python, 文档生成",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 文档团队",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
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
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "此示例演示如何使用 Aspose.PDF for Python 创建一个简单的 PDF 文档。",
    "articleBody": "一个简单的用例可以帮助演示编程语言或软件的功能。通常使用“Hello World”示例来实现。\n\nAspose.PDF for Python via C++ 是一个强大的 PDF API，开发人员可以在 Python 应用程序中创建、操作和转换 PDF 文档。它支持多种文件格式，如 PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX 和图像文件格式。在本文中，我们将向您展示如何使用 Aspose.PDF API 创建包含“Hello World!”文本的 PDF 文档。在运行以下代码示例之前，您需要在环境中安装 Aspose.PDF for Python via C++。\n1. 导入 AsposePdfPython 模块。\n2. 使用 document_create 函数创建一个新的 PDF 文档对象。\n3. 使用 document_get_pages 函数获取文档的页面集合。\n4. 使用 page_collection_add_page 函数向页面集合添加新页面。\n5. 使用 page_get_paragraphs 函数获取页面的段落集合。\n6. 使用 image_create 函数创建一个新的图像对象。\n7. 使用 image_set_file 函数将图像对象的文件名设置为“sample.jpg”。\n8. 使用 paragraphs_add_image 函数将图像对象添加到段落集合中。\n9. 使用 document_save 函数将文档保存为名为“document.pdf”的文件。\n10. 使用 close_handle 函数关闭文档句柄。"
}
</script>


一个简单的用例可以帮助展示编程语言或软件的功能。这通常通过一个“Hello World”的例子来完成。

Aspose.PDF for Python via C++ 是一个强大的 PDF API，使开发人员能够在他们的 Python 应用程序中创建、操作和转换 PDF 文档。它支持处理各种文件格式，如 PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX 和图像文件格式。在本文中，我们将向您展示如何使用 Aspose.PDF API 创建一个包含文本“Hello World!”的 PDF 文档。您需要在运行以下代码示例之前在您的环境中安装 Aspose.PDF for Python via C++。

1. 导入 `AsposePdfPython` 模块。
1. 使用 `document_create` 函数创建一个新的 PDF 文档对象。
1. 使用 `document_get_pages` 函数获取文档的页面集合。
1. 使用 `page_collection_add_page` 函数向页面集合中添加一个新页面。

1. 使用 `page_get_paragraphs` 函数获取页面的段落集合。
1. 使用 `image_create` 函数创建一个新的图像对象。
1. 使用 `image_set_file` 函数将图像对象的文件名设置为 "sample.jpg"。
1. 使用 `paragraphs_add_image` 函数将图像对象添加到段落集合中。
1. 使用 `document_save` 函数将文档保存为名为 "document.pdf" 的文件。
1. 使用 `close_handle` 函数关闭文档句柄。

以下代码片段是一个 Hello World 程序，演示了如何通过 C++ 使用 Aspose.PDF for Python。

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)
 
document_save(doc, "document.pdf")
close_handle(doc)
```