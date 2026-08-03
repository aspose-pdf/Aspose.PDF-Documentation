---
title: Configuración de parámetros
linktitle: Configuración de parámetros
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: Descubra cómo configurar parámetros para la representación de PDF en Aspose.PDF para Reporting Services. Logre un control preciso sobre la producción.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Puede especificar ciertos parámetros de configuración que afectan la forma en que Aspose.PDF para Reporting Services genera documentos. Esta sección describe este proceso.

{{% /alert %}}

Para configurar Aspose.Pdf para Reporting Services, debe editar el archivo `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Este es un archivo XML y la configuración del renderizador está dentro del elemento `<Extension>` correspondiente al renderizador Aspose.PDF.

## Example

```xml
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
```

{{% alert color="primary" %}}

Si desea establecer parámetros para un archivo de informe específico pero no para cada informe en el servidor, puede agregar un parámetro de informe para el informe específico en el Generador de informes siguiendo los siguientes pasos (por ejemplo, agregaremos un parámetro 'IsLandscape' que se mostró anteriormente):

1. Abra el informe en el Diseñador de informes, haga clic derecho en la carpeta 'Parámetros' en el panel 'Datos del informe' y seleccione 'Agregar parámetro...' (o, alternativamente, despliegue la lista 'Nuevo' y seleccione 'Parámetro...').

![Parameters set up. Step 1](setting-parameters_1.png)

1. En el cuadro de diálogo 'Propiedades de parámetros de informe', cree el parámetro denominado 'IsLandscape', con el tipo de datos booleano, y agregue el valor Verdadero en la pestaña 'Valores predeterminados'.

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
