---
title: Justify FullJustify Alignement du texte
linktitle: Justify FullJustify Alignement du texte
type: docs
weight: 40
url: /fr/reportingservices/justify-fulljustify-text-alignment/
description: Obtenez un alignement du texte parfait dans les rapports PDF avec Aspose.PDF for Reporting Services. Prise en charge des options justify et full justify.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report builder ne prend pas en charge la capacité de spécifier l'alignement du texte pour la zone de texte « Justify » et « FullJustify ». Avec Aspose.Pdf for Reporting Services, vous pouvez le faire facilement en ajoutant des propriétés personnalisées.

{{% /alert %}}

{{% alert color="primary" %}}
**Nom de la propriété personnalisée** : TextAlignment  
**Type de propriété personnalisée** : String  
**Valeurs de propriété personnalisée** : Justify, FullJustify  

Dans le rapport, le code doit être comme suit :

**Exemple**

{{< highlight csharp >}}
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}

