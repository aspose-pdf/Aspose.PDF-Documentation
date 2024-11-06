---
title: Aspose.PDF DOM API의 기초
linktitle: DOM API의 기초
type: docs
weight: 120
url: ko/cpp/basics-of-dom-api/
description: Aspose.PDF for C++는 또한 객체의 관점에서 PDF 문서의 구조를 나타내기 위해 DOM의 개념을 사용합니다. 여기서 이 구조에 대한 설명을 읽을 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 소개

문서 객체 모델(DOM)은 구조화된 문서를 객체 지향 모델로 표현하는 형식입니다. DOM은 플랫폼 및 언어에 구애받지 않는 방식으로 구조화된 문서를 표현하기 위한 공식 월드 와이드 웹 컨소시엄(W3C) 표준입니다.

간단히 말해, DOM은 일부 문서의 구조를 나타내는 객체의 트리입니다. Aspose.PDF for C++는 또한 객체의 관점에서 PDF 문서의 구조를 나타내기 위해 DOM의 아이디어를 사용합니다. 그러나 DOM의 측면(예: 요소)은 사용 중인 프로그래밍 언어의 구문 내에서 조작됩니다. DOM의 공개 인터페이스는 응용 프로그램 프로그래밍 인터페이스(API)에서 지정됩니다.

### PDF 문서 소개

Portable Document Format(PDF)는 문서 교환을 위한 개방형 표준입니다. PDF 문서는 텍스트와 이진 데이터의 조합입니다. 텍스트 편집기에서 열면 문서의 구조와 내용을 정의하는 원시 객체를 볼 수 있습니다.

PDF 파일의 논리적 구조는 계층적이며, 보기 응용 프로그램이 문서의 페이지와 그 내용을 그리는 순서를 결정합니다. PDF는 객체, 파일 구조, 문서 구조 및 콘텐츠 스트림의 네 가지 구성 요소로 구성됩니다.

### PDF 문서 구조

PDF 파일의 구조는 계층적이므로 Aspose.PDF for C++도 동일한 방식으로 요소에 접근합니다. 다음 계층 구조는 PDF 문서가 논리적으로 구성되는 방법과 Aspose.PDF for C++ DOM API가 이를 구성하는 방법을 보여줍니다.

![PDF Document Structure](../images/structure.png)

### PDF 문서 요소에 접근하기

Document 객체는 객체 모델의 루트 레벨에 있습니다. Aspose.PDF for C++ DOM API를 사용하면 Document 객체를 생성한 후 계층 구조의 다른 모든 객체에 접근할 수 있습니다. Pages와 같은 컬렉션이나 Page와 같은 개별 요소에 접근할 수 있습니다. DOM API는 아래와 같이 PDF 문서를 조작하기 위한 단일 진입점과 종료점을 제공합니다:

- PDF 문서 열기
- DOM 스타일로 PDF 문서 구조에 접근
- PDF 문서의 데이터 업데이트
- PDF 문서 검증
- 다양한 형식으로 PDF 문서 내보내기
- 마지막으로, 업데이트된 PDF 문서 저장

## 새로운 Aspose.PDF for C++ API 사용 방법

이 주제에서는 새로운 Aspose.PDF for C++ API를 설명하고 빠르고 쉽게 시작할 수 있도록 안내합니다. Please note that the details regarding the use of the particular features are not the part of this article.

Aspose.PDF for C++는 두 부분으로 구성되어 있습니다:

- Aspose.PDF for C++ DOM API
- Aspose.PDF.Facades

각 영역의 세부사항은 아래에서 확인할 수 있습니다.

### Aspose.PDF for C++ DOM API

Aspose.PDF for C++ DOM API는 PDF 문서 구조에 해당하며, 파일 및 문서 수준뿐만 아니라 객체 수준에서도 PDF 문서와 작업할 수 있도록 도와줍니다. 우리는 개발자들에게 PDF 문서의 모든 요소와 객체에 접근할 수 있는 더 많은 유연성을 제공했습니다. Aspose.PDF DOM API의 클래스를 사용하여 문서 요소와 서식에 대한 프로그래밍적 접근이 가능합니다. 이 새로운 DOM API는 아래와 같이 다양한 네임스페이스로 구성되어 있습니다:

### Aspose::Pdf Namespace Reference

이 네임스페이스는 PDF 문서를 열고 저장할 수 있는 Document 클래스를 제공합니다.

#### Aspose::Pdf::Text Namespace Reference

이 네임스페이스는 텍스트 및 다양한 측면, 예를 들어 Font, FontCollection, FontRepository, FontSource, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment 및 TextSegmentCollection 등을 다루는 데 도움을 주는 클래스를 제공합니다.
#### Aspose::Pdf::Collections 네임스페이스 참조

이 네임스페이스는 AsposeHashDictionary 클래스를 제공합니다.

#### Aspose::Pdf::CommonData 네임스페이스 참조

#### Aspose::Pdf::Diagnostics 네임스페이스 참조

#### Aspose::Pdf::Drawing 네임스페이스 참조

이 네임스페이스는 PDF 파일에 그래픽 요소를 추가하기 위한 Curve, Circle, Arc, Rectangle, Graph 등의 클래스를 제공합니다.

#### Aspose::Pdf::Engine 네임스페이스 참조

이 네임스페이스는 Addressing, Interactive, Security, CommonData, IO, Presentation 클래스를 제공합니다.

#### Aspose::Pdf::GroupProcessor 네임스페이스 참조

이 네임스페이스는 IPdfTypeExtractor 객체를 생성하기 위한 팩토리를 나타내는 ExtractorFactory 클래스와 IDocumentPageTextExtractor, IDocumentTextExtractor, IPdfTypeExtractor 클래스 - 추출기와 상호작용하기 위한 인터페이스를 제공합니다.

#### Aspose::Pdf::Interchange 네임스페이스 참조

#### Aspose::Pdf::LogicalStructure 네임스페이스 참조

이 네임스페이스는 AnnotationElement, AttributeOwnerStandard, CaptionElement, DocumentElement, FormElement, GroupingElement, ILSTextElement, PrivateElement, WarichuWTElement 등의 클래스를 제공합니다.

#### Aspose::Pdf::Operators Namespace Reference

이 네임스페이스는 다음 연산자의 클래스를 제공합니다: BasicSetColorAndPatternOperator, BlockTextOperator, SetCharWidthBoundingBox, SetColorStroke, SetHorizontalTextScaling, SetTextRenderingMode, TextShowOperator 등.

#### Aspose::Pdf::Optimization Namespace Reference

이 네임스페이스는 두 개의 클래스 - ImageCompressionOptions 및 OptimizationOptions를 제공합니다.

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

이 네임스페이스는 두 개의 클래스를 제공합니다: FontEmbeddingOptions - PDF/A 표준은 모든 글꼴이 문서에 포함되어야 한다고 요구합니다. 이 클래스는 대상 PC에 글꼴이 없어서 일부 글꼴을 포함할 수 없는 경우에 대한 플래그를 포함합니다. ToUnicodeProcessingRules - 이 클래스는 Adobe Preflight 오류 "텍스트를 유니코드로 매핑할 수 없음"을 해결하는 데 사용할 수 있는 규칙을 설명합니다.

#### Aspose::Pdf::Sanitization Namespace Reference

이 네임스페이스는 두 개의 클래스를 제공합니다: Details_SanitizationException 및 IRecovery.

#### Aspose::Pdf::Tagged 네임스페이스 참조

이 네임스페이스는 클래스 Details_TaggedException - 문서의 TaggedPDF 콘텐츠에 대한 예외를 나타냅니다. ITaggedContent - 문서의 TaggedPdf 콘텐츠 작업을 위한 인터페이스를 나타냅니다? 및 TaggedPdfExceptionCode를 제공합니다.

#### Aspose::Pdf::Validation 네임스페이스 참조

#### Aspose::Pdf::XfaConverter 네임스페이스 참조

이 네임스페이스는 관련 데이터 캡슐화를 처리하는 클래스 XfaParserOptions를 제공합니다.

#### Aspose::Pdf::Annotations 네임스페이스 참조

주석은 PDF 문서의 대화형 기능의 일부입니다. 우리는 주석을 위한 네임스페이스를 할당했습니다. 이 네임스페이스는 Annotation, AnnotationCollection, CircleAnnotation 및 LinkAnnotation 등 주석을 다루는 데 도움을 주는 클래스를 포함합니다.

#### Aspose::Pdf::Forms 네임스페이스 참조

이 네임스페이스는 PDF 양식 및 양식 필드를 다루는 데 도움을 주는 클래스, 예를 들어 Form, Field, TextBoxField 및 OptionCollection 등을 포함합니다.

#### Aspose::Pdf::Devices 네임스페이스 참조

We can perform various operations on the PDF documents such as converting PDF document to various image formats. However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

우리는 PDF 문서에 대해 다양한 작업을 수행할 수 있으며, PDF 문서를 다양한 이미지 형식으로 변환하는 등의 작업을 수행할 수 있습니다. 그러나 이러한 작업은 Document 객체에 속하지 않으며, 그러한 작업을 위해 Document 클래스를 확장할 수 없습니다. 그렇기 때문에 우리는 새로운 DOM API에서 Device의 개념을 도입했습니다.

##### Aspose::Pdf::Facades Namespace Reference

##### Aspose::Pdf::Facades 네임스페이스 참조

You can use Aspose.PDF.Facades namespace. This Namespace provides classes AutoFiller - represents a class to receive data from database or other datasource. Bookmark, Form, Stamp, PdfConverter anr more classes.

Aspose.PDF.Facades 네임스페이스를 사용할 수 있습니다. 이 네임스페이스는 데이터베이스 또는 기타 데이터 소스로부터 데이터를 받기 위한 클래스인 AutoFiller 클래스를 제공합니다. Bookmark, Form, Stamp, PdfConverter 및 기타 여러 클래스를 제공합니다.