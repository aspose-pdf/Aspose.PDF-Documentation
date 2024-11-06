---
title: Información de Depuración
type: docs
weight: 90
url: es/reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Es inevitable que haya algo mal con el renderizado o el resultado renderizado. Por algunas razones, como el secreto o la privacidad, no pudimos obtener la fuente de datos utilizada en el informe del usuario, por lo que no pudimos reproducir el error en el informe. Para hacer la comunicación entre clientes y desarrolladores más fácil y fluida, añadimos este parámetro. Si encuentra problemas al renderizar su informe con Aspose.PDF para Reporting Services, establezca este parámetro de informe, entonces obtendrá el documento renderizado con el formato de XML. Después de eso, por favor publique el archivo XML para nosotros en el foro del producto.

{{% /alert %}}

{{% alert color="primary" %}}
**Nombre del Parámetro**: SavingXmlFormat  
**Tipo de Dato**: Boolean  
**Valores soportados**: True, False (default)  

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
```