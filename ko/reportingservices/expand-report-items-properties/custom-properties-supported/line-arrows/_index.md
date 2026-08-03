---
title: 선 화살표
linktitle: 선 화살표
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: Reporting Services용 Aspose.PDF를 사용하여 PDF 보고서에 선 화살표를 추가하는 방법을 알아보세요. 손쉽게 보고서 시각적 요소를 향상하세요.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RDL 사양은 선 요소에 대한 화살표를 지정하지 않으므로 보고서 빌더는 선에 대한 화살표 설정을 지원하지 않습니다. 보고 서비스용 Aspose.PDF를 사용하면 이를 쉽게 수행할 수 있습니다.

{{% /alert %}}

현재 Aspose.PDF 렌더러는 사용자 정의 속성을 추가하여 선의 시작이나 끝 부분에 화살표를 추가하는 것을 지원합니다.

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

예를 들어, 다음과 같은 두 줄이 있습니다. `line1` 그리고 `line2` 현재 보고서 파일에서 line1에는 시작 화살표가 있고 line2에는 시작 및 끝 화살표가 있습니다. 이러한 요구 사항을 충족하려면 다음 코드 조각과 같이 사용자 정의 속성을 추가할 수 있습니다.

## 예

```xml
 <Line Name="line1">
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
```

