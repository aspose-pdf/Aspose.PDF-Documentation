---
title: Agregar propiedades personalizadas
linktitle: Agregar propiedades personalizadas
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
description: Aprenda a agregar propiedades personalizadas a informes PDF con Aspose.PDF para Reporting Services. Personalice sus documentos de manera eficiente.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Puede agregar propiedades personalizadas para algunos elementos del informe para ampliar su uso, como ToC, flechas de línea, etc. Esta sección describe este proceso.

{{% /alert %}}

Puede agregar propiedades personalizadas para algunos elementos del informe para ampliar su uso, como tabla de contenido, flechas de línea, etc. Esta sección describe este proceso.

Para agregar propiedades personalizadas, debe editar el archivo de código del documento RDL en los siguientes pasos:

1. Como en la siguiente figura, abra su proyecto, navegue hasta el explorador de soluciones, haga clic derecho en el archivo de informe seleccionado y luego seleccione el elemento de menú "Ver código".

![Add Custom Properties](adding-custom-properties_1.png)

2. Edite el archivo de código XML. Por ejemplo, si desea agregar una propiedad personalizada para el elemento del informe del gráfico, debe agregar un código similar al texto rojo en el siguiente ejemplo.

## Ejemplo

```xml
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
```

En este ejemplo de fragmento de código, el nombre de la propiedad personalizada es IsInList y el valor es `True`.

