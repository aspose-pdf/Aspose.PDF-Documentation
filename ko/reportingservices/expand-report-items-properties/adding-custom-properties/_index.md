---
title: 사용자 정의 속성 추가
linktitle: 사용자 정의 속성 추가
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
description: Reporting Services용 Aspose.PDF를 사용하여 PDF 보고서에 사용자 정의 속성을 추가하는 방법을 알아보세요. 문서를 효율적으로 사용자 정의하세요.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

일부 보고서 항목에 대한 사용자 정의 속성을 추가하여 ToC, 선 화살표 등과 같은 용도를 확장할 수 있습니다. 이 섹션에서는 이 프로세스에 대해 설명합니다.

{{% /alert %}}

일부 보고서 항목에 대한 사용자 정의 속성을 추가하여 목차, 선 화살표 등과 같은 용도를 확장할 수 있습니다. 이 섹션에서는 이 프로세스에 대해 설명합니다.

사용자 정의 속성을 추가하려면 다음 단계에 따라 RDL 문서의 코드 파일을 편집해야 합니다.

1. 다음 그림과 같이 프로젝트를 열고 솔루션 탐색기로 이동하여 선택한 보고서 파일을 마우스 오른쪽 버튼으로 클릭한 다음 '코드 보기' 메뉴 항목을 선택합니다.

![Add Custom Properties](adding-custom-properties_1.png)

2. XML 코드 파일을 편집합니다. 예를 들어 차트 보고서 항목에 대한 사용자 정의 속성을 추가하려면 다음 예의 빨간색 텍스트와 유사한 코드를 추가해야 합니다.

## 예

```xml
<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 
```

이 코드 단편 예에서 사용자 정의 특성 이름은 IsInList이고 값은 `True`입니다.

