---
title: PageSize
type: docs
weight: 60
url: /pt/reportingservices/pagesize/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não suporta tamanhos de página comuns, como A4, B5, Carta e assim por diante. Com o Aspose.Pdf para Reporting Services, você pode obtê-lo como no exemplo a seguir.

{{% /alert %}}

{{% alert color="primary" %}}

**Nome do Parâmetro**: PageSize  
**Tipo de Dado**: String  
**Valores suportados**: A0, A1, A2, A3, A4, A5, A6, B5, Carta, Legal, Ledger, P11x17  

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