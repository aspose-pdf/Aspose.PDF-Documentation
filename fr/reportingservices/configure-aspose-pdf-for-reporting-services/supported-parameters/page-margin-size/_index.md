---
title: Taille de marge de page
type: docs
weight: 70
url: fr/reportingservices/page-margin-size/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le concepteur de rapports de Reporting Services ne prend pas en charge le réglage de la taille des marges de page. Aspose.Pdf pour Reporting Services fournit quatre paramètres pour définir la taille de marge de page correspondante, ils sont :

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Nom du paramètre**: PageMarginLeft  
**Type de données**: Float  
**Valeurs prises en charge**: Tout nombre positif ou zéro

2)  
**Nom du paramètre**: PageMarginRight  
**Type de données**: Float  
**Valeurs prises en charge**: Tout nombre positif ou zéro

3)  
**Nom du paramètre**: PageMarginTop  
**Type de données**: Float  
**Valeurs prises en charge**: Tout nombre positif ou zéro

4)  
**Nom du paramètre**: PageMarginBottom  
**Type de données**: Float  
**Valeurs prises en charge**: Tout nombre positif ou zéro

**Exemple**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">

    <Configuration>
```

<PageMarginLeft>50</PageMarginLeft>
<PageMarginRight>50</PageMarginRight>
<PageMarginTop>50</PageMarginTop>
<PageMarginBottom>50</PageMarginBottom>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```