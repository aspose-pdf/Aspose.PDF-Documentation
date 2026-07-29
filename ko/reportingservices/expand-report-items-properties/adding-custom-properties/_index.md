---
title: 맞춤 속성 추가
linktitle: 맞춤 속성 추가
type: docs
weight: 10
url: /ko/reportingservices/adding-custom-properties/
description: Aspose.PDF for Reporting Services를 사용하여 PDF 보고서에 맞춤 속성을 추가하는 방법을 알아보세요. 문서를 효율적으로 맞춤 설정하십시오.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

보고서 항목 중 일부에 맞춤 속성을 추가하여 사용 범위를 확장할 수 있습니다(예: ToC, 선 화살표 등). 이 섹션에서는 이 과정을 설명합니다.

{{% /alert %}}

{{% alert color="primary" %}}

보고서 항목 중 일부에 맞춤 속성을 추가하여 사용 범위를 확장할 수 있습니다(예: 목차, 선 화살표 등). 이 섹션에서는 이 과정을 설명합니다.

사용자 정의 속성을 추가하려면, 다음 단계에 따라 RDL 문서의 코드 파일을 편집해야 합니다:

1. 아래 그림과 같이 프로젝트를 열고, 솔루션 탐색기로 이동한 뒤 선택한 보고서 파일을 오른쪽 클릭하고, ‘View Code’ 메뉴 항목을 선택합니다.

![todo:image_alt_text](adding-custom-properties_1.png)

2. XML 코드 파일을 편집합니다. 예를 들어 차트 보고서 항목에 대한 사용자 정의 속성을 추가하려면, 아래 예시의 빨간색 텍스트와 유사한 코드를 추가해야 합니다.

**Example**

{{< highlight csharp >}}

<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>목록에 있는지</Name>
        <Value>참</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

이 코드 조각 예제에서 사용자 지정 속성 이름은 IsInList이며, 값은 'True'입니다.

{{% /alert %}}
