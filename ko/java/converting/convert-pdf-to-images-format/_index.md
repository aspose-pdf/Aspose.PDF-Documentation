---
title: PDF를 이미지 형식으로 변환 
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/java/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 PDF를 다양한 이미지 형식으로 변환하는 방법을 보여줍니다. 몇 줄의 코드로 PDF 페이지를 PNG, JPEG, BMP 이미지로 변환합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java**는 PDF 문서를 BMP, JPEG, GIF, PNG, EMF, TIFF, SVG와 같은 이미지 형식으로 변환할 수 있도록 두 가지 접근 방식을 제공합니다. 변환은 Device를 사용하거나 SaveOption을 사용하여 수행됩니다.

라이브러리에는 가상 장치를 사용하여 이미지를 변환할 수 있도록 하는 여러 클래스가 있습니다. DocumentDevice는 전체 문서 변환을 지향하지만, ImageDevice는 특정 페이지를 위해 사용됩니다.

## DocumentDevice 클래스를 사용하여 PDF 변환

**Aspose.PDF for Java**는 PDF 페이지를 TIFF 이미지로 변환할 수 있습니다.

[TiffDevice 클래스](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice)는 PDF 페이지를 TIFF 이미지로 변환할 수 있도록 합니다.
 이 클래스는 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환할 수 있는 Process라는 메서드를 제공합니다.

### PDF 페이지를 하나의 TIFF 이미지로 변환하기

Aspose.PDF for Java는 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환하는 방법을 설명합니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 객체를 생성합니다.
1. 문서를 변환하기 위해 [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) 메서드를 호출합니다.
1. 출력 파일의 속성을 설정하려면 [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings) 클래스를 사용합니다.

다음 코드 스니펫은 모든 PDF 페이지를 하나의 TIFF 이미지로 변환하는 방법을 보여줍니다.

```java
// 문서 열기
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Resolution 객체 생성
Resolution resolution = new Resolution(300);

// TiffSettings 객체 생성
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);
tiffSettings.setSkipBlankPages(false);

// TIFF 장치 생성
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// 특정 페이지를 변환하고 이미지를 스트림에 저장
tiffDevice.process(document, DATA_DIR + "AllPagesToTIFF_out.tif");
```

### 단일 페이지를 TIFF 이미지로 변환

Aspose.PDF for Java는 PDF 파일의 특정 페이지를 TIFF 이미지로 변환할 수 있습니다. 변환을 위해 페이지 번호를 인수로 받는 Process(..) 메서드의 오버로드된 버전을 사용하세요. 다음 코드 스니펫은 PDF의 첫 페이지를 TIFF 형식으로 변환하는 방법을 보여줍니다.

```java
// 문서 열기
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
String tiffFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF_out.tif").toString();
Document document = new Document(documentFileName);

// 해상도 객체 생성
Resolution resolution = new Resolution(300);

// TiffSettings 객체 생성
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);

// TIFF 디바이스 생성
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// 특정 페이지를 변환하고 이미지를 스트림에 저장
tiffDevice.process(document, 1, 1, tiffFileName);
```


### 변환 중 Bradley 알고리즘 사용

Aspose.PDF for Java는 LZW 압축을 사용하여 PDF를 TIFF로 변환하는 기능을 지원하고 있으며 AForge를 사용하여 이진화를 적용할 수 있습니다. 그러나 고객 중 일부는 Otsu를 사용하여 임계값을 얻어야 하는 이미지를 요청했기 때문에 Bradley도 사용하고 싶어했습니다.

```java
// 문서 열기
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

String outputImageFileName = Paths.get(DATA_DIR.toString(), "resultant_out.tif").toString();
String outputBinImageFileName = Paths.get(DATA_DIR.toString(), "tiff-bin_out.tif").toString();

java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

// Resolution 객체 생성
Resolution resolution = new Resolution(300);
// TiffSettings 객체 생성
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.LZW);
tiffSettings.setDepth(ColorDepth.Format1bpp);

// TIFF 장치 생성
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
// 특정 페이지를 변환하고 이미지를 스트림에 저장
tiffDevice.process(document, outputImageFile);
outputImageFile.close();

// 출력 이미지를 저장할 스트림 객체 생성
java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);
```


### PDF 페이지를 픽셀화된 TIFF 이미지로 변환

PDF 파일의 모든 페이지를 픽셀화된 TIFF 형식으로 변환하려면 IndexedConversionType의 Pixelated 옵션을 사용하십시오.

```java
// PDF 페이지를 픽셀화된 TIFF 이미지로 변환
// PDF 파일의 모든 페이지를 픽셀화된 TIFF 형식으로 변환하려면 IndexedConversionType의
// Pixelated 옵션을 사용하십시오.

// 문서 열기
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// 출력 이미지를 저장할 스트림 객체 생성
java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

// 해상도 객체 생성
com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

// TiffSettings 객체 인스턴스화
com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

// 결과 TIFF 이미지의 압축 설정
tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
// 결과 이미지의 색상 깊이 설정
tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
// PDF를 TIFF로 렌더링하는 동안 빈 페이지 건너뛰기
tiffSettings.setSkipBlankPages(true);
// 이미지 밝기 설정
tiffSettings.setBrightness(.5f);

// IndexedConversion Type 설정, 기본값은 simple
tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

// 특정 해상도로 TiffDevice 객체 생성
TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

// 특정 페이지(Page 1)를 변환하고 이미지를 스트림에 저장
tiffDevice.process(document, 1, 1, imageStream);

// 스트림 닫기
imageStream.close();
```


{{% alert color="success" %}}
**PDF를 TIFF로 온라인에서 변환 시도하기**

Aspose.PDF for Java는 온라인 무료 애플리케이션 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)을 제공하며, 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## ImageDevice 클래스를 사용하여 PDF 변환하기

`ImageDevice`는 `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` 및 `EmfDevice`의 선조입니다.

- [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) 클래스는 PDF 페이지를 <abbr title="Bitmap Image File">BMP</abbr> 이미지로 변환할 수 있게 해줍니다.
- [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) 클래스는 PDF 페이지를 <abbr title="Enhanced Meta File">EMF</abbr> 이미지로 변환할 수 있게 해줍니다.

- [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) 클래스는 PDF 페이지를 JPEG 이미지로 변환할 수 있게 해줍니다.
- [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) 클래스는 PDF 페이지를 <abbr title="Portable Network Graphics">PNG</abbr> 이미지로 변환할 수 있도록 합니다.
- [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) 클래스는 PDF 페이지를 <abbr title="Graphics Interchange Format">GIF</abbr> 이미지로 변환할 수 있도록 합니다.

PDF 페이지를 이미지로 변환하는 방법을 살펴보겠습니다.

[BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) 클래스는 [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices.BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-)라는 메서드를 제공하여 PDF 파일의 특정 페이지를 BMP 이미지 형식으로 변환할 수 있도록 합니다. 다른 클래스들도 동일한 메서드를 가지고 있습니다. 따라서 PDF 페이지를 이미지로 변환하려면 필요한 클래스를 인스턴스화하기만 하면 됩니다.

다음 코드 스니펫은 이 가능성을 보여줍니다:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * PDF를 이미지로 변환합니다.
 */
public final class ConvertPDFtoImage {
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoImage() {

    }

    public static void run() throws IOException {
        runConvertPdfUsingImageDevice();
    }

    public static void runConvertPdfUsingImageDevice() throws IOException {
        // Resolution 객체 생성
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(DATA_DIR + "ConvertAllPagesToBmp.pdf");

        convertPDFtoImages(bmpDevice, "bmp", document);
        convertPDFtoImages(jpegDevice, "jpeg", document);
        convertPDFtoImages(gifDevice, "gif", document);
        convertPDFtoImages(pngDevice, "png", document);
        convertPDFtoImages(emfDevice, "emf", document);
    }

    public static void convertPDFtoImages(
            ImageDevice imageDevice,
            String ext,
            Document document)
            throws IOException {
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            java.io.OutputStream imageStream = new java.io.FileOutputStream(
                    DATA_DIR + "image" + pageCount + "_out." + ext);
            // 특정 페이지를 변환하고 이미지를 스트림에 저장
            imageDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // 스트림 닫기
            imageStream.close();
        }
    }
}
```


{{% alert color="success" %}}
**PDF를 PNG로 온라인 변환 시도**

우리의 무료 애플리케이션이 어떻게 작동하는지 예시로 다음 기능을 확인하세요.

Aspose.PDF for Java는 무료 온라인 애플리케이션 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)를 제공하며, 여기서 기능과 품질을 조사할 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptions 클래스를 사용하여 PDF 변환

이 기사 부분은 Java와 SaveOptions 클래스를 사용하여 PDF를 <abbr title="Scalable Vector Graphics">SVG</abbr>로 변환하는 방법을 보여줍니다.

{{% alert color="success" %}}
**PDF를 SVG로 온라인 변환 시도**

Aspose.PDF for Java는 무료 온라인 애플리케이션 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)를 제공하며, 여기서 기능과 품질을 조사할 수 있습니다.

[![무료 앱을 사용하여 PDF를 SVG로 변환](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**스케일러블 벡터 그래픽스(SVG)**는 정적 및 동적(인터랙티브 또는 애니메이션) 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양 가족입니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에 의해 개발되고 있는 오픈 표준입니다.

SVG 이미지와 그 동작은 XML 텍스트 파일로 정의됩니다. 이는 검색, 인덱싱, 스크립트 작성이 가능하며, 필요시 압축할 수도 있다는 것을 의미합니다. XML 파일로서, SVG 이미지는 텍스트 편집기로 생성하고 편집할 수 있지만, 일반적으로 Inkscape와 같은 드로잉 프로그램으로 작성하는 것이 더 편리합니다.

### PDF 페이지를 SVG 이미지로 변환

Aspose.PDF for Java는 PDF 파일을 SVG 형식으로 변환하는 기능을 지원합니다.
 이 요구 사항을 충족하기 위해 [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) 클래스가 com.aspose.pdf 패키지에 도입되었습니다. [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions)의 객체를 인스턴스화하고 [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 메서드의 두 번째 인수로 전달합니다.

다음 코드 스니펫은 PDF 파일을 SVG 형식으로 변환하는 단계를 보여줍니다.

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.SvgSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * PDF를 SVG로 변환합니다.
 */
public class ConvertPDFtoSVG {
    // 문서 디렉토리 경로입니다.
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoSVG() {

    }

    public static void run() throws IOException {
        String pdfFileName = Paths.get(DATA_DIR.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(DATA_DIR.toString(), "PDFToSVG_out.svg").toString();

        // PDF 문서 로드
        Document document = new Document(pdfFileName);

        // SvgSaveOptions의 객체 인스턴스화
        SvgSaveOptions saveOptions = new SvgSaveOptions();

        // SVG 이미지를 Zip 아카이브로 압축하지 않음
        saveOptions.setCompressOutputToZipArchive(false);

        // SVG 파일로 출력 저장
        document.save(svgFileName, saveOptions);
        document.close();
    }
}
```