---
title: Métadonnées XMP
linktitle: Métadonnées XMP
type: docs
weight: 80
url: /fr/reportingservices/xmp-metadata/
description: Apprenez à gérer les métadonnées XMP dans les rapports PDF à l'aide d'Aspose.PDF for Reporting Services. Améliorez la gestion des métadonnées des documents.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Le concepteur de rapports Reporting Services ne prend pas en charge l’intégration des métadonnées XMP dans le document. Aspose.Pdf for Reporting Services fournit quatre paramètres pour définir les métadonnées XMP correspondantes, à savoir :

{{% /alert %}}

{{% alert color="primary" %}}
**Nom du paramètre** : CreationDate  
**Date Type**: Chaîne  
**Values supported**: Date dans l'un des formats de date

**Parameter Name**: ModifyDate  
**Date Type**: Chaîne  
**Values supported**: Date dans l'un des formats de date 

**Parameter Name**: MetaDataDate  
**Date Type**: Chaîne  
**Values supported**: Date dans l'un des formats de date 

**Parameter Name**: CreatorTool  
**Date Type**: Chaîne  
**Values supported**: Tout texte simple  

**Exemple**
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


