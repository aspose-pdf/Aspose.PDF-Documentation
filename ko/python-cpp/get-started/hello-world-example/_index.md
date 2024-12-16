---
title: Python 언어를 사용한 Hello World 예제
linktitle: Hello World 예제
type: docs
weight: 20
url: /ko/python-cpp/hello-world-example/
description: 이 샘플은 Aspose.PDF for Python을 사용하여 간단한 PDF "Hello, World!" 문서를 만드는 방법을 보여줍니다.
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python 언어를 사용한 Hello World 예제",
    "alternativeHeadline": "Aspose.PDF Python (via C++) 예제",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, Python, 문서 생성",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "description": "이 샘플은 Aspose.PDF for Python을 사용하여 간단한 PDF 문서를 만드는 방법을 보여줍니다.",
    "articleBody": "간단한 사용 사례는 프로그래밍 언어 또는 소프트웨어의 기능을 보여주는 데 도움이 될 수 있습니다. 이는 일반적으로 \"Hello World\" 예제로 수행됩니다.\n\nAspose.PDF for Python via C++는 개발자가 Python 응용 프로그램에서 PDF 문서를 생성, 조작 및 변환할 수 있도록 하는 강력한 PDF API입니다. PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX 및 이미지 파일 형식과 같은 다양한 파일 형식을 지원합니다. 이 기사에서는 Aspose.PDF API를 사용하여 \"Hello World!\" 텍스트가 포함된 PDF 문서를 만드는 방법을 보여드립니다. 다음 코드 샘플을 실행하기 전에 환경에 Aspose.PDF for Python via C++를 설치해야 합니다.\n1. AsposePdfPython 모듈을 가져옵니다.\n2. document_create 함수를 사용하여 새 PDF 문서 객체를 생성합니다.\n3. document_get_pages 함수를 사용하여 문서의 페이지 컬렉션을 가져옵니다.\n4. page_collection_add_page 함수를 사용하여 페이지 컬렉션에 새 페이지를 추가합니다.\n5. page_get_paragraphs 함수를 사용하여 페이지의 단락 컬렉션을 가져옵니다.\n6. image_create 함수를 사용하여 새 이미지 객체를 생성합니다.\n7. image_set_file 함수를 사용하여 이미지 객체의 파일 이름을 \"sample.jpg\"로 설정합니다.\n8. paragraphs_add_image 함수를 사용하여 이미지 객체를 단락 컬렉션에 추가합니다.\n9. document_save 함수를 사용하여 문서를 \"document.pdf\"라는 파일로 저장합니다.\n10. close_handle 함수를 사용하여 문서 핸들을 닫습니다."
}
</script>


간단한 사용 사례는 프로그래밍 언어나 소프트웨어의 기능을 보여주는 데 도움을 줄 수 있습니다. 이는 일반적으로 "Hello World" 예제로 수행됩니다.

Aspose.PDF for Python via C++는 개발자가 그들의 Python 애플리케이션에서 PDF 문서를 생성, 조작 및 변환할 수 있도록 하는 강력한 PDF API입니다. PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX 및 이미지 파일 형식과 같은 다양한 파일 형식 작업을 지원합니다. 이 기사에서는 Aspose.PDF API를 사용하여 "Hello World!" 텍스트가 포함된 PDF 문서를 생성하는 방법을 보여줍니다. 다음 코드 샘플을 실행하기 전에 환경에 Aspose.PDF for Python via C++를 설치해야 합니다.

1. `AsposePdfPython` 모듈을 가져옵니다.
1. `document_create` 함수를 사용하여 새 PDF 문서 객체를 생성합니다.
1. `document_get_pages` 함수를 사용하여 문서의 페이지 컬렉션을 가져옵니다.
1. `page_collection_add_page` 함수를 사용하여 페이지 컬렉션에 새 페이지를 추가합니다.

1. `page_get_paragraphs` 함수를 사용하여 페이지의 단락 모음을 가져옵니다.
1. `image_create` 함수를 사용하여 새로운 이미지 객체를 생성합니다.
1. `image_set_file` 함수를 사용하여 이미지 객체의 파일 이름을 "sample.jpg"로 설정합니다.
1. `paragraphs_add_image` 함수를 사용하여 이미지 객체를 단락 모음에 추가합니다.
1. `document_save` 함수를 사용하여 문서를 "document.pdf"라는 이름의 파일로 저장합니다.
1. `close_handle` 함수를 사용하여 문서 핸들을 닫습니다.

다음 코드 스니펫은 Aspose.PDF for Python via C++가 작동하는 방식을 보여주는 Hello World 프로그램입니다.

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