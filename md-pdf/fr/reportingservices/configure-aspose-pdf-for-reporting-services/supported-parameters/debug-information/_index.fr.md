---
title: Informations de Débogage
type: docs
weight: 90
url: /reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Il est inévitable qu'il y ait quelque chose de mal avec le rendu ou le résultat rendu. Pour certaines raisons telles que le secret ou la confidentialité, nous ne pourrions pas obtenir la source de données utilisée dans le rapport de l'utilisateur, nous ne pourrions donc pas reproduire l'erreur dans le rapport. Pour rendre la communication entre les clients et les développeurs plus facile et fluide, nous ajoutons ce paramètre. Si vous rencontrez des problèmes lors du rendu de votre rapport avec Aspose.PDF pour Reporting Services, veuillez définir ce paramètre de rapport, puis vous obtiendrez le document rendu au format XML. Après cela, veuillez poster le fichier XML pour nous dans le forum produit.

{{% /alert %}}

{{% alert color="primary" %}}
**Nom du Paramètre**: SavingXmlFormat  
**Type de Donnée**: Boolean  
**Valeurs supportées**: True, False (par défaut)  

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
```