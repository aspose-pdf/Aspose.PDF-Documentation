---
title: XMP Metadata
type: docs
weight: 80
url: /es/reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El diseñador de informes de Reporting Services no admite la incrustación de metadatos XMP en el documento. Aspose.Pdf para Reporting Services proporciona cuatro parámetros para establecer los metadatos XMP correspondientes, son:

{{% /alert %}}

{{% alert color="primary" %}}
**Nombre del Parámetro**: CreationDate  
**Tipo de Dato**: String  
**Valores admitidos**: Fecha en uno de los formatos de fecha

**Nombre del Parámetro**: ModifyDate  
**Tipo de Dato**: String  
**Valores admitidos**: Fecha en uno de los formatos de fecha

**Nombre del Parámetro**: MetaDataDate  
**Tipo de Dato**: String  
**Valores admitidos**: Fecha en uno de los formatos de fecha

**Nombre del Parámetro**: CreatorTool  
**Tipo de Dato**: String  
**Valores admitidos**: Cualquier texto simple

**Ejemplo**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>

    <CreationDate>2017-12-10</CreationDate>
     <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.Pdf para Servicios de Reportes</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}