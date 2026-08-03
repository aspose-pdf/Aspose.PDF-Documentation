---
title: Información de depuración
linktitle: Información de depuración
type: docs
weight: 90
url: /reportingservices/debug-information/
description: Acceda y analice información de depuración para la representación de PDF en Aspose.PDF para Reporting Services para solucionar problemas de manera efectiva.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Es inevitable que haya algún problema con la renderización o el resultado renderizado. Por algunas razones, como el secreto o la privacidad, no pudimos obtener la fuente de datos utilizada en el informe del usuario, por lo que no pudimos reproducir el error en el informe. Para que la comunicación entre clientes y desarrolladores sea más fácil y fluida, agregamos este parámetro. Si tiene problemas al renderizar su informe con Aspose.PDF para Reporting Services, configure este parámetro de informe y obtendrá el documento renderizado con el formato XML. Después de eso, publique el archivo XML en el foro del producto.

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## Ejemplo

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}
