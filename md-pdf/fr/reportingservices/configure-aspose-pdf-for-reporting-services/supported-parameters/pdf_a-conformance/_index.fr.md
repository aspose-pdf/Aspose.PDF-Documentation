---
title: PDF_A Conformance
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Vous pouvez obtenir une introduction à la conformité PDF/A (PDF Archivable) dans la documentation Aspose.PDF.

Si vous souhaitez créer un document PDF/A, ajoutez le paramètre de rapport suivant.

{{% /alert %}}


{{% alert color="primary" %}}

**Nom du paramètre**: PdfConformance  
**Type de données**: String  
**Valeurs prises en charge**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U  

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