---
title: Ajouter des Propriétés Personnalisées
type: docs
weight: 10
url: /fr/reportingservices/adding-custom-properties/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Vous pouvez ajouter des propriétés personnalisées à certains éléments de rapport pour étendre leur utilisation, tels que la table des matières, les flèches de ligne, etc. Cette section décrit ce processus.

{{% /alert %}}

{{% alert color="primary" %}}

Vous pouvez ajouter des propriétés personnalisées à certains éléments de rapport pour étendre leur utilisation, tels que la table des matières, les flèches de ligne, etc. Cette section décrit ce processus.

Pour ajouter des propriétés personnalisées, vous devez modifier le fichier de code du document RDL selon les étapes suivantes :

1. Comme dans l'illustration suivante, ouvrez votre projet, naviguez jusqu'à l'explorateur de solutions et faites un clic droit sur le fichier de rapport sélectionné, puis sélectionnez l'élément de menu 'Afficher le code'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Modifiez le fichier de code XML. Par exemple, si vous souhaitez ajouter une propriété personnalisée pour un élément de rapport graphique, vous devez ajouter le code similaire au texte en rouge dans l'exemple suivant.
```

**Example**

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