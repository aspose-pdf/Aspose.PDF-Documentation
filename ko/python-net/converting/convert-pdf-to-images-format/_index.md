---
title: Python에서 PDF를 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/python-net/convert-pdf-to-images-format/
lastmod: "2026-06-10"
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 파이썬에서 PDF 페이지를 TIFF, BMP, EMF, JPEG, PNG, GIF 및 SVG 파일로 렌더링하는 방법을 알아봅니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 파이썬에서 PDF 페이지를 TIFF, PNG, JPEG, GIF, BMP, EMF 및 SVG로 변환
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 파일을 일반적인 이미지 형식으로 변환하는 방법을 설명합니다.'TIFFDevice'를 사용한 문서 전체 TIFF 내보내기, 'BMPDevice', 'JPEGDevice', 'PNGDevice', 'GIFDevice', 'EMFDevice'와 같은 'ImageDevice' 서브클래스를 사용한 페이지당 래스터 이미지 생성, 'SVGSaveOptions'를 사용한 SVG로의 벡터 내보내기를 다룹니다.각 섹션에는 PDF 콘텐츠를 이미지 출력으로 저장하는 데 필요한 핵심 단계와 Python 예제가 포함되어 있습니다.
---

## 파이썬 PDF를 이미지로 변환

**.NET을 통한 파이썬용 Aspose.pdf**는 PDF 콘텐츠를 이미지로 변환하는 여러 가지 방법을 지원합니다.실제로 대부분의 워크플로는 다음 두 가지 옵션 중 하나를 사용합니다.

- PDF 페이지를 래스터 이미지 형식으로 렌더링하기 위한 장치 접근 방식
- PDF 콘텐츠를 SVG로 내보내기 위한 저장 옵션 접근 방식

이 문서에서는 PDF 파일을 TIFF, BMP, EMF, JPEG, PNG, GIF 및 SVG로 변환하는 방법을 보여줍니다.

라이브러리에는 여러 렌더링 클래스가 포함되어 있습니다. `DocumentDevice` 전체 문서 변환을 위해 설계된 반면 `ImageDevice` 개별 페이지를 대상으로 합니다.

## 문서 장치 클래스를 사용하여 PDF 변환

용도 `DocumentDevice` 전체 PDF를 하나의 다중 페이지 TIFF 파일로 렌더링하려는 경우.

더 [TIFF 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) 수업은 다음을 기반으로 합니다. `DocumentDevice` 및 제공합니다 [방법](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) PDF 파일의 모든 페이지를 하나의 TIFF 출력으로 변환하는 방법입니다.

{{% alert color="success" %}}
**온라인에서 PDF를 TIFF로 변환해 보세요**

.NET을 통한 파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 TIFF로”](https://products.aspose.app/pdf/conversion/pdf-to-tiff)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![앱을 사용하여 Aspose.PDF PDF를 TIFF로 변환](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDF 페이지를 하나의 TIFF 이미지로 변환

.NET을 통한 파이썬용 Aspose.PDF 파일은 PDF 파일의 모든 페이지를 하나의 TIFF 이미지로 렌더링할 수 있습니다.

단계: 파이썬에서 PDF를 TIFF로 변환

1. 를 사용하여 소스 PDF를 로드합니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.
1. 작성 [TIFF 설정](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) 과 [TIFF 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) 사물.
1. 압축, 색 농도, 빈 페이지 처리와 같은 TIFF 옵션을 구성합니다.
1. 전화해 [방법](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) TIFF 파일을 작성하는 메서드입니다.

다음 코드 스니펫은 모든 PDF 페이지를 단일 TIFF 이미지로 변환하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_TIFF(infile, outfile):
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)
```

## 이미지 디바이스 클래스를 사용하여 PDF 변환

용도 `ImageDevice` 래스터 이미지 형식의 페이지별 출력이 필요한 경우

`ImageDevice` 의 기본 클래스입니다. `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, 및 `EmfDevice`.

- 더 [BMP 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 클래스를 사용하면 PDF 페이지를 BMP 이미지로 변환할 수 있습니다.
- 더 [EMF 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) 클래스를 사용하면 PDF 페이지를 EMF 이미지로 변환할 수 있습니다.
- 더 [JPEG 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) 클래스를 사용하면 PDF 페이지를 JPEG 이미지로 변환할 수 있습니다.
- 더 [PNG 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) 클래스를 사용하면 PDF 페이지를 PNG 이미지로 변환할 수 있습니다.
- 더 [GIF 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) 클래스를 사용하면 PDF 페이지를 GIF 이미지로 변환할 수 있습니다.

워크플로는 각 형식에 대해 동일합니다. 즉, 문서를 로드하고 적절한 장치를 만든 다음 필요한 페이지를 처리합니다.

[BMP 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 노출합니다 [방법](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) 특정 페이지를 BMP로 렌더링하는 방법.다른 이미지 장치 클래스도 동일한 패턴을 따르므로 장치 클래스를 변경하여 형식을 전환할 수 있습니다.

다음 링크와 코드 샘플은 PDF 페이지를 일반적인 이미지 형식으로 렌더링하는 방법을 보여줍니다.

- [파이썬에서 PDF를 BMP로 변환](#convert-pdf-to-bmp)
- [파이썬에서 PDF를 EMF로 변환](#convert-pdf-to-emf)
- [파이썬에서 PDF를 JPEG로 변환](#convert-pdf-to-jpeg)
- [파이썬에서 PDF를 PNG로 변환](#convert-pdf-to-png)
- [파이썬에서 PDF를 GIF로 변환](#convert-pdf-to-gif)

단계: 파이썬에서 PDF를 이미지 (BMP, EMF, JPG, PNG, GIF) 로

1. 를 사용하여 PDF 파일을 로드합니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.
1. 필요한 인스턴스 생성 [이미지 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) 서브클래스:
    - [BMP 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (PDF를 BMP로 변환하려면)
    - [EMF 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (PDF를 EMF로 변환하려면)
    - [JPEG 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (PDF를 JPG로 변환하려면)
    - [PNG 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (PDF를 PNG로 변환하려면)
    - [GIF 디바이스](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (PDF를 GIF로 변환하려면)
1. 내보내려는 페이지를 반복해서 살펴보세요.
1. 전화해 [이미지 장치. 프로세스 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) 각 페이지를 이미지로 저장하는 방법

### PDF를 BMP로 변환

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_BMP(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### PDF를 EMF로 변환

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_EMF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### PDF를 JPEG로 변환

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_JPEG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### PDF를 PNG로 변환

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### PDF를 기본 글꼴로 PNG로 변환

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG_with_default_font(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### PDF를 GIF로 변환

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_GIF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 PDF를 PNG로 변환해 보세요**

애플리케이션 작동 방식의 예로 다음 기능을 확인하십시오.

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 PNG로”](https://products.aspose.app/pdf/conversion/pdf-to-png)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 저장 옵션 클래스를 사용하여 PDF 변환

용도 `SaveOptions` PDF 콘텐츠를 SVG로 내보내려는 경우

{{% alert color="success" %}}
**온라인에서 PDF를 SVG로 변환해 보세요**

.NET을 통한 파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 SVG로”](https://products.aspose.app/pdf/conversion/pdf-to-svg)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PDF를 SVG로 변환](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**확장 가능한 벡터 그래픽 (SVG) **은 2차원 벡터 그래픽을 위한 XML 기반 형식입니다.SVG는 벡터 기반으로 유지되므로 웹, UI 또는 디자인 워크플로에 대해 확장 가능한 출력이 필요할 때 유용합니다.

SVG 파일은 텍스트 기반이고 검색이 가능하며 다른 도구에서 쉽게 사후 처리할 수 있습니다.

.NET을 통한 파이썬용 Aspose.PDF 는 SVG를 PDF로 변환하고 PDF 페이지를 SVG로 내보낼 수 있습니다.PDF를 SVG로 변환하려면 다음을 생성하십시오. [SVG 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 객체를 생성하여 전달하십시오. [문서. 저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법.

다음 단계는 Python을 사용하여 PDF 파일을 SVG로 변환하는 방법을 보여줍니다.

단계: 파이썬에서 PDF를 SVG로 변환

1. 를 사용하여 소스 PDF를 로드합니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.
1. 만들기 [SVG 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 필요한 옵션을 선택하고 구성합니다.
1. 전화해 [문서. 저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 를 사용한 방법 `SvgSaveOptions` SVG 출력을 작성할 인스턴스입니다.

### PDF를 SVG로 변환

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_SVG(infile, outfile):
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)
```

## 관련 전환

- [이미지 형식을 PDF로 변환](/pdf/ko/python-net/convert-images-format-to-pdf/) JPG, PNG, TIFF, SVG 또는 기타 이미지 소스에서 PDF를 다시 작성해야 하는 경우
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 래스터 이미지 대신 브라우저에 맞게 출력할 수 있습니다.
- [PDF를 다른 형식으로 변환](/pdf/ko/python-net/convert-pdf-to-other-files/) EPUB, 마크다운, 텍스트 및 XPS 내보내기 워크플로우에 적합합니다.
