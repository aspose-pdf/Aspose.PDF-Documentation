---
title: Utilisation de l'info-bulle 
linktitle: Info-bulle PDF
type: docs
weight: 20
url: /java/pdf-tooltip/
description: Apprenez à ajouter une info-bulle au fragment de texte dans un PDF en utilisant Java et Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter une info-bulle au texte recherché en ajoutant un bouton invisible

Il est souvent nécessaire d'ajouter des détails pour une phrase ou un mot spécifique sous forme d'info-bulle dans le document PDF afin qu'elle puisse apparaître lorsque l'utilisateur survole le texte avec le curseur de la souris. Aspose.PDF pour Java offre cette fonctionnalité pour créer des info-bulles en ajoutant un bouton invisible sur le texte recherché. Le code suivant vous montrera comment réaliser cette fonctionnalité :

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // Créer un document d'exemple avec du texte
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Déplacez le curseur ici pour afficher une info-bulle"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("Déplacez le curseur ici pour afficher une info-bulle très longue"));
        doc.save(outputFile);

        // Ouvrir le document avec du texte
        Document document = new Document(outputFile);
        // Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Déplacez le curseur ici pour afficher une info-bulle");
        // Accepter l'absorbeur pour les pages du document
        document.getPages().accept(absorber);
        // Obtenir les fragments de texte extraits
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // Boucle à travers les fragments
        for(TextFragment fragment : textFragments)
        {
            // Créer un bouton invisible sur la position du fragment de texte
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // La valeur AlternateName sera affichée comme info-bulle par une application de visualisation
            field.setAlternateName ("Info-bulle pour le texte.");
            // Ajouter le champ de bouton au document
            document.getForm().add(field);
        }

        // Ensuite, un exemple d'info-bulle très longue
        absorber = new TextFragmentAbsorber("Déplacez le curseur ici pour afficher une info-bulle très longue");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Définir un texte très long
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // Enregistrer le document
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

Concernant la longueur de l'infobulle, le texte de l'infobulle est contenu dans le document PDF en tant que type de chaîne PDF, en dehors du flux de contenu. Il n'y a pas de restriction effective sur de telles chaînes dans les fichiers PDF (voir PDF Reference Appendix C.). Cependant, un lecteur conforme (par exemple, Adobe Acrobat) fonctionnant sur un processeur particulier et dans un environnement d'exploitation particulier a une telle limite. Veuillez vous référer à la documentation de votre application de lecteur PDF.

{{% /alert %}}

## Créer un bloc de texte caché et l'afficher au survol de la souris

Dans Aspose.PDF, une fonctionnalité pour masquer les actions est implémentée permettant d'afficher/masquer un champ de boîte de texte (ou tout autre type d'annotation) lors de l'entrée/sortie de la souris sur un bouton invisible. À cette fin, la classe Aspose.Pdf.Annotations.HideAction est utilisée pour assigner l'action de masquage/affichage au bloc de texte. Veuillez utiliser l'extrait de code suivant pour afficher/masquer un bloc de texte à l'entrée/sortie de la souris.

Veuillez également prendre en compte que les actions PDF dans les documents fonctionnent bien dans les lecteurs conformes (par exemple.
 Adobe Reader) mais aucune garantie pour d'autres lecteurs PDF (par exemple, les plugins de navigateur Web). Nous avons mené une brève enquête et avons trouvé :

- Toutes les implémentations de l'action de masquage dans les documents PDF fonctionnent correctement dans Internet Explorer v.11.0.
- Toutes les implémentations de l'action de masquage fonctionnent également dans Opera v.12.14, mais nous avons remarqué un certain délai de réponse lors de la première ouverture du document.
- Seule l'implémentation utilisant le constructeur HideAction acceptant le nom du champ fonctionne si Google Chrome v.61.0 parcourt le document ; Veuillez utiliser les constructeurs correspondants si la navigation dans Google Chrome est significative :

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // Créer un document d'exemple avec du texte
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Déplacez le curseur de la souris ici pour afficher le texte flottant"));
        doc.save(outputFile);

        // Ouvrir le document avec du texte
        Document document = new Document(outputFile);
        // Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Déplacez le curseur de la souris ici pour afficher le texte flottant");
        // Accepter l'absorbeur pour les pages du document
        document.getPages().accept(absorber);
        // Obtenir le premier fragment de texte extrait
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // Créer un champ de texte caché pour le texte flottant dans le rectangle spécifié de la page
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // Définir le texte à afficher comme valeur du champ
        floatingField.setValue ("Ceci est le \"champ de texte flottant\".");
        // Nous recommandons de rendre le champ 'readonly' pour ce scénario
        floatingField.setReadOnly(true);

        // Définir le drapeau 'hidden' pour rendre le champ invisible à l'ouverture du document
        floatingField.setFlags( floatingField.getFlags() | AnnotationFlags.Hidden);

        // Définir un nom de champ unique n'est pas nécessaire mais autorisé
        floatingField.setPartialName ("FloatingField_1");

        // Définir les caractéristiques de l'apparence du champ n'est pas nécessaire mais améliore
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());;
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // Ajouter le champ de texte au document
        document.getForm().add(floatingField);

        // Créer un bouton invisible sur la position du fragment de texte
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // Créer une nouvelle action de masquage pour le champ spécifié (annotation) et le drapeau d'invisibilité.
        // (Vous pouvez également référencer le champ flottant par le nom si vous l'avez spécifié ci-dessus.)
        // Ajouter des actions sur l'entrée/sortie de la souris au champ de bouton invisible
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit (new HideAction(floatingField));

        // Ajouter le champ de bouton au document
        document.getForm().add(buttonField);

        // Sauvegarder le document
        document.save(outputFile);
    }
```