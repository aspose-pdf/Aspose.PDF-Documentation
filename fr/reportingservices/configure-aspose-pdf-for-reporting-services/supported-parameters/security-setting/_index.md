---
title: Paramètre de sécurité
linktitle: Paramètre de sécurité
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

La sécurité a toujours été la question la plus importante dans tous les domaines, qu'il s'agisse de la protection d'un réseau ou d'un document PDF. Les documents sont sécurisés pour de nombreuses raisons possibles : l'auteur du document peut souhaiter garder le contenu du document en sécurité et ne veut pas permettre à d'autres de le modifier, etc.

Aspose.PDF for Reporting Services a pris grand soin de ces aspects de sécurité en fournissant ces fonctionnalités aux développeurs qui peuvent leur être utiles pour protéger leurs documents PDF. Par conséquent, il contient un certain nombre de paramètres qui permettent aux développeurs d'appliquer différentes mesures de sécurité aux documents PDF.

L'une de ces mesures consiste à protéger par mot de passe le document PDF pendant le cryptage. Vous pouvez également restreindre ou autoriser la modification du contenu, la copie du contenu, l'impression de documents ou autoriser/désactiver le remplissage de formulaires. Ces fonctionnalités ne sont actuellement pas prises en charge par l'exportateur PDF SQL Reporting Services par défaut, mais vous pouvez implémenter ces fonctionnalités à l'aide d'Aspose.PDF pour Reporting Services. Ajoutez simplement les paramètres de sécurité correspondants à un rapport ou à un fichier de configuration de serveur de rapports et vous pourrez créer des documents PDF sécurisés avec des privilèges limités.

Actuellement, le moteur de rendu Aspose.PDF pour Reporting Services prend en charge les attributs de sécurité suivants :

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## Exemple

```xml
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
```

