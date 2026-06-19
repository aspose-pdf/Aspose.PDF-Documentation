---
title: Ajout de propriétés personnalisées
linktitle: Ajout de propriétés personnalisées
type: docs
weight: 10
url: /fr/reportingservices/adding-custom-properties/
description: Apprenez comment ajouter des propriétés personnalisées aux rapports PDF avec Aspose.PDF pour Reporting Services. Personnalisez vos documents efficacement.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Vous pouvez ajouter des propriétés personnalisées à certains éléments de rapport pour étendre leur utilisation, comme la ToC, les flèches de ligne, etc. Cette section décrit ce processus.

{{% /alert %}}

{{% alert color="primary" %}}

Vous pouvez ajouter des propriétés personnalisées à certains éléments de rapport pour étendre leur utilisation, comme la Table des matières, les flèches de ligne, etc. Cette section décrit ce processus.

Pour ajouter des propriétés personnalisées, vous devez modifier le fichier de code du document RDL selon les étapes suivantes :

1. Comme le montre la figure suivante, ouvrez votre projet, naviguez jusqu’à l’explorateur de solution, cliquez avec le bouton droit sur le fichier de rapport sélectionné, puis choisissez l’option \u0027View Code\u0027 du menu.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Modifiez le fichier de code XML. Par exemple, si vous souhaitez ajouter une propriété personnalisée pour un élément de rapport de type graphique, vous devez ajouter le code similaire au texte rouge dans l’exemple suivant.

**Exemple**

{{< highlight csharp >}}

<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 

{{< /highlight >}}

Dans cet exemple de fragment de code, le nom de la propriété personnalisée est IsInList, et la valeur est 'True'.

{{% /alert %}}

