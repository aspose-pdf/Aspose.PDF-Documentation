---
title: Tamaño del margen de página
linktitle: Tamaño del margen de página
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: Ajuste los tamaños de los márgenes de las páginas en informes PDF con Aspose.PDF para Reporting Services para mejorar la legibilidad y el diseño.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El diseñador de informes de Reporting Services no admite la configuración del tamaño de los márgenes de la página. Aspose.PDF para Reporting Services proporciona cuatro parámetros para establecer el tamaño del margen de página correspondiente, que son:

{{% /alert %}}

```text
Parameter Name: PageMarginLeft  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginRight  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginTop  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginBottom  
Date Type: Float  
Values supported:  Any positive number or zero
```

## Ejemplo

```xml
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
```
