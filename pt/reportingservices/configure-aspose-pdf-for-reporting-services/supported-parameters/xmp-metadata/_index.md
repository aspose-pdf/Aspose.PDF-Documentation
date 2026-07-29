---
title: Metadados XMP
linktitle: Metadados XMP
type: docs
weight: 80
url: /pt/reportingservices/xmp-metadata/
description: Aprenda a gerenciar metadados XMP em relatórios PDF usando Aspose.PDF for Reporting Services. Melhore o tratamento de metadados de documentos.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não suporta a incorporação de metadados XMP no documento. Aspose.PDF for Reporting Services fornece quatro parâmetros para definir os respectivos metadados XMP, são eles:

{{% /alert %}}

{{% alert color="primary" %}}
**Nome do Parâmetro**: CreationDate  
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
    <CreatorTool>Aspose.PDF for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

