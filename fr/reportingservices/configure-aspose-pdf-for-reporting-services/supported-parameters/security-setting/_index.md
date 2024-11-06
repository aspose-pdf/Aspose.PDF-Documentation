---
title: Paramètre de sécurité
type: docs
weight: 30
url: fr/reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

La sécurité a toujours été l'enjeu le plus important dans chaque domaine, qu'il s'agisse de la protection d'un réseau ou d'un document PDF. Les documents sont sécurisés pour de nombreuses raisons possibles : l'auteur du document peut souhaiter garder le contenu du document en sécurité et ne veut pas permettre à d'autres de le modifier, etc.

Aspose.Pdf pour Reporting Services a pris grand soin de ces aspects de sécurité en fournissant ces fonctionnalités aux développeurs qui peuvent leur être utiles pour protéger leurs documents PDF. Par conséquent, il contient un certain nombre de paramètres qui permettent aux développeurs d'appliquer différentes mesures de sécurité aux documents PDF.

L'une de ces mesures est de protéger par mot de passe le document PDF lors du cryptage. Vous pouvez également restreindre ou autoriser la modification du contenu, la copie du contenu, l'impression du document ou autoriser/désactiver le remplissage de formulaire. Ces fonctionnalités ne sont actuellement pas prises en charge par le module d'exportation PDF par défaut des services de rapports SQL, mais vous pouvez implémenter ces fonctionnalités en utilisant Aspose.Pdf pour Reporting Services. Il suffit d'ajouter les paramètres de sécurité correspondants à un rapport ou à un fichier de configuration du serveur de rapports, et vous pourrez créer des documents PDF sécurisés avec des privilèges limités.

Actuellement, le module Aspose.Pdf pour Reporting Services prend en charge les attributs de sécurité suivants :

{{% /alert %}}

{{% alert color="primary" %}}

**Nom du Paramètre**: Mot de Passe Utilisateur  
**Type de Donnée**: Chaîne  
**Valeurs prises en charge**: Tout texte brut  

**Nom du Paramètre**: Mot de Passe Administrateur  
**Type de Donnée**: Chaîne  
**Valeurs prises en charge**: Tout texte brut  

**Nom du Paramètre**: IsCopyingAllowed  
**Type de Donnée**: Booléen  
**Valeurs prises en charge**: True, False (défaut)  

**Nom du Paramètre**: IsPrintingAllowed  
**Type de Donnée**: Booléen  

**Valeurs prises en charge**: True, False (défaut)  
**Parameter Name**: IsContentsModifyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (défaut)  

**Parameter Name**: IsFormFillingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (défaut)  

**Exemple**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}