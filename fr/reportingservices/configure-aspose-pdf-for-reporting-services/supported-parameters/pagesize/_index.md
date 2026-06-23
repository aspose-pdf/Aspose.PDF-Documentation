---
title: Taille de page
linktitle: Taille de page
type: docs
weight: 60
url: /fr/reportingservices/pagesize/
description: Personnalisez les tailles de page pour les rapports PDF dans Aspose.PDF for Reporting Services afin de répondre à des exigences de document spécifiques.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Le concepteur de rapports Reporting Services ne prend pas en charge les tailles de page courantes telles que A4, B5, Letter, etc. Avec Aspose.Pdf for Reporting Services, vous pouvez l'obtenir comme dans l'exemple suivant.

{{% /alert %}}

{{% alert color="primary" %}}

**Nom du paramètre** : PageSize  
**Type de date**: String  
**Valeurs prises en charge**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**Exemple**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

