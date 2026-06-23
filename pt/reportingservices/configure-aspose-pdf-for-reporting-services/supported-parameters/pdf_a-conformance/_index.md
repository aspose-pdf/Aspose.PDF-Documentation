---
title: Conformidade PDF_A
linktitle: Conformidade PDF_A
type: docs
weight: 100
url: /pt/reportingservices/pdf_a-conformance/
description: Habilite a conformidade PDF/A no Aspose.PDF for Reporting Services. Crie documentos compatíveis com arquivamento sem esforço.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Você pode obter uma introdução à Conformidade PDF/A (PDF Arquivável) na documentação do Aspose.PDF.

Se você quiser criar um documento PDF/A, adicione o seguinte parâmetro de relatório.

{{% /alert %}}


{{% alert color="primary" %}}

**Nome do Parâmetro**: PdfConformance  
**Tipo de Dados**: String  
**Valores suportados**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

**Exemplo**
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

