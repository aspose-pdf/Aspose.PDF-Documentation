---
title: Python을 사용하여 PDF 만들기
linktitle: PDF 문서 만들기
type: docs
weight: 10
url: /ko/python-net/create-pdf-document/
description: Aspose.PDF for Python via .NET를 사용하여 PDF 문서를 생성하고 형식화합니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 파일 만들기
Abstract: Aspose.PDF for Python via .NET는 .NET 프레임워크를 대상으로 하는 Python 애플리케이션 내에서 PDF 파일을 조작하도록 설계된 다목적 API입니다. 사용자는 PDF 문서를 손쉽게 생성, 로드, 수정 및 변환할 수 있습니다. 이 문서에서는 Aspose.PDF를 사용하여 간단한 PDF 파일을 만드는 단계별 가이드를 제공합니다. 과정은 `Document` 객체를 초기화하고, 문서에 `Page`를 추가한 뒤, 페이지의 `paragraphs`에 `TextFragment`를 삽입하고, 파일을 PDF로 저장하는 흐름을 포함합니다. 포함된 Python 코드 스니펫은 텍스트 "Hello World!"가 포함된 PDF 문서를 생성하는 이러한 단계를 시연합니다. 이 API는 최소한의 코드로 PDF 처리를 단순화하여 .NET 환경에서 PDF를 다루는 개발자의 생산성을 향상시킵니다.
---

**Aspose.PDF for Python via .NET**은(는) 개발자가 .NET 애플리케이션용 Python에서 몇 줄의 코드만으로 PDF 파일을 직접 생성, 로드, 수정 및 변환할 수 있게 해주는 PDF 조작 API입니다.

## 간단한 PDF 파일 만드는 방법

Aspose.PDF를 사용하여 Python via .NET으로 PDF를 만들려면 다음 단계에 따라 진행하십시오:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 객체를 생성합니다
1. [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체를 Document 객체의 [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 컬렉션에 추가합니다
1. [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)을 페이지의 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 컬렉션에 추가합니다
1. 결과 PDF 문서를 저장합니다

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```


