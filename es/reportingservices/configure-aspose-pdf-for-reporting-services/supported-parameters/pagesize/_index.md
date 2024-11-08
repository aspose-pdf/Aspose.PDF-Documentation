---
title: PageSize
type: docs
weight: 60
url: /es/reportingservices/pagesize/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El diseñador de informes de Reporting Services no admite tamaños de página comunes como A4, B5, Carta, etc. Con Aspose.Pdf para Reporting Services, puedes obtenerlo como en el siguiente ejemplo.

{{% /alert %}}

{{% alert color="primary" %}}

**Nombre del Parámetro**: PageSize  
**Tipo de Dato**: String  
**Valores soportados**: A0, A1, A2, A3, A4, A5, A6, B5, Carta, Legal, Ledger, P11x17  

**Ejemplo**

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