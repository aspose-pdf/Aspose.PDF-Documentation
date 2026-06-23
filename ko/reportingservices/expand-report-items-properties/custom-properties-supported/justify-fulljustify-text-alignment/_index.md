---
title: Justify FullJustify 텍스트 정렬
linktitle: Justify FullJustify 텍스트 정렬
type: docs
weight: 40
url: /ko/reportingservices/justify-fulljustify-text-alignment/
description: Aspose.PDF for Reporting Services를 사용하여 PDF 보고서에서 완벽한 텍스트 정렬을 구현하십시오. 정렬(justify) 및 전체 정렬(full justify) 옵션을 지원합니다.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Builder는 텍스트 상자 “Justify” 및 “FullJustify”에 대한 텍스트 정렬 지정 기능을 지원하지 않습니다. Aspose.Pdf for Reporting Services를 사용하면 사용자 지정 속성을 추가하여 쉽게 수행할 수 있습니다.

{{% /alert %}}

{{% alert color="primary" %}}
**사용자 지정 속성 이름** : TextAlignment  
**사용자 정의 속성 유형** : String  
**사용자 정의 속성 값** : Justify, FullJustify  

보고서에서 코드는 다음과 같이 작성되어야 합니다:

**예시**

{{< highlight csharp >}}
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}


