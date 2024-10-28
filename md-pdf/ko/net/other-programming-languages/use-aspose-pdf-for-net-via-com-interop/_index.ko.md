---
title: Aspose.PDF for .NET via COM Interop
type: docs
weight: 20
url: /net/use-aspose-pdf-for-net-via-com-interop/
---

{{% alert color="primary" %}}

이 주제의 정보는 다음 프로그래밍 언어 중 하나에서 [Aspose.PDF for .NET](/pdf/net/)을 COM Interop을 통해 사용하려는 시나리오에 적용됩니다:

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

## COM Interop 작업

Aspose.PDF for .NET은 .NET Framework의 제어하에 실행되며 이를 관리 코드라고 합니다. 위에 언급된 모든 언어로 작성된 코드는 .NET Framework 외부에서 실행되며 이를 관리되지 않는 코드라고 합니다. 관리되지 않는 코드와 Aspose.PDF 간의 상호 작용은 COM Interop이라는 .NET 기능을 통해 발생합니다.

Aspose.PDF 객체는 .NET 객체이지만, COM Interop을 통해 사용될 때에는 프로그래밍 언어에서 COM 객체로 나타납니다.
Aspose.PDF 객체는 .NET 객체입니다. 하지만 COM Interop을 통해 사용될 때, 프로그래밍 언어에서 COM 객체로 나타납니다.

{{% alert color="primary" %}}

- COM 세계에서는 COM 서버와 COM 클라이언트를 구분합니다. COM 서버는 COM 클래스를 저장하며 COM 클라이언트는 클래스 인스턴스, 즉 COM 객체를 COM 서버에 요청합니다.
- COM 클라이언트 또는 단순히 클라이언트 애플리케이션은 COM 클래스의 내용을 알 수도 있고, 그 메소드와 속성에 대해 전혀 모를 수도 있습니다. 따라서 클라이언트 애플리케이션은 컴파일/빌딩 시 또는 실행 중에만 COM 클래스 구조를 발견할 수 있습니다. 이러한 "발견" 과정을 바인딩이라고 하며, 이에는 **조기 바인딩**과 **늦은 바인딩**이 있습니다.
- 간단히 말해 COM 클래스는 검은 상자와 같고, 이를 작업하기 위해 타입 라이브러리가 필요합니다. 이 이진 파일에는 COM 클래스의 메소드, 속성에 대한 설명이 포함되어 있으며, COM 객체를 지원하는 모든 고급 언어는 타입 라이브러리를 추가하는 구문 표현을 종종 가지고 있습니다. 예를 들어 C++에서는 이것이 [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx)입니다.

- 간단히 말해 COM 클래스는 검은 상자와 같고 작동하려면 타입 라이브러리가 필요합니다. 이 바이너리 파일은 COM 클래스 메소드, 속성에 대한 설명을 가지고 있으며 COM 객체를 지원하는 모든 고급 언어는 종종 타입 라이브러리를 추가하는 구문 표현을 가지고 있습니다. 예를 들어, C++에서는 [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) 입니다.
- 타입 라이브러리는 조기 바인딩을 위해 사용됩니다.
- COM 객체는 두 가지 방식으로 메소드와 속성을 노출할 수 있습니다: **dispatch interface** (dispinterface)를 통해 그리고 **vtable** (가상 함수 테이블)에서.
- **dispinterface** 내에서, 각 메소드와 속성은 고유한 회원에 의해 식별됩니다; 이 회원은 함수의 디스패치 식별자(또는 **DispID**)입니다.
- **vtable**은 단지 COM 클래스 인터페이스가 지원하는 함수들에 대한 포인터의 집합입니다.
- 두 인터페이스를 통해 메소드를 노출하는 객체는 **듀얼 인터페이스**를 지원합니다.
- 두 가지 유형의 바인딩 모두 장점이 있습니다.
- 두 종류의 바인딩에는 장점이 있습니다.
- 후바인딩 메커니즘에는 큰 장점이 있습니다: COM DLL의 제작자가 다른 함수 인터페이스 레이아웃을 가진 새 버전을 출시하기로 결정하면, 해당 메소드를 호출하는 코드는 메소드가 더 이상 사용할 수 없을 때까지 충돌하지 않습니다; **vtable**이 달라도 후바인딩은 새로운 DISPIDs를 발견하고 적절한 메소드를 호출할 수 있습니다.
{{% /alert %}}

다음은 결국 마스터해야 할 주제들입니다:
{{% alert color="primary" %}}

- 프로그래밍 언어에서 COM 객체 사용하기. 프로그래밍 언어 문서 및 이 문서에서 더 자세한 언어별 주제를 참조하세요.

- .NET COM Interop에 의해 노출된 COM 객체 작업하기. MSDN의 [비관리 코드와 상호 운용](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) 및 [COM에 .NET 프레임워크 구성 요소 노출](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx)을 참조하세요.

- Aspose.PDF 문서 객체 모델.
- Aspose.PDF 문서 객체 모델.

{{% /alert %}}

## Aspose.PDF for .NET을 COM Interop와 함께 등록하기

Aspose.PDF for .NET을 설치하고 COM Interop에 등록되어 있는지 확인해야 합니다(관리되지 않는 코드에서 호출할 수 있음을 보장).

{{% alert color="primary" %}}

Aspose.PDF for .NET을 수동으로 COM Interop에 등록하려면:

1. **시작** 메뉴에서 **모든 프로그램**, 그 다음 **Microsoft Visual Studio**, **Visual Studio 도구**를 선택하고, 마지막으로 **Visual Studio 명령 프롬프트**를 선택합니다.
1. 어셈블리를 등록하기 위한 명령을 입력합니다:
   1. .NET Framework 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /codebase
   1. .NET Framework 3.5
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /codebase
   1. .NET Framework 4.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Aspose.PDF.dll이 GAC에 없는 경우에만 /codebase가 필요함을 주의하세요. 이 옵션을 사용하면 regasm이 어셈블리 경로를 레지스트리에 넣습니다.
/코드베이스는 Aspose.PDF.dll이 GAC에 없는 경우에만 필요하며, 이 옵션을 사용하면 regasm이 레지스트리에 어셈블리 경로를 설정하도록 합니다.

{{% alert color="primary" %}}

regasm.exe는 .NET Framework SDK에 포함된 도구입니다. 모든 .NET Framework SDK 도구는 *\Microsoft .NET\Framework\<FrameworkVersion>* 디렉토리에 위치해 있습니다. 예를 들어 *C:\Windows\Microsoft .NET\Framework\v4.0.30319*입니다. Visual Studio .NET을 사용하는 경우:
**시작** 메뉴에서 **프로그램**, 그 다음 **Microsoft Visual Studio .NET**, **Visual Studio .NET 도구**를 선택하고 마지막으로 **Visual Studio .NET 2003 명령 프롬프트**를 선택합니다.
필요한 모든 환경 변수가 설정된 명령 프롬프트가 실행됩니다.

{{% /alert %}}

### ProgIDs

ProgID는 "프로그래밍 식별자"를 의미합니다. 이는 객체를 생성하는 데 사용되는 COM 클래스의 이름입니다. ProgIDs는 라이브러리 이름 "Aspose.PDF"와 클래스 이름으로 구성됩니다.

### Type Library

{{% alert color="primary" %}}

프로그래밍 언어(예: Visual Basic 또는 Delphi)가 COM 타입 라이브러리를 참조할 수 있는 경우, Aspose.PDF.tlb에 참조를 추가하고 Object Browser에서 Aspose.PDF for .NET 클래스, 메소드, 속성 및 열거형을 모두 확인하세요.
만약 여러분의 프로그래밍 언어(예를 들어 Visual Basic 또는 Delphi)가 COM 유형 라이브러리를 참조할 수 있다면, Aspose.PDF.tlb에 대한 참조를 추가하고 Object Browser에서 Aspose.PDF for .NET의 모든 클래스, 메서드, 속성 및 열거형을 확인하세요.

TLB 파일을 생성하기 위해:

- .NET Framework 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.tlb" /codebase
- .NET Framework 3.5
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.tlb" /codebase
- .NET Framework 4.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## COM 객체 생성

COM 객체를 생성하는 것은 일반적인 .NET 객체를 생성하는 것과 유사합니다:

```vb

'Instantiate Pdf instance by calling its empty constructor

Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

```
일단 생성하면, 객체의 메소드와 속성에 COM 객체처럼 접근할 수 있습니다:

```vb
'Pdf 객체에 섹션 추가
pdf.Sections.Add(pdfsection)
```

일부 메소드에는 오버로드가 있으며, COM Interop을 통해 노출될 때 숫자 접미사가 추가됩니다. 예를 들어, Pdf.Save 메소드 오버로드는 Pdf.Save, Pdf.Save_2 등으로 됩니다.

더 많은 정보는 이 문서에서 언어별 기사를 참조하세요.

## 래퍼 어셈블리 생성하기

Aspose.PDF for .NET의 많은 클래스, 메소드 및 속성을 사용해야 하는 경우, 래퍼 어셈블리를 생성하는 것을 고려하세요 (C# 또는 다른 .NET 프로그래밍 언어 사용). 래퍼 어셈블리는 관리되지 않는 코드에서 직접 Aspose.PDF for .NET을 사용하는 것을 피하는 데 도움이 됩니다.

좋은 접근 방식은 Aspose.PDF for .NET을 참조하는 .NET 어셈블리를 개발하고 그것으로 모든 작업을 처리하며, 최소한의 클래스와 메소드만을 관리되지 않는 코드에 노출하는 것입니다.
.NET 어셈블리를 개발하여 Aspose.PDF for .NET을 참조하고 모든 작업을 수행하며, 관리되지 않는 코드에는 최소한의 클래스와 메서드만 노출하는 것이 좋은 접근 방식입니다.

COM Interop을 통해 호출해야 하는 클래스와 메서드의 수를 줄이면 프로젝트가 단순해집니다. .NET 클래스를 COM Interop을 통해 사용하는 것은 종종 고급 기술이 필요합니다.
