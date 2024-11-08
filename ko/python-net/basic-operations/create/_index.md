---
title: 프로그래밍으로 PDF 문서 생성
linktitle: PDF 생성
type: docs
weight: 10
url: /ko/python-net/create-document/
description: 이 페이지는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 처음부터 PDF 문서를 생성하는 방법을 설명합니다.
---

개발자에게는 프로그래밍으로 PDF 파일을 생성해야 하는 많은 시나리오가 있습니다. 소프트웨어에서 PDF 보고서 및 기타 PDF 파일을 프로그래밍으로 생성해야 할 수도 있습니다. 처음부터 코드를 작성하고 함수를 작성하는 것은 상당히 길고 비효율적입니다. Python으로 PDF 파일을 생성하려면 더 나은 해결책이 있습니다 - **Aspose.PDF for Python via .NET**.

## Python을 사용하여 PDF 파일 생성 방법

Python을 사용하여 PDF 파일을 생성하려면 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 객체를 생성합니다.

1. [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체를 Document 객체의 [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 컬렉션에 추가합니다.
1. 페이지의 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 컬렉션에 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)를 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap

    # 문서 객체 초기화
    document = ap.Document()
    # 페이지 추가
    page = document.pages.add()
    # textfragment 객체 초기화
    text_fragment = ap.text.TextFragment("Hello,world!")
    # 새 페이지에 텍스트 조각 추가
    page.paragraphs.add(text_fragment)
    # 업데이트된 PDF 저장
    document.save("output.pdf")
```