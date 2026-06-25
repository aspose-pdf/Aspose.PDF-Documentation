---
title: Formato HTML
linktitle: Formato HTML
type: docs
weight: 20
url: /es/reportingservices/html-formatting/
description: Habilite el formato HTML en los informes PDF usando Aspose.PDF for Reporting Services. Agregue estilos y estructura con facilidad.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

A veces puede desear exportar texto en los cuadros de texto con formato. Desafortunadamente, Reporting Services no admite esto. Sin embargo, aún puede implementarlo usando Aspose.PDF for Reporting Services. Simplemente habilite un modo especial en el que todo el texto en los cuadros de texto se trate como HTML y coloque las etiquetas HTML necesarias para formatear el texto en el documento de salida. Por ejemplo, para tener texto normal, en negrita y en cursiva en el mismo cuadro de texto, ingrese el siguiente valor del cuadro de texto:

Parte de este texto es ```<b>bold</b>``` y otro texto es ```<i>italic</i>```.

Al exportarse, el texto aparecerá con parte de este texto en **bold** y otro texto en *italic*.

Tenga en cuenta que este enfoque tiene algunas limitaciones

{{% /alert %}}

{{% alert color="primary" %}}

- El formato no es visible en tiempo de diseño (en Report Builder, el portal web de Reporting Services, etc.). En su lugar, verá el texto HTML en forma de texto plano con etiquetas.
- La extensión de renderizado Aspose.PDF para Reporting Services reconoce y formatea correctamente el código HTML en los cuadros de texto. El renderizador PDF predeterminado de Reporting Services exportará este marcado como texto plano.

**Nombre del parámetro**: IsHtmlTagSupported  
**Tipo de dato**: Boolean  
**Valores compatibles**: True, False (predeterminado)   

**Ejemplo**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

Si desea agregar este parámetro en el Report Designer, use el tipo de datos 'Boolean'.

 
Actualmente Aspose.Pdf for Reporting Services admite un subconjunto de todas las etiquetas HTML. Puede encontrar más información en el Aspose.PDF [Documentación](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}


