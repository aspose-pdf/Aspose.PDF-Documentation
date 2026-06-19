---
title: HTML 서식
linktitle: HTML 서식
type: docs
weight: 20
url: /ko/reportingservices/html-formatting/
description: Aspose.PDF for Reporting Services를 사용하여 PDF 보고서에서 HTML 서식을 활성화합니다. 스타일과 구조를 손쉽게 추가합니다.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

때때로 텍스트 상자에서 서식이 적용된 텍스트를 내보내고 싶을 수 있습니다. 불행히도 Reporting Services는 이를 지원하지 않습니다. 그러나 여전히 Aspose.PDF for Reporting Services를 사용하여 구현할 수 있습니다. 텍스트 상자 내 모든 텍스트를 HTML로 처리하고 필요한 HTML 태그를 넣어 출력 문서에서 텍스트를 서식 지정하는 특수 모드를 활성화하기만 하면 됩니다. 예를 들어, 동일한 텍스트 상자에 일반, 굵게 및 기울임 텍스트를 표시하려면 다음 텍스트 상자 값을 입력하세요:

이 텍스트 중 일부는 ```<b>bold</b>``` 그리고 다른 텍스트는 ```<i>italic</i>```.

내보낸 후에는 이 텍스트 중 일부는 **bold**, 다른 텍스트는 *italic*처럼 보입니다.

이 접근 방식에는 몇 가지 제한 사항이 있음을 참고하십시오.

{{% /alert %}}

{{% alert color="primary" %}}

- 디자인 시간(Report Builder, Reporting Services 웹 포털 등)에서는 서식이 표시되지 않습니다. 대신 HTML 텍스트가 태그가 포함된 일반 텍스트 형태로 보입니다.
- Aspose.PDF for Reporting Services 렌더링 확장 기능은 텍스트 상자에서 HTML 코드를 인식하고 올바르게 서식 지정합니다. Reporting Services의 기본 PDF 렌더러는 이 마크업을 일반 텍스트로 내보냅니다.

**매개변수 이름**: IsHtmlTagSupported  
**날짜 유형**: Boolean  
**지원되는 값**: True, False (default)   

**예제**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

Report Designer에 이 매개변수를 추가하려면 'Boolean' 데이터 유형을 사용하십시오.

 
현재 Aspose.Pdf for Reporting Services는 모든 HTML 태그 중 일부만 지원합니다. 자세한 정보는 Aspose.PDF에서 찾을 수 있습니다. [문서](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}


