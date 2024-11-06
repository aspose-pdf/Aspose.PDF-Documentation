---
title: 线箭头
type: docs
weight: 20
url: zh/reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RDL 规范未指定有关线条元素的箭头，因此报表生成器不支持设置线条的箭头。但是使用 Aspose.Pdf for Reporting Services，您可以轻松做到这一点。

{{% /alert %}}

{{% alert color="primary" %}}

目前，Aspose.PDF 渲染器支持通过添加自定义属性在线条的开始或结束处添加箭头。

为线条添加起始箭头  
**自定义属性** **名称**: HasArrowAtStart  
**自定义属性值**: True  

为线条添加结束箭头  
**自定义属性** **名称**: HasArrowAtEnd  
**自定义属性值**: True  

例如，当前报告文件中有两条名为 'line1' 和 'line2' 的线，line1 有起始箭头，line2 有起始和结束箭头，为了满足这些要求，您可以添加自定义属性，如以下代码片段。

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
```