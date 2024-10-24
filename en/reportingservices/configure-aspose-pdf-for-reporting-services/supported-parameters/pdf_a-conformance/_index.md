---
title: PDF_A Conformance
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

You can get an introduction into PDF/A (Archivable PDF) Conformance in the Aspose.PDF documentation.

If you want to create a PDF/A document, add the following report parameter.

{{% /alert %}}


{{% alert color="primary" %}}

**Parameter Name**: PdfConformance  
**Date Type**: String  
**Values supported**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U  

**Example**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PdfConformance>PdfA1A</PdfConformance>
    </Configuration>
    </Extension>
</Render>
{{< /highlight >}}

{{% /alert %}}
