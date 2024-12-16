---
title: Obtenir la Résolution et les Dimensions des Images Intégrées
linktitle: Obtenir la Résolution et les Dimensions
type: docs
weight: 40
url: /fr/java/get-resolution-and-dimensions-of-embedded-images/
description: Cette section montre les détails pour obtenir la résolution et les dimensions des Images Intégrées
lastmod: "2021-06-05"
---

Ce sujet explique comment utiliser les classes opérateurs dans l'espace de noms Aspose.PDF qui offrent la capacité d'obtenir des informations sur la résolution et les dimensions des images sans avoir à les extraire.

Il existe différentes manières d'y parvenir. Cet article explique comment utiliser une `arraylist` et les [classes de placement d'image](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).

1. Tout d'abord, chargez le fichier PDF source (avec des images).
1. Ensuite, créez un objet ArrayList pour contenir les noms de toutes les images dans le document.
1. Obtenez les images en utilisant la propriété Page.Resources.Images.
1. Créez un objet stack pour contenir l'état graphique de l'image et utilisez-le pour suivre les différents états de l'image.

1. Créez un objet ConcatenateMatrix qui définit la transformation actuelle. Il prend également en charge la mise à l'échelle, la rotation et l'inclinaison de tout contenu. Il concatène la nouvelle matrice avec la précédente. Veuillez noter que nous ne pouvons pas définir la transformation à partir de zéro, mais seulement modifier la transformation existante.
1. Étant donné que nous pouvons modifier la matrice avec ConcatenateMatrix, nous pourrions également avoir besoin de revenir à l'état initial de l'image. Utilisez les opérateurs GSave et GRestore. Ces opérateurs sont appariés, ils doivent donc être appelés ensemble. Par exemple, si vous effectuez des travaux graphiques avec des transformations complexes et revenez enfin aux transformations à l'état initial, l'approche sera la suivante :

```java
// Dessiner du texte
GSave

ConcatenateMatrix  // faire pivoter le contenu après l'opérateur

// Quelques travaux graphiques

ConcatenateMatrix // mise à l'échelle (avec la rotation précédente) du contenu après l'opérateur

// Quelques autres travaux graphiques

GRestore

// Dessiner du texte
```

En conséquence, le texte est dessiné sous forme régulière, mais certaines transformations sont effectuées entre les opérateurs de texte.
 Pour afficher l'image ou dessiner des objets et des images de formulaire, nous devons utiliser l'opérateur Do.

Nous avons également une classe nommée XImage qui fournit deux propriétés, Width et Height, qui peuvent être utilisées pour obtenir les dimensions de l'image.

1. Effectuez quelques calculs pour calculer la résolution de l'image.
2. Affichez les informations dans une invite de commande avec le nom de l'image.

Le code suivant vous montre comment obtenir les dimensions et la résolution d'une image sans extraire l'image du document PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // Charger le fichier PDF source
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // Définir la résolution par défaut pour l'image
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // Définir un objet de liste de tableaux qui contiendra les noms des images
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // Insérer un objet dans la pile
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // Obtenir tous les opérateurs sur la première page du document
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // Utilisez les opérateurs GSave/GRestore pour revenir aux transformations précédemment définies
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // Instancier un objet ConcatenateMatrix car il définit la matrice de transformation actuelle.
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // Créer un opérateur Do qui dessine des objets à partir de ressources. Il dessine des objets de formulaire et des objets Image
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // Enregistrer l'état précédent et pousser l'état actuel en haut de la pile
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // Jeter l'état actuel et restaurer le précédent
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // Multiplier la matrice actuelle par la matrice d'état
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // Dans le cas où il s'agit d'un opérateur de dessin d'image
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // Créer un objet XImage pour contenir les images de la première page du pdf
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // Obtenir les dimensions de l'image
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // Obtenir les informations de hauteur et de largeur de l'image
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // Calculer la résolution basée sur les informations ci-dessus
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Afficher les informations de dimension et de résolution de chaque image
                    System.out.printf(_dataDir + "image %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // Enregistrer le document de sortie
                doc.save(_dataDir);
            }
        }
    }
}
```