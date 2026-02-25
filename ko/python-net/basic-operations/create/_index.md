---
title: 프로그래밍 방식으로 PDF 문서 만들기
linktitle: PDF 만들기
type: docs
weight: 10
url: /ko/python-net/create-document/
description: 이 페이지에서는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 처음부터 PDF 문서를 만드는 방법을 설명합니다.
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python을 사용한 PDF 파일 생성
Abstract: 소프트웨어 개발에서 PDF 파일을 프로그래밍 방식으로 생성하는 것은 일반적인 요구 사항이며, 특히 보고서 및 기타 문서를 만들 때 많이 필요합니다. 이 작업을 위해 직접 코드를 작성하면 비효율적이고 시간이 많이 소요될 수 있습니다. 대신 개발자는 **Aspose.PDF for Python via .NET**를 활용할 수 있으며, 이는 Python으로 PDF 파일을 생성하기 위한 강력한 솔루션입니다. 이 과정은 `Document` 객체를 생성하고, 문서의 `Pages` 컬렉션에 `Page` 객체를 추가한 다음, 페이지의 `paragraphs` 컬렉션에 `TextFragment`를 삽입하고, 마지막으로 문서를 저장하는 단계로 이루어집니다. 샘플 Python 코드 조각이 이러한 단계를 보여 주며, Aspose.PDF를 사용하여 PDF 파일을 쉽게 생성할 수 있음을 보여줍니다.
---

개발자에게는 프로그래밍 방식으로 PDF 파일을 생성해야 하는 다양한 상황이 있습니다. 소프트웨어에서 PDF 보고서 및 기타 PDF 파일을 프로그래밍 방식으로 생성해야 할 수도 있습니다. 처음부터 직접 코드와 함수를 작성하는 것은 매우 오래 걸리고 비효율적입니다. Python으로 PDF 파일을 생성하려면 더 나은 솔루션인 **Aspose.PDF for Python via .NET**를 사용할 수 있습니다.

## Python을 사용하여 PDF 파일 만드는 방법

Python을 사용하여 PDF 파일을 만들려면 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 객체를 생성합니다.
1. Document 객체의 [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 컬렉션에 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체를 추가합니다.
1. 페이지의 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 컬렉션에 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)를 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```



