---
title: Orientation de la page
linktitle: Orientation de la page
type: docs
weight: 10
url: /fr/reportingservices/page-orientation/
description: Configurez l'orientation des pages pour les rapports PDF dans Aspose.PDF for Reporting Services. Personnalisez les mises en page pour une meilleure présentation.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Le langage de définition de rapport (Report Definition Language) ne permet pas de spécifier explicitement l'orientation des pages dans le rapport. Avec Aspose.Pdf for Reporting Services, vous pouvez facilement indiquer à l'exportateur de produire des documents PDF avec une orientation de page paysage. L'orientation par défaut est portrait.

{{% /alert %}}

{{% alert color="primary" %}}

L'orientation par défaut est portrait.
**Nom du paramètre**: IsLandscape
**Type de données**: Boolean
**Valeurs prises en charge**: True, False (par défaut)

**Exemple**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

