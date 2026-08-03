---
title: Conformité PDF_A
linktitle: Conformité PDF_A
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
description: Activez la conformité PDF/A dans Aspose.PDF pour Reporting Services. Créez sans effort des documents conformes aux normes d'archivage.
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

Vous pouvez obtenir une introduction à la conformité PDF/A (PDF archivable) dans la documentation Aspose.PDF.

Si vous souhaitez créer un document PDF/A, ajoutez le paramètre de rapport suivant.

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## Exemple

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
