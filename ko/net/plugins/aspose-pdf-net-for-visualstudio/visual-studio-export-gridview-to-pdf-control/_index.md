---
title: Visual Studio Export GridView To PDF 컨트롤
type: docs
weight: 10
url: ko/net/visual-studio-export-gridview-to-pdf-control/
---

## 소개

Export GridView To Pdf Control은 [Aspose.PDF](http://www.aspose.com/.net/pdf-component.aspx)를 사용하여 GridView의 내용을 Pdf 문서로 내보내는 ASP.NET 서버 컨트롤입니다. 이 컨트롤은 GridView 컨트롤 상단에 **PDF로 내보내기** 버튼을 추가합니다. 이 버튼을 클릭하면 GridView 컨트롤의 내용이 동적으로 Pdf 문서로 내보내지며, 사용자가 선택한 디스크 위치로 내보낸 파일이 몇 초 안에 자동으로 다운로드됩니다.

### 모듈 기능

이 초기 버전의 컨트롤은 다음과 같은 기능을 제공합니다:

- 온라인 GridView 콘텐츠의 오프라인 복사본을 편집, 공유 및 인쇄할 수 있는 매우 인기 있는 Pdf 문서로 가져옵니다.
- 기본 ASP.NET GridView 컨트롤에서 상속되므로 모든 기능과 속성을 가지고 있습니다.
- .NET 2.0부터 시작하는 모든 .NET 버전과 함께 작동합니다.
- 내보내기 버튼 텍스트를 사용자 정의/지역화할 수 있는 기능.
- 내보내기 버튼 텍스트 사용자 정의/현지화 기능
- GridView 콘텐츠가 넓어 기본 세로 모드에 맞지 않는 경우 가로 모드로 내보내기 옵션
- css를 사용하여 내보내기 버튼에 자신의 테마 스타일 적용
- 내보낸 문서 상단에 사용자 정의 제목 추가 옵션
- 구성 가능한 디스크 경로에 각 내보낸 문서 저장 옵션
- 페이징이 활성화된 경우 현재 페이지 또는 모든 페이지 내보내기 옵션

## 시스템 요구사항 및 지원 플랫폼

### 시스템 요구사항

Visual Studio용 Export GridView To Pdf 제어는 IIS 및 .NET 프레임워크 2.0 이상이 설치된 모든 시스템에서 사용할 수 있습니다.

### 지원 플랫폼

Visual Studio용 Export GridView To Pdf 제어는 .NET 프레임워크 2.0 이상에서 실행되는 모든 버전의 ASP.NET을 지원합니다. 다음 Visual Studio 버전 중 하나를 사용하여 ASP.NET 애플리케이션에서 이 제어를 사용할 수 있습니다.

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013

## 다운로드
## 다운로드

다음 위치 중 하나에서 Export GridView To Pdf Control을 다운로드할 수 있습니다.

- [CodePlex](https://asposevs.codeplex.com/releases/view/617022)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0)

## 설치

Export GridView To Pdf Control을 설치하는 것은 매우 간단하고 쉽습니다. 다음 간단한 단계를 따르십시오.

### **Visual Studio 2010, 2012 및 2013용**

1. 다운로드한 zip 파일을 추출하십시오. 예: Aspose.PDF.GridViewExport_1.0.zip
1. VSIX 파일 Aspose.PDF.GridViewExport.vsix를 더블 클릭하십시오.
1. 설치 가능하고 지원되는 Visual Studio 버전이 표시된 대화 상자가 나타납니다.
1. Export GridView To Pdf Control을 추가할 버전을 선택하십시오.
1. 설치를 클릭하십시오.

설치가 완료되면 성공 대화 상자가 나타납니다.

**참고:** 변경 사항이 적용되려면 Visual Studio를 다시 시작해야 합니다.

### **Visual Studio 2005, 2008 및 Express 에디션용**

Export GridView To Pdf Control을 Visual Studio에 통합하여 다른 ASP.NET 컨트롤처럼 쉽게 드래그 앤 드롭할 수 있도록 다음 단계를 따르십시오.
Visual Studio에서 Export GridView To Pdf 컨트롤을 쉽게 드래그 앤 드롭할 수 있도록 통합하기 위한 다음 단계를 따르십시오.

1. 다운로드한 zip 파일을 추출하십시오. 예: Aspose.PDF.GridViewExport.NET2.0_1.0.zip
1. Visual Studio를 관리자로 실행하는지 확인하십시오.

도구 메뉴에서 도구 상자 항목 선택을 클릭하십시오.

1. 찾아보기를 클릭하십시오.
   열기 대화 상자가 나타납니다.
1. 추출된 폴더로 이동하여 Aspose.PDF.GridViewExport.dll을 선택하십시오.
1. 확인을 클릭하십시오.

aspx 또는 ascx 컨트롤을 열면 왼쪽 도구 상자의 일반 탭에서 ExportGridViewToPdf를 볼 수 있습니다.

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## 사용

설치 후 ASP.NET 응용 프로그램에서 이 컨트롤을 사용하기 시작하는 것은 매우 쉽습니다.

|**.NET framework 4.0 이상용**|**.NET framework 2.0 이상용**|** |
| :- | :- | :- |
|Visual Studio 2010 이상에서 .NET framework 4.0 이상에서 실행되는 애플리케이션의 경우 도구 모음의 Aspose 탭에서 아래와 같이 **ExportGridViewToPdf** 컨트롤을 볼 수 있어야 합니다.
.NET 프레임워크 4.0 이상에서 실행되는 응용 프로그램 및 Visual Studio 2010 이상에서는 아래와 같이 툴바의 **Aspose** 탭에서 **ExportGridViewToPdf** 컨트롤을 볼 수 있어야 합니다.

### ExportGridViewToPdf 컨트롤을 수동으로 추가하기

위의 방법을 사용하여 Visual Studio 툴박스를 사용하는 데 문제가 있는 경우, .NET 프레임워크 2.0 이상에서 실행되는 ASP.NET 애플리케이션에 이 컨트롤을 수동으로 추가할 수 있습니다.

1. Visual Studio를 사용하는 경우 관리자로 실행하세요
1. ASP.NET 프로젝트 또는 웹 애플리케이션에서 다운로드 패키지에서 추출된 **Aspose.PDF.GridViewExport.dll**에 대한 참조를 추가하세요. 웹 애플리케이션/Visual Studio가 이 폴더에 완전히 접근할 수 있어야 하며 그렇지 않으면 접근이 거부되었다는 예외가 발생할 수 있습니다.
1. 페이지, 컨트롤 또는 마스터 페이지의 상단에 다음 줄을 추가하세요

```csharp
 <%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```
```csharp
 <aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### 자주 묻는 질문들

이 컨트롤을 사용하면서 마주칠 수 있는 일반적인 질문과 문제들

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. 도구 상자에서 ExportGridViewToPdf 컨트롤을 볼 수 없습니다</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <p><strong>Visual Studio 2010 이상</strong></p>
<ol><li>다운로드한 패키지에서 찾은 VSIX 확장 파일을 사용하여 이 컨트롤을 설치했는지 확인하세요. 확인하려면 도구 -&gt; 확장 및 업데이트로 이동합니다. 설치된 항목 아래에서 'Aspose Export Export GridView To Pdf Control'을 보아야 합니다. 보이지 않으면 다시 설치해 보세요.</li>
<li>.NET 프레임워크 4.0 이상에서 웹 애플리케이션이 실행되고 있는지 확인하세요. .NET 프레임워크의 낮은 버전의 경우 위의 다른 방법을 확인하세요.
```
<li>.NET 프레임워크 4.0 이상에서 웹 애플리케이션이 실행되고 있는지 확인하세요. .NET 프레임워크의 이전 버전에 대해서는 위의 대체 방법을 확인해 주세요.
이전 버전의 Visual Studio</li>
<li>위의 지시에 따라 해당 컨트롤을 수동으로 툴박스에 추가했는지 확인하세요.</li></ol>
          </div>
        </div>
    </div>

    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">2. 애플리케이션 실행 시 '접근이 거부됨' 오류가 발생합니다</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <ol>
               <li>이 문제가 생산 환경에서 발생하는 경우, Aspose.PDF.dll과 Aspose.PDF.GridViewExport.dll을 모두 bin 폴더에 복사했는지 확인하세요.</li>
               <li>Visual Studio를 사용 중이라면 이미 관리자로 로그인되어 있다 하더라도 관리자 권한으로 실행하십시오.</li>
```
### **Aspose .NET Export GridView To Pdf 제어 속성**

다음 속성은 이 제어에서 제공하는 멋진 기능을 구성하고 사용하도록 노출됩니다.

|**속성 이름**|**유형**|**예시/가능한 값들**|**설명**|
| :- | :- | :- | :- |
|ExportButtonText|string|Export to Pdf|기본 텍스트를 재정의하는 데 이 속성을 사용할 수 있습니다|
|ExportButtonCssClass|string|btn btn-primary|내보내기 버튼의 외부 div에 적용되는 Css 클래스입니다. 버튼에 css를 적용하려면 .yourClass input을 사용할 수 있습니다|
|ExportInLandscape|bool|true or false|true인 경우 출력 문서의 방향을 가로로 변경합니다. 기본값은 세로입니다|
| | | | |
|ExportFileHeading|string|GridView Export Example Report|제목에 스타일을 추가하기 위해 html 태그를 사용할 수 있습니다|
|ExportOutputPathOnServer|string|c:/temp|서버에서 내보낸 사본이 자동으로 저장되는 로컬 출력 디스크 경로입니다|
|ExportOutputPathOnServer|string|c:/temp|서버에서 자동으로 저장되는 내보내기 사본의 로컬 출력 디스크 경로입니다.
|ExportDataSource|object|allRowsDataTable|이 데이터 바인드 컨트롤이 데이터 항목 목록을 검색하는 객체를 설정합니다. 객체는 내보낼 필요가 있는 모든 데이터를 가져야 합니다. 이 속성은 일반 DataSource 속성과 함께 사용되며 사용자 지정 페이징이 활성화되어 있고 현재 페이지가 화면에 표시할 행만 가져오는 경우 유용합니다.
|LicenseFilePath|string| |예를 들어 c:/inetpub/Aspose.PDF.lic 서버의 라이선스 파일의 로컬 경로입니다.

아래에는 모든 속성을 사용한 Export GridView to Pdf 컨트롤의 예가 나와 있습니다.

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="PDF로 내보내기"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>예제 보고서</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```
## 비디오 데모

아래 [비디오](https://www.youtube.com/watch?v=WNJ7T8u4JlM)를 확인하여 모듈을 작동하는 모습을 보세요.

### 지원

Aspose의 초기부터, 우리는 고객에게 좋은 제품만 제공하는 것으로 충분하지 않다는 것을 알고 있었습니다. 좋은 서비스도 제공해야 했습니다. 우리도 개발자이기 때문에 기술적 문제나 소프트웨어의 오류로 인해 필요한 작업을 수행할 수 없을 때 얼마나 답답한지 이해합니다. 문제를 해결하러 왔지, 문제를 만들러 온 것이 아닙니다.

이것이 우리가 무료 지원을 제공하는 이유입니다. 우리 제품을 구매하든, 평가판을 사용하든 간에, 모든 사용자는 우리의 전적인 주의와 존중을 받을 자격이 있습니다.

다음 플랫폼을 사용하여 이 Pdf와 관련된 문제나 제안을 로그할 수 있습니다.

- [CodePlex](https://asposevs.codeplex.com/workitem/list/basic)
- [Visual Studio Gallery - Q and A](https://visualstudiogallery.msdn.microsoft.com/fb8b9944-cfe5-44a9-8aa7-c785d32d1066)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)

### 확장하고 기여하기

Aspose .NET Export GridView To Pdf for Visual Studio는 오픈 소스이며 소스 코드는 아래에 나열된 주요 소셜 코딩 웹사이트에서 사용할 수 있습니다. 개발자는 소스 코드를 다운로드하여 자신의 요구에 맞게 기능을 확장할 수 있습니다.

#### 소스 코드

다음 위치 중 하나에서 최신 소스 코드를 받을 수 있습니다

- [CodePlex](https://asposevs.codeplex.com/SourceControl/latest#Aspose.PDF.GridViewExport/)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport)

#### 소스 코드 구성 방법

소스 코드를 열고 확장하려면 다음이 설치되어 있어야 합니다

- Visual Studio 2010

시작하려면 다음 간단한 단계를 따르세요

1. 소스 코드를 다운로드/복제합니다.
1.
1.
1. 최신 소스 코드를 다운로드한 곳으로 이동하여 **Aspose.PDF.GridViewExport.sln**을 엽니다.

#### 소스 코드 개요

해결책에는 세 개의 프로젝트가 있습니다.

- Aspose.PDF.GridViewExport - VSIX 패키지와 .NET 4.0용 서버 Pdf를 포함합니다.
- Aspose.PDF.GridViewExport_DotNet_2.0 - .NET 2.0용 확장된 GridView Pdf
- Aspose.PDF.GridViewExport.Website - Word 내보내기 가능한 GridView Pdf를 테스트하기 위한 웹 프로젝트
