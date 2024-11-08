---
title: PDF 파일을 HTML 형식으로 변환
linktitle: PDF 파일을 HTML 형식으로 변환
type: docs
weight: 50
url: /ko/php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: 이 주제는 Aspose.PDF가 PHP 라이브러리를 사용하여 PDF 파일을 HTML 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF for PHP는 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하는 많은 기능을 제공합니다. 이 문서에서는 PDF 파일을 HTML 형식으로 변환하고 PDF 파일의 이미지를 특정 폴더에 저장하는 방법에 대해 설명합니다.

{{% alert color="success" %}}
**PDF를 HTML로 온라인 변환 시도**

Aspose.PDF for PHP는 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 HTML로 무료 앱](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

큰 PDF 파일을 여러 페이지로 HTML 형식으로 변환할 때, 출력이 단일 HTML 페이지로 나타납니다. 이는 매우 길어질 수 있습니다. 페이지 크기를 제어하려면 PDF를 HTML로 변환하는 동안 출력을 여러 페이지로 나누는 것이 가능합니다.

## PDF 페이지를 HTML로 변환

Aspose.PDF for PHP는 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하는 많은 기능을 제공합니다. 이 문서는 PDF 파일을 HTML 형식으로 변환하고 PDF 파일의 이미지를 특정 폴더에 저장하는 방법에 대해 설명합니다.

다음 코드 스니펫은 PDF를 HTML로 변환할 때 사용할 수 있는 모든 가능한 옵션을 보여줍니다.

```php
// 새 Document 객체를 만들고 입력 PDF 파일을 로드합니다
$document = new Document($inputFile);

// 문서를 HTML로 저장하기 위한 새 HtmlSaveOptions 객체를 만듭니다
$saveOption = new HtmlSaveOptions();

// 지정된 저장 옵션을 사용하여 문서를 HTML로 저장합니다
$document->save($outputFile, $saveOption);
```

## PDF를 HTML로 변환 - 다중 페이지 HTML로 출력 분할

Aspose.PDF for PHP는 PDF 문서를 HTML을 포함한 다양한 출력 형식으로 변환하는 기능을 지원합니다. 그러나 여러 페이지로 구성된 큰 PDF 파일을 변환할 때 개별 PDF 페이지를 별도의 HTML 파일로 저장해야 할 수 있습니다.

여러 페이지로 구성된 큰 PDF 파일을 HTML 형식으로 변환할 때 출력은 단일 HTML 페이지로 나타납니다. 그 결과 매우 길어질 수 있습니다. 페이지 크기를 제어하기 위해 PDF를 HTML로 변환하는 동안 출력을 여러 페이지로 나누는 것이 가능합니다. 다음 코드 스니펫을 사용해 보세요.

```php
// 새로운 Document 객체를 생성하고 입력 PDF 파일을 로드합니다.
$document = new Document($inputFile);

// 문서를 HTML로 저장하기 위한 새로운 HtmlSaveOptions 객체를 생성합니다.
$saveOption = new HtmlSaveOptions();

// 출력을 여러 페이지로 나누도록 지정합니다.
$saveOption->setSplitIntoPages(true);

// 지정된 저장 옵션을 사용하여 문서를 HTML로 저장합니다.
$document->save($outputFile, $saveOption);
```

## PDF를 HTML로 변환 - 이미지를 SVG 형식으로 저장 피하기


PDF를 HTML로 변환할 때 이미지를 저장하는 기본 출력 형식은 SVG입니다. 변환 중에 PDF의 일부 이미지는 SVG 벡터 이미지로 변환됩니다. 이는 느릴 수 있습니다. 대신 이미지를 PNG로 변환할 수 있습니다. 이를 허용하려면 Aspose.PDF는 벡터에 SVG를 사용하거나 PNG를 생성하는 옵션을 제공합니다.

PDF 파일을 HTML 형식으로 변환할 때 이미지의 SVG 형식 렌더링을 완전히 제거하려면 다음 코드 스니펫을 사용해 보십시오.

```php
// 새로운 Document 객체를 생성하고 입력 PDF 파일을 로드합니다.
$document = new Document($inputFile);

// 문서를 HTML로 저장하기 위한 새로운 HtmlSaveOptions 객체를 생성합니다.
$saveOption = new HtmlSaveOptions();

// PDF를 HTML로 변환하는 동안 SVG 이미지가 저장되는 폴더를 지정합니다.
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// 지정된 저장 옵션을 사용하여 문서를 HTML로 저장합니다.
$document->save($outputFile, $saveOption);
```

## 변환 중 SVG 이미지 압축하기

PDF를 HTML로 변환하는 동안 SVG 이미지를 압축하려면 다음 코드를 사용해 보십시오.

```php
// 새 Document 객체를 생성하고 입력 PDF 파일을 로드합니다.
$document = new Document($inputFile);

// 문서를 HTML로 저장하기 위한 새로운 HtmlSaveOptions 객체를 생성합니다.
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// 지정된 저장 옵션을 사용하여 문서를 HTML로 저장합니다.
$document->save($outputFile, $saveOptions);
```

## PDF를 HTML로 변환 - 이미지 폴더 지정

기본적으로, PDF 파일을 HTML로 변환할 때, PDF 내의 이미지는 출력 HTML이 생성되는 동일한 디렉토리에 생성된 별도의 폴더에 저장됩니다. 그러나 때때로 HTML 파일을 생성할 때 이미지를 저장할 다른 폴더를 지정해야 할 필요가 있습니다. 이를 위해 [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions)를 도입했습니다.

[setSpecialFolderForAllImages 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-)는 이미지를 저장할 대상 폴더를 지정하는 데 사용됩니다.


```php
// 새로운 Document 객체를 생성하고 입력 PDF 파일을 로드합니다
$document = new Document($inputFile);

// 문서를 HTML로 저장하기 위한 HtmlSaveOptions 객체를 생성합니다
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// 지정된 저장 옵션을 사용하여 문서를 HTML로 저장합니다
$document->save($outputFile, $saveOptions);
```

## 투명 텍스트 렌더링

소스/입력 PDF 파일에 전경 이미지에 의해 가려진 투명 텍스트가 포함된 경우, 텍스트 렌더링 문제가 발생할 수 있습니다. 이러한 시나리오에 대응하기 위해 SaveShadowedTextsAsTransparentTexts 및 SaveTransparentTexts 속성을 사용할 수 있습니다.

```php
// 새로운 Document 객체를 생성하고 입력 PDF 파일을 로드합니다
$document = new Document($inputFile);

// 문서를 HTML로 저장하기 위한 HtmlSaveOptions 객체를 생성합니다
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// 지정된 저장 옵션을 사용하여 문서를 HTML로 저장합니다
$document->save($outputFile, $saveOptions);
```


## PDF 문서 레이어 렌더링

PDF를 HTML로 변환하는 동안 PDF 문서 레이어를 개별 레이어 유형 요소로 렌더링할 수 있습니다:

```php
// 새로운 Document 객체를 생성하고 입력 PDF 파일을 로드합니다
$document = new Document($inputFile);

// 문서를 HTML로 저장하기 위한 새로운 HtmlSaveOptions 객체를 생성합니다
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// 지정된 저장 옵션을 사용하여 문서를 HTML로 저장합니다
$document->save($outputFile, $saveOptions);
```

PDF를 HTML로 변환하는 것은 Aspose.PDF의 가장 인기 있는 기능 중 하나로, 다양한 플랫폼에서 PDF 파일의 내용을 PDF 문서 뷰어를 사용하지 않고도 볼 수 있게 해줍니다. 출력 HTML은 WWW 표준에 부합하며, 모든 웹 브라우저에서 쉽게 표시될 수 있습니다. 이 기능을 사용하여 PDF 파일은 간단한 웹 브라우저를 사용하여 손에 들고 다니는 장치에서 볼 수 있습니다. 이는 PDF 뷰잉 애플리케이션을 설치할 필요가 없기 때문입니다.