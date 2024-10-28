---
title: 对齐 FullJustify 文本对齐
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

报告生成器不支持为文本框指定文本对齐“Justify”和“FullJustify”的功能。使用 Aspose.Pdf for Reporting Services，您可以通过添加自定义属性轻松实现。

{{% /alert %}}

{{% alert color="primary" %}}
**自定义属性名称** : TextAlignment  
**自定义属性类型** : 字符串  
**自定义属性值** : Justify, FullJustify  

在报告中，代码应如下所示：

**示例**

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