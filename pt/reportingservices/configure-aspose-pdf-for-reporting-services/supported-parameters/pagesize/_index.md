---
title: PageSize
linktitle: PageSize
type: docs
weight: 60
url: /pt/reportingservices/pagesize/
description: Personalize os tamanhos de página para relatórios PDF no Aspose.PDF for Reporting Services para atender a requisitos específicos de documento.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não suporta tamanhos de página comuns, como A4, B5, Letter e assim por diante. Com o Aspose.Pdf for Reporting Services, você pode obtê-lo como no exemplo a seguir.

{{% /alert %}}

{{% alert color="primary" %}}

**Nome do parâmetro**: PageSize  
**Tipo de Data**: String  
**Valores suportados**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**Exemplo**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

