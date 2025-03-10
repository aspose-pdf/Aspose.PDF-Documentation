---
title: Aspose.PDF for .NET을 COM Interop을 통해
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/use-aspose-pdf-for-net-via-com-interop/
description: 비-.NET 애플리케이션과의 원활한 통합을 위해 COM Interop을 통해 Aspose.PDF for .NET을 사용하는 방법을 알아보세요.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NET은 이제 COM Interop을 통해 다양한 프로그래밍 언어와의 원활한 통합을 지원하여 개발자가 .NET 프레임워크 외부에서 강력한 PDF 조작 기능을 활용할 수 있도록 합니다. 이 기능은 Aspose.PDF 객체를 COM 객체로 변환하여 비관리 코드와의 상호작용을 간소화하고 조기 및 지연 바인딩 기술을 통해 높은 성능을 유지함으로써 유연성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

이 주제의 정보는 다음 프로그래밍 언어 중 하나에서 COM Interop을 통해 [Aspose.PDF for .NET](/pdf/ko/net/)을 사용하려는 시나리오에 적용됩니다:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## COM Interop 작업하기

Aspose.PDF for .NET은 .NET Framework의 제어 하에 실행되며 이를 관리 코드라고 합니다. 위의 모든 언어로 작성된 코드는 .NET Framework 외부에서 실행되며 이를 비관리 코드라고 합니다. 비관리 코드와 Aspose.PDF 간의 상호작용은 COM Interop이라는 .NET 기능을 통해 발생합니다.

Aspose.PDF 객체는 .NET 객체이지만 COM Interop을 통해 사용될 때는 프로그래밍 언어에서 COM 객체로 나타납니다. 따라서 [Aspose.PDF for .NET](/pdf/ko/net/)을 사용하기 전에 프로그래밍 언어에서 COM 객체를 생성하고 사용하는 방법을 아는 것이 가장 좋습니다.

{{% alert color="primary" %}}

- COM 세계에서는 COM 서버와 COM 클라이언트를 구분합니다. COM 서버는 COM 클래스를 저장하고 COM 클라이언트는 COM 서버에 클래스 인스턴스, 즉 COM 객체를 요청합니다.
- COM 클라이언트 또는 간단히 클라이언트 애플리케이션은 COM 클래스의 내용에 대해 알고 있거나 그 메서드와 속성에 대해 전혀 알지 못할 수 있습니다. 따라서 클라이언트 애플리케이션은 컴파일/빌드 중 또는 실행 중에 COM 클래스 구조를 발견할 수 있습니다. "발견" 과정은 바인딩으로 알려져 있으며, 그래서 우리는 **조기 바인딩**과 **지연 바인딩**이 있습니다.
- 간단히 말해 COM 클래스는 블랙 박스와 같으며 이를 작업하기 위해서는 타입 라이브러리가 필요합니다. 이 이진 파일은 COM 클래스의 메서드, 속성에 대한 설명을 가지고 있으며, COM 객체 작업을 지원하는 고급 언어는 종종 타입 라이브러리를 추가하기 위한 구문 표현을 가지고 있습니다. 예를 들어 C++에서는 [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx)입니다.
- 타입 라이브러리는 조기 바인딩에 사용됩니다.
- COM 객체는 두 가지 방법으로 메서드와 속성을 노출할 수 있습니다: **디스패치 인터페이스**(dispinterface)를 통해서와 **vtable**(가상 함수 테이블)에서.
- **dispinterface** 내에서 각 메서드와 속성은 고유한 멤버로 식별됩니다. 이 멤버는 함수의 디스패치 식별자(또는 **DispID**)입니다.
- **vtable**은 COM 클래스 인터페이스가 지원하는 함수에 대한 포인터 집합입니다.
- 두 인터페이스를 통해 메서드를 노출하는 객체는 **이중 인터페이스**를 지원합니다.
- 두 가지 바인딩 유형 모두 장점이 있습니다. 조기 바인딩은 성능 향상과 컴파일 타임 구문 검사를 제공합니다. 지연 바인딩은 COM 클래스의 ***미래 버전과 호환되도록*** 클라이언트를 작성할 때 가장 유리합니다. 지연 바인딩을 사용하면 타입 라이브러리의 정보가 클라이언트에 "하드 와이어"되지 않으므로 클라이언트가 코드 변경 없이 COM 클래스의 미래 버전과 작업할 수 있다는 확신을 가질 수 있습니다.
- 지연 바인딩 메커니즘은 큰 장점이 있습니다: COM DLL의 작성자가 다른 함수 인터페이스 레이아웃으로 새 버전을 출시하기로 결정하면, 해당 메서드를 호출하는 코드는 더 이상 사용 가능하지 않은 경우를 제외하고는 충돌하지 않습니다. **vtable**이 다르더라도 지연 바인딩은 새로운 DISPIDs를 발견하고 적절한 메서드를 호출하는 데 성공합니다.
{{% /alert %}}

여기에서 궁극적으로 마스터해야 할 주제는 다음과 같습니다:
{{% alert color="primary" %}}

- 프로그래밍 언어에서 COM 객체 사용하기. 프로그래밍 언어 문서와 이 문서의 언어별 주제를 참조하세요.

- .NET COM Interop에 의해 노출된 COM 객체 작업하기. MSDN의 [비관리 코드와의 상호 운용](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) 및 [COM에 .NET Framework 구성 요소 노출](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx)을 참조하세요.

- Aspose.PDF 문서 객체 모델. [Aspose.PDF 프로그래머 가이드](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) 및 [API 참조](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference)를 참조하세요.

{{% /alert %}}

## COM Interop으로 Aspose.PDF for .NET 등록하기

Aspose.PDF for .NET을 설치하고 COM Interop에 등록되어 있는지 확인해야 합니다(비관리 코드에서 호출할 수 있도록 보장).

{{% alert color="primary" %}}

COM Interop을 위해 Aspose.PDF for .NET을 수동으로 등록하려면:

1. **시작** 메뉴에서 **모든 프로그램**을 선택한 다음 **Microsoft Visual Studio**, **Visual Studio 도구** 및 마지막으로 **Visual Studio 명령 프롬프트**를 선택합니다.
1. 어셈블리를 등록하는 명령을 입력합니다:
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

/codebase는 Aspose.PDF.dll이 GAC에 없을 경우에만 필요하다는 점에 유의하세요. 이 옵션을 사용하면 regasm이 레지스트리에 어셈블리 경로를 추가합니다.

{{% alert color="primary" %}}

regasm.exe는 .NET Framework SDK에 포함된 도구입니다. 모든 .NET Framework SDK 도구는 *\Microsoft .NET\Framevork\<FrameworkVersion>* 디렉토리에 위치하며, 예를 들어 *C:\Windows\Microsoft .NET\Framework\v4.0.30319*입니다. Visual Studio .NET을 사용하는 경우:
**시작** 메뉴에서 **프로그램**을 선택한 다음 **Visual Studio 2022**를 선택하고 마지막으로 **VS 2022용 개발자 명령 프롬프트**를 선택합니다.
필요한 모든 환경 변수가 설정된 명령 프롬프트가 실행됩니다.

{{% /alert %}}

### ProgIDs

ProgID는 "프로그램 식별자"를 의미합니다. 객체를 생성하는 데 사용되는 COM 클래스의 이름입니다. ProgID는 라이브러리 이름 "Aspose.PDF"와 클래스 이름으로 구성됩니다.

### 타입 라이브러리

{{% alert color="primary" %}}

프로그래밍 언어(예: Visual Basic 또는 Delphi)가 COM 타입 라이브러리를 참조할 수 있도록 허용하는 경우, Aspose.PDF.tlb에 대한 참조를 추가하고 Object Browser에서 모든 Aspose.PDF for .NET 클래스, 메서드, 속성 및 열거형을 확인하세요.

TLB 파일을 생성하려면:

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## COM 객체 생성하기

COM 객체의 생성은 일반 .NET 객체의 생성과 유사합니다:

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

생성된 후에는 COM 객체인 것처럼 객체의 메서드와 속성에 접근할 수 있습니다:

```vb
'Add page to the document
document.Pages.Add()
```

일부 메서드는 오버로드가 있으며, 이들은 숫자 접미사가 추가되어 COM Interop에 의해 노출됩니다. 첫 번째 메서드는 변경되지 않습니다. 예를 들어, Document.Save 메서드 오버로드는 Document.Save, Document.Save_2 등으로 변환됩니다.

자세한 내용은 이 문서의 언어별 기사에서 확인하세요.

## 래퍼 어셈블리 생성하기

Aspose.PDF for .NET 클래스, 메서드 및 속성을 많이 사용해야 하는 경우, 래퍼 어셈블리(C# 또는 다른 .NET 프로그래밍 언어 사용)를 생성하는 것을 고려하세요. 래퍼 어셈블리는 비관리 코드에서 Aspose.PDF for .NET을 직접 사용하는 것을 피하는 데 도움이 됩니다.

좋은 접근 방식은 Aspose.PDF for .NET을 참조하고 이를 사용하여 모든 작업을 수행하며 비관리 코드에 최소한의 클래스와 메서드만 노출하는 .NET 어셈블리를 개발하는 것입니다. 그런 다음 애플리케이션은 래퍼 라이브러리와만 작업해야 합니다.

COM Interop을 통해 호출해야 하는 클래스와 메서드의 수를 줄이면 프로젝트가 단순해집니다. COM Interop을 통해 .NET 클래스를 사용하는 것은 종종 고급 기술을 요구합니다.