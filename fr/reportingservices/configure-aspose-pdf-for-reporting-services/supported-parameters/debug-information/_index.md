---
title: Informations de débogage
linktitle: Informations de débogage
type: docs
weight: 90
url: /fr/reportingservices/debug-information/
description: Accédez aux informations de débogage et analysez‑les pour le rendu PDF dans Aspose.PDF for Reporting Services afin de dépanner efficacement les problèmes.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Il est inévitable qu'il y ait quelque chose qui ne fonctionne pas correctement dans le rendu ou le résultat rendu. Pour certaines raisons, comme le secret ou la confidentialité, nous ne pouvons pas obtenir la source de données utilisée dans le rapport de l'utilisateur, et donc nous ne pouvons pas reproduire l'erreur dans le rapport. Afin de faciliter et d'améliorer la communication entre les clients et les développeurs, nous ajoutons ce paramètre. Si vous rencontrez des problèmes lors du rendu de votre rapport avec Aspose.PDF for Reporting Services, veuillez définir ce paramètre de rapport, vous obtiendrez alors le document rendu au format XML. Ensuite, veuillez publier le fichier XML sur le forum du produit.

{{% /alert %}}

{{% alert color="primary" %}}
**Nom du paramètre**: SavingXmlFormat  
**Type de date** : Boolean  
**Valeurs prises en charge** : True, False (par défaut)  

**Exemple**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

