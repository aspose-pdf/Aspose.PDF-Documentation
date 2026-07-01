---
title: Aspose.PDF DOM API 기본
linktitle: DOM API 기본
type: docs
weight: 10
url: /ko/androidjava/basics-of-dom-api/
description: Aspose.PDF for Android via Java도 객체 단위로 PDF 문서의 구조를 나타내기 위해 DOM 개념을 사용합니다. 여기에서 이 구조에 대한 설명을 읽을 수 있습니다.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 소개

문서 객체 모델(DOM)은 구조화된 문서를 객체 지향 모델로 표현하는 형태입니다. DOM은 플랫폼 및 언어에 구애받지 않는 방식으로 구조화된 문서를 표시하기 위한 공식 World Wide Web Consortium(W3C) 표준입니다.

간단히 말해, DOM은 문서의 구조를 나타내는 객체 트리입니다. Aspose.PDF for Android via Java도 객체 단위로 PDF 문서의 구조를 나타내기 위해 DOM 개념을 사용합니다. 그러나 DOM의 요소와 같은 측면은 사용 중인 프로그래밍 언어의 구문 내에서 조작됩니다. DOM의 공용 인터페이스는 해당 애플리케이션 프로그래밍 인터페이스(API)에서 지정됩니다.

### PDF 문서 소개

Portable Document Format (PDF)는 문서 교환을 위한 공개 표준입니다. PDF 문서는 텍스트와 바이너리 데이터의 조합입니다. 텍스트 편집기에서 열면 문서의 구조와 내용을 정의하는 원시 객체들을 볼 수 있습니다.

PDF 파일의 논리 구조는 계층적이며, 뷰어 애플리케이션이 문서의 페이지와 그 내용을 그리는 순서를 결정합니다. PDF는 네 가지 구성 요소로 이루어져 있습니다: 객체, 파일 구조, 문서 구조 및 내용 스트림.

### PDF 문서 구조

PDF 파일의 구조가 계층적이므로, Aspose.PDF for Java도 동일한 방식으로 요소에 접근합니다. 다음 계층 구조는 PDF 문서가 논리적으로 어떻게 구성되는지 그리고 Aspose.PDF for Java DOM API가 이를 어떻게 구축하는지를 보여줍니다.

![PDF 문서 구조](https://docs.aspose.com/pdf/java/images/structure.png)

### PDF 문서 요소에 접근하기

Document 객체는 객체 모델의 최상위 레벨에 있습니다. Aspose.PDF for Android via Java DOM API를 사용하면 Document 객체를 생성하고 계층 구조의 다른 모든 객체에 접근할 수 있습니다. Pages와 같은 컬렉션이나 Page와 같은 개별 요소에 접근할 수 있습니다. DOM API는 아래와 같이 PDF 문서를 조작하기 위한 단일 진입 및 종료 지점을 제공합니다:

- PDF 문서 열기
- DOM 스타일로 PDF 문서 구조에 접근
- PDF 문서의 데이터를 업데이트
- PDF 문서 검증
- PDF 문서를 다양한 형식으로 내보내기
- 마지막으로, 업데이트된 PDF 문서를 저장합니다

## Java API를 통한 새로운 Aspose.PDF for Android 사용 방법

이 주제에서는 Java API를 통한 새로운 Aspose.PDF for Android에 대해 설명하고 빠르고 쉽게 시작할 수 있도록 안내합니다. 특정 기능 사용에 관한 자세한 내용은 이 기사에 포함되지 않음을 유의하십시오.

Java를 통한 Aspose.PDF for Android는 두 부분으로 구성됩니다:

- Java DOM API를 통한 Aspose.PDF for Android
- Aspose.PDF.Facades 

아래에서 이러한 각 영역에 대한 자세한 내용을 찾을 수 있습니다.

### Java DOM API를 통한 Aspose.PDF for Android

새로운 Aspose.PDF for Android via Java DOM API는 PDF 문서 구조에 대응하며, 이를 통해 파일 및 문서 수준뿐만 아니라 객체 수준에서도 PDF 문서를 작업할 수 있습니다. 우리는 개발자에게 PDF 문서의 모든 요소와 객체에 접근할 수 있는 유연성을 더욱 제공했습니다. Aspose.PDF DOM API의 클래스를 사용하면 문서 요소와 서식에 프로그래밍 방식으로 접근할 수 있습니다. 이 새로운 DOM API는 아래와 같이 다양한 네임스페이스로 구성됩니다:

### com.aspose.pdf

이 네임스페이스는 PDF 문서를 열고 저장할 수 있는 Document 클래스를 제공합니다. License 클래스도 이 네임스페이스의 일부입니다. 또한 com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, com.aspose.pdf.OutlineCollection 등과 같은 PDF 페이지, 첨부 파일 및 북마크와 관련된 클래스를 제공합니다.

#### com.aspose.pdf.text

이 네임스페이스는 텍스트 및 그 다양한 측면을 작업하는 데 도움이 되는 클래스를 제공합니다. 예를 들어 com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment 및 com.aspose.pdf.TextSegmentCollection 등이 있습니다.

#### com.aspose.pdf.TextOptions

이 네임스페이스는 텍스트 검색, 편집 또는 교체를 위한 다양한 옵션을 설정할 수 있는 클래스를 제공합니다. 예를 들어 com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions 및 com.aspose.pdf.TextSearchOptions 등이 있습니다.

#### com.aspose.pdf.PdfAction

이 네임스페이스에는 PDF 문서의 대화형 기능을 작업하는 데 도움이 되는 클래스가 포함되어 있습니다. 예를 들어 문서 및 기타 작업을 다루는 클래스가 있습니다. 이 네임스페이스에는 com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction 및 com.aspose.pdf.GoToURIAction 등과 같은 클래스가 포함되어 있습니다.

#### com.aspose.pdf.Annotation

주석은 PDF 문서의 인터랙티브 기능의 일부입니다. 우리는 주석을 위해 전용 네임스페이스를 마련했습니다. 이 네임스페이스에는 주석 작업에 도움이 되는 클래스가 포함되어 있으며, 예를 들어 com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation 및 com.aspose.pdf.LinkAnnotation 등이 있습니다.

#### com.aspose.pdf.Form

이 네임스페이스에는 PDF 양식 및 양식 필드 작업에 도움이 되는 클래스가 포함되어 있으며, 예를 들어 com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField 및 com.aspose.pdf.OptionCollection 등이 있습니다.

#### com.aspose.pdf.devices 

우리는 PDF 문서를 다양한 이미지 형식으로 변환하는 등 다양한 작업을 수행할 수 있습니다. 그러나 이러한 작업은 Document 객체에 속하지 않으며, 이러한 작업을 위해 Document 클래스를 확장할 수 없습니다. 그래서 새로운 DOM API에서 Device 개념을 도입했습니다.

##### com.aspose.pdf.facades

이전 Aspose.PDF for Java t.o.o 이전에는 기존 PDF 파일을 조작하려면 Aspose.PDF.Kit for Java가 필요했습니다. 오래된 Aspose.PDF.Kit 코드를 실행하려면 com.aspose.pdf.facades 네임스페이스를 사용할 수 있습니다.

