---
title: 다양한 이미지 형식을 PDF로 변환 
linktitle: 이미지를 PDF로 변환
type: docs
weight: 60
url: ko/php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: 이 주제는 Aspose.PDF for PHP 라이브러리가 다양한 이미지 형식을 PDF로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for PHP**를 사용하면 다양한 형식의 이미지를 PDF 파일로 변환할 수 있습니다. 우리의 라이브러리는 BMP, CGM, D    MF, JPG, PNG, SVG 및 TIFF 형식과 같은 가장 인기 있는 이미지 형식을 변환하는 코드 스니펫을 보여줍니다.

## BMP를 PDF로 변환

**Aspose.PDF for PHP** 라이브러리를 사용하여 BMP 파일을 PDF 문서로 변환합니다.

<abbr title="Bitmap Image File">BMP</abbr> 이미지는 확장자가 .BMP인 파일로 비트맵 디지털 이미지를 저장하는 데 사용됩니다. 이러한 이미지는 그래픽 어댑터와 독립적이며 장치 독립 비트맵(DIB) 파일 형식이라고도 합니다. Aspose.PDF for PHP API를 사용하여 BMP를 PDF로 변환할 수 있습니다.
 다음 단계에 따라 BMP 이미지를 변환할 수 있습니다:

1. 새 Document 객체를 생성합니다
1. 문서에 새 페이지를 추가합니다
1. 필요하면 페이지의 여백을 0으로 설정합니다
1. 새 Image 객체를 생성하고 입력 BMP 파일을 설정합니다
1. 이미지를 페이지에 추가합니다
1. 문서를 출력 PDF 파일로 저장합니다

따라서 다음 코드 스니펫은 이러한 단계를 따르며 PHP를 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다:

```php
// 새 Document 객체를 생성합니다
$document = new Document();

// 문서에 새 페이지를 추가합니다
$page = $document->getPages()->add();

// 페이지의 여백을 0으로 설정합니다
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 새 Image 객체를 생성하고 입력 BMP 파일을 설정합니다
$image = new Image();
$image->setFile($inputFile);

// 이미지를 페이지에 추가합니다
$page->getParagraphs()->add($image);

// 문서를 출력 PDF 파일로 저장합니다
$document->save($outputFile);
```

## CGM을 PDF로 변환

<abbr title="Computer Graphics Metafile">CGM</abbr>은 그래픽 정보의 저장 및 검색을 위한 벡터 기반 2D 이미지 파일 형식을 제공하는 ISO 표준입니다. CGM은 장치 독립적인 형식입니다. CGM은 세 가지 다른 인코딩 방법을 지원하는 벡터 그래픽 형식입니다: 바이너리(프로그램 읽기 속도에 가장 적합), 문자 기반(가장 작은 파일 크기를 생성하고 더 빠른 데이터 전송을 허용) 또는 클리어텍스트 인코딩(사용자가 텍스트 편집기로 파일을 읽고 수정할 수 있도록 허용).

다음 코드 스니펫은 Aspose.PDF for PHP를 사용하여 CGM 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

1. CGM 파일을 로드하기 위한 특정 옵션을 지정하기 위해 [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) 인스턴스를 생성합니다.
1. 소스 파일 이름과 옵션을 명시하여 [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) 클래스의 인스턴스를 생성합니다.
1. 원하는 파일 이름으로 문서를 저장합니다.

```php
$options = new CgmLoadOptions();

// 지정된 옵션을 사용하여 CGM 파일을 로드하고 Document 객체를 생성합니다
$document = new Document($inputFile, $options);

// 문서를 PDF 파일로 저장합니다
$document->save($outputFile);
```


## DICOM을 PDF로 변환

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr>은 의료 영상에서 정보를 처리, 저장, 인쇄 및 전송하기 위한 표준입니다. 파일 형식 정의와 네트워크 통신 프로토콜을 포함합니다.

Aspose.PDF for PHP를 사용하면 DICOM 파일을 PDF 형식으로 변환할 수 있습니다. 다음 코드 스니펫을 확인하세요:

1. 새로운 Document 객체를 생성합니다
1. 문서에 새로운 페이지를 추가합니다
1. 페이지의 여백을 0으로 설정합니다 (필요한 경우)
1. 새로운 Image 객체를 생성하고 입력 BMP 파일을 설정합니다
1. 이미지의 소스 파일로 DICOM 파일을 설정합니다
1. 이미지의 파일 형식을 DICOM으로 설정합니다
1. 이미지를 페이지에 추가합니다
1. 문서를 출력 PDF 파일로 저장합니다

```php
// 새로운 Document 객체를 생성합니다
$document = new Document();

// 문서에 새로운 페이지를 추가합니다
$page = $document->getPages()->add();

// 페이지의 여백을 0으로 설정합니다
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 새로운 Image 객체를 생성합니다
$image = new Image();

// 이미지의 소스 파일로 DICOM 파일을 설정합니다
$image->setFile($inputFile);

// 이미지의 파일 형식을 DICOM으로 설정합니다
$image->setFileType(ImageFileType::$Dicom);

// 이미지를 페이지에 추가합니다
$page->getParagraphs()->add($image);

// 문서를 PDF 파일로 저장합니다
$document->save($outputFile);
```


{{% alert color="success" %}}
**DICOM을 PDF로 온라인 변환 시도하기**

Aspose는 ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)라는 무료 온라인 애플리케이션을 제공하며, 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 DICOM을 PDF로 무료 앱 사용](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF를 PDF로 변환

향상된 메타파일 형식(<abbr title="Enhanced metafile format">EMF</abbr>)은 장치 독립적으로 그래픽 이미지를 저장합니다. EMF의 메타파일은 시간 순서대로 가변 길이 레코드로 구성되어 있으며, 이를 파싱하여 저장된 이미지를 출력 장치에 렌더링할 수 있습니다.

우리는 EMF를 PDF로 변환하는 몇 가지 접근 방식을 가지고 있습니다.

## Image 클래스 사용

PDF 문서는 페이지로 구성되며 각 페이지는 하나 이상의 단락 객체를 포함합니다. 단락은 텍스트, 이미지, 테이블, 플로팅 박스, 그래프, 헤딩, 폼 필드 또는 첨부 파일일 수 있습니다.

이미지 파일을 PDF 형식으로 변환하려면 단락에 포함하십시오.

이미지를 로컬 하드 드라이브의 물리적 위치, 웹 URL 또는 Stream 인스턴스에서 변환할 수 있습니다.

이미지를 추가하려면:

1. com.aspose.pdf.Image 클래스의 객체를 생성합니다.
2. 페이지 인스턴스의 [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) 컬렉션에 이미지를 추가합니다.
3. 이미지의 경로 또는 소스를 지정합니다.
    - 이미지가 하드 드라이브의 위치에 있는 경우, [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image) 메서드를 사용하여 경로 위치를 지정합니다.
    - 이미지가 FileInputStream에 있는 경우, 이미지를 보유한 객체를 [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image) 메서드에 전달합니다.

다음 코드 스니펫은 이미지 객체를 로드하고, 페이지 여백을 설정하고, 페이지에 이미지를 배치하고, PDF로 출력 저장하는 방법을 보여줍니다.

```php
$inputFile = "sample.emf";

// 새 Document 객체를 생성합니다.
$document = new Document();

// 문서에 새 페이지를 추가합니다.
$page = $document->getPages()->add();

// 페이지의 여백을 0으로 설정합니다.
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 새 Image 객체를 생성하고 입력 파일을 설정합니다.
$image = new Image();
$image->setFile($inputFile);

// 페이지에 이미지를 추가합니다.
$page->getParagraphs()->add($image);

// 문서를 PDF 파일로 저장합니다.
$document->save($outputFile);
```


## JPG를 PDF로 변환

JPG를 PDF로 변환하는 방법을 고민할 필요가 없습니다. Apose.PDF for PHP 라이브러리가 최고의 솔루션을 제공합니다.

JPG 이미지를 Aspose.PDF for PHP를 사용하여 다음 단계를 통해 매우 쉽게 PDF로 변환할 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 객체를 초기화합니다
1. 문서에 새 페이지를 추가합니다
1. 페이지의 여백을 0으로 설정합니다
1. 새 이미지 객체를 생성하고 입력 파일을 설정합니다
1. 출력 PDF를 저장합니다

아래의 코드 스니펫은 PHP를 사용하여 JPG 이미지를 PDF로 변환하는 방법을 보여줍니다:

```php
$inputFile = "sample.jpg";

// 새 Document 객체를 생성합니다
$document = new Document();

// 문서에 새 페이지를 추가합니다
$page = $document->getPages()->add();

// 페이지의 여백을 0으로 설정합니다
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 새 이미지 객체를 생성하고 입력 파일을 설정합니다
$image = new Image();
$image->setFile($inputFile);

// 이미지가 페이지에 추가됩니다
$page->getParagraphs()->add($image);

// 문서를 PDF 파일로 저장합니다
$document->save($outputFile);
```


{{% alert color="success" %}}
**JPG를 PDF로 온라인 변환 시도**

Aspose는 온라인 무료 애플리케이션 ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF JPG를 PDF로 변환하기 무료 앱 사용](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## PNG를 PDF로 변환하기

**Aspose.PDF for PHP**는 PNG 이미지를 PDF 형식으로 변환하는 기능을 지원합니다. 다음 코드 스니펫을 확인하여 작업을 수행하십시오.

<abbr title="Portable Network Graphics">PNG</abbr>는 무손실 압축을 사용하는 래스터 이미지 파일 형식을 나타내며, 사용자들 사이에서 인기가 많습니다.

PNG를 PDF 이미지로 변환하려면 아래 단계를 따르십시오:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 객체를 초기화합니다.
1. 문서에 새 페이지를 추가합니다.
1. 페이지의 여백을 0으로 설정합니다.
1. 새로운 이미지 객체를 생성하고 입력 파일을 설정합니다.
1. 출력 PDF를 저장합니다.

또한, 아래 코드 스니펫은 PHP 애플리케이션에서 PNG를 PDF로 변환하는 방법을 보여줍니다:

```php
$inputFile = "sample.png";

// 새로운 Document 객체 생성
$document = new Document();

// 문서에 새 페이지 추가
$page = $document->getPages()->add();

// 페이지의 여백을 0으로 설정
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 새로운 Image 객체 생성 및 입력 파일 설정
$image = new Image();
$image->setFile($inputFile);

// 이미지 페이지에 추가
$page->getParagraphs()->add($image);

// 문서를 PDF 파일로 저장
$document->save($outputFile);
```

{{% alert color="success" %}}
**PNG를 PDF로 온라인 변환 시도**

Aspose는 온라인 무료 애플리케이션 ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)을 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PNG to PDF using Free App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## SVG를 PDF로 변환

스케일러블 벡터 그래픽(SVG)은 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양 모음으로, 정적 및 동적(대화형 또는 애니메이션) 그래픽을 포함합니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에 의해 개발된 오픈 표준입니다.

SVG 이미지와 그 동작은 XML 텍스트 파일로 정의됩니다. 이는 검색, 인덱싱, 스크립팅이 가능하며, 필요에 따라 압축할 수도 있다는 것을 의미합니다. XML 파일로서, SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, Inkscape와 같은 드로잉 프로그램을 사용하여 생성하는 것이 더 편리한 경우가 많습니다.

## SVG 파일을 PDF 형식으로 변환하는 방법

SVG 파일을 PDF로 변환하려면 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 객체를 초기화하는 데 사용되는 [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions)라는 클래스를 사용하십시오.
 나중에 이 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체 초기화 시 인수로 전달되어 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 SVG 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```php
// 새로운 SvgLoadOptions 객체 생성
$loadOption = new SvgLoadOptions();

// 새로운 Document 객체 생성 및 SVG 파일 로드
$document = new Document($inputFile, $loadOption);

// 문서를 PDF 파일로 저장
$document->save($outputFile);
```

{{% alert color="success" %}}
**SVG 형식을 PDF로 온라인 변환 시도**

Aspose.PDF for PHP는 ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)라는 온라인 무료 애플리케이션을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## TIFF를 PDF로 변환하기

**Aspose.PDF for PHP** 파일 형식을 지원하며, 단일 프레임 또는 다중 프레임 <abbr title="Tag Image File Format">TIFF</abbr> 이미지도 지원합니다. 즉, Java 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있습니다.

TIFF 또는 TIF, 태그 이미지 파일 형식은 이 파일 형식 표준을 준수하는 다양한 장치에서 사용하기 위한 래스터 이미지를 나타냅니다. TIFF 이미지는 서로 다른 이미지를 가진 여러 프레임을 포함할 수 있습니다. Aspose.PDF 파일 형식도 지원하며, 단일 프레임 또는 다중 프레임 TIFF 이미지도 지원합니다. 따라서 Java 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있습니다. 따라서 여러 페이지의 TIFF 이미지를 여러 페이지의 PDF 문서로 변환하는 예제를 다음 단계로 고려하겠습니다:

1. 새 Document 객체를 생성합니다
1. 문서에 새 페이지를 추가합니다
1. 페이지의 여백을 0으로 설정합니다
1. 새 Image 객체를 생성합니다
1. 입력 TIFF 이미지의 파일 경로를 설정합니다
1. 이미지를 페이지에 추가합니다
1. 문서를 PDF 파일로 저장합니다

또한, 다음 코드 스니펫은 여러 페이지 또는 여러 프레임의 TIFF 이미지를 PDF로 변환하는 방법을 보여줍니다:

```php
// 새로운 Document 객체를 생성합니다.
$document = new Document();

// 문서에 새 페이지를 추가합니다.
$page = $document->getPages()->add();

// 페이지의 여백을 0으로 설정합니다.
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// 새로운 Image 객체를 생성합니다.
$image = new Image();

// 입력 TIFF 이미지의 파일 경로를 설정합니다.
$image->setFile($inputFile);

// 이미지를 페이지에 추가합니다.
$page->getParagraphs()->add($image);

// 문서를 PDF 파일로 저장합니다.
$document->save($outputFile);
```