---
title: Python을 사용한 Hello World 예제
linktitle: Hello World 예제
type: docs
weight: 20
url: /ko/python-net/hello-world-example/
description: 이 샘플은 Aspose.PDF for Python via .NET을 사용하여 텍스트 Hello World가 포함된 간단한 PDF 문서를 만드는 방법을 보여줍니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 통한 Hello World 예제
Abstract: 이 문서는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서를 만드는 Hello World 예제를 제공합니다. 이 예제는 "Hello World!" 텍스트가 포함된 PDF를 생성함으로써 Aspose.PDF API 사용의 기본 단계를 보여줍니다. 과정은 `Document` 객체를 인스턴스화하고, `Page`를 추가하고, `TextFragment` 객체를 생성하고, 글꼴 크기 및 색상과 같은 텍스트 속성을 설정한 뒤, `TextBuilder`를 사용해 페이지에 텍스트를 추가하는 것을 포함합니다. 결과 PDF는 "HelloWorld_out.pdf"로 저장됩니다. 이 문서는 이러한 단계들을 보여주는 완전한 Python 코드 스니펫을 포함하여 라이브러리 사용에 대한 입문 안내서 역할을 합니다.
---

"Hello World" 예제는 모든 프로그래밍 언어에서 가장 간단한 구문과 프로그램을 보여줍니다. 개발자는 디바이스 화면에 "Hello World"를 출력하는 방법을 배우면서 기본 언어 구문을 소개받습니다. 따라서 우리는 전통적으로 우리 라이브러리를 이 예제로부터 소개합니다.

이 문서에서는 텍스트 "Hello World!"가 포함된 PDF 문서를 만들고 있습니다. 환경에 **Aspose.PDF for Python via .NET**을 설치한 후, 아래 코드 샘플을 실행하면 Aspose.PDF API가 어떻게 동작하는지 확인할 수 있습니다.

아래 코드 스니펫은 다음 단계들을 따릅니다:

1. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 인스턴스화합니다
1. 문서 객체에 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 추가합니다
1. [텍스트 조각](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 객체를 생성합니다
1. 텍스트 색상 설정
1. 텍스트 빌더 생성
1. 페이지에 [텍스트 조각](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)을 추가합니다
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 로 결과 PDF 문서를 저장합니다

다음 코드 스니펫은 Aspose.PDF for Python via .NET API의 기능을 보여주는 "Hello World" 프로그램입니다.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
