---
title: Définir les paramètres
linktitle: Définir les paramètres
type: docs
weight: 10
url: /fr/reportingservices/setting-parameters/
description: Découvrez comment définir les paramètres pour le rendu PDF dans Aspose.PDF for Reporting Services. Obtenez un contrôle précis sur la sortie.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Vous pouvez spécifier certains paramètres de configuration qui affectent la manière dont Aspose.Pdf for Reporting Services génère les documents. Cette section décrit ce processus.

{{% /alert %}}

Pour configurer Aspose.Pdf pour Reporting Services, vous devez modifier le fichier C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. Il s'agit d'un fichier XML et la configuration du rendu se trouve à l'intérieur du ```<Extension>``` élément correspondant au rendu Aspose.PDF.

**Exemple**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}

Si vous souhaitez définir des paramètres pour un fichier de rapport spécifique mais pas pour chaque rapport sur le serveur, vous pouvez ajouter un paramètre de rapport pour le rapport spécifique dans le Report Builder selon les étapes suivantes (par exemple, nous ajouterons un paramètre ‘IsLandscape’ montré précédemment) :

1. Ouvrez le rapport dans le Report Designer, faites un clic droit sur le dossier ‘Parameters’ dans le volet ‘Report Data’, puis sélectionnez ‘Add Parameter…’ (ou, alternativement, déroulez la liste ‘New’ et choisissez ‘Parameter…’).
 
![todo:image_alt_text](setting-parameters_1.png)

1. Dans la boîte de dialogue ‘Report Parameter Properties’, créez le paramètre nommé ‘IsLandscape’, de type de données Boolean, et ajoutez la valeur True dans l’onglet ‘Default Values’.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

