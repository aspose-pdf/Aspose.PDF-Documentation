---

title: Ajouter un filigrane au PDF 
linktitle: Ajouter un filigrane
type: docs
weight: 90
url: /fr/java/add-watermarks/
description: Cet article explique les fonctionnalités de travail avec des artefacts et d'obtention de filigranes dans les PDF en utilisant Java de manière programmatique.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** permet d'ajouter des filigranes à votre document PDF en utilisant des artefacts. Veuillez consulter cet article pour résoudre votre tâche.

Un filigrane créé avec Adobe Acrobat est appelé un artefact (comme décrit dans la section 14.8.2.2 Contenu Réel et Artefacts de la spécification PDF). Pour travailler avec des artefacts, Aspose.PDF dispose de deux classes : [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) et [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

Pour obtenir tous les artefacts sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) a la propriété Artifacts.
 This topic explains how to work with artifact in PDF files.

## Travailler avec des Artéfacts

La classe [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) contient les propriétés suivantes :

**Artifact.Type** – obtient le type d'artéfact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
**Artifact.Subtype** – obtient le sous-type d'artéfact (prend en charge les valeurs de l'énumération Artifact.ArtifactSubtype où les valeurs incluent Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Veuillez noter que les filigranes créés avec Adobe Acrobat ont le type Pagination et le sous-type Watermark.

{{% /alert %}}

**Artifact.Contents** – Obtient une collection d'opérateurs internes d'artéfact. Son type pris en charge est System.Collections.ICollection.
**Artifact.Form** – Obtient le XForm d'un artéfact (si un XForm est utilisé). Les artéfacts de filigrane, d'en-tête et de pied de page contiennent un XForm qui montre tous les contenus d'artéfact.

**Artifact.Image** – Obtient l'image d'un artéfact (si une image est présente, sinon null).**Artifact.Text** – Obtient le texte d'un artefact.  
**Artifact.Rectangle** – Obtient la position d'un artefact sur la page.  
**Artifact.Rotation** – Obtient la rotation d'un artefact (en degrés, une valeur positive indique une rotation dans le sens antihoraire).  
**Artifact.Opacity** – Obtient l'opacité d'un artefact. Les valeurs possibles sont dans la plage 0…1, où 1 est complètement opaque.

## Exemples de programmation : Obtenir des filigranes

Le snippet de code suivant montre comment obtenir chaque filigrane sur la première page d'un fichier PDF avec Java.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.EncodingType;
import com.aspose.pdf.facades.FontStyle;
import com.aspose.pdf.facades.FormattedText;

public class ExampleWatermark {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {

        // Ouvrir le document
        Document doc = new Document(_dataDir + "text.pdf");      
        FormattedText formattedText = new FormattedText("Watermark", java.awt.Color.BLUE,FontStyle.Courier, EncodingType.Identity_h, true, 72.0F);
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(formattedText);        
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }

}  
```