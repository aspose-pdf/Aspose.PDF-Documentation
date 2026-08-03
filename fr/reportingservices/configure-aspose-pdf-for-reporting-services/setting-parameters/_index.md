---
title: Paramètres de réglage
linktitle: Paramètres de réglage
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: Découvrez comment définir les paramètres de rendu PDF dans Aspose.PDF pour Reporting Services. Obtenez un contrôle précis de la production.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Vous pouvez spécifier certains paramètres de configuration qui affectent la manière dont Aspose.PDF for Reporting Services génère des documents. Cette section décrit ce processus.

{{% /alert %}}

Pour configurer Aspose.Pdf pour Reporting Services, vous devez modifier le fichier `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Il s'agit d'un fichier XML et la configuration du moteur de rendu se trouve à l'intérieur de l'élément `<Extension>` correspondant au moteur de rendu Aspose.PDF.

## Exemple

```xml
<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>
```

{{% alert color="primary" %}}

Si vous souhaitez définir des paramètres pour un fichier de rapport spécifique mais pas pour chaque rapport sur le serveur, vous pouvez ajouter un paramètre de rapport pour le rapport spécifique dans le générateur de rapports en suivant les étapes suivantes (par exemple, nous ajouterons un paramètre « IsLandscape » indiqué précédemment) :

1. Ouvrez le rapport dans le Concepteur de rapports, cliquez avec le bouton droit sur le dossier « Paramètres » dans le volet « Données du rapport » et sélectionnez « Ajouter un paramètre… » (ou, alternativement, déroulez la liste « Nouveau » et sélectionnez « Paramètre… »).

![Parameters set up. Step 1](setting-parameters_1.png)

1. Dans la boîte de dialogue « Propriétés des paramètres du rapport », créez le paramètre nommé « IsLandscape », avec le type de données Boolean, et ajoutez la valeur True dans l'onglet « Valeurs par défaut ».

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
