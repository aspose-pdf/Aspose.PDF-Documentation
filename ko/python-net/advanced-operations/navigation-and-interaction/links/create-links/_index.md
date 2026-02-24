---
title: Python으로 PDF 파일에 링크 만들기
linktitle: 링크 만들기
type: docs
weight: 10
url: /ko/python-net/create-links/
description: 이 섹션에서는 Python을 사용하여 PDF 문서에 링크를 만드는 방법을 설명합니다.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF에서 링크 만드는 방법
Abstract: Aspose.PDF for Python via .NET 링크 생성 가이드는 개발자에게 Python을 사용하여 PDF 문서에 대화형 하이퍼링크를 추가하는 실용적인 지침을 제공합니다. 여기에는 외부 애플리케이션을 실행하거나 같은 문서 내 특정 페이지로 이동하거나 다른 PDF 파일을 열 수 있는 다양한 유형의 링크를 만드는 방법이 포함됩니다. 설명서에서는 LinkAnnotation 객체를 사용하고 Rectangle 로 클릭 가능한 영역을 정의하며 LaunchAction 또는 GoToRemoteAction 과 같은 동작을 할당하는 방법을 설명합니다. 명확한 코드 예제와 단계별 안내를 통해 이 리소스는 개발자가 Python 애플리케이션에서 PDF 탐색 및 상호 작용성을 향상시키는 데 도움이 됩니다.
---

## PDF 문서의 링크

PDF 1.7 사양(ISO 32000-1:2008)에 따르면, **Link annotation**은 주석이 활성화될 때 발생하는 동작을 정의하는 여러 유형의 액션을 트리거할 수 있습니다. 지원되는 주요 액션은 다음과 같습니다:

1. **GoTo** – 같은 문서 내 목적지로 이동합니다.
1. **GoToR** – 다른 PDF 파일의 목적지로 이동합니다(원격 이동).
1. **URI** – 일반적으로 웹 링크인 통합 자원 식별자를 엽니다.
1. **Launch** – 애플리케이션을 실행하거나 파일을 엽니다(플랫폼에 따라 다르며 보안상 제한될 수 있음).
1. **Named** – 다음 페이지로 이동하거나 문서를 인쇄하는 등 미리 정의된 작업을 실행합니다.
1. **JavaScript** – 삽입된 JavaScript 코드를 실행합니다(보안 문제로 주의해서 사용).
1. **SubmitForm** – 양식 데이터를 지정된 URL로 전송합니다.
1. **ResetForm** – 양식 필드를 기본값으로 재설정합니다.
1. **ImportData** – 외부 파일에서 데이터를 문서로 가져옵니다.

문서에 애플리케이션에 대한 링크를 추가하면 문서에서 해당 애플리케이션으로 연결할 수 있습니다. 이는 예를 들어 튜토리얼의 특정 지점에서 독자가 특정 행동을 취하도록 하거나, 기능이 풍부한 문서를 만들 때 유용합니다.

‘LaunchAction’을 사용하여 애플리케이션 링크를 만들려면:

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## PDF 파일에 PDF 문서 링크 만들기

### GoToRemoteAction 사용

이 코드 조각은 Python PDF 라이브러리를 사용하여 PDF 문서의 특정 페이지에 링크 주석을 추가하는 방법을 보여줍니다.

1. PDF 문서를 엽니다
1. 문서의 두 번째 페이지를 선택합니다(인덱스 1).
1. 링크 주석을 생성합니다:
1. 좌표 (10, 580, 120, 600) 위치에
1. 색상을 녹색으로 설정
1. 'sample.pdf'의 첫 페이지로 연결
1. 페이지에 링크 주석을 추가합니다
1. 수정된 문서를 출력 파일 경로에 저장합니다

‘GoToRemoteAction’을 사용하여 PDF 문서 링크를 만들려면:

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### GoToAction 사용

이 코드는 Aspose.PDF for Python을 사용하여 PDF 문서의 특정 페이지에 링크 주석을 추가하는 방법을 보여줍니다. 해당 링크는 녹색 점선 테두리 사각형으로 표시되며 사용자가 같은 PDF 내의 다른 페이지로 이동할 수 있게 합니다. ‘GoToAction’을 사용하여 PDF 문서 링크를 만들려면:

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### GoToURIAction 적용

다음 예제는 Aspose.PDF for Python을 사용하여 PDF 문서에 링크 주석을 추가하는 방법을 보여줍니다. 해당 링크는 첫 페이지에 녹색 클릭 가능한 영역으로 표시되며, 클릭하면 GoToURIAction을 통해 웹 브라우저에서 Aspose.PDF for Python 문서가 열립니다.

이 기능은 유용한 외부 참고 자료, 문서 또는 지원 링크를 PDF에 직접 삽입하는 데 유용합니다.

1. PDF 문서를 로드합니다. ap.Document를 사용하여 기존 PDF 파일을 엽니다.
1. 첫 페이지에 접근합니다. document.pages[1]을 사용하여 첫 페이지에 접근합니다(Aspose는 1부터 시작하는 인덱스를 사용).
1. 링크 주석을 생성합니다. LinkAnnotation 객체를 만들고 ap.Rectangle를 사용하여 클릭 가능한 사각형 영역을 지정합니다.
1. 주석의 외관을 설정합니다. link.color = ap.Color.green를 사용하여 주석 색상을 녹색으로 지정합니다.
1. URI 동작을 할당합니다. GoToURIAction을 사용하여 주석을 외부 URL에 연결합니다.
1. 페이지에 주석을 추가합니다. 구성된 링크 주석을 첫 페이지의 주석 컬렉션에 추가합니다.
1. 수정된 문서를 저장합니다. 업데이트된 PDF 문서를 지정된 출력 경로에 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

