---
title: Aspose.PDF DOM API의 기초
linktitle: DOM API의 기초
type: docs
weight: 140
url: /net/basics-of-dom-api/
description: Aspose.PDF for .NET는 객체 측면에서 PDF 문서의 구조를 나타내기 위해 DOM 개념을 사용합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 소개

문서 객체 모델(DOM)은 구조화된 문서를 객체 지향 모델로 표현하는 형식입니다. DOM은 플랫폼과 언어에 중립적인 방식으로 구조화된 문서를 표현하기 위한 공식 World Wide Web Consortium (W3C) 표준입니다.

간단히 말해, DOM은 어떤 문서의 구조를 나타내는 객체의 트리입니다.
### DOM 소개

간단히 말해서, DOM은 어떤 문서의 구조를 나타내는 객체의 트리입니다.

### PDF 문서 소개

Portable Document Format (PDF)는 문서 교환을 위한 오픈 표준입니다. PDF 문서는 텍스트와 이진 데이터의 조합입니다. 텍스트 편집기에서 열면 문서의 구조와 내용을 정의하는 원시 객체를 볼 수 있습니다.

PDF 파일의 논리적 구조는 계층적이며, 보기 애플리케이션이 문서의 페이지와 그 내용을 그리는 순서를 결정합니다. PDF는 객체, 파일 구조, 문서 구조 및 콘텐츠 스트림의 네 가지 구성 요소로 구성됩니다.

### PDF 문서 구조

PDF 파일의 구조가 계층적인 것처럼, Aspose.PDF for .NET도 같은 방식으로 요소에 접근합니다. 다음 계층은 PDF 문서가 논리적으로 어떻게 구조화되어 있는지와 Aspose.PDF for .NET DOM API가 이를 어떻게 구성하는지 보여줍니다.

![PDF 문서 구조](../images/structure.png)

### PDF 문서 요소 접근

Document 객체는 객체 모델의 루트 레벨에 있습니다.
문서 객체는 객체 모델의 최상위 수준에 있습니다.

- PDF 문서 열기
- DOM 스타일로 PDF 문서 구조에 접근
- PDF 문서의 데이터 업데이트
- PDF 문서 검증
- 다양한 형식으로 PDF 문서 내보내기
- 마지막으로 업데이트된 PDF 문서 저장

## 새로운 Aspose.PDF for .NET API 사용 방법

이 주제는 새로운 Aspose.PDF for .NET API를 설명하고 빠르고 쉽게 시작할 수 있도록 안내합니다. 특정 기능 사용에 대한 상세 내용은 이 글의 일부가 아닙니다.

Aspose.PDF for .NET은 두 부분으로 구성됩니다:

- Aspose.PDF for .NET DOM API
- Aspose.PDF.Facades (구 Aspose.PDF.Kit for .NET)
각각의 영역에 대한 세부 사항은 아래에서 확인할 수 있습니다.

### Aspose.PDF for .NET DOM API

Aspose.PDF for .NET DOM API는 PDF 문서 구조에 해당하며, 파일 및 문서 수준뿐만 아니라 객체 수준에서도 PDF 문서 작업을 할 수 있도록 도와줍니다.
### Aspose.PDF

Aspose.PDF 네임스페이스는 PDF 문서를 열고 저장할 수 있는 Document 클래스를 제공합니다. 이 네임스페이스에는 License 클래스도 포함되어 있습니다. 또한 페이지, 첨부 파일, 북마크와 관련된 클래스도 제공합니다. 예를 들어 Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection, OutlineCollection 등이 있습니다.

#### Aspose.Text

이 네임스페이스는 텍스트와 그 다양한 측면을 다루는 데 도움이 되는 클래스를 제공합니다. 예를 들어 Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment, TextSegmentCollection 등이 있습니다.

#### Aspose.Text.TextOptions

이 네임스페이스는 텍스트 검색, 편집 또는 교체에 대한 다양한 옵션을 설정할 수 있는 클래스를 제공합니다. 예를 들어 TextEditOptions, TextReplaceOptions, TextSearchOptions 등이 있습니다.
#### Aspose.InteractiveFeatures

이 네임스페이스에는 PDF 문서의 상호작용 기능을 사용할 수 있도록 돕는 클래스가 포함되어 있습니다. 예를 들어 문서 작업 및 기타 작업을 수행합니다. 이 네임스페이스에는 GoToAction, GoToRemoteAction, GoToURIAction 등의 클래스가 포함되어 있습니다.

#### Aspose.InteractiveFeatures.Annotations

주석은 PDF 문서의 상호작용 기능의 일부입니다. 우리는 주석을 위한 네임스페이스를 헌정했습니다. 이 네임스페이스에는 주석을 다루는 데 도움이 되는 클래스가 포함되어 있습니다. 예를 들어, Annotation, AnnotationCollection, CircleAnnotation, LinkAnnotation 등이 있습니다.

#### Aspose.InteractiveFeatures.Forms

이 네임스페이스에는 PDF 양식과 양식 필드를 다루는 데 도움이 되는 클래스가 포함되어 있습니다. 예를 들어 Form, Field, TextBoxField, OptionCollection 등이 있습니다.

#### Aspose.PDF.Devices

PDF 문서에서 다양한 이미지 형식으로 PDF 문서를 변환하는 등의 여러 작업을 수행할 수 있습니다.
PDF 문서에 다양한 작업을 수행할 수 있습니다. 예를 들어 PDF 문서를 다양한 이미지 형식으로 변환할 수 있습니다.

##### Aspose.PDF.Facades

이전에는 Aspose.PDF for .NET 이전에 기존 PDF 파일을 조작하기 위해 Aspose.PDF.Kit for .NET이 필요했습니다. 오래된 Aspose.PDF.Kit 코드를 실행하려면 Aspose.PDF.Facades 네임스페이스를 사용할 수 있습니다.
