---
title: Taille de la marge de la page
linktitle: Taille de la marge de la page
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: Ajustez la taille des marges des pages dans les rapports PDF avec Aspose.PDF pour Reporting Services pour une lisibilité et une mise en page améliorées.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le concepteur de rapports Reporting Services ne prend pas en charge la définition de la taille des marges de page. Aspose.PDF pour Reporting Services fournit quatre paramètres pour définir la taille de marge de page correspondante, à savoir :

{{% /alert %}}

```text
Parameter Name: PageMarginLeft  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginRight  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginTop  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginBottom  
Date Type: Float  
Values supported:  Any positive number or zero
```

## Exemple

```xml
<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">
    <Configuration>
    <PageMarginLeft>50</PageMarginLeft>
    <PageMarginRight>50</PageMarginRight>
    <PageMarginTop>50</PageMarginTop>
    <PageMarginBottom>50</PageMarginBottom>
    </Configuration>
    </Extension>
</Render>
```
