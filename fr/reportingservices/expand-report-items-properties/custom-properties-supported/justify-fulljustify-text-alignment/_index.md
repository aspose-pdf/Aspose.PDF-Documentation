---
title: Justifier l'alignement du texte en Justify FullJustify
type: docs
weight: 40
url: /fr/reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le générateur de rapports ne prend pas en charge la capacité de spécifier l'alignement du texte pour la zone de texte « Justify » et « FullJustify ». Avec Aspose.Pdf pour Reporting Services, vous pouvez le faire facilement en ajoutant des propriétés personnalisées.

{{% /alert %}}

{{% alert color="primary" %}}
**Nom de la propriété personnalisée** : TextAlignment  
**Type de propriété personnalisée** : String  
**Valeurs de propriété personnalisée** : Justify, FullJustify  

Dans le rapport, le code doit être comme suit :

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