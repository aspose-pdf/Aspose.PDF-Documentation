---
title: Flèches de Ligne
type: docs
weight: 20
url: fr/reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

La spécification RDL ne précise pas les flèches concernant l'élément ligne, donc le générateur de rapports ne prend pas en charge le paramétrage des flèches pour la ligne. Avec Aspose.Pdf pour Reporting Services, vous pouvez le faire facilement.

{{% /alert %}}

{{% alert color="primary" %}}

Actuellement, le moteur de rendu Aspose.PDF prend en charge l'ajout de flèches au début ou à la fin des lignes en ajoutant des propriétés personnalisées.

Ajouter une flèche de début pour la ligne  
**Nom de la propriété personnalisée**: HasArrowAtStart  
**Valeur de la propriété personnalisée**: True  

Ajouter une flèche de fin pour la ligne  
**Nom de la propriété personnalisée**: HasArrowAtEnd  
**Valeur de la propriété personnalisée**: True  

Par exemple, il y a deux lignes nommées 'line1' et 'line2' dans le fichier de rapport actuel, et line1 a la flèche de début, line2 a les flèches de début et de fin, pour satisfaire ces exigences, vous pouvez ajouter des propriétés personnalisées comme dans le fragment de code suivant.

**Exemple**

{{< highlight csharp >}}

 <Line Name="line1">

<Style>
  ......
</style>
<CustomProperties>
  <CustomProperty>
    <Name>HasArrowAtStart</Name>
    <Value>Vrai</Value>
  </CustomProperty>
</CustomProperties>
</Line>
......
<Line Name="line2">
<Style>
  ......
</style>
<CustomProperties>
  <CustomProperty>
    <Name>HasArrowAtStart</Name>
    <Value>Vrai</Value>
  </CustomProperty>
<CustomProperty>
    <Name>HasArrowAtEnd</Name>
    <Value>Vrai</Value>
  </CustomProperty>
</CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
```