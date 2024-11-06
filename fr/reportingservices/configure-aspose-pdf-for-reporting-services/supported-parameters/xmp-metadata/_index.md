---
title: Métadonnées XMP
type: docs
weight: 80
url: fr/reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le concepteur de rapports Reporting Services ne prend pas en charge l'intégration des métadonnées XMP dans le document. Aspose.Pdf pour Reporting Services fournit quatre paramètres pour définir les métadonnées XMP correspondantes, ils sont :

{{% /alert %}}

{{% alert color="primary" %}}
**Nom du paramètre**: CreationDate  
**Type de données**: String  
**Valeurs prises en charge**: Date dans l'un des formats de date

**Nom du paramètre**: ModifyDate  
**Type de données**: String  
**Valeurs prises en charge**: Date dans l'un des formats de date 

**Nom du paramètre**: MetaDataDate  
**Type de données**: String  
**Valeurs prises en charge**: Date dans l'un des formats de date 

**Nom du paramètre**: CreatorTool  
**Type de données**: String  
**Valeurs prises en charge**: Tout texte simple  

**Exemple**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>

    <CreationDate>2017-12-10</CreationDate>

<ModifyDate>2018-1-12</ModifyDate>
<MetaDataDate>2018-3-7</MetaDataDate>
<CreatorTool>Aspose.Pdf pour les services de rapport</CreatorTool>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```