---
title: Setting Parameters
linktitle: Setting Parameters
type: docs
weight: 10
url: /ko/reportingservices/setting-parameters/
description: Aspose.PDF for Reporting Services에서 PDF 렌더링 매개변수를 설정하여 출력 결과를 정밀하게 제어하는 방법을 알아보세요.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

You can specify certain configuration parameters that affect how Aspose.PDF for Reporting Services generates documents. This section describes this process.

{{% /alert %}}

Aspose.PDF for Reporting Services를 구성하려면 `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config` 파일을 편집해야 합니다. 이 파일은 XML 파일이며, 렌더러 구성은 Aspose.PDF 렌더러에 해당하는 ```<Extension>``` 요소 안에 있습니다.

**Example**

{{< highlight csharp >}}

<Render>
...
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

특정 보고서 파일에만 매개변수를 설정하고 서버의 모든 보고서에는 적용하지 않으려면, 다음 단계에 따라 Report Builder에서 해당 보고서에 보고서 매개변수를 추가할 수 있습니다. 여기서는 앞에서 보여 준 `IsLandscape` 매개변수를 추가하는 예를 사용합니다.

1. Report Designer에서 보고서를 열고 `Report Data` 창의 `Parameters` 폴더를 마우스 오른쪽 버튼으로 클릭한 다음 `Add Parameter...`를 선택합니다. 또는 `New` 목록을 열고 `Parameter...`를 선택해도 됩니다.
 
![todo:image_alt_text](setting-parameters_1.png)

1. `Report Parameter Properties` 대화 상자에서 `IsLandscape`라는 이름의 매개변수를 만들고, 데이터 형식을 Boolean으로 설정한 뒤, `Default Values` 탭에 True 값을 추가합니다.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}
