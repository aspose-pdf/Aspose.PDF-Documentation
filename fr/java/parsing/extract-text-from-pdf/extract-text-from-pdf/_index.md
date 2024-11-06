---
title: Extraire le texte brut d'un fichier PDF
linktitle: Extraire le texte d'un PDF
type: docs
weight: 10
url: fr/java/extract-text-from-all-pdf/
description: Cet article décrit diverses façons d'extraire du texte des documents PDF en utilisant Aspose.PDF pour Java. De pages entières, d'une partie spécifique, basées sur des colonnes, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire le texte de toutes les pages d'un document PDF

Extraire du texte d'un document PDF est une exigence courante. Dans cet exemple, vous verrez comment Aspose.PDF pour Java permet d'extraire du texte de toutes les pages d'un document PDF. Pour extraire le texte de toutes les pages PDF :

1. Créez un objet de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Ouvrez le PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et appelez la méthode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) de la collection [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. La classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorbe le texte du document et le renvoie dans la propriété **Text**.

Le code suivant vous montre comment extraire du texte de toutes les pages d'un document PDF.

```java
public static void ExtractFromAllPages(){
    // Le chemin vers le répertoire des documents.
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // Ouvrir le document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Créer un objet TextAbsorber pour extraire le texte
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
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


## Extraire le texte des pages en utilisant Text Device

Vous pouvez utiliser la classe **TextDevice** pour extraire du texte d'un fichier PDF. TextDevice utilise [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) dans son implémentation, donc, en fait, ils font la même chose mais TextDevice est juste implémenté pour unifier l'approche "Device" pour extraire tout de la page ImageDevice, PageDevice, etc. TextAbsorber peut extraire du texte de la page, de l'ensemble du PDF ou de XForm, ce TextAbsorber est plus universel.

### Extraire du texte de toutes les pages

Les étapes suivantes et l'extrait de code vous montrent comment extraire du texte d'un PDF en utilisant le dispositif de texte.

1. Créez un objet de la classe Document avec le fichier PDF d'entrée spécifié
1. Créez un objet de la classe TextDevice
1. Utilisez l'objet de la classe TextExtractOptions pour spécifier les options d'extraction
1. Utilisez la méthode Process de la classe TextDevice pour convertir le contenu en texte
1. Enregistrez le texte dans le fichier de sortie

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // ouvrir le document
    Document pdfDocument = new Document("input.pdf");
    // fichier texte dans lequel le texte extrait sera enregistré
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // itérer à travers toutes les pages du fichier PDF
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // créer un dispositif de texte
        TextDevice textDevice = new TextDevice();
        // définir les options d'extraction de texte - définir le mode d'extraction de texte (Brut ou
        // Pur)
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // obtenir le texte des pages du PDF et l'enregistrer dans l'objet OutputStream
        textDevice.process(page, text_stream);
    }
    // fermer l'objet stream
    text_stream.close();
}
```


## Extraire du texte d'une région particulière de la page

La classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) fournit la capacité d'extraire du texte d'une ou de toutes les pages d'un document PDF. Cette classe renvoie le texte extrait dans la propriété **Text**. Cependant, si nous avons besoin d'extraire du texte d'une région particulière de la page, nous pouvons utiliser la propriété **Rectangle** de [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions). La propriété Rectangle prend un objet Rectangle comme valeur et en utilisant cette propriété, nous pouvons spécifier la région de la page à partir de laquelle nous devons extraire le texte.

La méthode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) d'une page est appelée pour extraire le texte.
 Créez des objets des classes [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). Appelez la méthode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) sur la page individuelle, en tant qu'**Index** de **Page**, de l'objet **Document**. L'**Index** est le numéro de page particulier à partir duquel le texte doit être extrait. Vous pouvez obtenir le texte de la propriété **Text** de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). Le code suivant vous montre comment extraire du texte d'une page individuelle.

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // ouvrir le document
    Document doc = new Document("page_0001.pdf");
    // créer un objet TextAbsorber pour extraire le texte
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // accepter l'absorbeur pour la première page
    doc.getPages().get_Item(1).accept(absorber);
    // obtenir le texte extrait
    String extractedText = absorber.getText();
    // créer un écrivain et ouvrir le fichier
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // écrire le contenu extrait
    writer.write(extractedText);
    // fermer l'écrivain
    writer.close();
}
```

## Extraire le texte en fonction des colonnes

Un fichier PDF peut comprendre des éléments tels que du texte, des images, des annotations, des pièces jointes, des graphiques, etc., et Aspose.PDF pour .NET offre la possibilité d'ajouter ainsi que de manipuler tous ces éléments. Cette API est remarquable lorsqu'il s'agit d'ajouter et d'extraire du texte d'un document PDF et nous pouvons rencontrer un scénario où un document PDF est composé de plusieurs colonnes (document PDF multicolonnes) et nous devons extraire le contenu de la page tout en respectant la même mise en page, alors Aspose.PDF pour .NET est le choix idéal pour accomplir cette exigence. Une approche consiste à réduire la taille de la police du contenu à l'intérieur du document PDF puis à effectuer l'extraction de texte. Le code suivant montre les étapes pour réduire la taille du texte puis essayer d'extraire le texte du document PDF.

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // ouvrir le document
    Document doc = new Document("page_0001.pdf");
    // créer un objet TextAbsorber pour extraire le texte
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // accepter l'absorbeur pour la première page
    doc.getPages().get_Item(1).accept(absorber);
    // obtenir le texte extrait
    String extractedText = absorber.getText();
    // créer un écrivain et ouvrir le fichier
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // écrire le contenu extrait
    writer.write(extractedText);
    // fermer l'écrivain
    writer.close();
}
```


### Deuxième approche - Utilisation de ScaleFactor

Dans cette nouvelle version, nous avons également introduit plusieurs améliorations dans TextAbsorber et dans le mécanisme de formatage de texte interne. Ainsi, lors de l'extraction de texte en mode ‘Pur’, vous pouvez spécifier l'option ScaleFactor et cela peut être une autre approche pour extraire du texte d'un document PDF à plusieurs colonnes en plus de l'approche mentionnée ci-dessus. Ce facteur d'échelle peut être réglé pour ajuster la grille utilisée pour le mécanisme de formatage de texte interne lors de l'extraction de texte. Spécifier les valeurs de ScaleFactor entre 1 et 0.1 (y compris 0.1) a le même effet que la réduction de police.

Spécifier les valeurs de ScaleFactor entre 0.1 et -0.1 est traité comme une valeur zéro, mais cela incite l'algorithme à calculer automatiquement le facteur d'échelle nécessaire lors de l'extraction du texte. Le calcul est basé sur la largeur moyenne des glyphes de la police la plus populaire sur la page, mais nous ne pouvons pas garantir que dans le texte extrait, aucune chaîne de colonne n'atteigne le début de la colonne suivante. Veuillez noter que si la valeur de ScaleFactor n'est pas spécifiée, la valeur par défaut de 1.0 sera utilisée. Cela signifie qu'aucune mise à l'échelle ne sera effectuée. Si la valeur spécifiée de ScaleFactor est supérieure à 10 ou inférieure à -0.1, la valeur par défaut de 1.0 sera utilisée.

Nous proposons l'utilisation de l'auto-scalage (ScaleFactor = 0) lors du traitement d'un grand nombre de fichiers PDF pour l'extraction de contenu textuel. Ou définissez manuellement la réduction redondante de la largeur de la grille (environ ScaleFactor = 0.5). Cependant, vous ne devez pas déterminer si le scalage est nécessaire ou non pour des documents concrets. Si vous définissez une réduction redondante de la largeur de la grille pour le document (qui n'en a pas besoin), le contenu textuel extrait restera entièrement adéquat. Veuillez jeter un œil à l'extrait de code suivant.

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // Définir le facteur d'échelle à 0.5 est suffisant pour diviser les colonnes dans la majorité des documents
    // La définition de zéro permet à l'algorithme de choisir automatiquement le facteur d'échelle
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

Veuillez noter qu'il n'existe pas de correspondance directe entre le nouveau ScaleFactor et l'ancien coefficient de réduction manuelle de la police. Cependant, par défaut, l'algorithme prend en compte la valeur de la taille de la police qui a déjà été réduite pour certaines raisons internes. Par exemple, réduire la taille de la police de 10 à 7 a le même effet que de définir un facteur d'échelle à 5/8 (= 0,625).

{{% /alert %}}

## Extraire le Texte Surligné d'un Document PDF

Dans divers scénarios d'extraction de texte d'un document PDF, vous pouvez avoir besoin d'extraire uniquement le texte surligné d'un document PDF. Pour implémenter cette fonctionnalité, nous avons ajouté les méthodes TextMarkupAnnotation.GetMarkedText() et TextMarkupAnnotation.GetMarkedTextFragments() dans l'API. Vous pouvez extraire le texte surligné d'un document PDF en filtrant TextMarkupAnnotation et en utilisant les méthodes mentionnées. Le code suivant montre comment vous pouvez extraire le texte surligné d'un document PDF.

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // Boucle à travers toutes les annotations
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // Filtrer TextMarkupAnnotation
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // Récupérer les fragments de texte surlignés
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // Afficher le texte surligné
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## Accéder aux éléments Text Fragment et Segment d'un XML

Parfois, nous avons besoin d'accéder aux éléments TextFragment ou TextSegment lors du traitement de documents PDF générés à partir de XML. Aspose.PDF pour .NET permet d'accéder à ces éléments par leur nom. Le code ci-dessous montre comment utiliser cette fonctionnalité.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```