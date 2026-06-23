---
title: 매개변수 설정
linktitle: 매개변수 설정
type: docs
weight: 10
url: /ko/reportingservices/setting-parameters/
description: Aspose.PDF for Reporting Services에서 PDF 렌더링에 대한 매개변수를 설정하는 방법을 확인하십시오. 출력에 대한 정확한 제어를 달성합니다.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services가 문서를 생성하는 방식에 영향을 주는 특정 구성 매개변수를 지정할 수 있습니다. 이 섹션에서는 이 과정을 설명합니다.

{{% /alert %}}

Aspose.Pdf for Reporting Services를 구성하려면 C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config 파일을 편집해야 합니다. 이 파일은 XML 파일이며 렌더러 구성은 내부에 ```<Extension>``` Aspose.PDF 렌더러에 해당하는 요소.

**예시**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% alert color="primary" %}}

특정 보고서 파일에 대한 매개변수를 설정하고 서버의 모든 보고서에 적용하고 싶지 않다면, 다음 단계와 같이 Report Builder에서 해당 보고서를 위한 보고서 매개변수를 추가할 수 있습니다(예: 앞에서 표시한 ‘IsLandscape’ 매개변수를 추가합니다):

1. Report Designer에서 보고서를 연 후, ‘Report Data’ 창의 ‘Parameters’ 폴더를 마우스 오른쪽 버튼으로 클릭하고 ‘Add Parameter…’를 선택합니다(또는 ‘New’ 목록을 내려 ‘Parameter…’를 선택할 수도 있습니다).
 
![todo:image_alt_text](setting-parameters_1.png)

1. ‘Report Parameter Properties’ 대화 상자에서 ‘IsLandscape’라는 이름의 매개변수를 만들고, 데이터 유형을 Boolean으로 지정한 뒤 ‘Default Values’ 탭에 값 True를 추가합니다.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}


