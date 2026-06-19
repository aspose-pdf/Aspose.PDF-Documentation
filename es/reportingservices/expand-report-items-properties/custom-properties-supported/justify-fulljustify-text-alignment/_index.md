---
title: Alineación de Texto Justificar y Justificar Completo
linktitle: Alineación de Texto Justificar y Justificar Completo
type: docs
weight: 40
url: /es/reportingservices/justify-fulljustify-text-alignment/
description: Logre una alineación de texto perfecta en los informes PDF con Aspose.PDF for Reporting Services. Compatibilidad con las opciones de justificar y justificar completo.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report builder no admite la capacidad de especificar la alineación de texto para el cuadro de texto “Justify” y “FullJustify”. Con Aspose.Pdf for Reporting Services, puede hacerlo fácilmente añadiendo propiedades personalizadas.

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


