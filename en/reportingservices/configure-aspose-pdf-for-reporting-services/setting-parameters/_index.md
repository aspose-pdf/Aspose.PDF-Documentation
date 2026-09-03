---
title: Setting Parameters
linktitle: Setting Parameters
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: Find out how to set parameters for PDF rendering in Aspose.PDF for Reporting Services. Achieve precise control over output.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

You can specify certain configuration parameters that affect how Aspose.PDF for Reporting Services generates documents. This section describes this process.

{{% /alert %}}

To configure Aspose.Pdf for Reporting Services, you need to edit the `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config` file. This is an XML file and the renderer configuration is inside the `<Extension>` element corresponding to the Aspose.PDF renderer.

## Example

```xml
<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>
```

{{% alert color="primary" %}}

If you want to set parameters for specific report file but not for every report on the server, you can add a report parameter for the specific report in the Report Builder as the following steps (for example, we’ll add an 'IsLandscape' parameter shown earlier):

1. Open the report in the Report Designer, right-click on the 'Parameters' folder in the 'Report Data' pane, and select 'Add Parameter…' (or, alternately, pull down the 'New' list and select 'Parameter…').

![Parameters set up. Step 1](setting-parameters_1.png)

1. In the 'Report Parameter Properties' dialog, create the parameter named 'IsLandscape', with the data type of Boolean, and add the value True in the 'Default Values' tab.

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
