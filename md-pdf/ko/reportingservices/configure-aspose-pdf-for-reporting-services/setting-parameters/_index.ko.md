---
title: 매개 변수 설정
type: docs
weight: 10
url: /reportingservices/setting-parameters/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.Pdf for Reporting Services가 문서를 생성하는 방식에 영향을 미치는 특정 구성 매개 변수를 지정할 수 있습니다. 이 섹션에서는 이 과정을 설명합니다.

{{% /alert %}}

Aspose.Pdf for Reporting Services를 구성하려면 C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config 파일을 편집해야 합니다. 이 파일은 XML 파일이며 렌더러 구성은 Aspose.PDF 렌더러에 해당하는 ```<Extension>``` 요소 내에 있습니다.

**예제**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--PDF로 내보내기 위한 구성 요소를 여기에 삽입합니다. 다음은 PageOrientation의 예입니다 -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}


{{% alert color="primary" %}}

특정 보고서 파일에 대한 매개변수를 설정하고 싶지만 서버의 모든 보고서에 대해 설정하고 싶지 않은 경우, 다음 단계에 따라 Report Builder에서 특정 보고서에 대한 보고서 매개변수를 추가할 수 있습니다 (예를 들어, 앞서 언급한 'IsLandscape' 매개변수를 추가할 것입니다):

1. 보고서를 Report Designer에서 열고, 'Report Data' 창의 'Parameters' 폴더를 마우스 오른쪽 버튼으로 클릭한 후 'Add Parameter…'를 선택합니다 (또는, 'New' 목록을 펼쳐 'Parameter…'를 선택합니다).

![todo:image_alt_text](setting-parameters_1.png)

1. 'Report Parameter Properties' 대화 상자에서, 'IsLandscape'라는 이름의 매개변수를 생성하고 데이터 유형을 Boolean으로 설정한 다음 'Default Values' 탭에서 값 True를 추가합니다.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}