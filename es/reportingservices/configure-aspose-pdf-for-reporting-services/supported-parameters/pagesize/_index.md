---
title: TamañoDePágina
linktitle: TamañoDePágina
type: docs
weight: 60
url: /es/reportingservices/pagesize/
description: Personaliza los tamaños de página para los informes PDF en Aspose.PDF for Reporting Services para cumplir con requisitos específicos de documentos.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

El diseñador de informes de Reporting Services no admite tamaños de página comunes como A4, B5, Letter, etc. Con Aspose.Pdf for Reporting Services, puedes lograrlo como en el siguiente ejemplo.

{{% /alert %}}

{{% alert color="primary" %}}

**Nombre del parámetro**: PageSize  
**Date Type**: Cadena  
**Valores admitidos**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

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


