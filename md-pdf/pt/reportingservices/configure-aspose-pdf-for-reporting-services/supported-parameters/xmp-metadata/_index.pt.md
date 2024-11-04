---
title: Metadados XMP
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não suporta a incorporação de metadados XMP no documento. Aspose.Pdf para Reporting Services fornece quatro parâmetros para definir os metadados XMP correspondentes, que são:

{{% /alert %}}

{{% alert color="primary" %}}
**Nome do Parâmetro**: CreationDate  
**Tipo de Dados**: String  
**Valores suportados**: Data em um dos formatos de data

**Nome do Parâmetro**: ModifyDate  
**Tipo de Dados**: String  
**Valores suportados**: Data em um dos formatos de data

**Nome do Parâmetro**: MetaDataDate  
**Tipo de Dados**: String  
**Valores suportados**: Data em um dos formatos de data

**Nome do Parâmetro**: CreatorTool  
**Tipo de Dados**: String  
**Valores suportados**: Qualquer texto simples

**Exemplo**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>

    <CreationDate>2017-12-10</CreationDate>
```
<ModifyDate>2018-1-12</ModifyDate>
<MetaDataDate>2018-3-7</MetaDataDate>
<CreatorTool>Aspose.Pdf para Serviços de Relatórios</CreatorTool>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}