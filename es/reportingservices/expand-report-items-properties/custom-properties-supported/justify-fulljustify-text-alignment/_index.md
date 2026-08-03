---
title: Justificar alineación completa del texto
linktitle: Justificar alineación completa del texto
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: Logre una alineación perfecta del texto en informes PDF con Aspose.PDF para Reporting Services. Soporte para opciones de justificación y justificación completa.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El generador de informes no admite la capacidad de especificar la alineación del texto para el cuadro de texto `Justify` y `FullJustify`. Con Aspose.PDF para Reporting Services, puede hacerlo fácilmente agregando propiedades personalizadas.

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

En el informe el código debería ser como el siguiente:

## Ejemplo

```xml
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
```
