---
title: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A veces es posible que desee exportar texto en cuadros de texto con formato. Desafortunadamente, Reporting Services no admite esto. Sin embargo, aún puede implementarlo usando Aspose.PDF para Reporting Services. Simplemente habilite un modo especial en el que todo el texto en los cuadros de texto se trata como HTML y coloque las etiquetas HTML necesarias para formatear el texto en el documento de salida. Por ejemplo, para tener texto normal, en negrita y en cursiva en el mismo cuadro de texto, ingrese el siguiente valor del cuadro de texto:

Some of this text is ```<b>bold</b>``` and other text is ```<i>italic</i>```.

Cuando se exporta, el texto se verá como si parte de este texto fuera **negrita** y otro texto es *cursiva*.

Tenga en cuenta que este enfoque tiene algunas limitaciones

{{% /alert %}}

{{% alert color="primary" %}}

- El formato no es visible en tiempo de diseño (en el Report Builder, portal web de Reporting Services, etc.). En su lugar, verá el texto HTML en forma de texto plano con etiquetas.
- La extensión de renderizado Aspose.PDF para Reporting Services reconoce y formatea correctamente el código HTML en los cuadros de texto. El renderizador PDF predeterminado de Reporting Services exportará este marcado como texto plano.

**Nombre del Parámetro**: IsHtmlTagSupported  
**Tipo de Dato**: Booleano  
**Valores soportados**: True, False (por defecto)   

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

Si desea agregar este parámetro en el Diseñador de Informes, utilice el tipo de dato 'Booleano'.

 
Actualmente, Aspose.Pdf para Reporting Services soporta un subconjunto de todas las etiquetas HTML. Puede encontrar más información en la [Documentación](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) de Aspose.PDF.

{{% /alert %}}