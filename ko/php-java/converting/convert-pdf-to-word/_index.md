---
title: PDF를 Microsoft Word로 변환하기
linktitle: PDF를 Word로 변환하기
type: docs
weight: 10
url: ko/php-java/convert-pdf-to-word/
lastmod: "2024-05-20"
description: Aspose.PDF for PHP를 사용하여 PDF 파일을 DOC 및 DOCX 형식으로 쉽게 변환하고 완벽한 제어를 할 수 있습니다. PDF를 Microsoft Word 문서로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 개요

이 문서는 PHP를 사용하여 PDF를 Word로 변환하는 방법을 설명합니다. 코드는 매우 간단하며, PDF를 Document 클래스에 로드하고 출력 Microsoft Word DOC 또는 DOCX 형식으로 저장하면 됩니다. 다음 주제를 다룹니다.

- [PHP PDF를 Word로](#convert-pdf-to-doc)
- [PHP PDF를 DOC로](#convert-pdf-to-doc)
- [PHP PDF를 DOCX로](#convert-pdf-to-docx)
- [PHP PDF를 Word로 변환](#convert-pdf-to-docx)
- [PHP PDF를 DOC로 변환](#convert-pdf-to-doc)
- [PHP PDF를 DOCX로 변환](#convert-pdf-to-docx)
- [PHP PDF 파일을 Word DOC 또는 Word DOCX로 변환하는 방법](#convert-pdf-to-doc)

- [PHP PDF를 Word 문서로 프로그램적으로 저장, 생성 또는 작성하기 위한 라이브러리, API 또는 코드](#convert-pdf-to-docx)

## PDF를 DOC로 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하는 것으로, 콘텐츠를 쉽게 조작할 수 있게 해줍니다. Aspose.PDF for PHP를 사용하면 PDF 파일을 DOC로 변환할 수 있습니다.

**Aspose.PDF for PHP**는 PDF 문서를 처음부터 생성할 수 있으며, 기존 PDF 문서를 업데이트, 편집 및 조작하는 데 탁월한 도구입니다. 중요한 기능 중 하나는 페이지와 전체 PDF 문서를 이미지로 변환할 수 있는 능력입니다. 또 다른 인기 있는 기능은 PDF를 Microsoft Word DOC로 변환하는 것으로, 콘텐츠를 쉽게 조작할 수 있게 해줍니다. (대부분의 사용자는 PDF 문서를 편집할 수 없지만 Microsoft Word에서는 표, 텍스트 및 이미지를 쉽게 작업할 수 있습니다.)

간단하고 이해하기 쉽게 하기 위해, Aspose.PDF for PHP는 소스 PDF 파일을 DOC 파일로 변환하는 두 줄의 코드를 제공합니다.

다음 Java 코드 스니펫은 PDF 파일을 DOC 형식으로 변환하는 과정을 보여줍니다.

1. 소스 PDF 문서를 사용하여 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 객체의 인스턴스를 만듭니다.

 2. **Document.save()** 메서드를 호출하여 **SaveFormat.Doc** 형식으로 저장합니다.

```php
// PDF 문서 불러오기
$document = new Document($inputFile);

// 새로운 DocSaveOptions 객체 생성
$saveOption = new DocSaveOptions();

// 출력 형식을 DOC로 설정
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// 문서를 DOC로 저장
$document->save($outputFile, $saveOption);
```

## DocSaveOptions 클래스 사용하기

[DocSaveOptions 클래스](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions)는 PDF 파일을 DOC 형식으로 변환하는 과정을 개선하는 다양한 속성을 제공합니다. 이러한 속성 중 Mode는 PDF 콘텐츠에 대한 인식 모드를 지정할 수 있게 해줍니다. 이 속성에 대해 RecognitionMode 열거형의 값을 지정할 수 있습니다. 각 값은 특정한 장점과 제한점을 가지고 있습니다:

- [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) 모드는 빠르고 PDF 파일의 원래 모양을 유지하는 데 좋지만, 결과 문서의 편집 가능성은 제한될 수 있습니다.
 원본 PDF의 시각적으로 그룹화된 모든 텍스트 블록은 출력 문서에서 텍스트 상자로 변환됩니다. 이렇게 하면 출력 문서가 원본과 최대한 유사하게 보이도록 하여 보기 좋지만, 텍스트 상자만으로 구성되어 Microsoft Word에서 편집하기 어려울 수 있습니다.

- Flow는 전체 인식 모드로, 엔진이 그룹화 및 다단계 분석을 수행하여 작성자의 의도에 따라 원본 문서를 복원하면서 쉽게 편집 가능한 문서를 생성합니다. 제한 사항은 출력 문서가 원본과 다르게 보일 수 있다는 것입니다.

- RelativeHorizontalProximity 속성은 텍스트 요소 간의 상대적 근접성을 제어하는 데 사용되며, 거리는 글꼴 크기로 정규화된다는 것을 의미합니다. 글꼴이 클수록 음절 사이의 거리가 더 멀어질 수 있으며 여전히 하나의 전체로 간주됩니다. 이는 글꼴 크기의 백분율로 지정되며, 예를 들어 1 = 100%를 의미합니다. 이는 12pt의 두 문자가 12pt 간격으로 배치되면 서로 근접하다는 것을 의미합니다.

- RecognitionBullets는 변환 중에 글머리 기호 인식을 켜는 데 사용됩니다.
```php
// PDF 문서 로드
$document = new Document($inputFile);

// 새로운 DocSaveOptions 객체 생성
$saveOption = new DocSaveOptions();

// 인식 모드를 EnhancedFlow로 설정
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// 출력 형식을 DOC로 설정
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// 인식 모드를 Flow로 설정
saveOptions->setMode(DocSaveOptions_RecognitionMode::$Flow);

// 수평 근접성을 2.5로 설정
saveOptions->setRelativeHorizontalProximity(2.5f);

// 변환 과정에서 글머리 기호를 인식하도록 값 활성화
saveOptions->setRecognizeBullets(true);

// 문서를 DOCX로 저장
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**PDF를 DOC로 온라인 변환 시도**

Aspose.PDF for PHP는 온라인 무료 애플리케이션 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc)를 제공하여 기능과 품질을 조사해 볼 수 있습니다.


[![PDF를 DOC로 변환](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOCX로 변환

DocFormat 열거형은 Word 문서의 출력 형식으로 DOCX를 선택하는 옵션도 제공합니다. 소스 PDF 파일을 DOCX 형식으로 렌더링하려면 아래에 지정된 코드 스니펫을 사용하십시오.

## PDF를 DOCX로 변환하는 방법

다음 Java 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 과정을 보여줍니다.

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 객체의 인스턴스를 만듭니다.
2. **Document.save()** 메서드를 호출하여 **SaveFormat.DocX** 형식으로 저장합니다.

```php
    // PDF 문서를 로드합니다.
    $document = new Document($inputFile);
    
    // 문서를 DOCX로 저장합니다.
    $document->save($outputFile, SaveFormat::$DocX);
```

[DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) 클래스에는 결과 문서의 형식을 지정할 수 있는 Format이라는 속성이 있으며, 이는 DOC 또는 DOCX입니다.
 PDF 파일을 DOCX 형식으로 변환하려면 DocSaveOptions.DocFormat 열거형에서 Docx 값을 전달하십시오.

다음의 코드 스니펫을 확인해 주세요. 이 코드는 Java로 PDF 파일을 DOCX 형식으로 변환하는 기능을 제공합니다.

```php
// PDF 문서 불러오기
$document = new Document($inputFile);

// 새로운 DocSaveOptions 객체 생성
$saveOption = new DocSaveOptions();

// 인식 모드를 EnhancedFlow로 설정
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// 출력 형식을 DOCX로 설정
$saveOption->setFormat(DocSaveOptions_DocFormat::$DocX);

// 문서를 DOCX로 저장
$document->save($outputFile, $saveOption);
```

{{% alert color="warning" %}}
**온라인에서 PDF를 DOCX로 변환 시도하기**

Aspose.PDF for PHP는 ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)라는 무료 온라인 애플리케이션을 제공하며, 기능과 품질을 조사해 볼 수 있습니다.


[![Aspose.PDF Convertion PDF to DOCX Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)
{{% /alert %}}
