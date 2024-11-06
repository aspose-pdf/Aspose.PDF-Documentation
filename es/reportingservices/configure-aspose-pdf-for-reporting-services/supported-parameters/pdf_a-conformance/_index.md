---
title: PDF_A Conformance
type: docs
weight: 100
url: es/reportingservices/pdf_a-conformance/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Puede obtener una introducción a la Conformidad PDF/A (PDF Archivable) en la documentación de Aspose.PDF.

Si desea crear un documento PDF/A, agregue el siguiente parámetro de informe.

{{% /alert %}}


{{% alert color="primary" %}}

**Nombre del Parámetro**: PdfConformance  
**Tipo de Dato**: String  
**Valores soportados**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U  

**Ejemplo**
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