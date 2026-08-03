---
title: Flèches de ligne
linktitle: Flèches de ligne
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: Apprenez à ajouter des flèches de ligne dans les rapports PDF à l'aide d'Aspose.PDF pour Reporting Services. Améliorez les visuels des rapports sans effort.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

La spécification RDL ne spécifie pas les flèches sur l'élément de ligne, donc le générateur de rapports ne prend pas en charge la définition des flèches pour la ligne. Avec Aspose.PDF pour Reporting Services, vous pouvez le faire facilement.

{{% /alert %}}

Actuellement, le moteur de rendu Aspose.PDF prend en charge l'ajout de flèches au début ou à la fin des lignes en ajoutant des propriétés personnalisées.

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

Par exemple, il y a deux lignes nommées `line1` et `line2` dans le fichier de rapport actuel, et line1 a la flèche de début, line2 a les flèches de début et de fin, pour satisfaire ces exigences, vous pouvez ajouter des propriétés personnalisées comme dans le fragment de code suivant.

## Exemple

```xml
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
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
        <Value>True</Value>
      </CustomProperty>
<CustomProperty>
        <Name>HasArrowAtEnd</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>
```

