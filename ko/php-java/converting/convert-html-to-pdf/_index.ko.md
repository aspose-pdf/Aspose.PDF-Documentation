---

title: HTML을 PDF로 변환하기  
linktitle: HTML을 PDF로 변환하기  
type: docs  
weight: 40  
url: /php-java/convert-html-to-pdf/  
lastmod: "2024-05-20"  
description: 이 주제는 Aspose.PDF가 HTML 및 MHTML 형식을 PDF 파일로 변환하는 방법을 보여줍니다.  
sitemap:  
changefreq: "monthly"  
priority: 0.8  
---

## 개요

이 글은 PHP를 사용하여 HTML을 PDF로 변환하는 방법을 설명합니다. 코드는 매우 간단하며, HTML을 Document 클래스에 로드하고 출력 PDF로 저장하기만 하면 됩니다. Java에서 MHTML을 PDF로 변환하는 것도 유사합니다. 다음 주제를 포함합니다.

## Java HTML에서 PDF로 변환 라이브러리

**Aspose.PDF for PHP via Java**는 기존의 HTML 문서를 PDF로 원활하게 변환할 수 있는 PDF 조작 API입니다. HTML을 PDF로 변환하는 과정은 유연하게 맞춤화할 수 있습니다.

## HTML을 PDF로 변환하기

다음 Java 코드 샘플은 HTML 문서를 PDF로 변환하는 방법을 보여줍니다.

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) 클래스의 인스턴스를 생성합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 객체를 초기화합니다.
1. [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) 메서드를 호출하여 출력 PDF 문서를 저장합니다.

```php
    // HTML 파일에 대한 로드 옵션을 지정하기 위해 HtmlLoadOptions의 인스턴스를 생성합니다
    $loadOption = new HtmlLoadOptions();

    // 새로운 Document 객체를 생성하고 HTML 파일을 로드합니다
    $document = new Document($inputFile, $loadOption);

    // 문서를 PDF 파일로 저장합니다
    $document->save($outputFile);
```

## HTML에서 PDF로의 고급 변환

HTML 변환 엔진에는 변환 프로세스를 제어할 수 있는 여러 옵션이 있습니다.

### 미디어 쿼리 지원

1. HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)를 생성합니다.
1. [인쇄 또는 화면](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-) 모드를 설정합니다.

1. [문서 객체](https://reference.aspose.com/page/java/com.aspose.page/document) 초기화.
1. 출력 PDF 문서 저장.

미디어 쿼리는 다양한 장치에 맞춘 스타일 시트를 제공하기 위한 인기 있는 기술입니다. [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType) 클래스를 사용하여 장치 유형을 설정할 수 있습니다.

```php

    // HTML 파일의 로드 옵션을 지정하기 위해 HtmlLoadOptions의 인스턴스를 생성합니다.
    $htmlMediaType = new HtmlMediaType();

    // 인쇄 또는 화면 모드를 설정합니다.
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // 새 문서 객체를 생성하고 HTML 파일을 로드합니다.
    $document = new Document($inputFile, $loadOption);

    // 문서를 PDF 파일로 저장합니다.
    $document->save($outputFile);
```

### 글꼴 포함 활성화 (비활성화)

1. 새로운 Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) 추가.
1. 글꼴 포함 비활성화.
1. 새 문서 저장.

HTML 페이지는 종종 글꼴을 사용합니다 (예:
 로컬 폴더, Google Fonts 등에서 글꼴을 가져옵니다. 우리는 또한 [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-) 속성을 사용하여 문서에 글꼴을 포함하는 것을 제어할 수 있습니다.

```php

    // HTML 파일에 대한 로드 옵션을 지정하기 위해 HtmlLoadOptions 인스턴스를 생성합니다.
    $loadOption = new HtmlLoadOptions();

    // 글꼴 포함을 비활성화합니다.
    $loadOption->setEmbedFonts(true);

    // 새 Document 객체를 생성하고 HTML 파일을 로드합니다.
    $document = new Document($inputFile, $loadOption);

    // 문서를 PDF 파일로 저장합니다.
    $document->save($outputFile);
```

## MHTML을 PDF로 변환

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>은 MIME HTML의 약자로, 일반적으로 외부 링크로 표현되는 리소스(이미지, Flash 애니메이션, Java 애플릿, 오디오 파일 등)를 HTML 코드와 함께 하나의 파일로 결합하는 데 사용되는 웹 페이지 아카이브 형식입니다. MHTML 파일의 내용은 MIME 유형 multipart/related를 사용하여 HTML 이메일 메시지처럼 인코딩됩니다.

다음 코드 스니펫은 MHTML 파일을 Java로 PDF 형식으로 변환하는 방법을 보여줍니다:

```php

    // MhtLoadOptions 클래스의 새 인스턴스를 생성합니다.
    $loadOption = new MhtLoadOptions();

    // Document 클래스의 새 인스턴스를 생성하고 MHTML 파일을 로드합니다.
    $document = new Document($inputFile, $loadOption);

    // 문서를 PDF 파일로 저장합니다.
    $document->save($outputFile);
```