---
title: Agregar propiedades personalizadas
linktitle: Agregar propiedades personalizadas
type: docs
weight: 10
url: /es/reportingservices/adding-custom-properties/
description: Aprenda cómo agregar propiedades personalizadas a los informes PDF con Aspose.PDF for Reporting Services. Personalice sus documentos de manera eficiente.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Puede agregar propiedades personalizadas a algunos elementos del informe para ampliar su uso, como ToC, flechas de línea, etc. Esta sección describe este proceso.

{{% /alert %}}

{{% alert color="primary" %}}

Puede agregar propiedades personalizadas a algunos elementos del informe para ampliar su uso, como la tabla de contenido, flechas de línea, etc. Esta sección describe este proceso.

Para agregar propiedades personalizadas, necesita editar el archivo de código del documento RDL en los siguientes pasos:

1. Como se muestra en la figura siguiente, abra su proyecto, navegue hasta el explorador de soluciones y haga clic derecho en el archivo de informe seleccionado, luego seleccione el elemento del menú 'View Code'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Edite el archivo de código XML. Por ejemplo, si desea agregar una propiedad personalizada para el elemento de informe de gráfico, necesita agregar el código similar al texto rojo en el siguiente ejemplo.

**Ejemplo**

{{< highlight csharp >}}

<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

En este ejemplo de fragmento de código, el nombre de la propiedad personalizada es IsInList y el valor es 'True'.

{{% /alert %}}


