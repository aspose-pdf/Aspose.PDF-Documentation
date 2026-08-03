---
title: Conformidade PDF_A
linktitle: PDF_A Conformance
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
description: Habilite a conformidade com PDF/A em Aspose.PDF para Reporting Services. Crie documentos compatíveis com arquivamento sem esforço.
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

Você pode obter uma introdução à conformidade com PDF/A (PDF arquivável) na documentação do Aspose.PDF.

Se você deseja criar um documento PDF/A, adicione o seguinte parâmetro de relatório.

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## Exemplo

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