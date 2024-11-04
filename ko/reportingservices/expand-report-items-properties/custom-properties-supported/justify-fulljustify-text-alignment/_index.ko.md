---
title: 정렬 꽉 채우기 텍스트 정렬
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보고서 작성기는 텍스트 상자에 대한 텍스트 정렬을 지정하는 기능을 지원하지 않습니다. "정렬" 및 "꽉 채우기 정렬"을 Aspose.Pdf for Reporting Services를 사용하여 사용자 지정 속성을 추가하여 쉽게 수행할 수 있습니다.

{{% /alert %}}

{{% alert color="primary" %}}
**사용자 지정 속성 이름** : TextAlignment  
**사용자 지정 속성 유형** : String  
**사용자 지정 속성 값** : Justify, FullJustify  

보고서에서 코드는 다음과 같아야 합니다:

**예제**

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