---
title: Orientación de la página
linktitle: Orientación de la página
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: Configure la orientación de la página para informes PDF en Aspose.PDF para Reporting Services. Personalice los diseños para una mejor presentación.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El lenguaje de definición de informes no permite especificar explícitamente la orientación de las páginas del informe. Con Aspose.PDF para Reporting Services, puede indicar fácilmente al exportador que produzca documentos PDF con orientación de página horizontal. La orientación predeterminada es vertical.

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## Ejemplo

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>
```

