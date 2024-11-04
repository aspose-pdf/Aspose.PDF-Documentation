---
title: 파이썬에서 PDF를 다양한 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /python-net/convert-pdf-to-images-format/
lastmod: "2022-12-23"
description: 이 주제는 Aspose.PDF for Python을 사용하여 PDF를 TIFF, BMP, EMF, JPEG, PNG, GIF, SVG와 같은 다양한 이미지 형식으로 몇 줄의 코드로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 개요

이 문서에서는 파이썬을 사용하여 PDF를 다양한 이미지 형식으로 변환하는 방법을 설명합니다. 다음 주제를 다룹니다.

_이미지 형식_: **TIFF**
- [파이썬 PDF를 TIFF로](#python-pdf-to-tiff)
- [파이썬 PDF를 TIFF로 변환](#python-pdf-to-tiff)
- [파이썬에서 PDF의 단일 또는 특정 페이지를 TIFF로 변환](#python-pdf-to-tiff-pages)

_이미지 형식_: **BMP**
- [파이썬 PDF를 BMP로](#python-pdf-to-bmp)
- [파이썬 PDF를 BMP로 변환](#python-pdf-to-bmp)
- [파이썬 PDF를 BMP 변환기](#python-pdf-to-bmp)

_이미지 형식_: **EMF**
- [파이썬 PDF를 EMF로](#python-pdf-to-emf)
- [파이썬 PDF를 EMF로 변환](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_이미지 형식_: **JPG**
- [Python PDF to JPG](#python-pdf-to-jpg)
- [Python Convert PDF to JPG](#python-pdf-to-jpg)
- [Python PDF to JPG Converter](#python-pdf-to-jpg)

_이미지 형식_: **PNG**
- [Python PDF to PNG](#python-pdf-to-png)
- [Python Convert PDF to PNG](#python-pdf-to-png)
- [Python PDF to PNG Converter](#python-pdf-to-png)

_이미지 형식_: **GIF**
- [Python PDF to GIF](#python-pdf-to-gif)
- [Python Convert PDF to GIF](#python-pdf-to-gif)
- [Python PDF to GIF Converter](#python-pdf-to-gif)

_이미지 형식_: **SVG**
- [Python PDF to SVG](#python-pdf-to-svg)
- [Python Convert PDF to SVG](#python-pdf-to-svg)
- [Python PDF to SVG Converter](#python-pdf-to-svg)

## Python Convert PDF to Image

**Aspose.PDF for Python**은(는) 여러 가지 접근 방식을 사용하여 PDF를 이미지로 변환합니다.
 일반적으로 두 가지 접근 방식을 사용합니다: Device 접근 방식을 사용하는 변환과 SaveOption을 사용하는 변환입니다. 이 섹션에서는 이러한 접근 방식 중 하나를 사용하여 PDF 문서를 BMP, JPEG, GIF, PNG, EMF, TIFF 및 SVG 형식의 이미지로 변환하는 방법을 보여줍니다.

라이브러리에는 가상 장치를 사용하여 이미지를 변환할 수 있게 하는 여러 클래스가 있습니다. DocumentDevice는 전체 문서 변환에 적합하며, ImageDevice는 특정 페이지에 적합합니다.

## DocumentDevice 클래스를 사용하여 PDF 변환

**Aspose.PDF for Python**은 PDF 페이지를 TIFF 이미지로 변환할 수 있게 합니다.

[TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (DocumentDevice 기반) 클래스는 PDF 페이지를 TIFF 이미지로 변환할 수 있게 합니다. 이 클래스는 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환할 수 있는 [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods)라는 메서드를 제공합니다.

{{% alert color="success" %}}

**PDF를 TIFF로 온라인 변환 시도**
Aspose.PDF for Python via .NET은 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)라는 온라인 무료 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDF 페이지를 하나의 TIFF 이미지로 변환

Aspose.PDF for Python은 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환하는 방법을 설명합니다:

<a name="csharp-pdf-to-tiff"><strong>단계: Python에서 PDF를 TIFF로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 객체를 생성합니다.
2. [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) 및 [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) 객체를 생성합니다.

3. PDF 문서를 TIFF로 변환하기 위해 [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) 메서드를 호출합니다.
4. 출력 파일의 속성을 설정하려면 [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) 클래스를 사용합니다.

다음 코드 스니펫은 모든 PDF 페이지를 단일 TIFF 이미지로 변환하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tiff.tiff"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # 해상도 객체 생성
    resolution = ap.devices.Resolution(300)

    # TiffSettings 객체 생성
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    # TIFF 장치 생성
    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)

    # 특정 페이지를 변환하고 이미지를 스트림에 저장
    tiffDevice.process(document, output_pdf)
```


## ImageDevice 클래스 사용하여 PDF 변환

`ImageDevice`는 `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` 및 `EmfDevice`의 조상입니다.

- [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 클래스는 PDF 페이지를 <abbr title="Bitmap Image File">BMP</abbr> 이미지로 변환할 수 있습니다.
- [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) 클래스는 PDF 페이지를 <abbr title="Enhanced Meta File">EMF</abbr> 이미지로 변환할 수 있습니다.
- [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) 클래스는 PDF 페이지를 JPEG 이미지로 변환할 수 있습니다.
- [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) 클래스는 PDF 페이지를 <abbr title="Portable Network Graphics">PNG</abbr> 이미지로 변환할 수 있습니다.

- [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) 클래스는 PDF 페이지를 <abbr title="Graphics Interchange Format">GIF</abbr> 이미지로 변환할 수 있습니다.

문서의 PDF 페이지를 이미지로 변환하는 방법을 살펴보겠습니다.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 클래스는 PDF 파일의 특정 페이지를 BMP 이미지 형식으로 변환할 수 있는 [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods)라는 메소드를 제공합니다. 다른 클래스도 동일한 메소드를 가지고 있습니다. 따라서 PDF 페이지를 이미지로 변환해야 할 경우, 필요한 클래스를 인스턴스화하면 됩니다.

다음 단계 및 Python 코드 스니펫은 이러한 가능성을 보여줍니다.

 - [Python에서 PDF를 BMP로 변환](#python-pdf-to-image)
 - [Python에서 PDF를 EMF로 변환](#python-pdf-to-image)
 - [Python에서 PDF를 JPG로 변환](#python-pdf-to-image)
 - [Python에서 PDF를 PNG로 변환](#python-pdf-to-image)
 - [Python에서 PDF를 GIF로 변환](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>단계: Python에서 PDF를 이미지(BMP, EMF, JPG, PNG, GIF)로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 로드합니다.
2. [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/)의 서브클래스의 인스턴스를 생성합니다. 즉,
   * [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (PDF를 BMP로 변환하기 위해)
   * [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (PDF를 Emf로 변환하기 위해)
   * [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (PDF를 JPG로 변환하기 위해)
   * [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (PDF를 PNG로 변환하기 위해)
   * [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (PDF를 GIF로 변환하기 위해)
3. PDF를 이미지로 변환하기 위해 [ImageDevice.Process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) 메서드를 호출합니다.

### PDF를 BMP로 변환하기

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_bmp"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # 해상도 객체 생성
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)

    for i in range(0, len(document.pages)):
        # 저장할 파일 생성
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.bmp", 'x'
        )
        # 특정 페이지를 변환하고 이미지를 스트림에 저장
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```


### PDF를 EMF로 변환

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_emf"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # 해상도 객체 생성
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)

    for i in range(0, len(document.pages)):
        # 저장할 파일 생성
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.emf", 'x'
        )
        # 특정 페이지를 변환하고 이미지를 스트림에 저장
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```  

### PDF를 JPEG로 변환

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_jpeg"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # 해상도 객체 생성
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)

    for i in range(0, len(document.pages)):
        # 저장할 파일 생성
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.jpeg", "x"
        )
        # 특정 페이지를 변환하고 이미지를 스트림에 저장
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()  
``` 


### PDF를 PNG로 변환

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_png"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # 해상도 객체 생성
    resolution = ap.devices.Resolution(300)
    device = ap.devices.PngDevice(resolution)

    for i in range(0, len(document.pages)):
        # 저장할 파일 생성
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.png", 'x'
        )
        # 특정 페이지를 변환하여 이미지를 스트림에 저장
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```

### PDF를 GIF로 변환

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_gif"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # 해상도 객체 생성
    resolution = ap.devices.Resolution(300)

    device = ap.devices.GifDevice(resolution)

    for i in range(0, len(document.pages)):
        # 저장할 파일 생성
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.gif", 'x'
        )
        # 특정 페이지를 변환하여 이미지를 스트림에 저장
        device.process(document.pages[i + 1], imageStream)
        # 스트림 닫기
        imageStream.close()  
```


{{% alert color="success" %}}
**PDF를 PNG로 온라인에서 변환해보세요**

우리의 무료 응용 프로그램이 어떻게 작동하는지 예로 다음 기능을 확인하십시오.

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)를 제공하며, 여기에서 기능과 작동 품질을 조사해볼 수 있습니다.

[![PDF를 PNG로 변환하는 방법을 무료 앱으로 사용하기](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptions 클래스를 사용하여 PDF 변환

이 기사 부분에서는 Python과 SaveOptions 클래스를 사용하여 PDF를 <abbr title="Scalable Vector Graphics">SVG</abbr>로 변환하는 방법을 보여줍니다.

{{% alert color="success" %}}
**PDF를 SVG로 온라인에서 변환해보세요**

Aspose.PDF for Python via .NET은 온라인 무료 애플리케이션 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)를 제공하며, 여기에서 기능과 작동 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 SVG로 변환](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)**는 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양으로, 정적 및 동적(대화형 또는 애니메이션) 그래픽을 포함하는 사양군입니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에 의해 개발되고 있는 개방형 표준입니다.

SVG 이미지와 그 동작은 XML 텍스트 파일에서 정의됩니다. 이는 검색, 인덱싱, 스크립팅이 가능하며 필요에 따라 압축될 수도 있음을 의미합니다. XML 파일로서 SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, 일반적으로 Inkscape와 같은 드로잉 프로그램으로 생성하는 것이 더 편리합니다.

Aspose.PDF for Python은 SVG 이미지를 PDF 형식으로 변환하는 기능을 지원하며, PDF 파일을 SVG 형식으로 변환하는 기능도 제공합니다.
 이 요구 사항을 충족하기 위해 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 클래스가 Aspose.PDF 네임스페이스에 도입되었습니다. SvgSaveOptions 객체를 인스턴스화하고 [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드의 두 번째 인수로 전달합니다.

다음 코드 스니펫은 Python으로 PDF 파일을 SVG 형식으로 변환하는 단계를 보여줍니다.

<a name="csharp-pdf-to-svg"><strong>단계: Python에서 PDF를 SVG로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 객체를 생성합니다.
2. 필요한 설정으로 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 객체를 생성합니다.
3. [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 객체를 전달하여 PDF 문서를 SVG로 변환합니다.

### PDF를 SVG로 변환

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_svg.svg"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    # SvgSaveOptions 객체 인스턴스화
    saveOptions = ap.SvgSaveOptions()

    # SVG 이미지를 Zip 아카이브로 압축하지 않음
    saveOptions.compress_output_to_zip_archive = False
    saveOptions.treat_target_file_name_as_directory = True

    # 출력 결과를 SVG 파일로 저장
    document.save(output_pdf, saveOptions)
```