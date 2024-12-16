---
title: .NET에서 PDF를 마이크로소프트 워드 문서로 변환
linktitle: PDF를 워드로 변환
type: docs
weight: 10
url: /ko/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Aspose.PDF for .NET을 사용하여 C# 코드로 PDF를 마이크로소프트 워드 형식으로 변환하는 방법을 배우고 PDF를 DOC(DOCX)로 변환을 조정합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 개요

이 문서는 **C#을 사용하여 PDF를 마이크로소프트 워드 문서로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **DOC**

- [C# PDF를 DOC로](#csharp-pdf-to-doc)
- [C# PDF를 DOC로 변환](#csharp-pdf-to-doc)
- [C# PDF 파일을 DOC로 변환하는 방법](#csharp-pdf-to-doc)

_형식_: **DOCX**

- [C# PDF를 DOCX로](#csharp-pdf-to-docx)
- [C# PDF를 DOCX로 변환](#csharp-pdf-to-docx)
- [C# PDF 파일을 DOCX로 변환하는 방법](#csharp-pdf-to-docx)

_형식_: **Word**

- [C# PDF를 워드로](#csharp-pdf-to-docx)
- [C# PDF를 워드로 변환](#csharp-pdf-to-doc)
- [C# PDF 파일을 워드로 변환하는 방법](#csharp-pdf-to-docx)

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 함께 작동합니다.
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

## PDF에서 DOC 및 DOCX로 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC으로 변환하는 것으로, 콘텐츠 관리를 더욱 수월하게 만듭니다. **Aspose.PDF for .NET**은 PDF 파일을 빠르고 효율적으로 DOC 및 DOCX 형식으로 변환할 수 있습니다.

## PDF를 DOC (Microsoft Word 97-2003) 파일로 변환

PDF 파일을 DOC 형식으로 쉽고 완전히 제어하여 변환하세요. Aspose.PDF for .NET은 유연하며 다양한 변환을 지원합니다. 예를 들어, PDF 문서의 페이지를 이미지로 변환하는 것은 매우 인기 있는 기능입니다.

많은 고객들이 PDF에서 DOC로의 변환을 요청했습니다: PDF 파일을 Microsoft Word 문서로 변환하는 것입니다. 고객들은 PDF 파일을 쉽게 편집할 수 없기 때문에 이를 원합니다. 반면, Word 문서는 편집할 수 있습니다. 일부 회사는 사용자가 PDF로 시작된 파일에서 텍스트, 테이블 및 이미지를 조작할 수 있기를 원합니다.

일을 간단하고 이해하기 쉽게 유지하는 전통을 살리면서, Aspose.PDF for .NET은 소스 PDF 파일을 DOC 파일로 변환하는 데 두 줄의 코드만으로 변환할 수 있게 해줍니다.
간단하고 이해하기 쉽게 만드는 전통을 이어가며, Aspose.PDF for .NET은 소스 PDF 파일을 DOC 파일로 변환할 수 있게 해주는 두 줄의 코드를 제공합니다.

다음 C# 코드 스니펫은 PDF 파일을 DOC 형식으로 변환하는 방법을 보여줍니다.

<a name="csharp-pdf-to-doc"><strong>단계: C#에서 PDF를 DOC로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. **Document.Save()** 메서드를 호출하여 **SaveFormat.Doc** 형식으로 저장합니다.

```csharp
public static void ConvertPDFtoWord()
{
    // 소스 PDF 문서를 엽니다
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // 파일을 MS 문서 형식으로 저장합니다
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### DocSaveOptions 클래스 사용하기

[`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) 클래스는 PDF 파일을 DOC 형식으로 변환할 때 여러 속성을 제공합니다.
[`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) 클래스는 PDF 파일을 DOC 형식으로 변환할 때 개선된 여러 속성을 제공합니다.

- [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) 모드는 빠르며 PDF 파일의 원래 모양을 보존하는데 좋지만, 결과 문서의 편집성이 제한될 수 있습니다. 원본 PDF의 시각적으로 그룹화된 텍스트 블록이 출력 문서에서 텍스트 박스로 변환됩니다. 이는 원본과 최대한 유사하게 하여 출력 문서가 좋아 보이도록 하지만, 전체적으로 텍스트 박스로 구성되어 있어 Microsoft Word에서 편집하기가 상당히 어려울 수 있습니다.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode)는 엔진이 그룹화 및 다중 레벨 분석을 수행하여 저자의 의도에 따라 원본 문서를 복원하면서 쉽게 편집할 수 있는 문서를 생성하는 전체 인식 모드입니다.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) 전체 인식 모드로, 엔진이 그룹화 및 다중 수준 분석을 수행하여 원본 문서를 저자의 의도대로 복원하면서 쉽게 편집할 수 있는 문서를 생성합니다.

- [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) 속성은 텍스트 요소 간의 상대적 근접성을 제어하는 데 사용됩니다. 이는 거리가 글꼴 크기에 의해 정규화된다는 것을 의미합니다. 큰 글꼴은 음절 사이의 더 큰 공간을 가질 수 있지만 여전히 하나의 전체로 간주될 수 있습니다. 예를 들어, 1 = 100%로 지정됩니다. 즉, 12pt의 두 문자가 12pt 떨어져 있으면 근접한 것으로 간주됩니다.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) 변환 중에 글머리 기호 인식을 켜는 데 사용됩니다.

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // Flow로 인식 모드 설정
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // 수평 근접성을 2.5로 설정
        RelativeHorizontalProximity = 2.5f,
        // 변환 과정에서 글머리 기호 인식을 활성화
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**온라인으로 PDF를 DOC로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)을 제공합니다. 여기에서 기능 및 품질을 조사해 볼 수 있습니다.

[![PDF를 DOC로 변환](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOCX(Microsoft Word 2007-2021) 파일로 변환

Aspose.PDF for .NET API는 C# 및 모든 .NET 언어를 사용하여 PDF 문서를 DOCX로 읽고 변환할 수 있습니다. DOCX는 Microsoft Word 문서의 형식으로, 구조가 일반 이진에서 XML과 이진 파일의 조합으로 변경되었습니다. Docx 파일은 Word 2007 이상 버전에서 열 수 있지만, DOC 파일 확장자를 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

다음 C# 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 방법을 보여줍니다.

<a name="csharp-pdf-to-docx"><strong>단계: C#에서 PDF를 DOCX로 변환</strong></a>

1.
1.
2. **SaveFormat.DocX** 형식으로 저장하려면 **Document.Save()** 메서드를 호출하세요.

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // PDF 원본 문서 열기
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // 결과 DOC 파일 저장
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### PDF를 DOCX로 변환하면서 향상된 모드 사용하기

PDF에서 DOCX로 변환할 때 더 좋은 결과를 얻으려면 `EnhancedFlow` 모드를 사용할 수 있습니다.
Flow와 Enhanced Flow의 주요 차이점은 테이블(테두리가 있는 테이블과 테두리가 없는 테이블 모두)이 배경에 그림이 있는 텍스트로 인식되지 않고 실제 테이블로 인식된다는 것입니다.
또한 번호가 매겨진 목록과 기타 여러 작은 사항들도 인식됩니다.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // PDF 원본 문서 열기
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // DocSaveOptions 객체 인스턴스화
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // 출력 형식으로 DOCX 지정
        Format = DocSaveOptions.DocFormat.DocX
        // 다른 DocSaveOptions 매개변수 설정
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // docx 형식으로 문서 저장
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**온라인으로 PDF를 DOCX로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 참조

이 글은 다음과 같은 주제도 다룹니다. 코드는 위와 동일합니다.

_형식_: **Word**

- [C# PDF를 Word로 코드](#csharp-pdf-to-docx)
- [C# PDF를 Word로 API](#csharp-pdf-to-docx)
- [C# 프로그래밍 방식으로 PDF를 Word로](#csharp-pdf-to-docx)
- [C# PDF를 Word 라이브러리로](#csharp-pdf-to-docx)
- [C# PDF를 Word로 저장](#csharp-pdf-to-docx)
- [C# PDF에서 Word 생성](#csharp-pdf-to-docx)
- [C# PDF에서 Word 생성](#csharp-pdf-to-docx)
- [C# PDF를 Word 변환기로](#csharp-pdf-to-docx)

_형식_: **DOC**

- [C# PDF를 DOC 코드로](#csharp-pdf-to-doc)
- [C# PDF를 DOC API로](#csharp-pdf-to-doc)
- [C# PDF를 DOC로 변환 API](#csharp-pdf-to-doc)
- [C# PDF를 DOC로 프로그래밍적으로 변환](#csharp-pdf-to-doc)
- [C# PDF를 DOC로 변환 라이브러리](#csharp-pdf-to-doc)
- [C# PDF를 DOC로 저장](#csharp-pdf-to-doc)
- [C# PDF에서 DOC 생성](#csharp-pdf-to-doc)
- [C# PDF에서 DOC 생성](#csharp-pdf-to-doc)
- [C# PDF를 DOC로 변환기](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [C# PDF를 DOCX로 코드](#csharp-pdf-to-docx)
- [C# PDF를 DOCX로 변환 API](#csharp-pdf-to-docx)
- [C# PDF를 DOCX로 프로그래밍적으로 변환](#csharp-pdf-to-docx)
- [C# PDF를 DOCX로 변환 라이브러리](#csharp-pdf-to-docx)
- [C# PDF를 DOCX로 저장](#csharp-pdf-to-docx)
- [C# PDF에서 DOCX 생성](#csharp-pdf-to-docx)
- [C# PDF에서 DOCX 생성](#csharp-pdf-to-docx)
- [C# PDF를 DOCX로 변환기](#csharp-pdf-to-docx)

