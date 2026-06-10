---
title: 파이썬을 사용한 헬로 월드 예제
linktitle: 헬로 월드 예제
type: docs
weight: 20
url: /ko/python-net/hello-world-example/
description: 이 샘플은 .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 Hello World 텍스트가 포함된 간단한 PDF 문서를 만드는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 이용한 헬로 월드 예제
Abstract: 이 문서에서는 .NET 라이브러리를 통해 파이썬용 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 만드는 Hello World 예제를 제공합니다.이 예제에서는 “Hello World!” 텍스트가 포함된 PDF를 생성하여 Aspose.PDF API를 사용하는 기본 단계를 보여줍니다.이 프로세스에는 '문서' 객체의 인스턴스화, '페이지' 추가, 'TextFragment' 객체 생성, 글꼴 크기 및 색상과 같은 텍스트 속성 설정, 'TextBuilder'를 사용하여 페이지에 텍스트를 추가하는 과정이 포함됩니다.그러면 결과 PDF가 "HelloWorld_out.pdf “로 저장됩니다.이 문서에는 이러한 단계를 설명하는 전체 Python 코드 스니펫이 포함되어 있으며 라이브러리 사용에 대한 입문 가이드 역할을 합니다.
---

“Hello World” 예제는 특정 프로그래밍 언어에서 가장 간단한 구문과 가장 간단한 프로그램을 보여줍니다.개발자는 기기 화면에 “Hello World”를 인쇄하는 방법을 학습하여 기본 프로그래밍 언어 구문을 배울 수 있습니다.따라서 우리는 전통적으로 라이브러리부터 익히기 시작합니다.

이 기사에서는 “Hello World!” 라는 텍스트가 포함된 PDF 문서를 만들고 있습니다.사용자 환경에.NET을 통해 파이썬용**Aspose.pdf를 설치한 후 아래 코드 샘플을 실행하여 Aspose.PDF API의 작동 방식을 확인할 수 있습니다.

아래 코드 스니펫은 다음 단계를 따릅니다.

1. a 인스턴스화 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 목적
1. 추가 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 문서 객체로
1. 만들기 [텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 목적
1. 텍스트 색상 설정
1. 텍스트 빌더 만들기
1. 추가 [텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 페이지로
1. [문서. 저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 결과 PDF 문서

다음 코드 스니펫은.NET API를 통해 파이썬용 Aspose.PDF 기능을 보여주는 “Hello World” 프로그램입니다.

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
    textFragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
