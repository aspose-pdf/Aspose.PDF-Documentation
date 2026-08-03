---
title: Justifier l'alignement complet du texte
linktitle: Justifier l'alignement complet du texte
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: Obtenez un alignement parfait du texte dans les rapports PDF avec Aspose.PDF pour Reporting Services. Prise en charge des options de justification et de justification complète.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Le générateur de rapports ne prend pas en charge la possibilité de spécifier l'alignement du texte pour la zone de texte. `Justify` et `FullJustify`. Avec Aspose.PDF pour Reporting Services, vous pouvez le faire facilement en ajoutant des propriétés personnalisées.

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

Dans le rapport, le code devrait ressembler à ce qui suit :

## Exemple

```xml
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
```
