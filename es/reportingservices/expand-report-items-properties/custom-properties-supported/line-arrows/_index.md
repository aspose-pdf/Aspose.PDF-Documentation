---
title: Flechas de Línea
type: docs
weight: 20
url: /es/reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

La especificación RDL no especifica las flechas sobre el elemento de línea, por lo que el creador de informes no admite la configuración de flechas para la línea. Con Aspose.Pdf para Reporting Services puedes hacerlo fácilmente.

{{% /alert %}}

{{% alert color="primary" %}}

Actualmente, el renderizador Aspose.PDF admite la adición de flechas al inicio o al final de las líneas mediante la adición de propiedades personalizadas.

Agregar flecha de inicio para la línea  
**Nombre de la Propiedad Personalizada**: HasArrowAtStart  
**Valor de la Propiedad Personalizada**: True  

Agregar flecha de fin para la línea  
**Nombre de la Propiedad Personalizada**: HasArrowAtEnd  
**Valor de la Propiedad Personalizada**: True  

Por ejemplo, hay dos líneas llamadas 'line1' y 'line2' en el archivo de informe actual, y line1 tiene la flecha de inicio, line2 tiene las flechas de inicio y fin, para satisfacer estos requisitos, puedes agregar propiedades personalizadas como en el siguiente fragmento de código.

**Ejemplo**

{{< highlight csharp >}}

 <Line Name="line1">

<Style>
  ......
</Style>
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
</Style>
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
```