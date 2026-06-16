---
title: 파이썬에서 이미지 형식을 PDF로 변환
linktitle: 이미지를 PDF로 변환
type: docs
weight: 60
url: /ko/python-net/convert-images-format-to-pdf/
lastmod: "2026-06-10"
description: .NET을 통해 파이썬용 Aspose.PDF 를 사용하여 BMP, CGM, DICOM, PNG, TIFF, EMF, SVG 및 기타 이미지 형식을 파이썬에서 PDF로 변환하는 방법을 알아봅니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python에서 이미지를 PDF로 변환하는 방법
Abstract: 이 문서에서는 Python을 사용하여 다양한 이미지 형식을 PDF로 변환하는 방법, 특히.NET을 통해 Python용 Aspose.PDF 라이브러리를 활용하는 방법에 대한 포괄적인 가이드를 제공합니다.이 문서에서는 BMP, CGM, DICOM, EMF, GIF, PNG, SVG 및 TIFF를 비롯한 다양한 이미지 형식을 다룹니다.각 섹션에서는 변환을 수행하는 데 필요한 단계를 자세히 설명하고 프로세스를 설명하는 코드 스니펫을 제공합니다.예를 들어 BMP를 PDF로 변환하려면 새 PDF 문서를 만들고, 이미지 배치를 정의하고, 이미지를 삽입하고, 문서를 저장해야 합니다.마찬가지로 CGM, DICOM 등과 같은 형식의 경우에도 특정 로드 옵션과 처리 단계가 설명되어 있습니다.또한 이 문서에서는 다양한 인코딩 방법을 지원하고 단일 프레임 및 다중 프레임 이미지를 모두 처리할 수 있는 기능 등 이러한 작업에 Aspose.PDF 를 사용할 때의 이점에 대해서도 설명합니다.
---

## 관련 전환

- [PDF를 이미지 형식으로 변환](/pdf/ko/python-net/convert-pdf-to-images-format/) 역방향 워크플로우가 필요할 때
- [HTML을 PDF로 변환](/pdf/ko/python-net/convert-html-to-pdf/) 웹 콘텐츠 및 MHTML 소스용
- [다른 파일 형식을 PDF로 변환](/pdf/ko/python-net/convert-other-files-to-pdf/) EPUB, XPS, 텍스트 및 기타 비이미지 입력에 사용됩니다.

## 파이썬 이미지를 PDF로 변환

**.NET을 통한 파이썬용 Aspose.pdf**를 사용하면 다양한 형식의 이미지를 PDF 파일로 변환할 수 있습니다.저희 라이브러리는 BMP, CGM, DICOM, EMF, JPG, PNG, SVG 및 TIFF 형식과 같이 가장 많이 사용되는 이미지 형식을 변환하기 위한 코드 스니펫을 보여줍니다.

## BMP를 PDF로 변환

.NET** 라이브러리를 통해 파이썬용**Aspose.pdf를 사용하여 BMP 파일을 PDF 문서로 변환합니다.

<abbr title="Bitmap Image File">BMP</abbr> 이미지는 확장자를 가진 파일입니다.BMP는 비트맵 디지털 이미지를 저장하는 데 사용되는 비트맵 이미지 파일을 나타냅니다.이러한 이미지는 그래픽 어댑터와는 독립적이며 DIB (장치 독립 비트맵) 파일 형식이라고도 합니다.

.NET API를 통해 파이썬용 Aspose.PDF 를 사용하여 BMP를 PDF 파일로 변환할 수 있습니다.따라서 다음 단계에 따라 BMP 이미지를 변환할 수 있습니다.

파이썬에서 BMP를 PDF로 변환하는 단계:

1. 빈 PDF 문서를 생성합니다.
1. 필요한 페이지를 작성하십시오. 예를 들어 A4를 만들었지만 원하는 형식을 지정할 수 있습니다.
1. 정의된 사각형을 사용하여 infile의 이미지를 페이지 안에 배치합니다.
1. 문서를 PDF로 저장합니다.

따라서 다음 코드 스니펫은 이러한 단계를 따르며 Python을 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 BMP를 PDF로 변환해 보세요**

Aspose는 온라인 신청서를 제공합니다 [“BMP를 PDF로”](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 BMP를 PDF로 변환](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGM을 PDF로 변환

.NET을 통해 Python용 Aspose.PDF 를 사용하여 CGM (컴퓨터 그래픽 메타파일) 을 PDF (또는 지원되는 다른 형식) 로 변환합니다.

<abbr title="Computer Graphics Metafile">CGM</abbr> CAD (컴퓨터 지원 설계) 및 프레젠테이션 그래픽 응용 프로그램에서 일반적으로 사용되는 컴퓨터 그래픽 메타파일 형식의 파일 확장자입니다.CGM은 바이너리 (프로그램 읽기 속도에 최적), 문자 기반 (파일 크기가 가장 작고 데이터 전송 속도 향상) 또는 일반 텍스트 인코딩 (텍스트 편집기로 파일을 읽고 수정할 수 있음) 의 세 가지 인코딩 방법을 지원하는 벡터 그래픽 형식입니다.

CGM 파일을 PDF 형식으로 변환하기 위한 다음 코드 스니펫을 확인하세요.

파이썬에서 CGM을 PDF로 변환하는 단계:

1. 파일 경로 정의
1. CGM의 로드 옵션을 설정합니다.
1. CGM을 PDF로 변환
1. 변환 메시지 인쇄

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## DICOM을 PDF로 변환

<abbr title="Digital Imaging and Communications in Medicine">디콤</abbr> 포맷은 디지털 의료 이미지 및 검사 대상 환자의 문서를 생성, 저장, 전송 및 시각화하기 위한 의료 산업 표준입니다.

**Python용 Aspose.pdf**에서는 DICOM 및 SVG 이미지를 변환할 수 있지만, 기술적인 이유로 이미지를 추가하려면 PDF에 추가할 파일 유형을 지정해야 합니다.

다음 코드 스니펫은 Aspose.PDF 를 사용하여 DICOM 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.DICOM 이미지를 로드하고 이미지를 PDF 파일의 페이지에 배치한 다음 출력을 PDF로 저장해야 합니다.추가 pydicom 라이브러리를 사용하여 이 이미지의 크기를 설정합니다.페이지에 이미지를 배치하려면 이 코드 스니펫을 건너뛰면 됩니다.

1. DICOM 파일을 로드합니다.
1. 이미지 크기를 추출합니다.
1. 이미지 크기를 인쇄합니다.
1. 새 PDF 문서 만들기
1. PDF용 DICOM 이미지를 준비합니다.
1. PDF 페이지 크기 및 여백을 설정합니다.
1. 페이지에 이미지를 추가합니다.
1. PDF를 저장합니다.
1. 변환 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 DICOM을 PDF로 변환해 보세요**

Aspose는 온라인 신청서를 제공합니다 [“DICOM에서 PDF로”](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 DICOM을 PDF로 변환](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF를 PDF로 변환

<abbr title="Enhanced metafile format">EMF</abbr> 그래픽 이미지를 장치 독립적으로 저장합니다.EMF의 메타파일은 모든 출력 장치에서 파싱한 후 저장된 이미지를 렌더링할 수 있는 시간순으로 가변 길이 레코드로 구성됩니다.

다음 코드 스니펫은 Python을 사용하여 EMF를 PDF로 변환하는 방법을 보여줍니다.

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**EMF를 온라인으로 PDF로 변환해 보세요**

Aspose는 온라인 신청서를 제공합니다 [“EMF를 PDF로”](https://products.aspose.app/pdf/conversion/emf-to-pdf/)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 EMF를 PDF로 변환](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## GIF를 PDF로 변환

.NET** 라이브러리를 통해 파이썬용**Aspose.pdf를 사용하여 GIF 파일을 PDF 문서로 변환합니다.

<abbr title="Graphics Interchange Format">GIF</abbr> 256색 이하의 형식으로 품질 손실 없이 압축된 데이터를 저장할 수 있습니다.하드웨어 독립적인 GIF 형식은 네트워크를 통해 비트맵 이미지를 전송하기 위해 CompuServe에서 1987년 (GIF87a) 에 의해 개발되었습니다.

따라서 다음 코드 스니펫은 이러한 단계를 따르며 Python을 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다.

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 GIF를 PDF로 변환해 보세요**

Aspose는 온라인 신청서를 제공합니다 [“GIF를 PDF로”](https://products.aspose.app/pdf/conversion/gif-to-pdf/)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 GIF를 PDF로 변환](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## PNG를 PDF로 변환

**.NET을 통한 파이썬용.pdf**는 PNG 이미지를 PDF 형식으로 변환하는 기능을 지원합니다.다음 코드 스니펫을 확인하여 작업을 완료하세요.

<abbr title="Portable Network Graphics">PNG</abbr> 무손실 압축을 사용하는 래스터 이미지 파일 형식의 일종으로, 사용자에게 널리 사용됩니다.

아래 단계를 사용하여 PNG를 PDF 이미지로 변환할 수 있습니다.

1. 새 PDF 문서 만들기
1. 이미지 배치를 정의합니다.
1. PDF를 저장합니다.
1. 변환 메시지를 인쇄합니다.

또한 아래 코드 스니펫은 Python을 사용하여 PNG를 PDF로 변환하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 PNG를 PDF로 변환해 보세요**

Aspose는 온라인 신청서를 제공합니다 [“PNG를 PDF로”](https://products.aspose.app/pdf/conversion/png-to-pdf/)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PNG를 PDF로 변환](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVG를 PDF로 변환

**.NET을 통한 파이썬용 Aspose.pdf**는 SVG 이미지를 PDF 형식으로 변환하는 방법과 소스 SVG 파일의 크기를 가져오는 방법을 설명합니다.

확장 가능한 벡터 그래픽 (SVG) 은 정적 및 동적 (대화형 또는 애니메이션) 2차원 벡터 그래픽에 대한 XML 기반 파일 형식의 사양 모음입니다.SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄 (W3C) 에서 개발 중인 공개 표준입니다.

<abbr title="Scalable Vector Graphics">SVG</abbr> 이미지와 해당 동작은 XML 텍스트 파일에 정의되어 있습니다.즉, 이미지를 검색하고, 인덱싱하고, 스크립팅하고, 필요한 경우 압축할 수 있습니다.XML 파일인 경우 모든 텍스트 편집기로 SVG 이미지를 만들고 편집할 수 있지만 Inkscape와 같은 드로잉 프로그램을 사용하여 만드는 것이 더 편리한 경우가 많습니다.

{{% alert color="success" %}}
**SVG 형식을 온라인으로 PDF로 변환해 보세요**

.NET을 통한 파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“SVG를 PDF로”](https://products.aspose.app/pdf/conversion/svg-to-pdf)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 SVG를 PDF로 변환](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

다음 코드 스니펫은 파이썬용 Aspose.PDF 를 사용하여 SVG 파일을 PDF 형식으로 변환하는 프로세스를 보여줍니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## TIFF를 PDF로 변환

**aspose.pdf** 파일 형식이 지원됩니다 (단일 프레임 또는 다중 프레임 TIFF 이미지).즉, TIFF 이미지를 PDF로 변환할 수 있습니다.

TIFF 또는 TIF (태그가 지정된 이미지 파일 형식) 는 이 파일 형식 표준을 준수하는 다양한 장치에서 사용하기 위한 래스터 이미지를 나타냅니다.TIFF 이미지에는 이미지가 서로 다른 여러 프레임이 포함될 수 있습니다.Aspose.PDF 파일 형식 (단일 프레임 또는 다중 프레임 TIFF 이미지) 도 지원됩니다.

나머지 래스터 파일 형식 그래픽과 같은 방식으로 TIFF를 PDF로 변환할 수 있습니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## CDR을 PDF로 변환

다음 코드 스니펫은 파이썬용 Aspose.PDF 파일의 'CDRLoadOptions'를 사용하여 코렐드로우 (CDR) 파일을 로드하고.NET을 통해 PDF로 저장하는 방법을 보여줍니다.

1. 'CDRLoadOptions () '를 생성하여 CDR 파일을 로드하는 방법을 구성하십시오.
1. CDR 파일 및 로드 옵션을 사용하여 문서 객체를 초기화합니다.
1. 문서를 PDF로 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## JPEG를 PDF로 변환

이 예제에서는 파이썬용 Aspose.PDF 파일을.NET을 통해 JPEG를 PDF 파일로 변환하는 방법을 보여줍니다.

1. 새 PDF 문서 만들기
1. 새 페이지를 추가합니다.
1. 배치 사각형을 정의합니다 (A4 크기: 595x842포인트).
1. 페이지에 이미지를 삽입합니다.
1. PDF를 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
