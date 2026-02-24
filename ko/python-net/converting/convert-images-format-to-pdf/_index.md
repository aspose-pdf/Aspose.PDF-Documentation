---
title: Python에서 다양한 이미지 형식을 PDF로 변환
linktitle: 이미지를 PDF로 변환
type: docs
weight: 60
url: /ko/python-net/convert-images-format-to-pdf/
lastmod: "2025-09-01"
description: BMP, CGM, DICOM, PNG, TIFF, EMF 및 SVG와 같은 다양한 이미지 형식을 Python을 사용하여 PDF로 변환합니다.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python에서 이미지를 PDF로 변환하는 방법
Abstract: 이 문서는 Python을 사용하여 다양한 이미지 형식을 PDF로 변환하는 포괄적인 가이드를 제공하며, 특히 .NET을 통해 Python용 Aspose.PDF 라이브러리를 활용합니다. 이 문서는 BMP, CGM, DICOM, EMF, GIF, PNG, SVG, TIFF 등 다양한 이미지 형식을 다룹니다. 각 섹션에서는 변환에 필요한 단계를 자세히 설명하고, 과정을 보여주는 코드 스니펫을 제공합니다. 예를 들어 BMP를 PDF로 변환하려면 새 PDF 문서를 생성하고, 이미지 배치를 정의한 뒤 이미지를 삽입하고 문서를 저장합니다. 마찬가지로 CGM, DICOM 등 다른 형식에 대해서는 특정 로드 옵션과 처리 절차가 제시됩니다. 또한 이 문서는 서로 다른 인코딩 방법을 지원하고 단일 프레임 및 다중 프레임 이미지를 모두 처리할 수 있는 Aspose.PDF의 장점을 강조합니다.
---

## Python 이미지를 PDF로 변환

**Aspose.PDF for Python via .NET** 는 다양한 이미지 형식을 PDF 파일로 변환할 수 있도록 합니다. 우리 라이브러리는 BMP, CGM, DICOM, EMF, JPG, PNG, SVG 및 TIFF 형식과 같은 가장 인기 있는 이미지 형식을 변환하는 코드 스니펫을 보여줍니다.

## BMP를 PDF로 변환

BMP 파일을 **Aspose.PDF for Python via .NET** 라이브러리를 사용하여 PDF 문서로 변환합니다.

<abbr title="Bitmap Image File">BMP</abbr> 이미지들은 확장자를 가진 파일입니다. BMP는 비트맵 디지털 이미지를 저장하는 데 사용되는 비트맵 이미지 파일을 나타냅니다. 이러한 이미지는 그래픽 어댑터와 무관하며 디바이스 독립 비트맵(DIB) 파일 형식이라고도 합니다.

Aspose.PDF for Python via .NET API를 사용하여 BMP를 PDF 파일로 변환할 수 있습니다. 따라서 BMP 이미지를 변환하려면 다음 단계에 따라 진행하십시오:

Python에서 BMP를 PDF로 변환하는 단계:

1. 빈 PDF 문서를 생성합니다.
1. 필요한 페이지를 생성합니다. 예를 들어 A4를 생성했지만 원하는 형식을 지정할 수 있습니다.
1. 정의된 사각형을 사용하여 페이지 안에 이미지(infile)를 배치합니다.
1. 문서를 PDF로 저장합니다.

따라서 다음 코드 스니펫은 이러한 단계를 따르며 Python을 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**BMP를 PDF로 온라인 변환해 보세요**

Aspose는 온라인 무료 애플리케이션 ["BMP를 PDF로"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)을 제공하며, 여기서 기능과 품질을 확인해 볼 수 있습니다.

[![무료 앱을 사용한 Aspose.PDF BMP to PDF 변환](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGM을 PDF로 변환

Aspose.PDF for Python via .NET을 사용하여 CGM(Computer Graphics Metafile)을 PDF(또는 다른 지원 형식)로 변환합니다.

<abbr title="Computer Graphics Metafile">CGM</abbr>는 CAD(컴퓨터 지원 설계) 및 프레젠테이션 그래픽 응용 프로그램에서 일반적으로 사용되는 컴퓨터 그래픽 메타파일 형식의 파일 확장자입니다. CGM은 세 가지 인코딩 방법을 지원하는 벡터 그래픽 형식으로, 바이너리(프로그램 읽기 속도에 가장 좋음), 문자 기반(가장 작은 파일 크기를 생성하고 데이터 전송을 빠르게 함), 혹은 클리어텍스트 인코딩(텍스트 편집기로 파일을 읽고 수정 가능) 등을 지원합니다.

다음 코드 스니펫을 확인하여 CGM 파일을 PDF 형식으로 변환하십시오.

Python에서 CGM을 PDF로 변환하는 단계:

1. 파일 경로 정의
1. CGM에 대한 로드 옵션 설정.
1. CGM을 PDF로 변환
1. 변환 메시지 출력

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = apdf.CgmLoadOptions()

    # Open PDF document
    document = apdf.Document(path_infile, options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## DICOM을 PDF로 변환

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 형식은 환자 검사의 디지털 의료 이미지와 문서를 생성, 저장, 전송 및 시각화하기 위한 의료 산업 표준입니다.

**Aspose.PDF for Python** 은 DICOM 및 SVG 이미지를 변환할 수 있지만, 기술적인 이유로 이미지를 추가하려면 PDF에 추가될 파일 유형을 지정해야 합니다.

다음 코드 스니펫은 Aspose.PDF를 사용하여 DICOM 파일을 PDF 형식으로 변환하는 방법을 보여줍니다. DICOM 이미지를 로드하고, PDF 파일의 페이지에 이미지를 배치한 뒤 출력물을 PDF로 저장해야 합니다. 우리는 이 이미지의 크기를 설정하기 위해 추가 pydicom 라이브러리를 사용합니다. 페이지에 이미지를 배치하려면 이 코드 스니펫을 건너뛸 수 있습니다.

1. 새로운 'ap.Document()'를 초기화하고 페이지를 추가합니다.
1. DICOM 이미지를 삽입합니다. apdf.Image()를 생성하고, 유형을 DICOM으로 설정한 뒤 파일 경로를 지정합니다.
1. 페이지 크기를 조정합니다. PDF 페이지 차원을 DICOM 이미지 크기에 맞추고 여백을 제거합니다.
1. 이미지를 페이지에 추가하고, 문서를 출력 파일에 저장합니다.

1. DICOM 파일을 로드합니다.
1. 이미지 차원을 추출합니다.
1. 이미지 크기를 출력합니다.
1. 새 PDF 문서를 만듭니다.
1. PDF용 DICOM 이미지를 준비합니다.
1. PDF 페이지 크기와 여백을 설정합니다.
1. 이미지를 페이지에 추가합니다.
1. PDF를 저장합니다.
1. 변환 메시지를 출력합니다.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    # Load the DICOM file
    dicom_file = pydicom.dcmread(path_infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = apdf.Document()
    page = document.pages.add()
    image = apdf.Image()
    image.file_type = apdf.ImageFileType.DICOM
    image.file = path_infile

    # Set page dimensions

    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 DICOM을 PDF로 변환해 보세요**

Aspose는 온라인 무료 애플리케이션 ["DICOM을 PDF로"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)을 제공합니다. 여기서 기능과 품질을 시험해 볼 수 있습니다.

[![Aspose.PDF 변환 DICOM을 PDF로 무료 앱 사용](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF를 PDF로 변환

<abbr title="Enhanced metafile format">EMF</abbr>는 그래픽 이미지를 장치 독립적으로 저장합니다. EMF 메타파일은 가변 길이 레코드로 구성되며, 순차적으로 기록되어 어떤 출력 장치에서도 파싱 후 이미지를 렌더링할 수 있습니다.

다음 코드 조각은 Python으로 EMF를 PDF로 변환하는 방법을 보여줍니다:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(path_infile, rectangle)

    # Save the file into PDF format
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 EMF를 PDF로 변환해 보세요**

Aspose는 온라인 무료 애플리케이션 ["EMF를 PDF로"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)을 제공합니다. 여기서 기능과 품질을 시험해 볼 수 있습니다.

[![Aspose.PDF 변환 EMF를 PDF로 무료 앱 사용](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## GIF를 PDF로 변환

**Aspose.PDF for Python via .NET** 라이브러리를 사용하여 GIF 파일을 PDF 문서로 변환합니다.

<abbr title="Graphics Interchange Format">GIF</abbr>는 256색 이하의 형식으로 품질 손실 없이 압축 데이터를 저장할 수 있습니다. 하드웨어에 독립적인 GIF 포맷은 1987년 (GIF87a) CompuServe에 의해 네트워크를 통한 비트맵 이미지 전송을 위해 개발되었습니다.

따라서 다음 코드 조각은 이러한 단계들을 따라 Python을 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 GIF를 PDF로 변환해 보세요**

Aspose는 온라인 무료 애플리케이션 ["GIF를 PDF로"](https://products.aspose.app/pdf/conversion/gif-to-pdf/)을 제공합니다. 여기서 기능과 품질을 시험해 볼 수 있습니다.

[![Aspose.PDF 변환 GIF를 PDF로 무료 앱 사용](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## PNG를 PDF로 변환

**Aspose.PDF for Python via .NET**은 PNG 이미지를 PDF 형식으로 변환하는 기능을 지원합니다. 다음 코드 조각을 확인하여 작업을 구현하십시오.

<abbr title="Portable Network Graphics">PNG</abbr>는 무손실 압축을 사용하는 래스터 이미지 파일 형식으로, 사용자들 사이에서 인기가 높습니다.

아래 단계에 따라 PNG를 PDF 이미지로 변환할 수 있습니다:

1. 새 PDF 문서를 생성합니다.
1. 이미지 배치를 정의합니다.
1. PDF를 저장합니다.
1. 변환 메시지를 출력합니다.

또한, 아래 코드 조각은 Python으로 PNG를 PDF로 변환하는 방법을 보여줍니다:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 PNG를 PDF로 변환해 보세요**

Aspose는 온라인 무료 애플리케이션 ["PNG를 PDF로"](https://products.aspose.app/pdf/conversion/png-to-pdf/)을 제공합니다. 여기서 기능과 품질을 시험해 볼 수 있습니다.

[![Aspose.PDF 변환 PNG를 PDF로 무료 앱 사용](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVG를 PDF로 변환

**Aspose.PDF for Python via .NET**은 SVG 이미지를 PDF 형식으로 변환하는 방법과 원본 SVG 파일의 치수를 얻는 방법을 설명합니다.

Scalable Vector Graphics (SVG)는 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양군으로, 정적 및 동적(대화형 또는 애니메이션) 모두를 지원합니다. SVG 사양은 1999년부터 World Wide Web Consortium (W3C)에서 개발해 온 오픈 표준입니다.

<abbr title="Scalable Vector Graphics">SVG</abbr> 이미지와 그 동작은 XML 텍스트 파일에 정의됩니다. 이는 검색, 색인, 스크립트 작성 및 필요시 압축이 가능함을 의미합니다. XML 파일이므로 SVG 이미지는 텍스트 편집기 어디서든 생성·편집할 수 있지만, Inkscape와 같은 드로잉 프로그램을 사용하는 것이 더 편리합니다.

{{% alert color="success" %}}
**온라인에서 SVG 포맷을 PDF로 변환해 보세요**

Aspose.PDF for Python via .NET은 온라인 무료 애플리케이션 ["SVG를 PDF로"](https://products.aspose.app/pdf/conversion/svg-to-pdf)를 제공합니다. 여기서 기능과 품질을 시험해 볼 수 있습니다.

[![Aspose.PDF 변환 SVG를 PDF로 무료 앱 사용](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

다음 코드 스니펫은 Aspose.PDF for Python을 사용하여 SVG 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.SvgLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## TIFF를 PDF로 변환

**Aspose.PDF** 파일 형식이 지원됩니다. 단일 프레임이든 다중 프레임 TIFF 이미지이든 관계없습니다. 즉, TIFF 이미지를 PDF로 변환할 수 있습니다.

TIFF 또는 TIF, Tagged Image File Format은 이 파일 형식 표준을 준수하는 다양한 장치에서 사용되는 래스터 이미지를 나타냅니다. TIFF 이미지는 서로 다른 여러 이미지를 포함하는 여러 프레임을 가질 수 있습니다. Aspose.PDF 파일 형식도 지원되며, 단일 프레임이든 다중 프레임 TIFF 이미지이든 관계없습니다.

다른 래스터 파일 형식 그래픽과 동일한 방식으로 TIFF를 PDF로 변환할 수 있습니다:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## CDR을 PDF로 변환

다음 코드 스니펫은 Aspose.PDF for Python via .NET에서 'CdrLoadOptions'를 사용하여 CorelDRAW(CDR) 파일을 로드하고 PDF로 저장하는 방법을 보여줍니다.

1. CDR 파일을 어떻게 로드할지 구성하기 위해 'CdrLoadOptions()'를 생성합니다.
1. CDR 파일과 로드 옵션을 사용하여 Document 객체를 초기화합니다.
1. 문서를 PDF로 저장합니다.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.CdrLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## JPEG를 PDF로 변환

이 예제는 Aspose.PDF for Python via .NET을 사용하여 JPEG를 PDF 파일로 변환하는 방법을 보여줍니다.

1. 새 PDF 문서를 생성합니다.
1. 새 페이지를 추가합니다.
1. 배치 사각형을 정의합니다 (A4 크기: 595x842 포인트).
1. 이미지를 페이지에 삽입합니다.
1. PDF를 저장합니다.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

