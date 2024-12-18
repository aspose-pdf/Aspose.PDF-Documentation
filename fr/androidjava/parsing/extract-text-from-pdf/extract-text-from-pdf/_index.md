---
title: Extraire le texte brut d'un fichier PDF 
linktitle: Extraire du texte d'un PDF
type: docs
weight: 10
url: /fr/androidjava/extract-text-from-all-pdf/
description: Cet article décrit différentes manières d'extraire du texte de documents PDF à l'aide d'Aspose.PDF pour Android via Java. De pages entières, d'une partie spécifique, basé sur des colonnes, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire le texte de toutes les pages d'un document PDF

Extraire du texte d'un document PDF est une exigence courante. Dans cet exemple, vous verrez comment Aspose.PDF pour Java permet d'extraire du texte de toutes les pages d'un document PDF.
Pour extraire du texte de toutes les pages PDF :

1. Créez un objet de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Ouvrez le PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et appelez la méthode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) de la collection [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. La classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorbe le texte du document et le retourne dans la propriété **Text**.

Le code suivant vous montre comment extraire le texte de toutes les pages d'un document PDF.

```java
public static void ExtractFromAllPages() {
        // Le chemin vers le répertoire des documents.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Ouvrir le document
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Créer un objet TextAbsorber pour extraire le texte
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Accepter l'absorbeur pour toutes les pages
        pdfDocument.getPages().accept(textAbsorber);

        // Obtenir le texte extrait
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Écrire une ligne de texte dans le fichier
            writer.write(extractedText);
            // Fermer le flux
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## Extraire le Texte Surligné d'un Document PDF

Dans divers scénarios d'extraction de texte à partir d'un document PDF, vous pouvez avoir besoin d'extraire uniquement le texte surligné du document PDF. Afin de mettre en œuvre cette fonctionnalité, nous avons ajouté les méthodes TextMarkupAnnotation.GetMarkedText() et TextMarkupAnnotation.GetMarkedTextFragments() dans l'API. Vous pouvez extraire le texte surligné d'un document PDF en filtrant TextMarkupAnnotation et en utilisant les méthodes mentionnées. Le code suivant montre comment vous pouvez extraire le texte surligné d'un document PDF.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Parcourir toutes les annotations
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filtrer TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Récupérer les fragments de texte surlignés
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Afficher le texte surligné
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## Accéder aux Éléments de Fragment et de Segment de Texte depuis XML

Parfois, nous avons besoin d'accéder aux éléments TextFragement ou TextSegment lors du traitement des documents PDF générés à partir de XML. Aspose.PDF pour Android via Java permet d'accéder à ces éléments par leur nom. Le code ci-dessous montre comment utiliser cette fonctionnalité.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    // Accéder à l'élément TextSegment par son identifiant
    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    // Afficher le texte du segment
    System.out.println(segment.getText());
}
```