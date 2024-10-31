---
title: Python을 사용한 Hello World 예제
linktitle: Hello World 예제
type: docs
weight: 20
url: /python-net/hello-world-example/
description: 이 샘플은 Aspose.PDF for Python via .NET을 사용하여 Hello World 텍스트가 포함된 간단한 PDF 문서를 만드는 방법을 보여줍니다.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

"Hello World" 예제는 주어진 프로그래밍 언어에서 가장 간단한 문법과 프로그램을 보여줍니다. 개발자는 기기 화면에 "Hello World"를 출력하는 방법을 배우면서 기본 프로그래밍 언어 문법을 소개받습니다. 따라서 우리는 전통적으로 라이브러리와의 첫 만남을 여기서부터 시작할 것입니다.

이 기사에서는 "Hello World!" 텍스트가 포함된 PDF 문서를 생성합니다. 환경에 **Aspose.PDF for Python via .NET**을 설치한 후, 아래 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.

아래 코드 스니펫은 다음 단계에 따릅니다:


1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체 인스턴스화
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 추가
1. [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 객체 생성
1. 페이지의 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 컬렉션에 TextFragment 추가
1. 결과 PDF 문서 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

다음 코드 스니펫은 .NET API를 통한 Python용 Aspose.PDF의 작동을 보여주는 "Hello World" 프로그램입니다.

```python

    import aspose.pdf as ap

    # 문서 객체 초기화
    document = ap.Document()
    # 페이지 추가
    page = document.pages.add()
    # 텍스트 프래그먼트 객체 초기화
    text_fragment = ap.text.TextFragment("Hello,world!")
    # 새 페이지에 텍스트 프래그먼트 추가
    page.paragraphs.add(text_fragment)
    # 업데이트된 PDF 저장
    document.save("output.pdf")
```