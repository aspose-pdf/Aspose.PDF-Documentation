---
title: Conformidad PDF_A
linktitle: Conformidad PDF_A
type: docs
weight: 100
url: /es/reportingservices/pdf_a-conformance/
description: Habilite la conformidad PDF/A en Aspose.PDF para Reporting Services. Cree documentos compatibles con archivado sin esfuerzo.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Puede obtener una introducción a la conformidad PDF/A (PDF archivable) en la documentación de Aspose.PDF.

Si desea crear un documento PDF/A, agregue el siguiente parámetro del informe.

{{% /alert %}}


{{% alert color="primary" %}}

**Nombre del parámetro**: PdfConformance  
**Tipo de dato**: String  
**Valores compatibles**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

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


