---
title: Conformidad PDF_A
linktitle: Conformidad PDF_A
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
description: Habilite la conformidad con PDF/A en Aspose.PDF para Reporting Services. Cree documentos compatibles con archivos sin esfuerzo.
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

Puede obtener una introducción a la conformidad con PDF/A (PDF archivable) en la documentación de Aspose.PDF.

Si desea crear un documento PDF/A, agregue el siguiente parámetro de informe.

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## Example

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PdfConformance>PdfA1A</PdfConformance>
    </Configuration>
    </Extension>
</Render>
```
