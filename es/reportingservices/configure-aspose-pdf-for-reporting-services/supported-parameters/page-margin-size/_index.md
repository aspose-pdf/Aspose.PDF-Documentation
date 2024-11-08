---
title: Tamaño del margen de la página
type: docs
weight: 70
url: /es/reportingservices/page-margin-size/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El diseñador de informes de Reporting Services no admite el ajuste del tamaño de los márgenes de la página. Aspose.Pdf para Reporting Services proporciona cuatro parámetros para establecer el tamaño correspondiente del margen de la página, son:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Nombre del Parámetro**: PageMarginLeft  
**Tipo de Dato**: Float  
**Valores admitidos**: Cualquier número positivo o cero

2)  
**Nombre del Parámetro**: PageMarginRight  
**Tipo de Dato**: Float  
**Valores admitidos**: Cualquier número positivo o cero

3)  
**Nombre del Parámetro**: PageMarginTop  
**Tipo de Dato**: Float  
**Valores admitidos**: Cualquier número positivo o cero

4)  
**Nombre del Parámetro**: PageMarginBottom  
**Tipo de Dato**: Float  
**Valores admitidos**: Cualquier número positivo o cero

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