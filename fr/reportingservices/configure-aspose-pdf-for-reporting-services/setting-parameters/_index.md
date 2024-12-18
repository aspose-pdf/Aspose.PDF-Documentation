---
title: Paramètres de Configuration
type: docs
weight: 10
url: /fr/reportingservices/setting-parameters/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Vous pouvez spécifier certains paramètres de configuration qui affectent la manière dont Aspose.Pdf pour Reporting Services génère les documents. Cette section décrit ce processus.

{{% /alert %}}

Pour configurer Aspose.Pdf pour Reporting Services, vous devez éditer le fichier C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. Il s'agit d'un fichier XML et la configuration du rendu se trouve à l'intérieur de l'élément ```<Extension>``` correspondant au moteur de rendu Aspose.PDF.

**Exemple**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insérez ici les éléments de configuration pour l'exportation en PDF. Voici un exemple
Pour l'orientation de la page -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}


{{% alert color="primary" %}}

Si vous souhaitez définir des paramètres pour un fichier de rapport spécifique mais pas pour chaque rapport sur le serveur, vous pouvez ajouter un paramètre de rapport pour le rapport spécifique dans le Générateur de Rapports en suivant les étapes suivantes (par exemple, nous ajouterons un paramètre 'IsLandscape' montré précédemment) :

1. Ouvrez le rapport dans le Concepteur de Rapports, cliquez avec le bouton droit sur le dossier 'Paramètres' dans le volet 'Données du Rapport', et sélectionnez 'Ajouter un Paramètre...' (ou, alternativement, déroulez la liste 'Nouveau' et sélectionnez 'Paramètre...').

![todo:image_alt_text](setting-parameters_1.png)

1. Dans la boîte de dialogue 'Propriétés du Paramètre de Rapport', créez le paramètre nommé 'IsLandscape', avec le type de données Boolean, et ajoutez la valeur True dans l'onglet 'Valeurs par Défaut'.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}