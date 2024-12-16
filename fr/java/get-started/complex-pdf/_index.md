---
title: Création d'un PDF complexe
linktitle: Création d'un PDF complexe
type: docs
weight: 60
url: /fr/java/complex-pdf-example/
description: Aspose.PDF pour Java vous permet de créer des documents plus complexes contenant des images, des fragments de texte et des tableaux dans un seul document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'exemple [Hello, World](/pdf/fr/java/hello-world-example/) a montré les étapes simples pour créer un document PDF en utilisant Java et Aspose.PDF. Dans cet article, nous allons examiner la création d'un document plus complexe avec Java et Aspose.PDF pour Java. À titre d'exemple, nous prendrons un document d'une entreprise fictive qui exploite des services de ferry pour passagers.
Notre document contiendra une image, deux fragments de texte (en-tête et paragraphe), et un tableau. Pour construire un tel document, nous utiliserons une approche basée sur le DOM. Vous pouvez en lire plus dans la section [Notions de base de l'API DOM](/pdf/fr/java/basics-of-dom-api/).

Si nous créons un document à partir de zéro, nous devons suivre certaines étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Dans cette étape, nous allons créer un document PDF vide avec quelques métadonnées mais sans pages.
1. Ajouter une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) à l'objet document. Ainsi, notre document aura maintenant une page.
1. Ajouter une [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). C'est une opération complexe basée sur des actions de bas niveau avec des opérateurs PDF.
    - Charger l'image depuis le flux
    - Ajouter l'image à la collection Images des ressources de la page
    - Utilisation de l'opérateur GSave : cet opérateur enregistre l'état graphique actuel.
    - Créer un objet [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Utilisation de l'opérateur ConcatenateMatrix : définit comment l'image doit être placée.
    - Utilisation de l'opérateur Do : cet opérateur dessine l'image.
    - Utilisation de l'opérateur GRestore : cet opérateur restaure l'état graphique.

1. Créer un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) pour l'en-tête. Pour l'en-tête, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajouter l'en-tête aux [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Créer un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) pour la description. Pour la description, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajouter (description) aux Paragraphs de la page.
1. Créer un tableau, ajouter les propriétés du tableau.
1. Ajouter (table) aux [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Enregistrer un document "Complex.pdf".

```java
package com.aspose.pdf.examples;

/**
 * Exemple Complexe
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // Initialiser l'objet document
        Document document = new Document();
        // Ajouter une page
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // Ajouter une image
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // Ajouter l'image à la collection d'images des ressources de la page
        page.getResources().getImages().add(imageStream);

        // Utiliser l'opérateur GSave : cet opérateur sauvegarde l'état graphique actuel
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // Créer un objet Matrix
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // Utiliser l'opérateur ConcatenateMatrix (concaténer la matrice) : définit comment l'image doit être placée
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Utiliser l'opérateur Do : cet opérateur dessine l'image
        page.getContents().add(new Do(ximage.getName()));
        // Utiliser l'opérateur GRestore : cet opérateur restaure l'état graphique
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // Ajouter l'en-tête
        TextFragment header = new TextFragment("Nouvelles lignes de ferry à l'automne 2020");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Ajouter la description
        String descriptionText = "Les visiteurs doivent acheter des billets en ligne et les billets sont limités à 5 000 par jour. Le service de ferry fonctionne à moitié capacité et sur un horaire réduit. Attendez-vous à des files d'attente.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Ajouter le tableau
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Départs Ville");
        headerRow.getCells().add("Départs Île");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```