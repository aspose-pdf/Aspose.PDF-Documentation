---
title: 다양한 파일 형식을 PDF로 변환하기
linktitle: 다른 파일 형식을 PDF로 변환하기
type: docs
weight: 80
url: /php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: 이 주제에서는 Aspose.PDF가 다른 파일 형식을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## EPUB을 PDF로 변환하기

**Aspose.PDF for PHP**는 간단히 EPUB 파일을 PDF 형식으로 변환할 수 있도록 합니다.

<abbr title="electronic publication">EPUB</abbr>은 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 오픈 전자책 표준입니다. 파일 확장자는 .epub입니다. EPUB은 재구성 가능한 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 최적화된 텍스트를 제공할 수 있음을 의미합니다.

EPUB 파일을 PDF 형식으로 변환하기 위해 Aspose.PDF for PHP에는 소스 EPUB 파일을 로드하기 위해 사용되는 [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions)라는 클래스가 있습니다.
 그런 다음, 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체 초기화의 인수로 전달됩니다. 이는 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 EPUB 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

1. EPUB [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) 생성.
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 객체 초기화.
1. 출력 PDF 문서 저장.

```php
// EpubLoadOptions의 새 인스턴스 생성
$loadOption = new EpubLoadOptions();

// 새 Document 객체 생성 및 EPUB 파일 로드
$document = new Document($inputFile, $loadOption);

// 문서를 PDF 파일로 저장
$document->save($outputFile);
```

{{% alert color="success" %}}
**EPUB을 PDF로 온라인으로 변환해 보세요**

Aspose.PDF for PHP는 온라인 무료 애플리케이션 ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)를 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.
[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Markdown을 PDF로 변환

{{% alert color="success" %}}
**온라인에서 Markdown을 PDF로 변환해보세요**

Aspose.PDF for PHP는 온라인 무료 응용 프로그램 ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)를 제공합니다. 이 응용 프로그램을 통해 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion Markdown to PDF with Free App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown은 웹 저자를 위한 텍스트에서 HTML로의 변환 도구입니다. Markdown을 사용하면 읽고 쓰기 쉬운 일반 텍스트 형식으로 작성한 후 구조적으로 유효한 XHTML(또는 HTML)로 변환할 수 있습니다.

다음 코드 스니펫은 PHP용 Aspose.PDF를 사용하여 이 기능을 사용하는 방법을 보여줍니다:

```php
// MdLoadOptions의 새 인스턴스 생성
$loadOption = new MdLoadOptions();

// Document의 새 인스턴스를 생성하고 입력 Markdown 파일을 로드
$document = new Document($inputFile, $loadOption);

// 문서를 PDF 파일로 저장
$document->save($outputFile);
```


## PCL을 PDF로 변환

<abbr title="Printer Command Language">PCL</abbr> (프린터 명령 언어)는 표준 프린터 기능에 접근하기 위해 개발된 Hewlett-Packard 프린터 언어입니다. PCL 레벨 1부터 5e/5c까지는 수신된 순서대로 처리되고 해석되는 제어 시퀀스를 사용하는 명령 기반 언어입니다. 소비자 수준에서는 PCL 데이터 스트림이 프린터 드라이버에 의해 생성됩니다. PCL 출력은 사용자 지정 응용 프로그램에 의해 쉽게 생성될 수도 있습니다.

{{% alert color="success" %}}
**온라인으로 PCL을 PDF로 변환해보세요**

Aspose.PDF for PHP는 ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)라는 무료 온라인 응용 프로그램을 제공하여 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 PCL을 PDF로 무료 앱으로](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**현재, PCL5와 이전 버전만 지원됩니다.**

|**명령 세트**|**지원**|**예외**|**설명**|

| :- | :- | :- | :- |
|작업 제어 명령어|+|양면 인쇄 모드|인쇄 프로세스를 제어: 복사본 수, 출력 트레이, 단면/양면 인쇄, 왼쪽 및 상단 오프셋 등|
|페이지 제어 명령어|+|천공 건너뛰기 명령어|페이지 크기, 여백, 페이지 방향, 줄 간격, 문자 간 거리 등을 지정|
|커서 위치 명령어|+| |커서 위치를 지정하고, 따라서 텍스트, 래스터 또는 벡터 이미지와 세부 사항의 기원을 지정합니다.|

|Font selection commands|+|<p>1. 투명 인쇄 데이터 명령.</p><p>2. 임베디드 소프트 폰트. 현재 버전에서는 소프트 폰트를 생성하는 대신, 타겟 머신에 설치된 기존의 "하드" 트루타입 폰트에서 적합한 폰트를 선택합니다. <br>   적합성은 너비/높이 비율로 정의됩니다. <br>   이 기능은 비트맵 및 트루타입 폰트에서만 작동하며 소프트 폰트로 인쇄된 텍스트가 원본 파일의 텍스트와 일치한다는 보장을 하지 않습니다. <br>   소프트 폰트의 문자 코드가 기본 문자 코드와 일치하지 않을 수 있기 때문입니다.</p><p>3. 사용자 정의 심볼 세트.</p>|PCL 파일에서 소프트(임베디드) 폰트를 로드하고 메모리에서 이를 관리할 수 있습니다.|
|Raster graphics commands|+|흑백만 가능|PCL 파일에서 래스터 이미지를 메모리로 로드하고, 너비, 높이, 압축 유형, 해상도 등의 래스터 매개변수를 지정할 수 있습니다.|
|Color commands|+| |모든 인쇄 가능한 객체에 색상을 지정할 수 있습니다.|
|Print Model commands|+| |텍스트, 래스터 이미지 및 직사각형 영역을 미리 정의된 패턴 및 사용자 정의 패턴으로 채우고, 패턴 및 원본 래스터 이미지에 대한 투명 모드를 지정할 수 있습니다.|
 <br>미리 정의된 패턴은 해칭, 크로스 해치 및 음영 패턴입니다.|
|사각형 영역 채우기 명령어|+| |패턴으로 사각형 영역을 생성하고 채우는 것을 허용합니다.|
|HP-GL/2 벡터 그래픽 명령어|+|스크린 벡터 명령어(SV), 투명 모드 명령어(TR), 투명 데이터 명령어(TD), RO(좌표계 회전), 스케일러블 또는 비트맵 폰트 명령어(SB), 문자 기울기 명령어(SL) 및 여분의 공간(ES)은 구현되지 않았으며 DV(가변 텍스트 경로 정의) 명령어는 베타 버전에서 구현되었습니다.|<p>- PCL 파일에서 HP-GL/2 벡터 이미지를 메모리로 로드할 수 있습니다. 벡터 이미지는 인쇄 가능한 영역의 좌하단 모서리에 원점을 가지고 있으며, 크기 조정, 이동, 회전 및 잘라내기가 가능합니다.</p><p>- 벡터 이미지는 레이블로서의 텍스트와 사각형, 원, 타원, 선, 호, 베지에 곡선 및 단순한 것들로 구성된 복잡한 도형과 같은 기하학적 도형을 포함할 수 있습니다.</p><p>- 레이블의 문자 포함 폐쇄된 도형은 단색 채우기나 벡터 패턴으로 채울 수 있습니다.</p><p>- 패턴은 해칭, 교차 해칭, 음영, 사용자 정의 래스터, PCL 해칭 또는 교차 해칭 및 PCL 사용자 정의일 수 있습니다. PCL 패턴은 래스터입니다. 레이블은 개별적으로 회전, 확대할 수 있으며 네 방향으로 지시될 수 있습니다: 위, 아래, 왼쪽 및 오른쪽. 왼쪽 및 오른쪽 방향은 연속적인 문자 배열을 포함합니다. 위 및 아래 방향은 연속적인 문자 배열을 포함합니다.</p>|
|Macross|―| |PCL 명령의 시퀀스를 메모리에 로드하고 이 시퀀스를 여러 번 사용할 수 있도록 허용합니다. 예를 들어, 페이지 헤더를 인쇄하거나 일련의 페이지에 대해 하나의 서식을 설정할 수 있습니다.|
|Unicode text|―| |비 ASCII 문자를 인쇄할 수 있도록 허용합니다. 샘플 파일의 부족으로 구현되지 않음 <br>유니코드 텍스트와 함께|
|PCL6 (PCL-XL)| |테스트 파일의 부족으로 인해 베타 버전에서만 구현됨. 내장된 폰트도 지원되지 않음. JetReady 확장은 JetReady 사양을 갖는 것이 불가능하기 때문에 지원되지 않음.|바이너리 파일 형식.|

### PCL 파일을 PDF 형식으로 변환

PCL에서 PDF로의 변환을 허용하기 위해 [Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java)에는 [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) 클래스가 있으며, 이는 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 객체를 초기화하는 데 사용됩니다. 이 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체 초기화 시 인수로 전달되며 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 PCL 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```php
// PclLoadOptions의 새 인스턴스 생성
$loadOption = new PclLoadOptions();

// Document의 새 인스턴스를 생성하고 PCL 파일을 로드
$document = new Document($inputFile, $loadOption);

// 문서를 PDF 파일로 저장
$document->save($outputFile);
```

### 알려진 문제

1. 텍스트 문자열과 이미지의 원본이 인쇄 방향이 0º가 아닌 경우 소스 PCL 파일과 약간 다를 수 있습니다. 벡터 이미지의 경우 벡터 플롯의 좌표계가 회전된 경우(RO 명령으로 선행됨)에도 동일하게 적용됩니다.
2. 벡터 이미지의 레이블 원본은 레이블 원본(LO), 변수 텍스트 경로 정의(DV), 절대 방향(DI) 또는 상대 방향(DR) 명령의 영향을 받는 경우 소스 PCL 파일과 다를 수 있습니다.
3. 텍스트가 비트맵 또는 트루타입 소프트(내장) 폰트로 렌더링되어야 하는 경우, 현재 이들 폰트는 부분적으로만 지원되므로 텍스트가 잘못 읽힐 수 있습니다("지원되는 기능 표"의 예외 참조). 이 경우 소프트 폰트의 문자 코드가 기본 코드와 일치하는 경우에만 텍스트를 올바르게 읽을 수 있습니다. 읽은 텍스트의 스타일도 소프트 폰트 헤더에서 스타일을 설정할 필요가 없기 때문에 소스 PCL 파일의 스타일과 다를 수 있습니다.

1. 구문 분석된 PCL 파일에 Intellifont 또는 Universal 소프트 폰트가 포함된 경우 예외가 발생합니다. Intellifont 및 Universal 폰트는 전혀 지원되지 않기 때문입니다.
1. 구문 분석된 PCL 파일에 매크로 명령이 포함된 경우, 매크로 명령은 지원되지 않기 때문에 구문 분석 결과가 원본 파일과 크게 다를 것입니다.

## 텍스트를 PDF로 변환

**Aspose.PDF for PHP**는 텍스트 파일을 PDF 형식으로 변환할 수 있는 기능을 제공합니다. 이 글에서는 Aspose.PDF를 사용하여 텍스트 파일을 PDF로 얼마나 쉽게 그리고 효율적으로 변환할 수 있는지를 보여줍니다.

텍스트 파일을 PDF로 변환해야 할 때, 처음에는 일부 리더에서 원본 텍스트 파일을 읽습니다. 우리는 StringBuilder를 사용하여 텍스트 파일의 내용을 읽었습니다. Document 객체를 인스턴스화하고 Pages 컬렉션에 새 페이지를 추가합니다. TextFragment의 새 객체를 생성하고 StringBuilder 객체를 생성자에 전달합니다. TextFragment 객체를 사용하여 Paragraphs 컬렉션에 새 단락을 추가하고 Document 클래스의 Save 메서드를 사용하여 결과 PDF 파일을 저장합니다.
**텍스트를 PDF로 온라인으로 변환해 보세요**

Aspose.PDF for PHP는 무료 온라인 애플리케이션 ["텍스트를 PDF로"](https://products.aspose.app/pdf/conversion/txt-to-pdf)를 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 텍스트를 PDF로 무료 앱](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### 일반 텍스트 파일을 PDF로 변환

```php
// 새로운 Document 객체를 생성합니다.
$document = new Document();

// 문서에 새 페이지를 추가합니다.
$page = $document->getPages()->add();

// 입력 텍스트 파일의 내용을 읽습니다.
$text = file_get_contents($inputFile);

// 새로운 FontRepository 객체를 생성합니다.
$fontRepository = new FontRepository();

// 저장소에서 "Courier" 폰트를 찾습니다.
$font = $fontRepository->findFont("Courier");

// 입력 텍스트로 새로운 TextFragment 객체를 생성합니다.
$textFragment = new TextFragment($text);

// 텍스트 조각의 폰트를 "Courier"로 설정합니다.
$textFragment->getTextState()->setFont($font);

// 페이지에 텍스트 조각을 추가합니다.
$page->getParagraphs()->add($textFragment);

// 문서를 출력 파일로 저장합니다.
$document->save($outputFile);
```


## XPS를 PDF로 변환

**Aspose.PDF for PHP**는 <abbr title="XML Paper Specification">XPS</abbr> 파일을 PDF 형식으로 변환하는 기능을 지원합니다. 이 기사를 확인하여 작업을 해결하세요.

XPS, XML Paper Specification은 문서 생성 및 보기를 Windows에 통합하기 위해 사용되는 Microsoft 파일 형식입니다. Aspose.PDF for PHP를 사용하면 XPS 파일을 Adobe의 휴대용 파일 형식인 PDF로 변환할 수 있습니다.

파일 형식은 기본적으로 압축된 XML 파일로, 주로 배포 및 저장에 사용됩니다. 편집이 매우 어렵고 주로 Microsoft에 의해 구현됩니다.

[Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java)를 사용하여 XPS 파일을 PDF로 변환하려면 [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions) 클래스를 사용하세요.
 이것은 [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) 객체를 초기화하는 데 사용됩니다. 나중에 이 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체 초기화 시 인수로 전달되며, PDF 렌더링 엔진이 원본 문서의 입력 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 XPS 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```php
// XpsLoadOptions 클래스의 새 인스턴스 생성
$loadOption = new XpsLoadOptions();

// Document 클래스의 새 인스턴스를 만들고 XPS 파일을 로드합니다.
$document = new Document($inputFile, $loadOption);

// 문서를 PDF 파일로 저장합니다.
$document->save($outputFile);
```

{{% alert color="success" %}}
**XPS 형식을 PDF로 온라인으로 변환해보세요**

Aspose.PDF for PHP는 ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.


[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## PostScript를 PDF로 변환

**Aspose.PDF for PHP**는 PostScript 파일을 PDF 형식으로 변환하는 기능을 지원합니다. Aspose.PDF의 기능 중 하나는 변환 중에 사용할 글꼴 폴더 세트를 설정할 수 있다는 점입니다.

PostScript 파일을 PDF 형식으로 변환하기 위해, Aspose.PDF for PHP는 LoadOptions 객체를 초기화하는 데 사용되는 [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) 클래스를 제공합니다. 나중에 이 객체는 Document 객체 생성자의 인수로 전달될 수 있으며, 이는 PDF 렌더링 엔진이 원본 문서의 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 PostScript 파일을 PDF 형식으로 변환하는 데 사용할 수 있습니다:

```php
// 새로운 PsLoadOptions 객체를 생성합니다.
$loadOption = new PsLoadOptions();

// 새로운 Document 객체를 생성하고 입력 PS 파일을 로드합니다.
$document = new Document($inputFile, $loadOption);

// 문서를 PDF 파일로 저장합니다.
$document->save($outputFile);
```

## XML을 PDF로 변환

XML 형식은 구조화된 데이터를 저장하는 데 사용됩니다.
 여러 가지 방법으로 Aspose.PDF에서 <abbr title="Extensible Markup Language">XML</abbr>을 PDF로 변환할 수 있습니다.

{{% alert color="success" %}}
**XML을 PDF로 온라인으로 변환해 보세요**

Aspose.PDF for PHP는 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)라는 무료 온라인 응용 프로그램을 제공하여 기능과 품질을 조사할 수 있습니다.

[![Aspose.PDF XML을 PDF로 변환하는 무료 앱](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

XSL-FO 표준을 기반으로 하는 XML 문서를 사용하는 옵션을 고려해 보세요.

### XSL-FO를 PDF로 변환

XSL-FO 파일을 PDF로 변환하는 것은 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 객체와 [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions)를 사용하여 구현할 수 있습니다.

```php
// 샘플 파일의 경로를 설정합니다
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// XslFoLoadOptions 클래스의 새 인스턴스를 생성하고 입력 XSL-FO 파일 경로를 전달합니다
$loadOption = new XslFoLoadOptions($inputFoFile);

// Document 클래스의 새 인스턴스를 생성하고 입력 XML 파일 및 XSL-FO 로드 옵션을 전달합니다
$document = new Document($inputFile, $loadOption);

// 변환된 PDF 문서를 출력 파일 경로에 저장합니다
$document->save($outputFile);
```

## LaTeX/TeX를 PDF로 변환

LaTeX 파일 형식은 LaTeX 언어 가족의 파생 언어인 LaTeX의 마크업이 포함된 텍스트 파일 형식이며, LaTeX는 TeX 시스템의 파생 형식입니다. LaTeX (ˈleɪtɛk/ 레이텍 또는 라텍)은 문서 준비 시스템이자 문서 마크업 언어입니다. 수학, 물리학, 컴퓨터 과학을 포함한 여러 분야에서 과학 문서의 커뮤니케이션 및 출판에 널리 사용됩니다. 또한 산스크리트어 및 아랍어와 같은 복잡한 다국어 자료를 포함하는 책 및 기사 작성 및 출판에서 중요한 역할을 합니다. LaTeX는 출력 형식을 지정하기 위해 TeX 조판 프로그램을 사용하며, 자체적으로 TeX 매크로 언어로 작성되어 있습니다.

**Aspose.PDF for PHP**는 TeX 파일을 PDF 형식으로 변환하는 기능을 지원하며, 이 요구사항을 충족하기 위해 com.aspose.pdf 패키지에는 LaTex 파일을 로드하고 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 클래스를 사용하여 PDF 형식으로 출력하는 기능을 제공하는 [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions)라는 클래스가 있습니다.
 다음 코드 스니펫은 LaTex 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```php
// LatexLoadOptions 클래스의 새 인스턴스를 만듭니다
$loadOption = new LatexLoadOptions();

// Document 클래스의 새 인스턴스를 만들고 TeXLoadOptions를 사용하여 TeX 파일을 로드합니다
$document = new Document($inputFile, $loadOption);

// 문서를 PDF 파일로 저장합니다
$document->save($outputFile);
```

{{% alert color="success" %}}
**LaTeX/TeX를 PDF로 온라인 변환 시도**

Aspose.PDF for PHP는 온라인 무료 애플리케이션 ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)를 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF LaTeX/TeX를 PDF로 무료 앱으로 변환](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}