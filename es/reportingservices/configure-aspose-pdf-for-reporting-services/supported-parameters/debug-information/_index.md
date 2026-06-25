---
title: Información de depuración
linktitle: Información de depuración
type: docs
weight: 90
url: /es/reportingservices/debug-information/
description: Acceda y analice la información de depuración para la renderización de PDF en Aspose.PDF for Reporting Services para solucionar problemas de manera eficaz.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Es inevitable que haya algo incorrecto en la renderización o el resultado renderizado. Por razones como la confidencialidad o la privacidad, no podemos obtener la fuente de datos utilizada en el informe del usuario, por lo que no podemos reproducir el error en el informe. Para facilitar y agilizar la comunicación entre clientes y desarrolladores, añadimos este parámetro. Si encuentra problemas al renderizar su informe con Aspose.PDF for Reporting Services, establezca este parámetro del informe; así obtendrá el documento renderizado en formato XML. Después, por favor publique el archivo XML para nosotros en el foro del producto.

{{% /alert %}}

{{% alert color="primary" %}}
**Nombre del parámetro**: SavingXmlFormat  
**Tipo de fecha**: Booleano  
**Valores admitidos**: Verdadero, Falso (predeterminado)  

**Ejemplo**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


