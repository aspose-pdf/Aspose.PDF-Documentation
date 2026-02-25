---
title: PDF를 Python에서 다양한 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/python-net/convert-pdf-to-images-format/
lastmod: "2025-09-27"
description: Aspose.PDF를 사용하여 .NET을 통해 Python에서 PDF 페이지를 PNG, JPEG, TIFF와 같은 이미지로 변환하는 방법을 살펴보세요.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python에서 PDF를 이미지 형식으로 변환하는 방법
Abstract: 이 문서는 Python을 사용하여 PDF 파일을 다양한 이미지 형식으로 변환하는 포괄적인 가이드를 제공하며, 특히 Aspose.PDF for Python 라이브러리를 활용합니다. 문서에는 TIFF, BMP, EMF, JPG, PNG, GIF, SVG 등 이미지 형식으로 PDF를 변환하는 방법이 설명되어 있습니다. 두 가지 주요 변환 접근법—Device 접근법과 SaveOption—이 논의됩니다. Device 접근법은 `DocumentDevice` 및 `ImageDevice`와 같은 클래스를 사용하여 전체 문서 또는 특정 페이지를 변환합니다. PDF 페이지를 TIFF(`TiffDevice`) 및 BMP, EMF, JPEG, PNG, GIF와 같은 형식으로 변환하기 위한 상세 단계와 Python 코드 예제가 제공됩니다(`BmpDevice`, `EmfDevice`, `JpegDevice`, `PngDevice`, `GifDevice`). SVG 변환을 위해 `SvgSaveOptions` 클래스가 소개됩니다. 또한 이러한 변환을 체험할 수 있는 온라인 도구도 강조합니다.
---

## Python에서 PDF를 이미지로 변환

**Aspose.PDF for Python**은 PDF를 이미지로 변환하기 위해 여러 접근법을 사용합니다. 일반적으로 우리는 두 가지 접근법, 즉 Device 접근법과 SaveOption 접근법을 사용합니다. 이 섹션에서는 이러한 접근법 중 하나를 사용하여 PDF 문서를 BMP, JPEG, GIF, PNG, EMF, TIFF, SVG와 같은 이미지 형식으로 변환하는 방법을 보여줍니다.

라이브러리에는 가상 디바이스를 사용하여 이미지를 변환할 수 있는 여러 클래스가 있습니다. DocumentDevice는 전체 문서 변환에, ImageDevice는 특정 페이지 변환에 사용됩니다.

## DocumentDevice 클래스를 사용하여 PDF 변환

**Aspose.PDF for Python**은 PDF 페이지를 TIFF 이미지로 변환할 수 있게 합니다.

[TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (DocumentDevice 기반) 클래스는 PDF 페이지를 TIFF 이미지로 변환할 수 있게 해줍니다. 이 클래스는 [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods)라는 메서드를 제공하며, PDF 파일의 모든 페이지를 하나의 TIFF 이미지로 변환할 수 있습니다.

{{% alert color="success" %}}
**온라인에서 PDF를 TIFF로 변환해 보세요**

Aspose.PDF for Python via .NET은 온라인 무료 애플리케이션 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)을 제공하며, 여기서 기능과 품질을 시험해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF to TIFF 무료 앱](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDF 페이지를 하나의 TIFF 이미지로 변환

Aspose.PDF for Python은 PDF 파일의 모든 페이지를 하나의 TIFF 이미지로 변환하는 방법을 설명합니다:

단계: Python에서 PDF를 TIFF로 변환

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 객체를 생성합니다.
1. [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) 및 [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) 객체를 생성합니다.
1. PDF 문서를 TIFF로 변환하기 위해 [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) 메서드를 호출합니다.
1. 출력 파일의 속성을 설정하려면 [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) 클래스를 사용합니다.

다음 코드 조각은 모든 PDF 페이지를 하나의 TIFF 이미지로 변환하는 방법을 보여줍니다.

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    resolution = apdf.devices.Resolution(300)
    tiffSettings = apdf.devices.TiffSettings()
    tiffSettings.compression = apdf.devices.CompressionType.LZW
    tiffSettings.depth = apdf.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = apdf.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, path_outfile)

    print(infile + " converted into " + outfile)
```

## ImageDevice 클래스를 사용하여 PDF 변환

`ImageDevice`는 `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, `EmfDevice`의 상위 클래스입니다.

- [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 클래스를 사용하면 PDF 페이지를 <abbr title="Bitmap Image File">BMP</abbr> 이미지로 변환할 수 있습니다.
- [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) 클래스를 사용하면 PDF 페이지를 <abbr title="Enhanced Meta File">EMF</abbr> 이미지로 변환할 수 있습니다.
- [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) 클래스를 사용하면 PDF 페이지를 JPEG 이미지로 변환할 수 있습니다.
- [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) 클래스를 사용하면 PDF 페이지를 <abbr title="Portable Network Graphics">PNG</abbr> 이미지로 변환할 수 있습니다.
- [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) 클래스를 사용하면 PDF 페이지를 <abbr title="Graphics Interchange Format">GIF</abbr> 이미지로 변환할 수 있습니다.

PDF 페이지를 이미지로 변환하는 방법을 살펴보겠습니다.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 클래스는 PDF 파일의 특정 페이지를 BMP 이미지 형식으로 변환할 수 있는 [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) 메서드를 제공합니다. 다른 클래스들도 동일한 메서드를 가지고 있습니다. 따라서 PDF 페이지를 이미지로 변환하려면 필요한 클래스를 인스턴스화하면 됩니다.

다음 단계와 Python 코드 조각은 이 가능성을 보여줍니다:

- [Python에서 PDF를 BMP로 변환](#python-pdf-to-image)
- [Python에서 PDF를 EMF로 변환](#python-pdf-to-image)
- [Python에서 PDF를 JPG로 변환](#python-pdf-to-image)
- [Python에서 PDF를 PNG로 변환](#python-pdf-to-image)
- [Python에서 PDF를 GIF로 변환](#python-pdf-to-image)

단계: Python에서 PDF를 이미지(BMP, EMF, JPG, PNG, GIF)로 변환

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 로드합니다.
1. [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/)의 서브클래스 인스턴스를 생성합니다.
* [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (PDF를 BMP로 변환)
* [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (PDF를 EMF로 변환)
* [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (PDF를 JPG로 변환)
* [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (PDF를 PNG로 변환)
* [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (PDF를 GIF로 변환)
1. PDF를 이미지 변환하기 위해 [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) 메서드를 호출합니다.

### PDF를 BMP로 변환

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### PDF를 EMF로 변환

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### PDF를 JPEG로 변환

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```


### PDF를 PNG로 변환

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)

    device = apdf.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### 기본 글꼴을 사용하여 PDF를 PNG로 변환

```python

    from os import path
    import aspose.pdf as ap
    from io import FileIO


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### PDF를 GIF로 변환

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 PDF를 PNG로 변환해 보세요**

무료 애플리케이션이 작동하는 예시로 다음 기능을 확인해 주세요.

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)를 제공하며, 여기서 기능과 품질을 확인해 볼 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptions 클래스를 사용하여 PDF 변환

이 문서의 이 부분에서는 Python과 SaveOptions 클래스를 사용하여 PDF를 <abbr title="Scalable Vector Graphics">SVG</abbr>로 변환하는 방법을 보여줍니다.

{{% alert color="success" %}}
**온라인에서 PDF를 SVG로 변환해 보세요**

Aspose.PDF for Python via .NET은 온라인 무료 애플리케이션 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)를 제공하며, 여기서 기능과 품질을 확인해 볼 수 있습니다.

[![무료 앱을 사용한 Aspose.PDF PDF를 SVG로 변환](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** 은 정적 및 동적(대화형 또는 애니메이션) 2차원 벡터 그래픽을 위한 XML 기반 파일 형식 사양군입니다. SVG 사양은 1999년부터 World Wide Web Consortium (W3C)에서 개발 중인 오픈 표준입니다.

SVG 이미지와 그 동작은 XML 텍스트 파일에 정의됩니다. 이는 검색, 인덱싱, 스크립트 작성 및 필요에 따라 압축이 가능함을 의미합니다. XML 파일이므로 SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, Inkscape와 같은 드로잉 프로그램을 사용하면 더 편리합니다.

Aspose.PDF for Python은 SVG 이미지를 PDF 형식으로 변환하는 기능을 지원하며 PDF 파일을 SVG 형식으로 변환하는 기능도 제공합니다. 이 요구 사항을 수행하기 위해 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 클래스가 Aspose.PDF 네임스페이스에 도입되었습니다. SvgSaveOptions 객체를 인스턴스화하고 이를 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드에 두 번째 인수로 전달합니다.

다음 코드 스니펫은 Python으로 PDF 파일을 SVG 형식으로 변환하는 단계를 보여줍니다.

단계: Python에서 PDF를 SVG로 변환

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 객체를 생성합니다.
1. 필요한 설정으로 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 객체를 생성합니다.
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하고 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 객체를 전달하여 PDF 문서를 SVG로 변환합니다.

### PDF를 SVG로 변환

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    save_options = apdf.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

