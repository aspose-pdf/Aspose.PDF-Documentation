---
title: Flechas de línea
linktitle: Flechas de línea
type: docs
weight: 20
url: /es/reportingservices/line-arrows/
description: Aprenda a agregar flechas de línea en informes PDF usando Aspose.PDF for Reporting Services. Mejore los visuales del informe sin esfuerzo.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

La especificación RDL no especifica las flechas para el elemento de línea, por lo que el generador de informes no admite la configuración de flechas para la línea. Con Aspose.Pdf for Reporting Services puede hacerlo fácilmente.

{{% /alert %}}

{{% alert color="primary" %}}

Actualmente, el renderizador Aspose.PDF admite la incorporación de flechas al inicio o al final de las líneas mediante la adición de propiedades personalizadas.

Agregar flecha de inicio para la línea  
**Propiedad personalizada** **Nombre**: HasArrowAtStart  
**Valor de la propiedad personalizada**: True  

Agregar flecha de fin para la línea  
**Propiedad personalizada** **Nombre**: HasArrowAtEnd  
**Valor de la propiedad personalizada**: True  

Por ejemplo, hay dos líneas llamadas 'line1' y 'line2' en el archivo de informe actual, y line1 tiene la flecha de inicio, line2 tiene las flechas de inicio y fin; para cumplir con estos requisitos, puede agregar propiedades personalizadas como se muestra en el siguiente fragmento de código.

**Ejemplo**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>
......
<Line Name="line2">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
      </CustomProperty>
<CustomProperty>
        <Name>HasArrowAtEnd</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}


