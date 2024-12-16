---
title: Aspose.PDF DOM API의 기초
linktitle: DOM API의 기초
type: docs
weight: 10
url: /ko/androidjava/basics-of-dom-api/
description: Aspose.PDF for Android via Java는 또한 DOM의 아이디어를 사용하여 객체 관점에서 PDF 문서의 구조를 나타냅니다. 여기에서 이 구조의 설명을 읽을 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 소개

문서 객체 모델(DOM)은 구조화된 문서를 객체 지향 모델로 표현하는 형태입니다. DOM은 플랫폼 및 언어 중립적인 방식으로 구조화된 문서를 표현하기 위한 공식 월드 와이드 웹 컨소시엄(W3C) 표준입니다.

간단히 말해, DOM은 일부 문서의 구조를 나타내는 객체의 트리입니다.
 Aspose.PDF for Android via Java는 또한 객체 측면에서 PDF 문서의 구조를 나타내기 위해 DOM의 개념을 사용합니다. 그러나 DOM의 측면(예: 요소)은 사용 중인 프로그래밍 언어의 구문 내에서 조작됩니다. DOM의 공개 인터페이스는 응용 프로그램 프로그래밍 인터페이스(API)에서 지정됩니다.

### PDF 문서 소개

Portable Document Format (PDF)는 문서 교환을 위한 개방형 표준입니다. PDF 문서는 텍스트와 이진 데이터의 조합입니다. 텍스트 편집기에서 열면 문서의 구조와 내용을 정의하는 원시 객체를 볼 수 있습니다.

PDF 파일의 논리 구조는 계층적이며 보기 응용 프로그램이 문서의 페이지와 내용을 그리는 순서를 결정합니다. PDF는 객체, 파일 구조, 문서 구조 및 콘텐츠 스트림의 네 가지 구성 요소로 구성됩니다.

### PDF 문서 구조

PDF 파일의 구조가 계층적이므로 Aspose.PDF for Java도 동일한 방식으로 요소에 접근합니다. 다음 계층 구조는 PDF 문서가 논리적으로 구조화된 방법과 Aspose.PDF for Java DOM API가 이를 구성하는 방법을 보여줍니다.

![PDF 문서 구조](https://docs.aspose.com/pdf/java/images/structure.png)

### PDF 문서 요소에 접근하기

Document 객체는 객체 모델의 최상위 수준에 있습니다. Aspose.PDF for Android via Java DOM API를 사용하여 Document 객체를 생성하고 계층 구조의 다른 모든 객체에 접근할 수 있습니다. Pages와 같은 컬렉션에 접근하거나 Page와 같은 개별 요소에 접근할 수 있습니다. DOM API는 아래에 표시된 대로 PDF 문서를 조작하기 위한 단일 진입 및 종료 지점을 제공합니다:

- PDF 문서 열기
- DOM 스타일로 PDF 문서 구조에 접근
- PDF 문서의 데이터 업데이트
- PDF 문서 검증
- PDF 문서를 다른 형식으로 내보내기
- 마지막으로 업데이트된 PDF 문서 저장

## 새로운 Aspose.PDF for Android via Java API 사용 방법

이 주제는 새로운 Aspose.PDF for Android via Java API를 설명하고 빠르고 쉽게 시작할 수 있도록 안내합니다. 특정 기능 사용에 관한 세부 사항은 이 문서의 일부가 아닙니다.

Aspose.PDF for Android via Java는 두 부분으로 구성됩니다:

- Aspose.PDF for Android via Java DOM API
- Aspose.PDF.Facades 

각 영역의 세부 사항은 아래에서 확인할 수 있습니다.

### Aspose.PDF for Android via Java DOM API

새로운 Aspose.PDF for Android via Java DOM API는 PDF 문서 구조에 대응하여, 파일 및 문서 수준뿐만 아니라 객체 수준에서도 PDF 문서 작업을 할 수 있도록 도와줍니다. 개발자에게 PDF 문서의 모든 요소와 객체에 접근할 수 있는 더 많은 유연성을 제공합니다. Aspose.PDF DOM API의 클래스를 사용하여 문서 요소와 서식에 프로그래밍적으로 접근할 수 있습니다. 이 새로운 DOM API는 아래와 같이 다양한 네임스페이스로 구성되어 있습니다:

### com.aspose.pdf

이 네임스페이스는 PDF 문서를 열고 저장할 수 있는 Document 클래스를 제공합니다. The License 클래스도 이 네임스페이스의 일부입니다. 또한 com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, com.aspose.pdf.OutlineCollection 등과 같이 PDF 페이지, 첨부 파일 및 책갈피와 관련된 클래스를 제공합니다.

#### com.aspose.pdf.text

이 네임스페이스는 텍스트와 그 다양한 측면을 다루는 데 도움이 되는 클래스를 제공합니다. 예를 들어 com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment 및 com.aspose.pdf.TextSegmentCollection 등이 있습니다.

#### com.aspose.pdf.TextOptions

이 네임스페이스는 텍스트 검색, 편집 또는 대체를 위한 다양한 옵션을 설정할 수 있는 클래스를 제공합니다. 예를 들어 com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, 및 com.aspose.pdf.TextSearchOptions 등이 있습니다.
#### com.aspose.pdf.PdfAction

이 네임스페이스는 PDF 문서의 대화형 기능을 다루는 데 도움을 주는 클래스를 포함하고 있습니다. 예를 들어 문서 및 기타 작업을 다루는 클래스입니다. 이 네임스페이스는 com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction 및 com.aspose.pdf.GoToURIAction 등의 클래스를 포함하고 있습니다.

#### com.aspose.pdf.Annotation

주석은 PDF 문서의 대화형 기능의 일부입니다. 우리는 주석을 위한 네임스페이스를 전용으로 만들었습니다. 이 네임스페이스는 주석을 다루는 데 도움을 주는 클래스를 포함하고 있습니다. 예를 들어, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation 및 com.aspose.pdf.LinkAnnotation 등의 클래스가 있습니다.

#### com.aspose.pdf.Form

이 네임스페이스는 PDF 폼 및 폼 필드를 다루는 데 도움을 주는 클래스를 포함하고 있습니다. 예를 들어 com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField 및 com.aspose.pdf.OptionCollection 등의 클래스가 있습니다.

#### com.aspose.pdf.devices 

우리는 PDF 문서에 대해 다양한 작업을 수행할 수 있습니다. 예를 들어 PDF 문서를 다양한 이미지 형식으로 변환하는 작업을 수행할 수 있습니다.
 그러나 이러한 작업은 Document 객체에 속하지 않으며 이러한 작업을 위해 Document 클래스를 확장할 수 없습니다. 그래서 우리는 새로운 DOM API에서 Device의 개념을 도입했습니다.

##### com.aspose.pdf.facades

이전에는 기존 PDF 파일을 조작하기 위해 Java용 Aspose.PDF.Kit이 필요했습니다. 이전 Aspose.PDF.Kit 코드를 실행하려면 com.aspose.pdf.facades 네임스페이스를 사용할 수 있습니다.