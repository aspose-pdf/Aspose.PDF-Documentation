---
title: Conformité PDF_A
linktitle: Conformité PDF_A
type: docs
weight: 100
url: /fr/reportingservices/pdf_a-conformance/
description: Activez la conformité PDF/A dans Aspose.PDF for Reporting Services. Créez des documents conformes aux exigences d'archivage sans effort.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Vous pouvez consulter une introduction à la conformité PDF/A (PDF archivables) dans la documentation d'Aspose.PDF.

Si vous souhaitez créer un document PDF/A, ajoutez le paramètre de rapport suivant.

{{% /alert %}}


{{% alert color="primary" %}}

**Nom du paramètre**: PdfConformance  
**Type de date**: String  
**Valeurs prises en charge**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

**Exemple**
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

