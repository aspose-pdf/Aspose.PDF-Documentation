---
title: Justificar Alineación de Texto Justificar Completo
type: docs
weight: 40
url: es/reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El generador de informes no admite la capacidad de especificar la alineación de texto para el cuadro de texto “Justificar” y “Justificar Completo”. Con Aspose.Pdf para Reporting Services, puedes hacerlo fácilmente añadiendo propiedades personalizadas.

{{% /alert %}}

{{% alert color="primary" %}}
**Nombre de Propiedad Personalizada** : TextAlignment  
**Tipo de Propiedad Personalizada** : String  
**Valores de Propiedad Personalizada** : Justify, FullJustify  

En el informe, el código debería ser como el siguiente:

**Ejemplo**

{{< highlight csharp >}}
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}