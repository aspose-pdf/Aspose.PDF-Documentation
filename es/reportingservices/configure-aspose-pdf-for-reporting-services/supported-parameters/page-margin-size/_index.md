---
title: Tamaño del margen de página
linktitle: Tamaño del margen de página
type: docs
weight: 70
url: /es/reportingservices/page-margin-size/
description: Ajuste los tamaños de los márgenes de página en los informes PDF con Aspose.PDF for Reporting Services para mejorar la legibilidad y el diseño.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

El diseñador de informes de Reporting Services no admite la configuración del tamaño de los márgenes de página. Aspose.Pdf for Reporting Services ofrece cuatro parámetros para establecer el tamaño correspondiente del margen de página, que son:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Nombre del parámetro**: PageMarginLeft  
**Tipo de fecha**: Float  
**Valores admitidos**:  Any positive number or zero

2)  
**Nombre del parámetro**: PageMarginRight  
**Tipo de fecha**: Float  
**Valores admitidos**:  Any positive number or zero

3)  
**Nombre del parámetro**: PageMarginTop  
**Tipo de fecha**: Float  
**Valores admitidos**:  Any positive number or zero

4)  
**Nombre del parámetro**: PageMarginBottom  
**Tipo de fecha**: Float  
**Valores admitidos**:  Any positive number or zero

**Ejemplo**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">
    <Configuration>
    <PageMarginLeft>50</PageMarginLeft>
    <PageMarginRight>50</PageMarginRight>
    <PageMarginTop>50</PageMarginTop>
    <PageMarginBottom>50</PageMarginBottom>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


