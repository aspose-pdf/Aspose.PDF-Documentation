---
title: EstFontEmbedded
linktitle: EstFontEmbedded
type: docs
weight: 50
url: /reportingservices/isfontembedded/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

RS Designer ne prend pas en charge la police intégrée pour le texte ; avec Aspose.PDF pour Reporting Services, vous pouvez facilement intégrer des informations sur les polices dans votre document PDF.

{{% /alert %}}

```txt
Parameter Name: IsFontEmbedded  
Date Type: Boolean  
Values supported: True, False (default)  
```

## Exemple

```xml
<Render>
...
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsFontEmbedded>True</IsFontEmbedded>
    </Configuration>
    </Extension>
</Render>
```
