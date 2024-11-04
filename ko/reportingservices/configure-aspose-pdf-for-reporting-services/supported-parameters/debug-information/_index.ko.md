---
title: 디버그 정보
type: docs
weight: 90
url: /reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

렌더링 또는 렌더링된 결과에 문제가 있는 것은 피할 수 없습니다. 비밀이나 개인 정보 보호와 같은 이유로 인해 사용자의 보고서에서 사용된 데이터 소스를 얻을 수 없으므로 보고서의 오류를 재현할 수 없습니다. 고객과 개발자 간의 의사소통을 더 쉽고 원활하게 하기 위해 이 매개변수를 추가했습니다. Aspose.PDF for Reporting Services로 보고서를 렌더링할 때 문제가 발생하면 이 보고서 매개변수를 설정하십시오. 그러면 XML 형식으로 렌더링된 문서를 받게 됩니다. 그런 다음 제품 포럼에 XML 파일을 게시하십시오.

{{% /alert %}}

{{% alert color="primary" %}}
**매개변수 이름**: SavingXmlFormat  
**데이터 유형**: Boolean  
**지원되는 값**: True, False (기본값)  

**예시**
{{< highlight csharp >}}

<Render>
...

<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">

<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```