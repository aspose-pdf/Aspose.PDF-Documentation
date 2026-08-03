---
title: Orientation des pages
linktitle: Orientation des pages
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: Configurez l'orientation de la page pour les rapports PDF dans Aspose.PDF pour Reporting Services. Personnalisez les mises en page pour une meilleure présentation.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Definition Language ne permet pas de spécifier explicitement l’orientation des pages dans le rapport. Avec Aspose.PDF pour Reporting Services, vous pouvez facilement demander à l'exportateur de produire des documents PDF avec une orientation de page paysage. L'orientation par défaut est portrait.

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## Exemple

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>
```

