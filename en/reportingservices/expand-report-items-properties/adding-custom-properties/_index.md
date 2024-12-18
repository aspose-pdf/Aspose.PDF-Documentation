---
title: Adding Custom Properties
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
description: Learn how to add custom properties to PDF reports with Aspose.PDF for Reporting Services. Customize your documents efficiently.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

You can add custom properties for some report items to expand their usage, such as ToC, line arrows and so on. This section describes this process.

{{% /alert %}}

{{% alert color="primary" %}}

You can add custom properties for some report items to expand their usage, such as Table of Contents, line arrows and so on. This section describes this process.

To add custom properties, you need to edit the code file of RDL document in the following steps:

1. As in the following figure, open your project, navigate to the solution explorer, and right click on the selected report file, then select the 'View Code' menu item.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Edit the XML code file. For example, if you want to add a custom property for chart report item, you need to add the code similar to the red text in the following example.

**Example**

{{< highlight csharp >}}

<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

In this code fragment example, the custom property name is IsInList, and the value is 'True'.

{{% /alert %}}
