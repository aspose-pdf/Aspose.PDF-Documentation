---
title: Taille de la marge de page
linktitle: Taille de la marge de page
type: docs
weight: 70
url: /fr/reportingservices/page-margin-size/
description: Ajustez les tailles des marges de page dans les rapports PDF avec Aspose.PDF for Reporting Services pour améliorer la lisibilité et la mise en page.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Le concepteur de rapports Reporting Services ne prend pas en charge la définition de la taille des marges de page. Aspose.Pdf for Reporting Services fournit quatre paramètres pour définir la taille correspondante des marges de page, à savoir :

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Nom du paramètre** : PageMarginLeft  
**Type de date**: Float  
**Valeurs prises en charge**:  Any positive number or zero

2)  
**Nom du paramètre**: PageMarginRight  
**Type de date**: Float  
**Valeurs prises en charge**:  Any positive number or zero

3)  
**Nom du paramètre**: PageMarginTop  
**Type de date**: Float  
**Valeurs prises en charge**:  Any positive number or zero

4)  
**Nom du paramètre**: PageMarginBottom  
**Type de date**: Float  
**Valeurs prises en charge**:  Any positive number or zero

**Exemple**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% /alert %}}

