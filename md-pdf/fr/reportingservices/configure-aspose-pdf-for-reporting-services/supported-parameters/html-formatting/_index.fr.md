---
title: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Parfois, vous pourriez souhaiter exporter du texte dans des zones de texte avec formatage. Malheureusement, Reporting Services ne le prend pas en charge. Cependant, vous pouvez toujours le mettre en œuvre en utilisant Aspose.PDF pour Reporting Services. Il suffit d'activer un mode spécial dans lequel tout le texte des zones de texte est traité comme du HTML et d'insérer les balises HTML nécessaires pour formater le texte dans le document de sortie. Par exemple, pour avoir du texte normal, en gras et en italique dans la même zone de texte, entrez la valeur suivante dans la zone de texte :

Some of this text is ```<b>bold</b>``` and other text is ```<i>italic</i>```.

Lors de l'exportation, le texte apparaîtra comme suit : une partie de ce texte est **en gras** et une autre partie est *en italique*.

Veuillez noter que cette approche présente certaines limitations

{{% /alert %}}

{{% alert color="primary" %}}

- Le formatage n'est pas visible lors de la conception (dans le Report Builder, le portail web de Reporting Services, etc.). Au lieu de cela, vous verrez le texte HTML sous forme de texte brut avec des balises.
- L'extension de rendu Aspose.PDF pour Reporting Services reconnaît et formate correctement le code HTML dans les zones de texte. Le moteur de rendu PDF par défaut de Reporting Services exportera ce balisage en tant que texte brut.

**Nom du Paramètre**: IsHtmlTagSupported  
**Type de Donnée**: Boolean  
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

Si vous souhaitez ajouter ce paramètre dans le Concepteur de rapports, utilisez le type de données 'Boolean'.

Actuellement, Aspose.Pdf pour Reporting Services prend en charge un sous-ensemble de toutes les balises HTML. Vous pouvez trouver plus d'informations dans la [Documentation](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) Aspose.PDF.