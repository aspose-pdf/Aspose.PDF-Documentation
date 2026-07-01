---
title: Extraction du texte brut d'un fichier PDF
linktitle: Extraire le texte d'un PDF
type: docs
weight: 10
url: /fr/androidjava/extract-text-from-all-pdf/
description: Cet article décrit diverses méthodes pour extraire du texte de documents PDF en utilisant Aspose.PDF pour Android via Java. À partir de pages entières, d'une partie spécifique, selon les colonnes, etc.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire le texte de toutes les pages d'un document PDF

L'extraction de texte d'un document PDF est une exigence courante. Dans cet exemple, vous verrez comment Aspose.PDF pour Java permet d'extraire le texte de toutes les pages d'un document PDF.
Pour extraire le texte de toutes les pages PDF :

1. Créer un objet de [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) classe.
1. Ouvrez le PDF en utilisant [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) classe et appelez le [Accepter](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) méthode de la [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) collection.
1. Le [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) La classe absorbe le texte du document et le renvoie dans **Text** propriété.

L'extrait de code suivant vous montre comment extraire le texte de toutes les pages d'un document PDF.

```java
public static void ExtractFromAllPages() {
        // The path to the documents directory.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Open document
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Create TextAbsorber object to extract text
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Accept the absorber for all the pages
        pdfDocument.getPages().accept(textAbsorber);

        // Get the extracted text
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Write a line of text to the file
            writer.write(extractedText);
            // Close the stream
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```

## Extraire le texte surligné d'un document PDF

Dans divers scénarios d'extraction de texte à partir d'un document PDF, vous pouvez être confronté à la nécessité d'extraire uniquement le texte surligné du document PDF. Afin de mettre en œuvre cette fonctionnalité, nous avons ajouté les méthodes TextMarkupAnnotation.GetMarkedText() et TextMarkupAnnotation.GetMarkedTextFragments() à l'API. Vous pouvez extraire le texte surligné du document PDF en filtrant TextMarkupAnnotation et en utilisant les méthodes mentionnées. Le fragment de code suivant montre comment extraire le texte surligné d'un document PDF.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Loop through all the annotations
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filter TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Retrieve highlighted text fragments
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Display highlighted text
                    System.out.println(tf.getText());
                }
            }
        }
    }
```

## Accéder aux éléments de Text Fragment et de Segment depuis XML

Parfois, nous devons accéder aux éléments TextFragement ou TextSegment lors du traitement de documents PDF générés à partir de XML. Aspose.PDF for Android via Java fournit un accès à ces éléments par nom. Le fragment de code ci‑dessous montre comment utiliser cette fonctionnalité.

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = "40014.xml";
        Document doc = new Document();
        doc.bindXml(_dataDir + inXml);

        TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```

