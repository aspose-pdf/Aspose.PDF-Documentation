---
title: 선 화살표
linktitle: 선 화살표
type: docs
weight: 20
url: /ko/reportingservices/line-arrows/
description: Aspose.PDF for Reporting Services를 사용하여 PDF 보고서에 선 화살표를 추가하는 방법을 배우세요. 보고서 시각 효과를 손쉽게 강화합니다.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

RDL 사양에는 선 요소에 대한 화살표가 명시되어 있지 않아, Report Builder는 선에 화살표 설정을 지원하지 않습니다. Aspose.PDF for Reporting Services를 사용하면 이를 쉽게 구현할 수 있습니다.

{{% /alert %}}

{{% alert color="primary" %}}

현재 Aspose.PDF 렌더러는 사용자 지정 속성을 추가하여 선의 시작 또는 끝에 화살표를 추가하는 것을 지원합니다.

라인에 시작 화살표를 추가  
**사용자 정의 속성** **이름**: HasArrowAtStart  
**사용자 정의 속성 값**: True  

라인에 끝 화살표를 추가  
**사용자 정의 속성** **이름**: HasArrowAtEnd  
**사용자 정의 속성 값**: True  

예를 들어, 현재 보고서 파일에 'line1'과 'line2'라는 두 개의 라인이 있고, line1은 시작 화살표가 있으며, line2는 시작 및 끝 화살표가 있습니다. 이러한 요구사항을 충족하려면 다음 코드 조각과 같이 사용자 정의 속성을 추가할 수 있습니다.

**예시**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>시작에 화살표가 있음</Name>
        <Value>참</Value>
      </CustomProperty>
    </CustomProperties>
</Line>
......
<Line Name="line2">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>시작에 화살표가 있음</Name>
        <Value>참</Value>
      </CustomProperty>
<CustomProperty>
        <Name>끝에 화살표가 있음</Name>
        <Value>참</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
