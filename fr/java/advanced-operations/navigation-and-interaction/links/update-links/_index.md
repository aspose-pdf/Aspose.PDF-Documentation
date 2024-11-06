---
title: Mettre à jour les liens dans un PDF 
linktitle: Mettre à jour les liens
type: docs
weight: 20
url: fr/java/update-links/
description: Mettre à jour les liens dans un PDF par programmation. Ce guide explique comment mettre à jour les liens dans un PDF en langage Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mettre à jour les liens dans un fichier PDF

Comme discuté dans Ajouter un lien hypertexte dans un fichier PDF, la classe [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) permet d'ajouter des liens dans un fichier PDF. Il existe également une classe similaire utilisée pour obtenir des liens existants à partir de fichiers PDF. Utilisez cela si vous devez mettre à jour un lien existant. Pour mettre à jour un lien existant :

1. Chargez un fichier PDF.
1. Allez à une page spécifique dans le fichier PDF.
1. Spécifiez la destination du lien en utilisant la propriété Destination de l'objet [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction).

1. La page de destination est spécifiée en utilisant le constructeur [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination).

### Définir la cible du lien vers une page dans le même document

Le code suivant vous montre comment mettre à jour un lien dans un fichier PDF et définir sa cible sur la deuxième page du document.

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // Obtenez la première annotation de lien de la première page du document
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Lien de modification : changer la destination du lien
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // Spécifiez la destination pour l'objet lien
        // Représente une destination explicite qui affiche la page avec les coordonnées (gauche, haut) positionnées dans le coin supérieur gauche de
        // la fenêtre et le contenu de la page agrandi par le facteur de zoom.
        // Le 1er paramètre est le numéro de la page de destination.
        // Le 2ème est la coordonnée gauche
        // Le 3ème est la coordonnée haute
        // Le 4ème argument est le facteur de zoom lors de l'affichage de la page respective. Utiliser 2 signifie que la page sera affichée avec un zoom de 200%
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // Enregistrer le document avec le lien mis à jour
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Définir la Destination du Lien vers une Adresse Web

Pour mettre à jour l'hyperlien afin qu'il pointe vers une adresse web, instanciez l'objet [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) et passez-le à la propriété Action de LinkAnnotation. Le code suivant montre comment mettre à jour un lien dans un fichier PDF et définir sa cible sur une adresse web.

```java
    public static void SetLinkDestinationToWebAddress() {        
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // Obtenez la première annotation de lien de la première page du document
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modification du lien : changer l'action du lien et définir la cible comme adresse web
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // Enregistrer le document avec le lien mis à jour
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Définir la Cible du Lien vers un Autre Fichier PDF

Le code suivant montre comment mettre à jour un lien dans un fichier PDF et définir sa cible vers un autre fichier PDF.

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // La ligne suivante met à jour la destination, ne met pas à jour le fichier
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // La ligne suivante met à jour le fichier
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // Enregistrer le document avec le lien mis à jour
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### Mettre à Jour la Couleur du Texte de LinkAnnotation

L'annotation de lien ne contient pas de texte.
 Au lieu de cela, le texte est placé dans le contenu de la page sous l'annotation. Par conséquent, pour changer la couleur du texte, remplacez la couleur du texte de la page au lieu d'essayer de changer la couleur de l'annotation. Le code suivant montre comment mettre à jour la couleur de l'annotation de lien dans un fichier PDF.

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // Rechercher le texte sous l'annotation
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // Changer la couleur du texte.
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // Enregistrer le document avec le lien mis à jour
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```