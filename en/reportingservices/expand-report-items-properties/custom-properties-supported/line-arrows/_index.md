---
title: Line Arrows
linktitle: Line Arrows
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: Learn to add line arrows in PDF reports using Aspose.PDF for Reporting Services. Enhance report visuals effortlessly.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

RDL specification does not specify the arrows about the line element, so report builder doesn’t support the setting of arrows for line. With Aspose.PDF for Reporting Services you can do that easily.

{{% /alert %}}

Currently, Aspose.PDF renderer support adding arrows at the start or end for lines by adding custom properties.

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

For example, there are two lines named `line1` and `line2` in the current report file, and line1 has the start arrow, line2 has the start and end arrows, to satisfy these requirements, you can add custom properties as in the following code fragment.

## Example

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

