---
title: Paramètre de sécurité
linktitle: Paramètre de sécurité
type: docs
weight: 30
url: /fr/reportingservices/security-setting/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

La sécurité a toujours été la question la plus importante dans tous les domaines, qu'il s'agisse de la protection d'un réseau ou d'un document PDF. Les documents sont sécurisés pour de nombreuses raisons possibles : l'auteur du document peut vouloir garder le contenu du document en sécurité et ne pas vouloir permettre à d'autres de le modifier, etc.

Aspose.Pdf for Reporting Services a accordé une grande attention à ces aspects de sécurité en offrant ces fonctionnalités aux développeurs, lesquelles peuvent leur être utiles pour protéger leurs documents PDF. Par conséquent, il comprend un certain nombre de paramètres qui permettent aux développeurs d'appliquer différentes mesures de sécurité aux documents PDF.

L'une de ces mesures consiste à protéger le document PDF par un mot de passe lors du chiffrement. Vous pouvez également restreindre ou autoriser la modification du contenu, la copie du contenu, l'impression du document ou autoriser/désactiver le remplissage de formulaires. Ces fonctionnalités ne sont actuellement pas prises en charge par l'exportateur PDF par défaut de SQL Reporting Services, mais vous pouvez les implémenter en utilisant Aspose.Pdf for Reporting Services. Il suffit d'ajouter les paramètres de sécurité correspondants à un rapport ou à un fichier de configuration du serveur de rapports, et vous pourrez créer des documents PDF sécurisés avec des privilèges limités.

Actuellement, le rendu Aspose.Pdf pour Reporting Services prend en charge les attributs de sécurité suivants :

{{% /alert %}}

{{% alert color="primary" %}}

**Nom du paramètre**: Mot de passe utilisateur  
**Type de date**: Chaîne  
**Valeurs prises en charge**: Tout texte brut

**Nom du paramètre**: Mot de passe maître  
**Type de date**: Chaîne  
**Valeurs prises en charge**: Tout texte brut 

**Nom du paramètre**: IsCopyingAllowed  
**Type de données**: Booléen  
**Valeurs prises en charge**: True, False (défaut)  

**Nom du paramètre**: IsPrintingAllowed  
**Type de données**: Booléen  
**Valeurs prises en charge**: True, False (défaut)  

**Nom du paramètre**: IsContentsModifyingAllowed  
**Type de données**: Booléen  
**Valeurs prises en charge**: True, False (défaut)  

**Nom du paramètre**: IsFormFillingAllowed  
**Type de données**: Booléen  
**Valeurs prises en charge**: True, False (défaut)  

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

