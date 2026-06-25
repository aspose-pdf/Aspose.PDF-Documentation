---
title: Orientación de página
linktitle: Orientación de página
type: docs
weight: 10
url: /es/reportingservices/page-orientation/
description: Configure la orientación de página para informes PDF en Aspose.PDF for Reporting Services. Personalice los diseños para una mejor presentación.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

El lenguaje de definición de informes (Report Definition Language) no permite especificar la orientación de las páginas del informe de forma explícita. Con Aspose.Pdf for Reporting Services puede indicar fácilmente al exportador que produzca documentos PDF con orientación de página horizontal. La orientación predeterminada es vertical.

{{% /alert %}}

{{% alert color="primary" %}}

La orientación predeterminada es vertical.
**Nombre del Parámetro**: IsLandscape
**Tipo de Dato**: Boolean
**Valores compatibles**: True, False (por defecto)

**Ejemplo**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


