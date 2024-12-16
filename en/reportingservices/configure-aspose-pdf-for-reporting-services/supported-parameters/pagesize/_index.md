---
title: PageSize
type: docs
weight: 60
url: /reportingservices/pagesize/
description: Customize page sizes for PDF reports in Aspose.PDF for Reporting Services to meet specific document requirements.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services report designer does not support common page sizes such as A4, B5, Letter and so on. With Aspose.Pdf for Reporting Services, you can get it as in the following example.

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: PageSize  
**Date Type**: String  
**Values supported**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**Example**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
