---
title: Configuración de parámetros
linktitle: Configuración de parámetros
type: docs
weight: 10
url: /es/reportingservices/setting-parameters/
description: Descubra cómo establecer parámetros para la renderización de PDF en Aspose.PDF for Reporting Services. Logre un control preciso sobre la salida.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Puede especificar ciertos parámetros de configuración que afectan cómo Aspose.Pdf for Reporting Services genera documentos. Esta sección describe este proceso.

{{% /alert %}}

Para configurar Aspose.Pdf for Reporting Services, necesita editar el archivo C:\\Program Files\\Microsoft SQL Server\\<Instance>\\Reporting Services\\ReportServer\\rsreportserver.config. Este es un archivo XML y la configuración del renderizador está dentro del ```<Extension>``` elemento correspondiente al renderizador Aspose.PDF.

**Ejemplo**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% alert color="primary" %}}

Si deseas establecer parámetros para un archivo de informe específico pero no para cada informe en el servidor, puedes agregar un parámetro de informe para el informe específico en Report Builder siguiendo los pasos siguientes (por ejemplo, agregaremos un parámetro ‘IsLandscape’ mostrado anteriormente):

1. Abre el informe en Report Designer, haz clic con el botón derecho en la carpeta ‘Parameters’ en el panel ‘Report Data’ y selecciona ‘Add Parameter…’ (o, alternativamente, despliega la lista ‘New’ y selecciona ‘Parameter…’).
 
![todo:image_alt_text](setting-parameters_1.png)

1. En el cuadro de diálogo ‘Report Parameter Properties’, crea el parámetro llamado ‘IsLandscape’, con el tipo de datos Boolean, y agrega el valor True en la pestaña ‘Default Values’.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}


