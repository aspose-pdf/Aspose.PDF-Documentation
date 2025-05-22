---
title: PDF_A Conformance
type: docs
weight: 100
url: /pt/reportingservices/pdf_a-conformance/
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

Você pode obter uma introdução à Conformidade PDF/A (PDF Arquivável) na documentação Aspose.PDF.

Se você quiser criar um documento PDF/A, adicione o seguinte parâmetro de relatório.

{{% /alert %}}


{{% alert color="primary" %}}

**Nome do Parâmetro**: PdfConformance  
**Tipo de Dado**: String  
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