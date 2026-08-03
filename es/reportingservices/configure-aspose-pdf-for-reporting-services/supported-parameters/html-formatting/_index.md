---
title: Formato HTML
linktitle: Formato HTML
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: Habilite el formato HTML en informes PDF usando Aspose.PDF para Reporting Services. Agregue estilos y estructura con facilidad.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A veces es posible que desees exportar texto en cuadros de texto con formato. Lamentablemente, Reporting Services no admite esto. Sin embargo, aún puede implementarlo utilizando Aspose.PDF para Reporting Services. Simplemente habilite un modo especial en el que todo el texto en los cuadros de texto se trata como HTML y coloque las etiquetas HTML necesarias para formatear el texto en el documento de salida. Por ejemplo, para tener texto normal, negrita y cursiva en el mismo cuadro de texto, ingrese el siguiente valor de cuadro de texto:

Parte de este texto es `<b>bold</b>` y otro texto es `<i>italic</i>`.

When exported, the text will look like as some of this text is **bold** and other text is *italic*.

Tenga en cuenta que este enfoque tiene algunas limitaciones.

{{% /alert %}}

{{% alert color="primary" %}}

- El formato no es visible en tiempo de diseño (en el Generador de informes, el portal web de Reporting Services, etc.). En su lugar, verá el texto HTML en forma de texto sin formato con etiquetas.
- La extensión de representación Aspose.PDF para Reporting Services reconoce y formatea correctamente el código HTML en los cuadros de texto. El procesador de PDF predeterminado de Reporting Services exportará este marcado como texto sin formato.

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## Ejemplo

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

Si desea agregar este parámetro en el Diseñador de informes, utilice el tipo de datos `Boolean`.

Actualmente, Aspose.Pdf para Reporting Services admite un subconjunto de todas las etiquetas HTML. Puede encontrar más información en Aspose.PDF [Documentación](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}
