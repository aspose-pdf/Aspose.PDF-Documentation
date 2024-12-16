---
title: Aspose.PDF DOM API의 기초
linktitle: DOM API의 기초
type: docs
weight: 110
url: /ko/java/basics-of-dom-api/
description: Aspose.PDF for Java는 PDF 문서의 구조를 객체의 측면에서 나타내기 위해 DOM의 개념을 사용합니다. 여기에서 이 구조의 설명을 읽을 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 소개

문서 객체 모델(DOM)은 구조화된 문서를 객체 지향 모델로 표현하는 한 형태입니다. DOM은 플랫폼과 언어에 구애받지 않고 구조화된 문서를 표현하기 위한 공식 월드 와이드 웹 컨소시엄(W3C) 표준입니다.

간단히 말해서, DOM은 어떤 문서의 구조를 나타내는 객체들의 트리입니다.
 Aspose.PDF for Java는 또한 객체 측면에서 PDF 문서의 구조를 표현하기 위해 DOM의 개념을 사용합니다. 그러나 DOM의 측면(예: 그 요소들)은 사용 중인 프로그래밍 언어의 구문 내에서 조작됩니다. DOM의 공용 인터페이스는 애플리케이션 프로그래밍 인터페이스(API)에서 지정됩니다.

### PDF 문서 소개

이동식 문서 형식(PDF)은 문서 교환을 위한 개방형 표준입니다. PDF 문서는 텍스트와 바이너리 데이터의 조합입니다. 텍스트 편집기에서 열면 문서의 구조와 내용을 정의하는 원시 객체를 볼 수 있습니다.

PDF 파일의 논리적 구조는 계층적이며, 뷰어 애플리케이션이 문서의 페이지와 그 내용을 그리는 순서를 결정합니다. PDF는 객체, 파일 구조, 문서 구조 및 콘텐츠 스트림의 네 가지 구성 요소로 구성됩니다.

### PDF 문서 구조

PDF 파일의 구조가 계층적이므로, Aspose.PDF for Java도 동일한 방식으로 요소에 접근합니다. 다음 계층 구조는 PDF 문서가 논리적으로 어떻게 구성되어 있는지와 Aspose.PDF for Java DOM API가 이를 어떻게 구성하는지를 보여줍니다.

![PDF 문서 구조](../images/structure.png)

### PDF 문서 요소 접근하기

Document 객체는 객체 모델의 최상위 레벨에 있습니다. Aspose.PDF for Java DOM API를 사용하면 Document 객체를 생성한 후 계층 구조의 다른 모든 객체에 접근할 수 있습니다. Pages와 같은 컬렉션이나 Page와 같은 개별 요소에 접근할 수 있습니다. DOM API는 PDF 문서를 조작하기 위한 단일 입출력 지점을 제공합니다. 아래와 같이 설명됩니다:

- PDF 문서 열기
- DOM 스타일로 PDF 문서 구조 접근하기
- PDF 문서의 데이터 업데이트하기
- PDF 문서 검증하기
- PDF 문서를 다른 형식으로 내보내기
- 마지막으로, 업데이트된 PDF 문서 저장하기

## 새로운 Aspose.PDF for Java API 사용 방법

이 주제는 새로운 Aspose.PDF for Java API를 설명하고 빠르고 쉽게 시작할 수 있도록 안내합니다. 사용 특정 기능에 대한 세부사항은 이 기사에 포함되지 않습니다.

Aspose.PDF for Java는 두 부분으로 구성되어 있습니다:

- Aspose.PDF for Java DOM API
- Aspose.PDF.Facades

각 영역의 세부사항은 아래에서 확인할 수 있습니다.

### Aspose.PDF for Java DOM API

새로운 Aspose.PDF for Java DOM API는 PDF 문서 구조에 해당하며, 이를 통해 파일 및 문서 수준뿐만 아니라 객체 수준에서도 PDF 문서를 작업할 수 있습니다. 개발자가 PDF 문서의 모든 요소와 객체에 더 유연하게 접근할 수 있도록 했습니다. Aspose.PDF DOM API의 클래스를 사용하여 문서 요소와 서식에 프로그래밍적으로 접근할 수 있습니다. 이 새로운 DOM API는 아래에 나열된 다양한 네임스페이스로 구성되어 있습니다:

### com.aspose.pdf

이 네임스페이스는 Document 클래스를 제공하며, 이를 통해 PDF 문서를 열고 저장할 수 있습니다. The License 클래스도 이 네임스페이스의 일부입니다. 또한 com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, com.aspose.pdf.OutlineCollection 등과 같은 PDF 페이지, 첨부 파일 및 책갈피와 관련된 클래스를 제공합니다.

#### com.aspose.pdf.text

이 네임스페이스는 텍스트와 그 다양한 측면을 다루는 데 도움이 되는 클래스를 제공합니다. 예를 들어, com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment 및 com.aspose.pdf.TextSegmentCollection 등이 있습니다.

#### com.aspose.pdf.TextOptions

이 네임스페이스는 텍스트 검색, 편집 또는 교체를 위한 다양한 옵션을 설정할 수 있는 클래스를 제공합니다. 예를 들어, com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions 및 com.aspose.pdf.TextSearchOptions 등이 있습니다.
#### com.aspose.pdf.PdfAction

이 네임스페이스는 PDF 문서의 대화형 기능, 예를 들어 문서 및 기타 작업을 다루는 데 도움을 주는 클래스를 포함하고 있습니다. 이 네임스페이스에는 com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction 및 com.aspose.pdf.GoToURIAction 등의 클래스가 포함되어 있습니다.

#### com.aspose.pdf.Annotation

주석은 PDF 문서의 대화형 기능의 일부입니다. 우리는 주석을 위한 네임스페이스를 전용으로 할당했습니다. 이 네임스페이스는 주석을 다루는 데 도움을 주는 클래스를 포함하고 있습니다. 예를 들어, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation 및 com.aspose.pdf.LinkAnnotation 등의 클래스가 포함되어 있습니다.

#### com.aspose.pdf.Form

이 네임스페이스는 PDF 양식 및 양식 필드를 다루는 데 도움을 주는 클래스를 포함하고 있습니다. 예를 들어 com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField 및 com.aspose.pdf.OptionCollection 등의 클래스가 포함되어 있습니다.

#### com.aspose.pdf.devices

우리는 PDF 문서에 대해 다양한 작업을 수행할 수 있으며, 예를 들어 PDF 문서를 다양한 이미지 형식으로 변환할 수 있습니다.
 그러나 그러한 작업은 Document 객체에 속하지 않으며, 이러한 작업을 위해 Document 클래스를 확장할 수 없습니다. 그래서 우리는 새로운 DOM API에서 Device라는 개념을 도입했습니다.

##### com.aspose.pdf.facades

이전에는 Aspose.PDF for Java t.o.o를 사용하기 위해 기존 PDF 파일을 조작하려면 Aspose.PDF.Kit for Java가 필요했습니다. 이전 Aspose.PDF.Kit 코드를 실행하려면 com.aspose.pdf.facades 네임스페이스를 사용할 수 있습니다.