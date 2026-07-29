---
title: 디버그 정보
linktitle: 디버그 정보
type: docs
weight: 90
url: /ko/reportingservices/debug-information/
description: Aspose.PDF for Reporting Services에서 PDF 렌더링에 대한 디버그 정보를 액세스하고 분석하여 문제를 효과적으로 해결하십시오.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

렌더링이나 렌더링 결과에 문제가 있는 것은 불가피합니다. 기밀성이나 프라이버시와 같은 이유로 사용자의 보고서에 사용된 데이터 소스를 얻을 수 없어서 보고서에서 오류를 재현할 수 없었습니다. 고객과 개발자 간의 커뮤니케이션을 더 쉽고 원활하게 만들기 위해 이 매개변수를 추가했습니다. Aspose.PDF for Reporting Services로 보고서를 렌더링할 때 문제가 발생하면 이 보고서 매개변수를 설정하십시오. 그러면 XML 형식의 렌더링된 문서를 받을 수 있습니다. 그 후, 제품 포럼에 XML 파일을 게시해 주세요.

{{% /alert %}}

{{% alert color="primary" %}}
**매개변수 이름**: SavingXmlFormat  
**데이터 형식**: Boolean  
**지원되는 값**: True, False (default)  

**예시**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > 참 </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
