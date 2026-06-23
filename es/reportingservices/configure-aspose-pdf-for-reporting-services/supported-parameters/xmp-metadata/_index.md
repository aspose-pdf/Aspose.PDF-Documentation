---
title: Metadatos XMP
linktitle: Metadatos XMP
type: docs
weight: 80
url: /es/reportingservices/xmp-metadata/
description: Aprende a gestionar los metadatos XMP en informes PDF usando Aspose.PDF for Reporting Services. Mejora el manejo de los metadatos del documento.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

El diseñador de informes de Reporting Services no admite incrustar metadatos XMP en el documento. Aspose.Pdf for Reporting Services proporciona cuatro parámetros para establecer los metadatos XMP correspondientes, que son:

{{% /alert %}}

{{% alert color="primary" %}}
**Nombre del Parámetro**: CreationDate  
**Tipo de fecha**: String  
**Valores admitidos**: Date en uno de los formatos de fecha

**Nombre del parámetro**: ModifyDate  
**Tipo de fecha**: String  
**Valores admitidos**: Date en uno de los formatos de fecha 

**Nombre del parámetro**: MetaDataDate  
**Tipo de fecha**: String  
**Valores admitidos**: Date en uno de los formatos de fecha 

**Nombre del parámetro**: CreatorTool  
**Tipo de fecha**: String  
**Valores admitidos**: Cualquier texto plano  

**Ejemplo**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.Pdf for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}



