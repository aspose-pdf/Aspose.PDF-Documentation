---
title: Mise en forme HTML
linktitle: Mise en forme HTML
type: docs
weight: 20
url: /fr/reportingservices/html-formatting/
description: Activez la mise en forme HTML dans les rapports PDF à l'aide d'Aspose.PDF for Reporting Services. Ajoutez des styles et une structure en toute simplicité.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Il arrive parfois que vous souhaitiez exporter du texte dans les zones de texte avec mise en forme. Malheureusement, Reporting Services ne le prend pas en charge. Cependant, vous pouvez tout de même le mettre en œuvre en utilisant Aspose.PDF for Reporting Services. Il suffit d'activer un mode spécial dans lequel tout le texte des zones de texte est traité comme du HTML et d'insérer les balises HTML nécessaires pour formater le texte dans le document de sortie. Par exemple, pour avoir du texte normal, gras et italique dans la même zone de texte, saisissez la valeur suivante de la zone de texte :

Une partie de ce texte est ```<b>bold</b>``` et l'autre texte est ```<i>italic</i>```.

Une fois exporté, le texte apparaîtra comme suit, certaines parties de ce texte sont **bold** et d'autres parties sont *italic*.

Veuillez noter que cette approche comporte certaines limites

{{% /alert %}}

{{% alert color="primary" %}}

- Le formatage n’est pas visible au moment de la conception (dans le Report Builder, le portail web de Reporting Services, etc.). Au lieu de cela, vous verrez le texte HTML sous forme de texte brut avec des balises.
- L’extension de rendu Aspose.PDF for Reporting Services reconnaît et formate correctement le code HTML dans les zones de texte. Le rendu PDF par défaut de Reporting Services exportera ce balisage en texte brut.

**Nom du paramètre**: IsHtmlTagSupported  
**Type de données**: Boolean  
**Valeurs prises en charge**: True, False (par défaut)   

**Exemple**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

Si vous souhaitez ajouter ce paramètre dans le Report Designer, utilisez le type de données 'Boolean'.

 
Actuellement, Aspose.Pdf for Reporting Services prend en charge un sous‑ensemble de toutes les balises HTML. Vous pouvez trouver plus d’informations dans la documentation Aspose.PDF. [Documentation](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}

