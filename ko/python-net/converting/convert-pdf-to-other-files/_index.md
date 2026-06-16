---
title: 파이썬에서 PDF를 EPUB, 텍스트, XPS 등으로 변환
linktitle: PDF를 다른 형식으로 변환
type: docs
weight: 90
url: /ko/python-net/convert-pdf-to-other-files/
lastmod: "2026-06-10"
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 파이썬에서 EPUB, LaTeX, 마크다운, 텍스트, XPS, MobiXML로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Python에서 PDF를 다른 형식으로 변환하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 파일을 다양한 형식으로 변환하는 방법에 대한 포괄적인 가이드를 제공합니다.PDF를 EPUB, 라텍스/텍스, 텍스트, XPS 및 XML 형식으로 변환하는 방법을 다룹니다.각 섹션은 PDF를 각 형식으로 변환하기 위해 Aspose에서 제공하는 온라인 응용 프로그램을 사용해 볼 수 있는 초대로 시작하며, 이러한 도구의 사용 편의성과 품질을 강조합니다.
---

## PDF를 EPUB로 변환

{{% alert color="success" %}}
**온라인에서 PDF를 EPUB로 변환해 보세요**

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 EPUB로”](https://products.aspose.app/pdf/conversion/pdf-to-epub)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PDF를 EPUB로 변환](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> 국제 디지털 출판 포럼 (IDPF) 에서 제공하는 무료 공개 전자책 표준입니다.파일의 확장자는.epub입니다.
EPUB은 리플로우 가능 콘텐츠용으로 설계되었습니다. 즉, EPUB 리더는 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있습니다.EPUB은 고정 레이아웃 콘텐츠도 지원합니다.이 형식은 출판사와 전환 업체가 배포 및 판매뿐만 아니라 사내에서 사용할 수 있는 단일 형식으로 설계되었습니다.이 표준은 Open eBook 표준을 대체합니다.

파이썬용 Aspose.PDF 는 PDF 문서를 EPUB 형식으로 변환하는 기능도 지원합니다.파이썬용 Aspose.PDF 에는 'EPubSaveOptions'라는 이름의 클래스가 있는데, 이 클래스는 두 번째 인수로 사용할 수 있습니다. [문서. 저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메소드, EPUB 파일을 생성합니다.
Python에서 이 요구 사항을 충족하려면 다음 코드 스니펫을 사용해 보십시오.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 관련 전환

- [PDF를 워드로 변환](/pdf/ko/python-net/convert-pdf-to-word/) 편집 가능한 Office 문서 출력용
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 브라우저 지향 출력용.
- [PDF를 PDF/A, PDF/E 및 PDF/X로 변환](/pdf/ko/python-net/convert-pdf-to-pdf_x/) 아카이브 및 표준 준수 변환 워크플로우에 적합합니다.

## PDF를 라텍스/텍스로 변환

**.NET을 통한 파이썬용 ASpose.pdf**는 PDF를 라텍스/텍스로 변환하는 기능을 지원합니다.
LaTeX 파일 형식은 특수 마크업이 있는 텍스트 파일 형식이며 고품질 조판을 위해 TEX 기반 문서 준비 시스템에서 사용됩니다.

{{% alert color="success" %}}
**온라인에서 PDF를 라텍스/텍스로 변환해 보세요**

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 라텍스로”](https://products.aspose.app/pdf/conversion/pdf-to-tex)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PDF를 라텍스/텍스로 변환](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDF 파일을 TeX로 변환하기 위해 Aspose.PDF 클래스는 다음과 같습니다. [라텍스 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) 변환 프로세스 중에 임시 이미지를 저장하기 위한 outDirectoryPath 속성을 제공합니다.

다음 코드 스니펫은 Python을 사용하여 PDF 파일을 TEX 형식으로 변환하는 프로세스를 보여줍니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF를 텍스트로 변환

**파이썬용 Aspose.pdf**는 전체 PDF 문서와 단일 페이지를 텍스트 파일로 변환하는 기능을 지원합니다.'TextDevice' 클래스를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다.다음 코드 스니펫은 모든 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 PDF 변환을 텍스트로 변환해 보세요**

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 텍스트로”](https://products.aspose.app/pdf/conversion/pdf-to-txt)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PDF를 텍스트로 변환](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF를 XPS로 변환

**파이썬용 Aspose.pdf**를 사용하면 PDF 파일을 XPS 형식으로 변환할 수 있습니다.제시된 코드 스니펫을 사용하여 Python을 사용하여 PDF 파일을 XPS 형식으로 변환해 보겠습니다.

{{% alert color="success" %}}
**온라인에서 PDF를 XPS로 변환해 보세요**

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 XPS로”](https://products.aspose.app/pdf/conversion/pdf-to-xps)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PDF를 XPS로 변환](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 파일 형식은 주로 마이크로소프트의 XML 문서 사양과 관련이 있습니다.이전에 코드명이 메트로이고 차세대 인쇄 경로 (NGPP) 마케팅 개념을 포함하는 XML 문서 사양 (XPS) 은 문서 작성 및 보기 기능을 Windows 운영 체제에 통합하려는 Microsoft의 이니셔티브입니다.

PDF 파일을 XPS로 변환하기 위해 Aspose.PDF 클래스는 다음과 같습니다. [XPS 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) 의 두 번째 인수로 사용됩니다. [문서. 저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) XPS 파일을 생성하는 메서드입니다.

다음 코드 스니펫은 PDF 파일을 XPS 형식으로 변환하는 과정을 보여줍니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF를 MD로 변환

Aspose.PDF 에는 이미지와 리소스를 보존하면서 PDF 문서를 마크다운 (MD) 형식으로 변환하는 'MarkdownSaveOptions () '클래스가 있습니다.

1. 'AP.Document'를 사용하여 소스 PDF를 로드합니다.
1. '마크다운 저장 옵션' 인스턴스를 생성합니다.
1. '리소스_디렉터리_이름'을 '이미지'로 설정하면 추출된 이미지가 이 폴더에 저장됩니다.
1. 구성된 옵션을 사용하여 변환된 마크다운 문서를 저장합니다.
1. 변환 후 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

지정된 이미지 폴더에 저장된 텍스트와 연결된 이미지가 포함된 마크다운 파일입니다.

## PDF를 모비XML로 변환

이 메서드는 PDF 문서를 킨들 장치의 전자책에 일반적으로 사용되는 MOBI (MobiXML) 형식으로 변환합니다.

1. 'AP.Document'를 사용하여 원본 PDF 문서를 로드합니다.
1. 문서를 'ap.SaveFormat.mobi_XML' 형식으로 저장합니다.
1. 변환이 완료되면 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
