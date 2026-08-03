---
title: 전체 양쪽 맞춤텍스트 정렬 맞춤
linktitle: 전체 양쪽 맞춤텍스트 정렬 맞춤
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: Reporting Services용 Aspose.PDF를 사용하여 PDF 보고서에서 완벽한 텍스트 정렬을 달성하세요. 양쪽 맞춤 및 전체 양쪽 맞춤 옵션을 지원합니다.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보고서 빌더는 텍스트 상자의 텍스트 정렬을 지정하는 기능을 지원하지 않습니다. `Justify` 그리고 `FullJustify`. Reporting Services용 Aspose.PDF를 사용하면 사용자 지정 속성을 추가하여 쉽게 수행할 수 있습니다.

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

보고서에서 코드는 다음과 같아야 합니다.

## 예

```xml
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
```
