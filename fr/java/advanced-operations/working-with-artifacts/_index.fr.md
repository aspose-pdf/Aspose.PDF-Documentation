---
title: Travailler avec des Artéfacts 
linktitle: Travailler avec des Artéfacts
type: docs
weight: 110
url: /java/artifacts/
description: Cette page décrit comment travailler avec la classe Artifact en utilisant Aspose.PDF pour Java. Les extraits de code montrent comment ajouter une image de fond aux pages PDF et comment obtenir chaque filigrane sur la première page d'un fichier PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Les artéfacts sont généralement des objets graphiques ou d'autres marques qui ne font pas partie du contenu créé. Dans votre PDF, les exemples d'artéfacts incluent différentes informations, il y a l'en-tête ou le pied de page, des lignes ou d'autres graphiques séparant les sections de la page, ou des images décoratives.

La classe [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) contient :

- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – obtient le type d'artéfact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – obtient le sous-type d'artifact (supporte les valeurs de l'énumération Artifact.ArtifactSubtype où les valeurs incluent Background, Footer, Header, Undefined, Watermark).

Un filigrane créé avec Adobe Acrobat est appelé un artifact (comme décrit dans 14.8.2.2 Contenu Réel et Artifacts de la spécification PDF). Afin de travailler avec des artifacts, Aspose.PDF dispose de deux classes : [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) et [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection).

Pour obtenir tous les artifacts sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) a la propriété Artifacts. Ce sujet explique comment travailler avec les artifacts dans les fichiers PDF.

L'extrait de code suivant montre comment placer un filigrane sur la première page d'un fichier PDF.

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane ou un autre design subtil aux documents. Dans Aspose.PDF pour Java, chaque document PDF est une collection de pages et chaque page contient une collection d'artéfacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

Le code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact.

```java

    public static void SetBackground() throws FileNotFoundException {

        // Ouvrir le document
        Document pdfDocument = new Document();
                
        // Ajouter une nouvelle page à l'objet document
        Page page = pdfDocument.getPages().add();

        // Créer un objet Background Artifact
        BackgroundArtifact background = new BackgroundArtifact();

        // Spécifier l'image pour l'objet backgroundartifact
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // Ajouter BackgroundArtifact à la collection d'artéfacts de la page
        page.getArtifacts().add(background);

        // Enregistrer le PDF modifié
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## Exemples de Programmation : Obtenir un Filigrane

Le snippet de code suivant montre comment obtenir chaque filigrane sur la première page d'un fichier PDF.

```java
    public static void GettingWatermarks() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // Itérer et obtenir le sous-type, le texte et l'emplacement de l'artéfact
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## Exemples de Programmation : Compter les Artéfacts d'un Type Particulier

Pour calculer le nombre total d'artéfacts d'un type particulier (par exemple, le nombre total de filigranes), utilisez le code suivant :

```java
    public static void CountingArtifacts() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // Si le type d'artéfact est filigrane, augmenter le compteur
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("La page contient " + count + " filigranes");
    }
```