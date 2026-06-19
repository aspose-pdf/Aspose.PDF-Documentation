---
title: Metadados XMP
linktitle: Metadados XMP
type: docs
weight: 80
url: /pt/reportingservices/xmp-metadata/
description: Aprenda a gerenciar metadados XMP em relatórios PDF usando Aspose.PDF for Reporting Services. Aprimore o gerenciamento de metadados de documentos.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não oferece suporte à incorporação de metadados XMP no documento. Aspose.Pdf for Reporting Services fornece quatro parâmetros para definir os metadados XMP correspondentes, que são:

{{% /alert %}}

{{% alert color="primary" %}}
**Nome do parâmetro**: CreationDate  
**Tipo de Data**: String  
**Valores suportados**: Data em um dos formatos de data

**Nome do Parâmetro**: ModifyDate  
**Tipo de Data**: String  
**Valores suportados**: Data em um dos formatos de data 

**Nome do Parâmetro**: MetaDataDate  
**Tipo de Data**: String  
**Valores suportados**: Data em um dos formatos de data 

**Nome do Parâmetro**: CreatorTool  
**Tipo de Data**: String  
**Valores suportados**: Qualquer texto simples  

**Exemplo**
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


