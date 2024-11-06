---
title: Installer sur le serveur de rapports
type: docs
weight: 10
url: fr/reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Vous n'avez besoin de suivre ces étapes que si vous installez Aspose.PDF pour Reporting Services manuellement, sans utiliser l'installateur MSI. L'installateur MSI effectue automatiquement toutes les actions nécessaires d'installation et d'enregistrement.

{{% /alert %}}

Dans les étapes suivantes, vous devrez copier et modifier des fichiers dans le répertoire où Microsoft SQL Server Reporting Services est installé. L'assemblage SSRS 2016 est situé dans le répertoire \Bin\SSRS2016 du package zip; l'assemblage SSRS 2017 est situé dans le répertoire \Bin\SSRS2017; l'assemblage SSRS 2019 est situé dans le répertoire \Bin\SSRS2019; l'assemblage SSRS 2022 est situé dans le répertoire \Bin\SSRS2022; l'assemblage Power BI Report Server est situé dans le répertoire \Bin\PowerBI.

{{% alert color="primary" %}}

**Étape 1.** Localisez le répertoire d'installation du serveur de rapports. Le répertoire racine pour Microsoft SQL Server est généralement C:\Program Files\Microsoft SQL Server. Le processus est légèrement différent pour Reporting Services 2016, Reporting Services 2017 et versions ultérieures, et Power BI Report Server :

- Par défaut, Report Server 2016 est installé dans le répertoire C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Si vous utilisez des instances nommées personnalisées au lieu de l'instance par défaut, le chemin par défaut sera C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Par défaut, Report Server 2017 et versions ultérieures sont installés dans le répertoire C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Par défaut, Power BI Report Server est installé dans le répertoire C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

Dans le texte suivant, le répertoire d'installation des Reporting Services (l'un des chemins susmentionnés) sera référencé comme ```<Instance>```.
{{% /alert %}}


{{% alert color="primary" %}}**Étape 2.** Copiez Aspose.Pdf.ReportingServices.dll pour la version SSRS correspondante dans le dossier ```<Instance>```\bin.
{{% /alert %}}

{{% alert color="primary" %}}
**Étape 3.** Enregistrez Aspose.Pdf pour Reporting Services en tant qu'extension de rendu. Ouvrez le fichier ```<Instance>```\rsreportserver.config et ajoutez les lignes suivantes dans l'élément ```<Render>``` :
{{% /alert %}}

**Exemple**

{{< highlight csharp >}}

 <Render>
...
<!--Commencez ici.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**Étape 4.** Autorisez Aspose.Pdf pour Reporting Services à exécuter. Ouvrez le fichier ```<Instance>```\rssrvpolicy.config et ajoutez le texte suivant comme dernier élément dans le deuxième à l'extérieur de l'élément ```<CodeGroup>``` (qui devrait être ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="Ce groupe de code accorde l'autorisation d'exécution du code MyComputer. ">):```

{{% /alert %}}

**Example**

{{< highlight csharp >}}

<CodeGroup>
...

<CodeGroup>
...

<!--Commencez ici.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="Ce groupe de code accorde une confiance totale à l'assemblage AP4SSRS.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--Terminez ici. -->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

{{% alert color="primary" %}}
**Étape 5.** Vérifiez que Aspose.Pdf pour Reporting Services a été installé avec succès. Ouvrez le portail web de Reporting Services et vérifiez la liste des formats d'exportation disponibles pour un rapport. Vous pouvez lancer le portail web en démarrant un navigateur web et en tapant l'URL du portail web de Reporting Services dans la barre d'adresse (par défaut, c'est http://```<Reporting_Services_server_name>```/reports/). Sélectionnez l'un des rapports disponibles dans votre portail web et déroulez la liste Exporter. Vous devriez voir la liste des formats d'exportation, y compris ceux fournis par l'extension Aspose.Pdf pour Reporting Services. Sélectionnez l'élément PDF via Aspose.PDF.

![todo:image_alt_text](install-to-report-server_1.png)

Cliquez sur l'élément sélectionné. Cela générera le rapport dans le format sélectionné, l'enverra au client et, en fonction des paramètres de votre navigateur web, soit vous montrera la boîte de dialogue Enregistrer le fichier pour choisir où enregistrer le rapport exporté, soit téléchargera automatiquement le fichier dans votre dossier Téléchargements.

Félicitations, vous avez installé avec succès Aspose.Pdf pour Reporting Services et exporté un rapport en tant que document PDF !{{% /alert %}}