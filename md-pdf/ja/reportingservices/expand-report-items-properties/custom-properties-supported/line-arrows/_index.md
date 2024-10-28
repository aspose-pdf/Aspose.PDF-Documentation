---
title: Line Arrows
type: docs
weight: 20
url: /reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RDL specification does not specify the arrows about the line element, so report builder doesn’t support the setting of arrows for line. With Aspose.Pdf for Reporting Services you can do that easily.

{{% /alert %}}

{{% alert color="primary" %}}

Currently, Aspose.PDF renderer support adding arrows at the start or end for lines by adding custom properties.

Add Start Arrow for Line  
**Custom Property** **Name**: HasArrowAtStart  
**Custom Property Value**: True  

Add End Arrow for Line  
**Custom Property** **Name**: HasArrowAtEnd  
**Custom Property Value**: True  

For example, there are two lines named 'line1' and 'line2' in the current report file, and line1 has the start arrow, line2 has the start and end arrows, to satisfy these requirements, you can add custom properties as in the following code fragment.

**Example**

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
