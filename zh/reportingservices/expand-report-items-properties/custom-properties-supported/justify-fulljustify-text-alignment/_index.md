---
title: 两端对齐 完全两端对齐 文本对齐
linktitle: 两端对齐 完全两端对齐 文本对齐
type: docs
weight: 40
url: /zh/reportingservices/justify-fulljustify-text-alignment/
description: 使用 Aspose.PDF for Reporting Services 实现 PDF 报表中文本对齐的完美效果。支持两端对齐和完全两端对齐选项。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report builder 不支持为文本框 “Justify” 和 “FullJustify” 指定文本对齐的功能。使用 Aspose.Pdf for Reporting Services，您可以通过添加自定义属性轻松实现此功能。

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

