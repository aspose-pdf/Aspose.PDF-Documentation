---
title: 파이썬으로 PDF 링크 만들기
linktitle: 링크 생성
type: docs
weight: 10
url: /ko/python-net/create-links/
description: Python에서 내부, 외부 및 원격 PDF 링크를 만드는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 링크를 만드는 방법
Abstract: .NET을 통한 링크 생성에 관한 Aspose.PDF Python용 안내서는 Python을 사용하여 PDF 문서에 대화형 하이퍼링크를 추가하는 방법에 대한 실용적인 지침을 개발자에게 제공합니다.외부 응용 프로그램을 실행하거나, 동일한 문서 내의 특정 페이지로 이동하거나, 다른 PDF 파일을 여는 링크를 비롯한 다양한 유형의 링크를 만드는 방법을 다룹니다.이 문서에서는 링크 주석 객체를 사용하고, 사각형을 사용하여 클릭 가능한 영역을 정의하고, LaunchAction 또는 GoToRemoteAction과 같은 작업을 할당하는 방법을 설명합니다.명확한 코드 예제와 단계별 지침을 제공하는 이 리소스는 개발자가 Python 응용 프로그램에서 PDF 탐색 및 상호 작용을 향상시키는 데 도움이 됩니다.
---

## PDF 문서의 링크

PDF 1.7 사양 (ISO 32000-1:2008) 에 따르면**링크 주석**은 주석이 활성화될 때 발생하는 상황을 정의하는 여러 유형의 작업을 트리거할 수 있습니다.지원되는 기본 작업은 다음과 같습니다.

1. **GoTo** — 동일한 문서 내에서 목적지로 이동합니다.
1. **GoTor** — 다른 PDF 파일의 목적지로 이동합니다 (원격 이동).
1. **URI** — 통일 리소스 식별자 (일반적으로 웹 링크) 를 엽니다.
1. **Launch** — 애플리케이션을 시작하거나 파일을 엽니다 (플랫폼에 따라 다르며 보안을 위해 제한되는 경우가 많음).
1. **이름** — 다음 페이지로 이동하거나 문서를 인쇄하는 등 미리 정의된 작업을 실행합니다.
1. **JavaScript** — 내장된 자바스크립트 코드를 실행합니다 (보안 문제로 인해 주의해서 사용).
1. **제출양식** — 지정된 URL에 양식 데이터를 제출합니다.
1. **resetForm** — 양식 필드를 기본값으로 재설정합니다.
1. **ImportData** — 외부 파일에서 문서로 데이터를 가져옵니다.

문서에 응용 프로그램 링크를 추가하면 문서에서 응용 프로그램으로 연결할 수 있습니다.예를 들어 독자가 자습서의 특정 시점에서 특정 작업을 수행하도록 하거나 기능이 풍부한 문서를 만들고자 할 때 유용합니다.

'LaunchAction'을 사용하여 애플리케이션 링크를 생성하려면:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## PDF 파일에 PDF 문서 링크 만들기

### GoToToRemoteAction 사용

이 코드 스니펫은 Python PDF 라이브러리를 사용하여 PDF 문서의 특정 페이지에 링크 주석을 추가하는 방법을 보여줍니다.

1. PDF 문서 열기
1. 문서의 두 번째 페이지 선택 (색인 1)
1. 링크 주석 만들기:
1. 좌표 (10, 580, 120, 600) 에 위치 지정
1. 컬러 그린
1. 첫 페이지에 있는 'sample.pdf' 링크
1. 페이지에 링크 주석 추가
1. 수정된 문서를 출력 파일 경로에 저장

'GoToRemoteAction'을 사용하여 PDF 문서 링크를 만들려면:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### GoToAction 사용

이 코드는 Python용 Aspose.PDF 를 사용하여 PDF 문서의 특정 페이지에 링크 주석을 추가하는 방법을 보여줍니다.링크는 대시 테두리가 있는 녹색 사각형으로 표시되며, 이를 통해 사용자는 동일한 PDF 내에서 다른 페이지로 이동할 수 있습니다.'GoToAction'을 사용하여 PDF 문서 링크를 만들려면:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### 고투어액션 적용

다음 예제는 Python용 Aspose.PDF 를 사용하여 PDF 문서에 링크 주석을 추가하는 방법을 보여줍니다.링크는 첫 페이지에 녹색 클릭 가능 영역으로 표시되며, 클릭하면 GoTouriAction을 통해 웹 브라우저에서 Python용 Aspose.PDF 문서가 열립니다.

이 기능은 유용한 외부 참조, 문서 또는 지원 링크를 PDF에 직접 포함시키는 데 유용합니다.

1. PDF 문서를 로드합니다.AP.Document를 사용하여 기존 PDF 파일을 엽니다.
1. 첫 페이지에 접속하세요.document.pages [1] 를 사용하여 첫 페이지에 액세스합니다 (Aspose는 1 기반 인덱싱을 사용합니다).
1. 링크 주석 만들기LinkAnnotation 객체를 만들고 ap.Rectangle 을 사용하여 클릭 가능한 사각형 영역을 지정합니다.
1. 주석 모양을 설정합니다.link.color = ap.Color.Green을 사용하여 주석의 색상을 녹색으로 설정합니다.
1. URI 작업을 할당합니다.GoTouriAction을 사용하여 주석을 외부 URL에 연결할 수 있습니다.
1. 페이지에 주석을 추가합니다.구성된 링크 주석을 첫 페이지의 주석 컬렉션에 추가합니다.
1. 수정된 문서를 저장합니다.업데이트된 PDF 문서를 지정된 출력 경로에 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## 관련 링크 주제

- [파이썬에서 PDF 링크로 작업하기](/pdf/ko/python-net/links/)
- [파이썬에서 PDF에서 링크 추출하기](/pdf/ko/python-net/extract-links/)
- [Python을 사용하여 PDF에서 링크 업데이트](/pdf/ko/python-net/update-links/)