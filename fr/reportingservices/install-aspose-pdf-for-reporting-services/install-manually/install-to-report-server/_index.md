---
title: Installer sur le serveur de rapports
linktitle: Installer sur le serveur de rapports
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Vous ne devez suivre ces étapes que si vous installez Aspose.PDF pour Reporting Services manuellement, sans utiliser le programme d'installation MSI. Le programme d'installation MSI effectue automatiquement toutes les actions d'installation et d'enregistrement nécessaires.

{{% /alert %}}

Dans les étapes suivantes, vous devrez copier et modifier les fichiers dans le répertoire où Microsoft SQL Server Reporting Services est installé. L'assembly SSRS 2016 se trouve dans le répertoire \Bin\SSRS2016 du package zip ; l'assembly SSRS 2017 se trouve dans le répertoire \Bin\SSRS2017 ; l'assembly SSRS 2019 se trouve dans le répertoire \Bin\SSRS2019 ; l'assembly SSRS 2022 se trouve dans le répertoire \Bin\SSRS2022 ; l’assembly Power BI Report Server se trouve dans le répertoire \Bin\PowerBI.

**Étape 1.** Localisez le répertoire d'installation de Report Server. Le répertoire racine de Microsoft SQL Server est généralement C:\Program Files\Microsoft SQL Server. La suite du processus est légèrement différente pour Reporting Services 2016, Reporting Services 2017 et versions ultérieures et Power BI Report Server :

- Report Server 2016 est installé par défaut dans le répertoire C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Si vous utilisez des instances nommées personnalisées au lieu de celle par défaut, le chemin par défaut sera C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Report Server 2017 et versions ultérieures sont installés par défaut dans le répertoire C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Power BI Report Server est installé par défaut dans le répertoire C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

Dans le texte suivant, le répertoire d'installation de Reporting Services (l'un des chemins mentionnés ci-dessus) sera référencé par `<Instance>`.

**Étape 2.** Copiez Aspose.Pdf.ReportingServices.dll pour la version SSRS correspondante dans le dossier `<Instance>\bin`.

**Étape 3.** Enregistrez Aspose.PDF pour Reporting Services en tant qu'extension de rendu. Ouvrez le fichier `<Instance>\rsreportserver.config` et ajoutez les lignes suivantes dans l'élément `<Render>` :

## Exemple

```xml
<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>
</Render>
```

**Étape 4.** Fournissez à Aspose.PDF pour Reporting Services les autorisations d'exécution. Ouvrez le fichier `<Instance>\rssrvpolicy.config` et ajoutez le texte suivant comme dernier élément du deuxième élément externe `<CodeGroup>` qui devrait être `<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):`

## Exemple

```xml

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>
```

**Étape 5.** Vérifiez qu'Aspose.PDF pour Reporting Services a été installé avec succès. Ouvrez le portail Web Reporting Services et vérifiez la liste des formats d'exportation disponibles pour un rapport. Vous pouvez lancer le portail Web en démarrant un navigateur Web et en tapant l'URL du portail Web Reporting Services dans la barre d'adresse (par défaut, il s'agit de `http://<Reporting_Services_server_name>/reports/`). Sélectionnez l'un des rapports disponibles dans votre portail Web et tirez la liste déroulante Exporter. Vous devriez voir la liste des formats d'exportation, y compris ceux fournis par l'extension Aspose.PDF pour Reporting Services. Sélectionnez PDF via l'élément Aspose.PDF.

![Install to report server](install-to-report-server_1.png)

Cliquez sur l'élément sélectionné. Il générera le rapport dans le format sélectionné, l'enverra au client et, en fonction des paramètres de votre navigateur Web, vous montrera la boîte de dialogue Enregistrer le fichier pour choisir où enregistrer le rapport exporté ou téléchargera automatiquement le fichier dans votre dossier Téléchargements.

Félicitations, vous avez installé avec succès Aspose.PDF pour Reporting Services et exporté un rapport sous forme de document PDF !


