---
title: Line Arrows
type: docs
weight: 20
url: /reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RDL 사양은 선 요소에 대한 화살표를 지정하지 않으므로 보고서 작성기는 선에 대한 화살표 설정을 지원하지 않습니다. Aspose.Pdf for Reporting Services를 사용하면 이를 쉽게 수행할 수 있습니다.

{{% /alert %}}

{{% alert color="primary" %}}

현재 Aspose.PDF 렌더러는 사용자 지정 속성을 추가하여 선의 시작 또는 끝에 화살표를 추가하는 것을 지원합니다.

선의 시작 화살표 추가  
**사용자 지정 속성 이름**: HasArrowAtStart  
**사용자 지정 속성 값**: True  

선의 끝 화살표 추가  
**사용자 지정 속성 이름**: HasArrowAtEnd  
**사용자 지정 속성 값**: True  

예를 들어, 현재 보고서 파일에 'line1'과 'line2'라는 두 개의 선이 있고, line1은 시작 화살표가 있으며, line2는 시작 및 끝 화살표가 있는 경우, 이러한 요구 사항을 충족시키기 위해 다음 코드 조각과 같이 사용자 지정 속성을 추가할 수 있습니다.

**예제**

{{< highlight csharp >}}

 <Line Name="line1">
```

<Style>
  ......
</style>
<CustomProperties>
  <CustomProperty>
    <Name>HasArrowAtStart</Name>
    <Value>True</Value>
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
    <Name>HasArrowAtStart</Name>
    <Value>True</Value>
  </CustomProperty>
  <CustomProperty>
    <Name>HasArrowAtEnd</Name>
    <Value>True</Value>
  </CustomProperty>
</CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
```