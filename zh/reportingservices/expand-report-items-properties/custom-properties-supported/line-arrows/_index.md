---
title: 线条箭头
linktitle: 线条箭头
type: docs
weight: 20
url: /zh/reportingservices/line-arrows/
description: 学习如何在 PDF 报告中使用 Aspose.PDF for Reporting Services 添加线条箭头。轻松提升报告视觉效果。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

RDL 规范未对线元素的箭头进行规定，因此 Report Builder 不支持线的箭头设置。使用 Aspose.PDF for Reporting Services，您可以轻松实现此功能。

{{% /alert %}}

{{% alert color="primary" %}}

当前，Aspose.PDF 渲染器支持通过添加自定义属性为线的起点或终点添加箭头。

为线添加起始箭头  
**自定义属性** **名称**: HasArrowAtStart  
**自定义属性值**: True  

为线添加结束箭头  
**自定义属性** **名称**: HasArrowAtEnd  
**自定义属性值**: True  

例如，在当前报告文件中有两条线，分别名为 'line1' 和 'line2'，其中 line1 带有起始箭头，line2 带有起始和结束箭头。为满足这些要求，您可以按以下代码片段添加自定义属性。

**示例**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>起始处有箭头</Name>
        <Value>真</Value>
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
        <Name>起始处有箭头</Name>
        <Value>真</Value>
      </CustomProperty>
<CustomProperty>
        <Name>末尾有箭头</Name>
        <Value>真</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
