---
title: 线箭头
linktitle: 线箭头
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: 了解使用 Aspose.PDF for Reporting Services 在 PDF 报告中添加线条箭头。轻松增强报告视觉效果。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RDL规范没有指定线元素的箭头，因此报表生成器不支持线的箭头设置。借助 Aspose.PDF for Reporting Services，您可以轻松做到这一点。

{{% /alert %}}

目前，Aspose.PDF 渲染器支持通过添加自定义属性在行的开头或结尾添加箭头。

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

例如，有两行名为 `line1` 和 `line2` 在当前报表文件中，line1 有开始箭头，line2 有开始和结束箭头，为了满足这些要求，您可以添加自定义属性，如以下代码片段所示。

## 例子

```xml
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
```

