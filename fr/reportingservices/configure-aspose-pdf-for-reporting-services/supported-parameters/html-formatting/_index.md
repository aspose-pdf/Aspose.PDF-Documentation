---
title: Formatage HTML
linktitle: Formatage HTML
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: Activez le formatage HTML dans les rapports PDF à l'aide d'Aspose.PDF pour Reporting Services. Ajoutez facilement des styles et de la structure.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Parfois, vous souhaiterez peut-être exporter du texte dans des zones de texte avec mise en forme. Malheureusement, Reporting Services ne prend pas en charge cela. Cependant, vous pouvez toujours l'implémenter à l'aide d'Aspose.PDF pour Reporting Services. Activez simplement un mode spécial dans lequel tout le texte des zones de texte est traité comme du HTML et placez les balises HTML nécessaires pour formater le texte dans le document de sortie. Par exemple, pour avoir du texte normal, gras et italique dans la même zone de texte, saisissez la valeur de zone de texte suivante :

Une partie de ce texte est `<b>bold</b>` et une autre partie du texte est `<i>italic</i>`.

Une fois exporté, le texte ressemblera à une partie de ce texte en **gras** et d'autres textes en *italique*.

Veuillez noter que cette approche présente certaines limites

{{% /alert %}}

{{% alert color="primary" %}}

- Le formatage n'est pas visible au moment de la conception (dans le Report Builder, le portail Web Reporting Services, etc.). Au lieu de cela, vous verrez le texte HTML sous forme de texte brut avec des balises.
- L'extension de rendu Aspose.PDF pour Reporting Services reconnaît et formate correctement le code HTML dans les zones de texte. Le moteur de rendu PDF par défaut de Reporting Services exportera ce balisage sous forme de texte brut.

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## Exemple

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

Si vous souhaitez ajouter ce paramètre dans Report Designer, utilisez le type de données `Boolean`.

Actuellement, Aspose.Pdf pour Reporting Services prend en charge un sous-ensemble de toutes les balises HTML. Vous pouvez trouver plus d'informations dans Aspose.PDF [Documentation] (https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}
