---
title: Python에서 다른 파일 형식을 PDF로 변환
linktitle: 다른 파일 형식을 PDF로 변환
type: docs
weight: 80
url: /ko/python-net/convert-other-files-to-pdf/
lastmod: "2026-06-10"
description: .NET을 통해 파이썬용 Aspose.PDF 를 사용하여 EPUB, 마크다운, PCL, XPS, 포스트스크립트, XML 및 LaTeX 파일을 파이썬에서 PDF로 변환하는 방법을 알아봅니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python에서 다른 파일 형식을 PDF로 변환하는 방법
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 기능을 활용하여 Python을 사용하여 다양한 파일 형식을 PDF로 변환하는 방법에 대한 포괄적인 가이드를 제공합니다.이 문서에서는 EPUB, 마크다운, PCL, 텍스트, XPS, 포스트스크립트, XML, XSL-FO, 라텍스/텍스를 비롯한 여러 형식의 변환 프로세스를 간략하게 설명합니다.각 섹션에서는 이러한 변환을 구현하기 위한 특정 코드 스니펫과 지침을 제공합니다.이 문서에서는 정확하고 효율적인 변환을 보장하기 위해 각 파일 유형에 맞게 조정된 로드 옵션과 같은 Aspose.PDF 기능의 유용성을 강조합니다.또한 사용자가 직접 기능을 탐색할 수 있도록 온라인 변환 응용 프로그램을 사용할 수 있다는 점도 강조합니다.이 안내서는 PDF 변환 기능을 Python 응용 프로그램에 통합하려는 개발자를 위한 실용적인 리소스 역할을 합니다.
---

이 문서에서는**Python을 사용하여 다양한 다른 유형의 파일 형식을 PDF로 변환하는 방법**을 설명합니다.다음 주제를 다룹니다.

## OFD를 PDF로 변환

OFD는 열린 고정 레이아웃 문서 (열린 고정 문서 형식이라고도 함) 의 약자입니다.PDF의 대안으로 도입된 전자 문서에 대한 중국 국가 표준 (GB/T 33190-2016) 입니다.

파이썬에서 OFD를 PDF로 변환하는 단계:

1. OFD 로드 옵션 () 을 사용하여 OFD 로드 옵션을 설정합니다.
1. OFD 문서를 로드합니다.
1. PDF로 저장합니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 라텍스/텍스를 PDF로 변환

LaTeX 파일 형식은 TeX 언어 계열의 LaTeX 파생어에 마크업이 있는 텍스트 파일 형식이고 LaTeX는 TeX 시스템에서 파생된 형식입니다.LaTeX (letk/lay-tek 또는 lah-tek) 는 문서 준비 시스템이자 문서 마크업 언어입니다.수학, 물리학, 컴퓨터 과학 등 다양한 분야의 과학 문서 커뮤니케이션 및 출판에 널리 사용됩니다.또한 특별판을 포함하여 한국어, 일본어, 중국어, 아랍어 등 복잡한 다국어 자료를 포함하는 서적 및 기사를 준비하고 출판하는 데에도 중요한 역할을 합니다.

LaTeX는 TeX 조판 프로그램을 사용하여 출력 형식을 지정하며 자체적으로 TeX 매크로 언어로 작성되었습니다.

{{% alert color="success" %}}
**라텍스/텍스를 온라인으로 PDF로 변환해 보세요**

.NET을 통한 파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“라텍스를 PDF로”](https://products.aspose.app/pdf/conversion/tex-to-pdf)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 라텍스/텍스를 PDF로 변환](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

파이썬에서 TEX를 PDF로 변환하는 단계:

1. LaTeXLoadOptions () 를 사용하여 라텍스 로드 옵션을 설정합니다.
1. LaTeX 문서를 로드합니다.
1. PDF로 저장합니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## EPUB를 PDF로 변환

**.NET을 통한 파이썬용 Aspose.pdf**를 사용하면 EPUB 파일을 PDF 형식으로 간단히 변환할 수 있습니다.

EPUB (전자 출판의 줄임말) 은 국제 디지털 출판 포럼 (IDPF) 에서 제공하는 무료 공개 전자책 표준입니다.파일의 확장자는.epub입니다.EPUB은 리플로우 가능한 콘텐츠용으로 설계되었습니다. 즉, EPUB 리더는 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있습니다.

<abbr title="electronic publication">EPUB</abbr> 고정 레이아웃 콘텐츠도 지원합니다.이 형식은 출판사와 전환 업체가 사내에서 사용할 수 있을 뿐만 아니라 배포 및 판매에도 사용할 수 있는 단일 형식으로 설계되었습니다.이 버전은 Open eBook 표준을 대체합니다. 또한 EPUB 3 버전은 표준화된 모범 사례, 연구, 정보 및 이벤트를 위한 선도적인 도서 무역 협회인 도서 산업 스터디 그룹 (BISG) 에서도 콘텐츠 패키징을 지지합니다.

{{% alert color="success" %}}
**EPUB를 온라인으로 PDF로 변환해 보세요**

.NET을 통한 파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“EPUB에서 PDF로”](https://products.aspose.app/pdf/conversion/epub-to-pdf)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 EPUB를 PDF로 변환](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

파이썬에서 EPUB를 PDF로 변환하는 단계:

1. EPUB 로드 옵션 () 을 사용하여 EPUB 문서를 로드합니다.
1. EPUB를 PDF로 변환합니다.
1. 확인 인쇄.

다음 다음 코드 스니펫은 Python을 사용하여 EPUB 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## 마크다운을 PDF로 변환

**이 기능은 버전 19.6 이상에서 지원됩니다.**

{{% alert color="success" %}}
**마크다운을 온라인에서 PDF로 변환해 보세요**

.NET을 통한 파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF로 마크다운”](https://products.aspose.app/pdf/conversion/md-to-pdf)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![앱을 사용하여 Aspose.PDF 마크다운을 PDF로 변환](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

.NET을 통해 Python용 Aspose.PDF 에서 작성한 이 코드 스니펫은 마크다운 파일을 PDF로 변환하여 문서 공유, 서식 보존 및 인쇄 호환성을 향상하는 데 도움이 됩니다.o

다음 코드 스니펫은 Aspose.PDF 라이브러리에서 이 기능을 사용하는 방법을 보여줍니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## PCL을 PDF로 변환

<abbr title="Printer Command Language">PCL</abbr> (프린터 명령 언어) 는 표준 프린터 기능에 액세스하기 위해 개발된 Hewlett-Packard 프린터 언어입니다.PCL 레벨 1~5e/5c는 수신된 순서대로 처리되고 해석되는 제어 시퀀스를 사용하는 명령 기반 언어입니다.소비자 수준에서 PCL 데이터 스트림은 프린터 드라이버에 의해 생성됩니다.또한 사용자 지정 애플리케이션에서 PCL 출력을 쉽게 생성할 수 있습니다.

{{% alert color="success" %}}
**온라인에서 PCL을 PDF로 변환해 보세요**

.NET용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PCL을 PDF로”](https://products.aspose.app/pdf/conversion/pcl-to-pdf)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PCL을 PDF로 변환](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

PCL에서 PDF로 변환할 수 있도록 하기 위해 Aspose.PDF 클래스는 다음과 같습니다. [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) LoadOptions 객체를 초기화하는 데 사용됩니다.이후 이 객체는 Document 객체 초기화 중에 인수로 전달되며, 이는 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움이 됩니다.

다음 코드 스니펫은 PCL 파일을 PDF 형식으로 변환하는 프로세스를 보여줍니다.

파이썬에서 PCL을 PDF로 변환하는 단계:

1. PCL로드 옵션 () 을 사용하여 PCL에 대한 옵션을 로드합니다.
1. 문서를 로드합니다.
1. PDF로 저장합니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 미리 서식이 지정된 텍스트를 PDF로 변환

**.NET을 통한 파이썬용 Aspose.pdf**는 일반 텍스트와 미리 서식이 지정된 텍스트 파일을 PDF 형식으로 변환하는 기능을 지원합니다.

텍스트를 PDF로 변환한다는 것은 PDF 페이지에 텍스트 조각을 추가하는 것을 의미합니다.텍스트 파일의 경우 두 가지 유형의 텍스트를 처리합니다. 하나는 사전 서식 지정 (예: 25줄에 80자로 구성된 사전 서식 지정) 이고 다른 하나는 서식이 지정되지 않은 텍스트 (일반 텍스트) 입니다.필요에 따라 이 추가 기능을 직접 제어하거나 라이브러리의 알고리즘에 맡길 수 있습니다.

{{% alert color="success" %}}
**온라인에서 텍스트를 PDF로 변환해 보세요**

.NET을 통한 파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“텍스트를 PDF로”](https://products.aspose.app/pdf/conversion/txt-to-pdf)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 텍스트를 PDF로 변환](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

파이썬에서 텍스트를 PDF로 변환하는 단계:

1. 입력 텍스트 파일을 한 줄씩 읽습니다.
1. 일관된 텍스트 정렬을 위해 고정 폭 글꼴 (Courier New) 을 설정합니다.
1. 새 PDF 문서를 만들고 사용자 지정 여백 및 글꼴 설정이 있는 첫 페이지를 추가합니다.
1. 텍스트 파일의 여러 줄을 반복합니다. 타자기를 시뮬레이션하기 위해 'monospace_font' 글꼴과 크기 12를 사용합니다.
1. 페이지 생성을 4페이지로 제한합니다.
1. 최종 PDF를 지정된 경로에 저장합니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 포스트스크립트를 PDF로 변환

이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 포스트스크립트 파일을 PDF 문서로 변환하는 방법을 보여줍니다.

1. PS 파일을 올바르게 해석하려면 'PSLoadOptions' 인스턴스를 생성하십시오.
1. 로드 옵션을 사용하여 'PostScript' 파일을 문서 객체에 로드합니다.
1. 문서를 원하는 출력 경로에 PDF 형식으로 저장합니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## XPS를 PDF로 변환

**.NET을 통한 파이썬용.pdf**는 기능 변환을 지원합니다. <abbr title="XML Paper Specification">XPS</abbr> 파일을 PDF 형식으로 변환합니다.작업을 해결하려면 이 문서를 확인하세요.

XPS 파일 형식은 주로 마이크로소프트의 XML 문서 사양과 관련이 있습니다.이전에 코드명이 메트로이고 차세대 인쇄 경로 (NGPP) 마케팅 개념을 포함하는 XML 문서 사양 (XPS) 은 문서 작성 및 보기를 Windows 운영 체제에 통합하려는 Microsoft의 이니셔티브입니다.

다음 코드 스니펫은 Python을 사용하여 XPS 파일을 PDF 형식으로 변환하는 프로세스를 보여줍니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**XPS 형식을 온라인으로 PDF로 변환해 보세요**

.NET을 통한 파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“XPS에서 PDF로”](https://products.aspose.app/pdf/conversion/xps-to-pdf/)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 XPS를 PDF로 변환](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## XSL-FO를 PDF로 변환

다음 코드 스니펫을 사용하여.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 XSLFO를 PDF 형식으로 변환할 수 있습니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## XSLT를 사용하여 XML을 PDF로 변환

이 예제에서는 먼저 XSLT 템플릿을 사용하여 XML 파일을 HTML로 변환한 다음 HTML을 Aspose.PDF 에 로드하여 PDF로 변환하는 방법을 보여줍니다.

1. 'HTMLLoadOptions'의 인스턴스를 생성하여 HTML을 PDF로 변환하도록 구성하십시오.
1. 변환된 HTML 파일을 Aspose.PDF 문서 객체로 로드합니다.
1. 문서를 지정된 출력 경로에 PDF로 저장합니다.
1. 변환에 성공하면 임시 HTML 파일을 제거합니다.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## 관련 전환

- [HTML을 PDF로 변환](/pdf/ko/python-net/convert-html-to-pdf/) HTML 및 MHTML 변환 시나리오에 적합합니다.
- [이미지 형식을 PDF로 변환](/pdf/ko/python-net/convert-images-format-to-pdf/) 입력이 PNG, JPEG, TIFF, SVG 또는 기타 이미지인 경우
- [PDF를 다른 형식으로 변환](/pdf/ko/python-net/convert-pdf-to-other-files/) PDF에서 EPUB, 마크다운 또는 텍스트로의 역변환도 필요한 경우
