---
title: Flèches de ligne
linktitle: Flèches de ligne
type: docs
weight: 20
url: /fr/reportingservices/line-arrows/
description: Apprenez à ajouter des flèches de ligne dans les rapports PDF à l’aide d’Aspose.PDF for Reporting Services. Améliorez l’aspect visuel des rapports sans effort.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

La spécification RDL ne définit pas les flèches pour l’élément ligne, de sorte que le générateur de rapports ne prend pas en charge le paramétrage des flèches pour les lignes. Avec Aspose.Pdf for Reporting Services, vous pouvez le faire facilement.

{{% /alert %}}

{{% alert color="primary" %}}

Actuellement, le rendu Aspose.PDF prend en charge l’ajout de flèches au début ou à la fin des lignes en ajoutant des propriétés personnalisées.

Ajouter une flèche de début pour la ligne  
**Propriété personnalisée** **Nom**: HasArrowAtStart  
**Valeur de la propriété personnalisée**: True  

Ajouter une flèche de fin pour la ligne  
**Propriété personnalisée** **Nom**: HasArrowAtEnd  
**Valeur de la propriété personnalisée**: True  

Par exemple, il existe deux lignes nommées 'line1' et 'line2' dans le fichier de rapport actuel, et line1 possède la flèche de départ, line2 possède les flèches de départ et de fin, pour répondre à ces exigences, vous pouvez ajouter des propriétés personnalisées comme dans le fragment de code suivant.

**Exemple**

{{< highlight csharp >}}
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

{{< /highlight >}}
{{% /alert %}}

