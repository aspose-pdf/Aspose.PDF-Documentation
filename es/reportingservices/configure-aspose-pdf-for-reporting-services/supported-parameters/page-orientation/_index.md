---
title: Orientación de Página
type: docs
weight: 10
url: es/reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El Lenguaje de Definición de Informes no permite especificar la orientación de las páginas en el informe explícitamente. Con Aspose.Pdf para Reporting Services, puede instruir fácilmente al exportador para producir documentos PDF con orientación de página apaisada. La orientación predeterminada es vertical.

{{% /alert %}}

{{% alert color="primary" %}}

La orientación predeterminada es vertical.
**Nombre del Parámetro**: IsLandscape
**Tipo de Dato**: Boolean
**Valores soportados**: True, False (predeterminado)

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