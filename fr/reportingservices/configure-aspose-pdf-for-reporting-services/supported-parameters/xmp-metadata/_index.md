---
title: Métadonnées XMP
linktitle: Métadonnées XMP
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: Apprenez à gérer les métadonnées XMP dans les rapports PDF à l'aide d'Aspose.PDF pour Reporting Services. Améliorez la gestion des métadonnées des documents.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le concepteur de rapports Reporting Services ne prend pas en charge l'intégration de métadonnées XMP dans le document. Aspose.PDF pour Reporting Services fournit quatre paramètres pour définir les métadonnées XMP correspondantes :

{{% /alert %}}

```text
**Parameter Name: CreationDate  
**Date Type: String  
**Values supported: Date in one of the date formats
```

```text
**Parameter Name: ModifyDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: MetaDataDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: CreatorTool  
**Date Type: String  
**Values supported: Any plain text  
```

## Exemple

```xml
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
```


