---
title: Informations de débogage
linktitle: Informations de débogage
type: docs
weight: 90
url: /reportingservices/debug-information/
description: Accédez et analysez les informations de débogage pour le rendu PDF dans Aspose.PDF for Reporting Services afin de résoudre efficacement les problèmes.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Il est inévitable qu'il y ait un problème avec le rendu ou le résultat rendu. Pour certaines raisons telles que le secret ou la confidentialité, nous n'avons pas pu obtenir la source de données utilisée dans le rapport de l'utilisateur, et nous n'avons donc pas pu reproduire l'erreur dans le rapport. Pour rendre la communication entre clients et développeurs plus facile et plus fluide, nous ajoutons ce paramètre. Si vous rencontrez des problèmes lors du rendu de votre rapport avec Aspose.PDF pour Reporting Services, veuillez définir ce paramètre de rapport, vous obtiendrez alors le document rendu au format XML. Après cela, veuillez publier le fichier XML pour nous sur le forum produit.

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## Exemple

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}
