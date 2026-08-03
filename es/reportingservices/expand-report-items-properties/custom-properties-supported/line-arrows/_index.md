---
title: Flechas de línea
linktitle: Flechas de línea
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: Aprenda a agregar flechas de línea en informes PDF usando Aspose.PDF para Reporting Services. Mejore las imágenes del informe sin esfuerzo.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

La especificación RDL no especifica las flechas sobre el elemento de línea, por lo que el generador de informes no admite la configuración de flechas para la línea. Con Aspose.PDF para Reporting Services puede hacerlo fácilmente.

{{% /alert %}}

Actualmente, el renderizador Aspose.PDF admite la adición de flechas al principio o al final de las líneas mediante la adición de propiedades personalizadas.

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

Por ejemplo, hay dos líneas llamadas `line1` y `line2` en el archivo de informe actual, y la línea1 tiene la flecha de inicio, la línea2 tiene las flechas de inicio y fin; para satisfacer estos requisitos, puede agregar propiedades personalizadas como en el siguiente fragmento de código.

## Ejemplo

```xml
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
```

