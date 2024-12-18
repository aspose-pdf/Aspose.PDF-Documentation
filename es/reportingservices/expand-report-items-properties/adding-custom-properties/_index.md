---
title: Adding Custom Properties
type: docs
weight: 10
url: /es/reportingservices/adding-custom-properties/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Puede agregar propiedades personalizadas a algunos elementos del informe para expandir su uso, como el índice, flechas de línea, etc. Esta sección describe este proceso.

{{% /alert %}}

{{% alert color="primary" %}}

Puede agregar propiedades personalizadas a algunos elementos del informe para expandir su uso, como el índice, flechas de línea, etc. Esta sección describe este proceso.

Para agregar propiedades personalizadas, debe editar el archivo de código del documento RDL en los siguientes pasos:

1. Como en la figura siguiente, abra su proyecto, navegue al explorador de soluciones y haga clic derecho en el archivo de informe seleccionado, luego seleccione el elemento de menú 'Ver código'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Edite el archivo de código XML. Por ejemplo, si desea agregar una propiedad personalizada para el elemento de informe de gráfico, necesita agregar el código similar al texto en rojo en el siguiente ejemplo.

**Example**

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

En este fragmento de código de ejemplo, el nombre de la propiedad personalizada es IsInList y el valor es 'True'.

{{% /alert %}}