---
title: PDF를 다양한 이미지 형식으로 변환하기
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: 이 주제는 Aspose.PDF for Python을 사용하여 PDF를 TIFF, BMP, EMF, JPEG, PNG, GIF, SVG와 같은 다양한 이미지 형식으로 몇 줄의 코드로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 개요

이 문서는 파이썬을 사용하여 PDF를 다양한 이미지 형식으로 변환하는 방법을 설명합니다. 다음 주제를 다룹니다.

_이미지 형식_: **TIFF**
- [파이썬 PDF를 TIFF로 변환](#python-pdf-to-tiff)
- [파이썬 PDF를 TIFF로 변환](#python-pdf-to-tiff)
- [파이썬 PDF의 단일 또는 특정 페이지를 TIFF로 변환](#python-pdf-to-tiff-pages)


_이미지 형식_: **BMP**
- [파이썬 PDF를 BMP로 변환](#python-pdf-to-bmp)
- [파이썬 PDF를 BMP로 변환](#python-pdf-to-bmp)
- [파이썬 PDF를 BMP로 변환기](#python-pdf-to-bmp)

_이미지 형식_: **EMF**
- [파이썬 PDF를 EMF로 변환](#python-pdf-to-emf)

- [파이썬 PDF를 EMF로 변환](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_이미지 형식_: **JPG**
- [Python PDF를 JPG로](#python-pdf-to-jpg)
- [Python PDF를 JPG로 변환](#python-pdf-to-jpg)
- [Python PDF를 JPG 변환기](#python-pdf-to-jpg)

_이미지 형식_: **PNG**
- [Python PDF를 PNG로](#python-pdf-to-png)
- [Python PDF를 PNG로 변환](#python-pdf-to-png)
- [Python PDF를 PNG 변환기](#python-pdf-to-png)

_이미지 형식_: **GIF**
- [Python PDF를 GIF로](#python-pdf-to-gif)
- [Python PDF를 GIF로 변환](#python-pdf-to-gif)
- [Python PDF를 GIF 변환기](#python-pdf-to-gif)

_이미지 형식_: **SVG**
- [Python PDF를 SVG로](#python-pdf-to-svg)
- [Python PDF를 SVG로 변환](#python-pdf-to-svg)
- [Python PDF를 SVG 변환기](#python-pdf-to-svg)

## Python PDF를 이미지로 변환

**Aspose.PDF for Python**은 PDF를 이미지로 변환하기 위해 여러 가지 접근 방식을 사용합니다.
 일반적으로 우리는 두 가지 접근 방식을 사용합니다: Device 접근 방식을 사용한 변환과 SaveOption을 사용한 변환. 이 섹션에서는 이러한 접근 방식 중 하나를 사용하여 PDF 문서를 BMP, JPEG, GIF, PNG, EMF, TIFF 및 SVG 형식의 이미지로 변환하는 방법을 보여줍니다.

라이브러리에는 이미지를 변환하기 위해 가상 디바이스를 사용할 수 있는 여러 클래스가 있습니다. DocumentDevice는 전체 문서 변환을 지향하지만, ImageDevice는 특정 페이지를 위한 것입니다.

## DocumentDevice 클래스를 사용하여 PDF 변환

**Aspose.PDF for Python**은 PDF 페이지를 TIFF 이미지로 변환할 수 있게 합니다.

[TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) (DocumentDevice 기반) 클래스는 PDF 페이지를 TIFF 이미지로 변환할 수 있게 합니다. 이 클래스는 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환할 수 있는 [`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods)라는 메소드를 제공합니다.

{{% alert color="success" %}}

**PDF를 TIFF로 온라인에서 변환해보세요**
Aspose.PDF for Python via .NET은 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDF 페이지를 하나의 TIFF 이미지로 변환

Aspose.PDF for Python은 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환하는 방법을 설명합니다:

<a name="csharp-pdf-to-tiff"><strong>단계: Python에서 PDF를 TIFF로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 클래스의 객체를 생성합니다.
2. [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) 및 [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) 객체를 생성합니다.

3. PDF 문서를 TIFF로 변환하려면 [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) 메서드를 호출하십시오.
4. 출력 파일의 속성을 설정하려면 [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) 클래스를 사용하십시오.

다음 코드 스니펫은 모든 PDF 페이지를 단일 TIFF 이미지로 변환하는 방법을 보여줍니다.

```python
from asposepdf import Api, Device

# 라이선스 초기화
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# PDF 문서 열기
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# PDF 문서 열기
document = Api.Document(input_pdf)
# Resolution 객체 생성
resolution = Device.Resolution(300)

# TiffSettings 객체 생성
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# TIFF 장치 생성
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# 특정 페이지를 변환하고 이미지를 스트림에 저장
tiffDevice.process(document, output_image)
```


## ImageDevice 클래스를 사용하여 PDF 변환

`ImageDevice`는 `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` 및 `EmfDevice`의 상위 클래스입니다.

- [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) 클래스는 PDF 페이지를 <abbr title="Bitmap Image File">BMP</abbr> 이미지로 변환할 수 있습니다.
- [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) 클래스는 PDF 페이지를 <abbr title="Enhanced Meta File">EMF</abbr> 이미지로 변환할 수 있습니다.
- [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) 클래스는 PDF 페이지를 JPEG 이미지로 변환할 수 있습니다.
- [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) 클래스는 PDF 페이지를 <abbr title="Portable Network Graphics">PNG</abbr> 이미지로 변환할 수 있습니다.

- [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) 클래스는 PDF 페이지를 <abbr title="Graphics Interchange Format">GIF</abbr> 이미지로 변환할 수 있습니다.

PDF 페이지를 이미지로 변환하는 방법을 살펴보겠습니다.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 클래스는 [Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods)라는 메서드를 제공하여 PDF 파일의 특정 페이지를 BMP 이미지 형식으로 변환할 수 있습니다. 다른 클래스들도 동일한 메서드를 가지고 있습니다. 따라서 PDF 페이지를 이미지로 변환해야 하는 경우 필요한 클래스를 인스턴스화하면 됩니다.

다음의 단계와 Python 코드 스니펫은 이러한 가능성을 보여줍니다.

- [Python에서 PDF를 BMP로 변환](#python-pdf-to-image)
- [Python에서 PDF를 EMF로 변환](#python-pdf-to-image)
- [Python에서 PDF를 JPG로 변환](#python-pdf-to-image)
- [Python에서 PDF를 PNG로 변환](#python-pdf-to-image)
- [Python에서 PDF를 GIF로 변환](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>단계: Python에서 PDF를 이미지(BMP, EMF, JPG, PNG, GIF)로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 로드합니다.
2. [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/)의 서브클래스의 인스턴스를 생성합니다. 예를 들어:
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) (PDF를 BMP로 변환)
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) (PDF를 Emf로 변환)
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) (PDF를 JPG로 변환)
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) (PDF를 PNG로 변환)
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) (PDF를 GIF로 변환)
3. PDF를 이미지로 변환하기 위해 [ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods) 메서드를 호출합니다.

### PDF를 BMP로 변환

```python


from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDF 문서를 엽니다
document = Api.Document(input_pdf)

# 해상도 객체를 생성합니다
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # 저장할 파일 이름을 생성합니다
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # 특정 페이지를 변환하고 이미지를 파일로 저장합니다
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### PDF를 EMF로 변환

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDF 문서 열기
document = Api.Document(input_pdf)

# 해상도 객체 생성
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # 저장할 파일 이름 생성
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # 특정 페이지를 변환하고 이미지를 파일로 저장
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### PDF를 JPEG로 변환

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDF 문서 열기
document = Api.Document(input_pdf)

# 해상도 객체 생성
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # 저장할 파일 이름 생성
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # 특정 페이지를 변환하고 이미지를 파일로 저장
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


### PDF를 PNG로 변환

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDF 문서 열기
document = Api.Document(input_pdf)

# 해상도 객체 생성
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # 저장할 파일 이름 생성
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # 특정 페이지를 변환하고 이미지를 파일로 저장
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 

### PDF를 GIF로 변환

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# PDF 문서 열기
document = Api.Document(input_pdf)

# 해상도 객체 생성
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # 저장할 파일 이름 생성
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # 특정 페이지를 변환하고 이미지를 파일로 저장
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


{{% alert color="success" %}}
**PDF를 PNG로 온라인에서 변환 시도하기**

우리의 무료 애플리케이션이 어떻게 작동하는지 예를 들어, 다음 기능을 확인해 보세요.

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)을 제공합니다. 여기서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![PDF를 PNG로 변환하는 방법 무료 앱 사용](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptions 클래스를 사용하여 PDF 변환

이 문서의 이 부분에서는 Python과 SaveOptions 클래스를 사용하여 PDF를 <abbr title="Scalable Vector Graphics">SVG</abbr>로 변환하는 방법을 보여줍니다.

{{% alert color="success" %}}
**PDF를 SVG로 온라인에서 변환 시도하기**

Aspose.PDF for Python via .NET은 온라인 무료 애플리케이션 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)을 제공합니다. 여기서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 SVG로 무료 앱 사용](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)**는 정적 및 동적(인터랙티브 또는 애니메이션) 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양 집합입니다. SVG 사양은 1999년부터 World Wide Web Consortium (W3C)에 의해 개발된 개방형 표준입니다.

SVG 이미지와 그 동작은 XML 텍스트 파일로 정의됩니다. 이는 검색, 색인화, 스크립팅이 가능하며 필요한 경우 압축할 수 있음을 의미합니다. XML 파일로서, SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, Inkscape와 같은 드로잉 프로그램을 사용하여 생성하는 것이 더 편리합니다.

Aspose.PDF for Python은 SVG 이미지를 PDF 형식으로 변환하는 기능을 지원하며, PDF 파일을 SVG 형식으로 변환하는 기능도 제공합니다.
 이 요구 사항을 충족하기 위해 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 클래스가 Aspose.PDF 네임스페이스에 도입되었습니다. SvgSaveOptions 객체를 인스턴스화하고 이를 [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 전달합니다.

다음 코드 스니펫은 Python으로 PDF 파일을 SVG 형식으로 변환하는 단계를 보여줍니다.

<a name="csharp-pdf-to-svg"><strong>단계: Python에서 PDF를 SVG로 변환하기</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 클래스의 객체를 생성합니다.
2. 필요한 설정으로 [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) 객체를 생성합니다.
3. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 메서드를 호출하고 [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) 객체를 전달하여 PDF 문서를 SVG로 변환합니다.

### PDF를 SVG로 변환

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```