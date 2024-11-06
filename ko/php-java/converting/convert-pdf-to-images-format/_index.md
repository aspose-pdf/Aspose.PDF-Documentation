---
title: PDF를 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: ko/php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: 이 주제는 Aspose.PDF가 PDF를 다양한 이미지 형식으로 변환하는 방법을 보여줍니다. PDF 페이지를 몇 줄의 코드로 PNG, JPEG, BMP 이미지로 변환하세요.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for PHP**는 BMP, JPEG, GIF, PNG, EMF, TIFF, SVG와 같은 이미지 형식으로 PDF 문서를 변환할 수 있도록 두 가지 접근 방식을 제공합니다. 변환은 `Device`와 `SaveOption`을 사용하여 수행됩니다.

라이브러리에는 이미지를 변환하기 위해 가상 장치를 사용할 수 있는 여러 클래스가 있습니다. `DocumentDevice`는 전체 문서 변환을 지향하지만, `ImageDevice`는 특정 페이지에 대한 것입니다.

## DocumentDevice 클래스를 사용하여 PDF 변환하기

**Aspose.PDF for PHP**는 PDF 페이지를 TIFF 이미지로 변환할 수 있습니다.

[TiffDevice 클래스](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice)는 PDF 페이지를 TIFF 이미지로 변환할 수 있게 해줍니다.
 이 클래스는 PDF 파일의 모든 페이지를 하나의 TIFF 이미지로 변환할 수 있는 Process라는 메서드를 제공합니다.

### PDF 페이지를 하나의 TIFF 이미지로 변환

Aspose.PDF for PHP는 PDF 파일의 모든 페이지를 하나의 TIFF 이미지로 변환하는 방법을 설명합니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 객체를 생성합니다.
1. 문서를 변환하기 위해 [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) 메서드를 호출합니다.
1. 출력 파일의 속성을 설정하려면 [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings) 클래스를 사용합니다.

다음 코드 스니펫은 PDF의 모든 페이지를 하나의 TIFF 이미지로 변환하는 방법을 보여줍니다.

```php
// PDF 문서 로드
$document = new Document($inputFile);

// 새로운 TiffSettings 객체 생성
$tiffSettings = new devices_TiffSettings();

// TIFF 설정을 사용자 정의하려면 다음 줄의 주석을 해제하세요
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// TIFF 이미지의 해상도 설정
$resolution = new devices_Resolution(300);

// 지정된 해상도 및 설정으로 새로운 TiffDevice 객체 생성
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// TiffDevice를 사용하여 PDF 문서를 TIFF로 변환
$tiffDevice->process($document, $outputFile);
```

### 단일 페이지를 TIFF 이미지로 변환

Aspose.PDF for PHP를 사용하면 PDF 파일의 특정 페이지를 TIFF 이미지로 변환할 수 있습니다. 변환을 위해 페이지 번호를 인수로 사용하는 Process(..) 메서드의 오버로드된 버전을 사용합니다. 다음 코드 스니펫은 PDF의 첫 번째 페이지를 TIFF 형식으로 변환하는 방법을 보여줍니다.

```php
// PDF 문서 불러오기
$document = new Document($inputFile);

// 새로운 TiffSettings 객체 생성
$tiffSettings = new devices_TiffSettings();

// TIFF 설정을 사용자 지정하려면 다음 줄의 주석을 해제하세요
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// TIFF 이미지의 해상도 설정
$resolution = new devices_Resolution(300);

// 지정된 해상도 및 설정으로 새로운 TiffDevice 객체 생성
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// TiffDevice를 사용하여 PDF 문서를 TIFF로 변환
$tiffDevice->process($document, 1, 1, $outputFile);
```


### 변환 중 Bradley 알고리즘 사용

Aspose.PDF for PHP는 LZW 압축을 사용하여 PDF를 TIFF로 변환하는 기능을 지원하며, AForge를 사용하여 이진화 처리할 수 있습니다. 그러나 일부 고객은 특정 이미지에 대해 Otsu를 사용하여 임계값을 얻어야 하므로 Bradley도 사용하고 싶어합니다.

```php
// 새 TiffSettings 객체 생성
$tiffSettings = new devices_TiffSettings();

// TIFF 설정을 사용자 정의하려면 다음 줄의 주석을 해제하세요
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// TIFF 이미지의 해상도 설정
$resolution = new devices_Resolution(300);

// 지정된 해상도와 설정으로 새 TiffDevice 객체 생성
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// TiffDevice를 사용하여 PDF 문서를 TIFF로 변환
$tiffDevice->process($document, 1, 1, $outputFile);

// 출력 이미지를 저장할 스트림 객체 생성
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### PDF 페이지를 픽셀화된 TIFF 이미지로 변환

PDF 파일의 모든 페이지를 픽셀화된 TIFF 형식으로 변환하려면 IndexedConversionType의 Pixelated 옵션을 사용하세요.

```php
// 새로운 TiffSettings 객체를 생성
$tiffSettings = new devices_TiffSettings();

// TIFF 설정을 사용자 정의하려면 다음 줄의 주석을 해제
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// 이미지 밝기 설정
$tiffSettings->setBrightness(0.5f);
// IndexedConversion Type 설정, 기본값은 simple
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);


$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// TIFF 이미지의 해상도 설정
$resolution = new devices_Resolution(300);

// 지정된 해상도와 설정으로 새로운 TiffDevice 객체 생성
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// TiffDevice를 사용하여 PDF 문서를 TIFF로 변환
$tiffDevice->process($document, 1, 1, $outputFile);

// 출력 이미지를 저장할 스트림 객체 생성
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}  
**PDF를 TIFF로 온라인 변환 시도하기**  

Aspose.PDF for PHP는 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)라는 무료 온라인 응용 프로그램을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PDF to TIFF 무료 앱](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)  
{{% /alert %}}  

## ImageDevice 클래스를 사용하여 PDF 변환하기  

`ImageDevice`는 `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` 및 `EmfDevice`의 상위 클래스입니다.  

- [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) 클래스는 PDF 페이지를 <abbr title="Bitmap Image File">BMP</abbr> 이미지로 변환할 수 있게 해줍니다.
- [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) 클래스는 PDF 페이지를 <abbr title="Enhanced Meta File">EMF</abbr> 이미지로 변환할 수 있게 해줍니다.  

- [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) 클래스는 PDF 페이지를 JPEG 이미지로 변환할 수 있게 해줍니다.
- [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) 클래스는 PDF 페이지를 PNG 이미지로 변환할 수 있게 해줍니다.
- [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) 클래스는 PDF 페이지를 GIF 이미지로 변환할 수 있게 해줍니다.

PDF 페이지를 이미지로 변환하는 방법을 살펴보겠습니다.

[BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) 클래스는 [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-)라는 메서드를 제공하며, 이를 통해 PDF 파일의 특정 페이지를 BMP 이미지 형식으로 변환할 수 있습니다. 다른 클래스들도 동일한 메서드를 가지고 있습니다. 따라서, PDF 페이지를 이미지로 변환해야 할 경우, 필요한 클래스를 인스턴스화하면 됩니다.

다음 코드 스니펫은 이 가능성을 보여줍니다:

```php
// PDF 문서 로드
$document = new Document($inputFile);

// 문서의 페이지 모음 가져오기
$pages = $document->getPages();

// 문서의 총 페이지 수 가져오기
$count = $pages->size();

// PNG 이미지의 해상도 설정
$resolution = new devices_Resolution(300);

// 지정된 해상도로 새로운 PNG 장치 생성
$imageDevice = new devices_PngDevice($resolution);

// 문서의 각 페이지를 순회
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // 현재 페이지의 출력 이미지 파일 이름 설정
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // 모음에서 현재 페이지 가져오기
    $page = $document->getPages()->get_Item($pageCount);

    // 현재 페이지를 처리하고 PNG 이미지로 저장
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**PDF를 PNG로 온라인 변환 시도하기**

우리의 무료 응용 프로그램이 어떻게 작동하는지 예시로 다음 기능을 확인해 보세요.

Aspose.PDF for PHP는 온라인 무료 응용 프로그램 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)를 제공합니다. 여기서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptions 클래스를 사용하여 PDF 변환

이 문서의 이 부분에서는 Java와 SaveOptions 클래스를 사용하여 PDF를 <abbr title="Scalable Vector Graphics">SVG</abbr>로 변환하는 방법을 보여줍니다.

{{% alert color="success" %}}
**PDF를 SVG로 온라인 변환 시도하기**

Aspose.PDF for PHP는 온라인 무료 응용 프로그램 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)를 제공합니다. 여기서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![무료 앱을 사용하여 Aspose.PDF 변환 PDF를 SVG로](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**스케일러블 벡터 그래픽 (SVG)**은 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양 가족으로, 정적 및 동적(대화형 또는 애니메이션) 그래픽을 포함합니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에 의해 개발된 개방형 표준입니다.

SVG 이미지와 그 동작은 XML 텍스트 파일로 정의됩니다. 이것은 검색, 인덱싱, 스크립팅이 가능하며 필요한 경우 압축할 수 있음을 의미합니다. XML 파일로서, SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, Inkscape와 같은 드로잉 프로그램을 사용하여 만드는 것이 더 편리할 수 있습니다.

### PDF 페이지를 SVG 이미지로 변환하기

Aspose.PDF for PHP는 PDF 파일을 SVG 형식으로 변환하는 기능을 지원합니다.
 이 요구 사항을 충족시키기 위해 [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) 클래스가 com.aspose.pdf 패키지에 도입되었습니다. [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions)의 객체를 인스턴스화하고 이를 [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 메서드의 두 번째 인수로 전달합니다.

다음 코드 스니펫은 PDF 파일을 SVG 형식으로 변환하는 단계를 보여줍니다.

```php
// PDF 문서를 로드합니다
$document = new Document($inputFile);

// SvgSaveOptions 클래스의 인스턴스를 만듭니다
$saveOption = new SvgSaveOptions();

// PDF 문서를 SVG로 저장합니다
$document->save($outputFile, $saveOption);
```