---
title: Orientation de la Page
type: docs
weight: 10
url: /fr/reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le langage de définition de rapport ne permet pas de spécifier explicitement l'orientation des pages dans le rapport. Avec Aspose.Pdf pour Reporting Services, vous pouvez facilement instruire l'exportateur pour produire des documents PDF avec une orientation de page en paysage. L'orientation par défaut est le portrait.

{{% /alert %}}

{{% alert color="primary" %}}

L'orientation par défaut est le portrait.
**Nom du Paramètre**: IsLandscape
**Type de Donnée**: Boolean
**Valeurs supportées**: True, False (défaut)

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