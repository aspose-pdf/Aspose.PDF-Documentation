---
title: Page Orientation
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: Configure page orientation for PDF reports in Aspose.PDF for Reporting Services. Customize layouts for better presentation.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Definition Language does not allow specifying the orientation of pages in the report explicitly. With Aspose.Pdf for Reporting Services you can easily instruct the exporter to produce PDF documents with landscape page orientation. The default orientation is portrait.

{{% /alert %}}

{{% alert color="primary" %}}

The default orientation is portrait.
**Parameter Name**: IsLandscape
**Date Type**: Boolean
**Values supported**: True, False (default)

**Example**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
