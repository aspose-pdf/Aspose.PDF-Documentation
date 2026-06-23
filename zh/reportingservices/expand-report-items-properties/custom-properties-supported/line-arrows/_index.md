---
title: 线条箭头
linktitle: 线条箭头
type: docs
weight: 20
url: /zh/reportingservices/line-arrows/
description: 学习如何在使用 Aspose.PDF for Reporting Services 的 PDF 报表中添加线条箭头。轻松提升报告的视觉效果。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

RDL 规范未对线条元素的箭头进行规定，因而 Report Builder 不支持对线条设置箭头。使用 Aspose.PDF for Reporting Services，您可以轻松实现此功能。

{{% /alert %}}

{{% alert color="primary" %}}

目前，Aspose.PDF 渲染器通过添加自定义属性支持在直线的起始或结束位置添加箭头。

为线条添加起始箭头  
**自定义属性** **名称**: HasArrowAtStart  
**自定义属性值**: True  

为线条添加结束箭头  
**自定义属性** **名称**: HasArrowAtEnd  
**自定义属性值**: True  

例如，在当前报告文件中有两条线，名称分别为 'line1' 和 'line2'，其中 line1 具有起始箭头，line2 具有起始和结束箭头。为满足这些要求，您可以按以下代码片段添加自定义属性。

**示例**

{{< highlight csharp >}}
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

{{< /highlight >}}
{{% /alert %}}

