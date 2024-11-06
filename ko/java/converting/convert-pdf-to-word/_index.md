---
title: Java에서 PDF를 Microsoft Word 문서로 변환
linktitle: PDF를 Word로 변환
type: docs
weight: 10
url: ko/java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for Java를 사용하여 PDF 파일을 DOC 및 DOCX 형식으로 쉽게 변환하고 완벽하게 제어합니다. PDF를 Microsoft Word 문서로 변환하는 방법에 대해 자세히 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 개요

이 문서에서는 Java를 사용하여 PDF를 Word로 변환하는 방법을 설명합니다. 코드는 매우 간단하며, PDF를 Document 클래스에 로드하고 출력 Microsoft Word DOC 또는 DOCX 형식으로 저장하기만 하면 됩니다. 다음 주제를 다룹니다.

- [Java PDF를 Word로 변환](#convert-pdf-to-doc)
- [Java PDF를 DOC로 변환](#convert-pdf-to-doc)
- [Java PDF를 DOCX로 변환](#convert-pdf-to-docx)
- [Java PDF를 Word로 변환](#convert-pdf-to-docx)
- [Java PDF를 DOC로 변환](#convert-pdf-to-doc)
- [Java PDF를 DOCX로 변환](#convert-pdf-to-docx)
- [Java PDF 파일을 Word DOC](#convert-pdf-to-doc) 또는 [Word DOCX](#convert-pdf-to-docx)로 변환하는 방법

- [Java PDF를 Word 문서로 프로그래밍 방식으로 저장, 생성 또는 생성하는 라이브러리, API 또는 코드](#convert-pdf-to-docx)

## PDF를 DOC로 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하는 것으로, 콘텐츠를 쉽게 조작할 수 있게 해줍니다. Aspose.PDF for Java를 사용하면 PDF 파일을 DOC로 변환할 수 있습니다.

**Aspose.PDF for Java**는 처음부터 PDF 문서를 생성할 수 있으며, 기존 PDF 문서를 업데이트, 편집 및 조작하는 데 훌륭한 도구입니다. 중요한 기능 중 하나는 페이지와 전체 PDF 문서를 이미지로 변환할 수 있는 능력입니다. 또 다른 인기 있는 기능은 PDF를 Microsoft Word DOC로 변환하는 것으로, 콘텐츠를 쉽게 조작할 수 있게 해줍니다. (대부분의 사용자는 PDF 문서를 편집할 수 없지만 Microsoft Word에서 표, 텍스트 및 이미지를 쉽게 작업할 수 있습니다.)

간단하고 이해하기 쉽게 하기 위해, Aspose.PDF for Java는 소스 PDF 파일을 DOC 파일로 변환하는 두 줄의 코드를 제공합니다.

다음 Java 코드 스니펫은 PDF 파일을 DOC 형식으로 변환하는 과정을 보여줍니다.

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 객체의 인스턴스를 생성합니다.
2. **Document.save()** 메서드를 호출하여 **SaveFormat.Doc** 형식으로 저장합니다.

```java
public static void convertPDFtoWord() {
    // 소스 PDF 문서를 엽니다
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // 파일을 MS 문서 형식으로 저장합니다
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## DocSaveOptions 클래스 사용하기

[DocSaveOptions 클래스](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions)는 PDF 파일을 DOC 형식으로 변환하는 과정을 개선하는 다양한 속성을 제공합니다. 이러한 속성 중 Mode는 PDF 콘텐츠에 대한 인식 모드를 지정할 수 있게 해줍니다. 이 속성에 대해 RecognitionMode 열거형의 값을 지정할 수 있습니다. 이러한 값 각각은 특정한 장점과 제한 사항을 가지고 있습니다:

- [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) 모드는 빠르고 PDF 파일의 원래 모양을 유지하는 데 좋지만, 결과 문서의 편집 가능성은 제한될 수 있습니다.
 원본 PDF의 시각적으로 그룹화된 텍스트 블록은 출력 문서에서 텍스트 박스로 변환됩니다. 이는 원본과 최대한 유사하게 만들어 출력 문서가 보기 좋도록 하지만, 전적으로 텍스트 박스로만 구성되어 Microsoft Word에서 편집하기 어려울 수 있습니다.

- Flow는 전체 인식 모드로, 엔진이 그룹화 및 다단계 분석을 수행하여 저자의 의도에 따라 원본 문서를 복원하면서 쉽게 편집할 수 있는 문서를 생성합니다. 제한 사항은 출력 문서가 원본과 다르게 보일 수 있다는 점입니다.

- RelativeHorizontalProximity 속성은 텍스트 요소 간의 상대적 근접성을 제어하는 데 사용되며, 거리는 글꼴 크기에 따라 표준화됩니다. 더 큰 글꼴은 음절 사이의 거리가 더 크더라도 단일 전체로 간주될 수 있습니다. 이는 글꼴 크기의 백분율로 지정됩니다. 예를 들어, 1 = 100%를 의미합니다. 이는 12pt의 두 문자가 12pt 떨어진 곳에 배치된 경우 근접함을 의미합니다.

- RecognitionBullets는 변환 중에 불릿 인식을 활성화하는 데 사용됩니다.
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // 출력 형식을 DOC로 지정
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // 인식 모드를 Flow로 설정
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // 수평 근접성을 2.5로 설정
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // 변환 과정에서 불렛을 인식하도록 설정
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**PDF를 DOC로 온라인 변환 시도하기**

Aspose.PDF for Java는 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc)라는 무료 온라인 애플리케이션을 제공하며, 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## PDF를 DOCX로 변환

DocFormat 열거형은 Word 문서의 출력 형식으로 DOCX를 선택할 수 있는 옵션도 제공합니다. 소스 PDF 파일을 DOCX 형식으로 렌더링하려면 아래에 지정된 코드 스니펫을 사용하세요.

## PDF를 DOCX로 변환하는 방법

다음 Java 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 과정을 보여줍니다.

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 객체의 인스턴스를 생성합니다.
2. **Document.save()** 메서드를 호출하여 **SaveFormat.DocX** 형식으로 저장합니다.

```java
public static void convertPDFtoWord_DOCX_Format() {
    // 소스 PDF 문서를 엽니다
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // 결과 DOC 파일을 저장합니다
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

[DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) 클래스는 결과 문서의 형식을 DOC 또는 DOCX로 지정할 수 있는 Format이라는 속성을 가지고 있습니다.
 PDF 파일을 DOCX 형식으로 변환하려면 DocSaveOptions.DocFormat 열거형에서 Docx 값을 전달하십시오.

다음 코드 스니펫을 참고하여 Java로 PDF 파일을 DOCX 형식으로 변환하는 기능을 제공합니다.

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // 소스 PDF 문서를 엽니다
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // DocSaveOptions 객체를 인스턴스화합니다
    DocSaveOptions saveOptions = new DocSaveOptions();
    // 출력 형식을 DOCX로 지정합니다
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // 다른 DocSaveOptions 매개변수를 설정합니다
    // ....

    // 문서를 docx 형식으로 저장합니다
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**PDF를 DOCX로 온라인 변환 시도하기**

Aspose.PDF for Java는 ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)라는 무료 온라인 애플리케이션을 제공하며, 이를 통해 기능과 품질을 조사해 볼 수 있습니다.
[![Aspose.PDF 변환 PDF에서 DOCX 무료 앱](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}