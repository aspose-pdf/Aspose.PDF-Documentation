---
title: Aspose.Pdf for .NET을 Coldfusion과 함께 사용하기
type: docs
weight: 300
url: /net/using-aspose-pdf-for-net-with-coldfusion/
description: Aspose.Pdf for .NET을 Coldfusion에서 PdfFileInfo 클래스를 사용하여 작업해야 합니다.
lastmod: "2021-07-14"
draft: false
---

{{% alert color="primary" %}}

이 기사에서는 Aspose.PDF for .NET을 Coldfusion과 함께 사용하는 방법을 설명합니다. Aspose.PDF for .Net과 Coldfusion 통합의 세부 사항을 이해하는 데 도움이 될 것입니다. 간단한 예를 통해 Aspose.PDF for .Net의 기능을 Coldfusion 애플리케이션에 통합하는 과정을 보여 드리겠습니다.

{{% /alert %}}

## 배경

Aspose.PDF for .NET은 기존 PDF 파일을 편집하고 조작할 수 있는 기능도 제공하는 구성 요소입니다.
Aspose.PDF for .NET은 기존 PDF 파일을 편집하고 조작할 수 있는 기능도 제공하는 구성 요소입니다.

## Prerequisite

Aspose.PDF for .Net를 Coldfusion과 함께 실행하려면 IIS, .Net 2.0, 그리고 Coldfusion이 필요합니다. 저는 IIS 5, .Net 2.0, 그리고 Colfusion 8을 사용하여 구성 요소를 테스트했습니다. Coldfusion을 설치하는 동안 확인해야 할 두 가지가 더 있습니다. 첫째, IIS 아래에서 Coldfusion을 실행할 사이트를 지정해야 합니다. 둘째, Coldfusion 설치 프로그램에서 '.Net Integration Services'를 선택해야 합니다. .Net Integration Services는 Coldfusion 애플리케이션에서 .Net 구성 요소 어셈블리에 접근할 수 있게 해줍니다; 이 경우 구성 요소는 Aspose.PDF for .NET이 될 것입니다.

## Explanation

먼저 DLL(Aspose.PDF .dll)을 나중에 사용하기 위해 접근할 위치로 복사해야 합니다; 이 경로는 설정되어 cfobject 태그의 어셈블리 속성에 할당됩니다. 아래에 표시된 것처럼:

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.PDF.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```
위 태그에서 attribute class는 Aspose.PDF. Facades 클래스를 가리킵니다. 이 경우는 PdfFileInfo입니다. name attribute는 클래스의 인스턴스 이름이며 나중에 코드에서 클래스 메소드나 속성에 접근할 때 사용됩니다. type attribute는 컴포넌트의 유형을 지정합니다 - 우리의 경우는 .Net입니다.

Coldfusion에서 .Net 컴포넌트를 사용할 때 중요하게 기억해야 할 점은, 클래스 객체의 어떤 속성을 가져오거나 설정할 때 특정 구조를 따라야 한다는 것입니다. 속성을 설정할 때는 Set_propertyname 같은 구문을 사용하고, 속성 값을 가져올 때는 Get_propertyname을 사용합니다.

예를 들어

속성 값을 설정:

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

속성 값을 가져오기:

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

Coldfusion에서 Aspose.PDF for .NET을 사용하는 과정을 이해하는 데 도움이 될 기본적이면서도 완전한 예제입니다.

### PDF 파일 정보를 보여줍니다

```html
<!--- PdfFileInfo 클래스의 인스턴스 생성 --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.PDF.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- pdf 파일 경로 가져오기 --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- 클래스 객체에 pdf 파일 경로를 입력파일 속성으로 할당 --->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- 파일 정보 표시 --->

<cfoutput><b>제목:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>주제:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>저자:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>생성자:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```
## 결론

{{% alert color="primary" %}}
이 기사에서는 Coldfusion과 .Net 통합의 몇 가지 기본 규칙을 따르면, Aspose.PDF for .NET을 사용하여 Coldfusion 애플리케이션에서 PDF 문서 조작과 관련된 많은 기능과 유연성을 통합할 수 있음을 보았습니다.
{{% /alert %}}
