---
title: Configuración de Parámetros
type: docs
weight: 10
url: /es/reportingservices/setting-parameters/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Puede especificar ciertos parámetros de configuración que afectan cómo Aspose.Pdf for Reporting Services genera documentos. Esta sección describe este proceso.

{{% /alert %}}

Para configurar Aspose.Pdf for Reporting Services, necesita editar el archivo C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. Este es un archivo XML y la configuración del renderizador está dentro del elemento ```<Extension>``` correspondiente al renderizador de Aspose.PDF.

**Ejemplo**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insertar elementos de configuración para exportar a PDF aquí. El siguiente es un ejemplo
Para PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}


{{% alert color="primary" %}}

If you want to set parameters for specific report file but not for every report on the server, you can add a report parameter for the specific report in the Report Builder as the following steps (for example, we’ll add an 'IsLandscape' parameter shown earlier):

Si desea establecer parámetros para un archivo de informe específico pero no para cada informe en el servidor, puede agregar un parámetro de informe para el informe específico en el Constructor de Informes siguiendo los siguientes pasos (por ejemplo, agregaremos un parámetro 'IsLandscape' mostrado anteriormente):

1. Open the report in the Report Designer, right-click on the 'Parameters' folder in the 'Report Data' pane, and select 'Add Parameter…' (or, alternately, pull down the 'New' list and select 'Parameter…').

1. Abra el informe en el Diseñador de Informes, haga clic derecho en la carpeta 'Parámetros' en el panel de 'Datos del Informe', y seleccione 'Agregar Parámetro…' (o, alternativamente, despliegue la lista 'Nuevo' y seleccione 'Parámetro…').

![todo:image_alt_text](setting-parameters_1.png)

1. In the 'Report Parameter Properties' dialog, create the parameter named 'IsLandscape', with the data type of Boolean, and add the value True in the 'Default Values' tab.

1. En el diálogo 'Propiedades del Parámetro de Informe', cree el parámetro llamado 'IsLandscape', con el tipo de dato Booleano, y agregue el valor True en la pestaña 'Valores Predeterminados'.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}