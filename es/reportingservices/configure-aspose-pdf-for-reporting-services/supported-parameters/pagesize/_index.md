---
title: Tamaño de página
linktitle: Tamaño de página
type: docs
weight: 60
url: /reportingservices/pagesize/
description: Personalice los tamaños de página para informes PDF en Aspose.PDF para Reporting Services para cumplir con requisitos de documentos específicos.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El diseñador de informes de Reporting Services no admite tamaños de página comunes, como A4, B5, Carta, etc. Con Aspose.PDF para Reporting Services, puede obtenerlo como en el siguiente ejemplo.

{{% /alert %}}

```text
Parameter Name: PageSize  
Date Type: String  
Values supported: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  
```

## Ejemplo

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>
```
