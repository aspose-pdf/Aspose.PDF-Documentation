---
title: Justify FullJustify Text Alignment
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report builder does not support the capability to specify text alignment for textbox “Justify” and “FullJustify”. With Aspose.Pdf for Reporting Services, you can do that easily by adding custom properties.

{{% /alert %}}

{{% alert color="primary" %}}
**Custom Property Name** : TextAlignment  
**Custom Property Type** : String  
**Custom Property Values** : Justify, FullJustify  

In report the code should be like the following:

**Example**

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
