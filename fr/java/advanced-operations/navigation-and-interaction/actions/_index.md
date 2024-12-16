---
title: Travailler avec les Actions
linktitle: Actions
type: docs
weight: 20
url: /fr/java/actions/
description: Cette section explique comment ajouter des actions aux documents et aux champs de formulaire par programmation avec Java. Apprenez à Ajouter, Créer et Obtenir un Hyperlien dans un Fichier PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Un fichier PDF peut contenir des pièces jointes intégrées et il est souvent nécessaire de créer un hyperlien vers ces documents. Vous pouvez diriger les lecteurs du document PDF principal vers une pièce jointe PDF en créant un lien dans le document parent qui pointe vers la pièce jointe.

## Ajouter un Hyperlien dans un Fichier PDF

Il est possible d'ajouter des hyperliens aux fichiers PDF, soit pour permettre aux lecteurs de naviguer vers une autre partie du PDF, soit vers un contenu externe.

Pour ajouter des hyperliens web aux documents PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Obtenez la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à laquelle vous souhaitez ajouter le lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle). L'objet rectangle est utilisé pour spécifier l'emplacement sur la page où le lien doit être ajouté.
1. Définissez la méthode getAction sur l'objet [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction) qui spécifie l'emplacement de l'URI distant.
1. Pour afficher un texte hyperlien, ajoutez une chaîne de texte à un emplacement similaire à celui où l'objet [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) est placé.
1. Pour ajouter un texte libre :

- Instanciez un objet [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation).
 Il accepte également les objets Page et Rectangle comme arguments, il est donc possible de fournir les mêmes valeurs que celles spécifiées pour le constructeur LinkAnnotation.
- En utilisant la propriété Contents de l'objet [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation), spécifiez la chaîne qui doit être affichée dans le PDF de sortie.
- Facultativement, définissez la largeur de bordure des objets [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) et FreeTextAnnotation à 0 afin qu'ils n'apparaissent pas dans le document PDF.
- Une fois que les objets [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) et [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) ont été définis, ajoutez ces liens à la collection Annotations de l'objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

- Enfin, enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
The following code snippet shows you how to add a hyperlink to a PDF file.

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // Ouvrir le document
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // Créer un lien
        Page page = document.getPages().get_Item(1);
        // Créer un objet annotation de lien
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // Créer un objet bordure pour LinkAnnotation
        Border border = new Border(link);
        // Définir la valeur de la largeur de la bordure à 0
        border.setWidth(0);
        // Définir la bordure pour LinkAnnotation
        link.setBorder(border);
        // Spécifier le type de lien comme URI distant
        link.setAction(new GoToURIAction("www.aspose.com"));
        // Ajouter l'annotation de lien à la collection d'annotations de la première page du fichier PDF
        page.getAnnotations().add(link);

        // Créer une annotation de texte libre
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // Chaîne à ajouter comme texte libre
        textAnnotation.setContents("Lien vers le site Aspose");
        // Définir la bordure pour l'annotation de texte libre
        textAnnotation.setBorder(border);
        // Ajouter l'annotation de texte libre à la collection d'annotations de la première page du document
        page.getAnnotations().add(textAnnotation);

        // Enregistrer le document mis à jour
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## Créer un lien hypertexte vers des pages dans le même PDF

Aspose.PDF pour Java offre une excellente fonctionnalité pour la création de PDF ainsi que sa manipulation. Il offre également la possibilité d'ajouter des liens vers des pages PDF et un lien peut diriger soit vers des pages dans un autre fichier PDF, une URL web, un lien pour lancer une application ou même un lien vers des pages dans le même fichier PDF.

Pour ajouter le lien hypertexte local, nous devons créer un TextFragment afin que le lien puisse être associé au TextFragment. La classe [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) possède une méthode nommée [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--) qui est utilisée pour associer une instance LocalHyperlink. Le code suivant montre les étapes pour accomplir cette tâche.

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // Créer une instance de Document
        Document document = new Document();

        // Ajouter une page à la collection de pages du fichier PDF
        Page page = document.getPages().add();

        // Créer une instance de Text Fragment
        TextFragment text = new TextFragment("tester le numéro de page du lien vers la page 2");

        // Créer une instance de lien hypertexte local
        LocalHyperlink link = new LocalHyperlink();

        // Définir la page cible pour l'instance de lien
        link.setTargetPageNumber(2);

        // Définir le lien hypertexte du TextFragment
        text.setHyperlink(link);

        // Ajouter du texte à la collection de paragraphes de la page
        page.getParagraphs().add(text);

        // Créer une nouvelle instance de TextFragment
        text = new TextFragment("tester le numéro de page du lien vers la page 1");

        // TextFragment doit être ajouté sur une nouvelle page
        text.setInNewPage(true);

        // Créer une autre instance de lien hypertexte local
        link = new LocalHyperlink();

        // Définir la page cible pour le second lien hypertexte
        link.setTargetPageNumber(1);

        // Définir le lien pour le second TextFragment
        text.setHyperlink(link);

        // Ajouter du texte à la collection de paragraphes de l'objet page
        page.getParagraphs().add(text);

        // Enregistrer le document mis à jour
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## Obtenir la Destination du Lien Hypertexte PDF (URL)

Les liens sont représentés comme des annotations dans un fichier PDF et ils peuvent être ajoutés, mis à jour ou supprimés. Aspose.PDF pour Java prend également en charge l'obtention de la destination (URL) du lien hypertexte dans un fichier PDF.

Pour obtenir l'URL d'un lien :

1. Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Obtenez la [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à partir de laquelle vous souhaitez extraire des liens.
1. Utilisez la classe [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) pour extraire tous les objets [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) de la page spécifiée.
1. Passez l'objet [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) à la méthode Accept de l'objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

1. Obtenez toutes les annotations de lien sélectionnées dans un objet IList en utilisant la propriété Selected de l'objet [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector).
1. Enfin, extrayez l'action LinkAnnotation en tant que GoToURIAction.

Le code suivant montre comment obtenir des destinations de lien hypertexte (URL) à partir d'un fichier PDF.

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Extraire les actions
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // Itérer à travers chaque élément individuel dans la liste
        if (list.size() == 0)
            System.out.println("Aucun hyperlien trouvé..");
        else {
            // Boucler à travers tous les signets
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // Imprimer l'URL de destination
                    System.out.println("Destination: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // fin sinon
    }
```


## Obtenir le Texte du Lien Hypertexte

Un lien hypertexte a deux parties : le texte qui s'affiche dans le document et l'URL de destination. Dans certains cas, c'est le texte plutôt que l'URL dont nous avons besoin.

Le texte et les annotations/actions dans un fichier PDF sont représentés par différentes entités. Le texte sur une page est juste un ensemble de mots et de caractères, tandis que les annotations apportent une certaine interactivité telle que celle inhérente à un lien hypertexte.

Pour trouver le contenu de l'URL, vous devez travailler à la fois avec l'annotation et le texte. L'objet [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) n'a pas lui-même le texte mais se trouve sous le texte sur la page. Donc, pour obtenir le texte, l'Annotation donne les limites de l'URL, tandis que l'objet Texte donne le contenu de l'URL. Veuillez voir l'extrait de code suivant.

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Extraire les actions
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // Imprimer l'URL de chaque Annotation de Lien
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // Imprimer le texte associé au lien hypertexte
                System.out.println(extractedText);
            }
        }
    }
```


## Supprimer l'Action d'Ouverture de Document d'un Fichier PDF

[Comment Spécifier la Page PDF lors de la Visualisation du Document](#how-to-specify-pdf-page-when-viewing-document) explique comment indiquer à un document de s'ouvrir sur une page différente de la première. Lors de la concaténation de plusieurs documents, et si un ou plusieurs d'entre eux ont une action GoTo définie, vous voudrez probablement les supprimer. Par exemple, si vous combinez deux documents et que le deuxième a une action GoTo qui vous amène à la deuxième page, le document de sortie s'ouvrira sur la deuxième page du deuxième document au lieu de la première page du document combiné. Pour éviter ce comportement, supprimez la commande d'action d'ouverture.

Pour supprimer une action d'ouverture :

1. Définissez la méthode [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) sur null.
2. Enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet Document.

Le snippet de code suivant montre comment supprimer une action d'ouverture de document du fichier PDF.

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // Ouvrir le document
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // Supprimer l'action d'ouverture du document
        document.setOpenAction(null);
        
        // Enregistrer le document mis à jour
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## Comment Spécifier la Page PDF lors de l'Affichage du Document {#how-to-specify-pdf-page-when-viewing-document}

Lors de l'affichage de fichiers PDF dans un visualiseur PDF tel qu'Adobe Reader, les fichiers s'ouvrent généralement sur la première page. Cependant, il est possible de configurer le fichier pour qu'il s'ouvre sur une page différente.

La classe [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) vous permet de spécifier une page dans un fichier PDF que vous souhaitez ouvrir. Lors du passage de la valeur de l'objet GoToAction à la méthode getOpenAction de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), le document s'ouvre à la page spécifiée contre l'objet XYZExplicitDestination. Le fragment de code suivant montre comment spécifier une page comme action d'ouverture du document.

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // Charger le fichier PDF
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // Obtenir l'instance de la deuxième page du document
        Page page2 = document.getPages().get_Item(2);
        // Créer la variable pour définir le facteur de zoom de la page cible
        double zoom = 1;
        // Créer une instance GoToAction
        GoToAction action = new GoToAction(page2);
        // Aller à la page 2
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // Définir l'action d'ouverture du document
        document.setOpenAction (action);
        // Sauvegarder le document mis à jour
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```