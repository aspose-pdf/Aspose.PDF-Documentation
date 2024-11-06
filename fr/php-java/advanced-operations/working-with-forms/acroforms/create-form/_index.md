---
title: Créer des AcroForms - Créer un PDF remplissable en PHP
linktitle: Créer des AcroForms
type: docs
weight: 10
url: fr/php-java/create-forms/
description: Cette section explique comment créer des AcroForms à partir de zéro dans vos documents PDF avec Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un champ de formulaire dans un document PDF

La classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) fournit une collection nommée Form qui aide à gérer les champs de formulaire dans un document PDF.

Pour ajouter un champ de formulaire :

1. Créez le champ de formulaire que vous souhaitez ajouter.
2. Appelez la méthode add de la collection [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Cet exemple montre comment ajouter un TextBoxField. Vous pouvez ajouter n'importe quel champ de formulaire en utilisant la même approche :

1. Tout d'abord, créez un objet champ et définissez ses propriétés.
2. Ensuite, ajoutez le champ à la collection Form.

### Ajouter un TextBoxField

Un champ de texte est un élément de formulaire qui permet à un destinataire de saisir du texte dans votre formulaire.
 Cela serait utilisé chaque fois que vous souhaitez permettre à l'utilisateur la liberté de taper ce qu'il veut.

Les extraits de code suivants montrent comment ajouter un TextBoxField à un document PDF.

```php

    // Ouvrir le document
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // Créer un champ
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("Une valeur dans la zone de texte");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // Ajouter le champ au document
    $document->getForm()->add($textBoxField, 1);

    // Enregistrer le PDF modifié
    $document->save($outputFile);
    $document->close();
```

## Ajout de RadioButtonField

Un bouton radio est le plus couramment utilisé pour les questions à choix multiples, dans le scénario où une seule réponse peut être sélectionnée.
Les extraits de code suivants montrent comment ajouter [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) dans un document PDF.

```php

    // Ouvrir le document            
    $document = new Document($inputFile);

    // ajouter une page au fichier PDF
    $page = $document->getPages()->get_Item(1);

    // instancier un objet RadioButtonField avec le numéro de page comme argument
    $radio = new RadioButtonField($page);

    // ajouter la première option de bouton radio et spécifier également son origine 
    // en utilisant l'objet Rectangle

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // ajouter la deuxième option de bouton radio
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // ajouter le bouton radio à l'objet formulaire de l'objet Document
    $document->getForm()->add($radio);

    // enregistrer le fichier PDF
    $document->save($outputFile);
    $document->close();
```

L'extrait de code suivant montre les étapes pour ajouter [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) avec trois options et les placer à l'intérieur des cellules du tableau.

```php

    $colors = new Color();
    $document = new Document();
    $page = $document->getPages()->add();

    $table = new Table();
    $table->setColumnWidths("120 120 120");
    $page->getParagraphs()->add($table);
    $r1 = $table->getRows()->add();
    $c1 = $r1->getCells()->add();
    $c2 = $r1->getCells()->add();
    $c3 = $r1->getCells()->add();

    $rf = new RadioButtonField($page);
    $rf->setPartialName("radio1");
    $document->getForm()->add($rf, 1);

    $opt1 = new RadioButtonOptionField();
    $opt2 = new RadioButtonOptionField();
    $opt3 = new RadioButtonOptionField();

    $opt1->setOptionName("Item1");
    $opt2->setOptionName("Item2");
    $opt3->setOptionName("Item3");

    $opt1->setWidth(15.0);
    $opt1->setHeight(15.0);
    $opt2->setWidth(15.0);
    $opt2->setHeight(15.0);
    $opt3->setWidth(15.0);
    $opt3->setHeight(15.0);

    $rf->add($opt1);
    $rf->add($opt2);
    $rf->add($opt3);

    $border1 = new Border($opt1);
    $opt1->setBorder($border1);
    $opt1->getBorder()->setWidth(1.0);
    $opt1->getBorder()->setStyle(BorderStyle::$Solid);
    $opt1->getCharacteristics()->setBorder($colors->getBlack());
    $opt1->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt1->setCaption(new TextFragment("Élément1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("Élément2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("Élément3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## Ajouter un champ ComboBox

Une Combo Box est un champ de formulaire qui ajoutera un menu déroulant à votre document.

Les extraits de code suivants montrent comment ajouter un champ [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) dans un document PDF.

```php

        $document = new Document($inputFile);

        // instancier l'objet Champ ComboBox
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // ajouter une option à la ComboBox
        $combo->addOption("Rouge");
        $combo->addOption("Jaune");
        $combo->addOption("Vert");
        $combo->addOption("Bleu");

        // ajouter l'objet combo box à la collection de champs de formulaire de l'objet document
        $document->getForm()->add($combo);

        // enregistrer le document PDF
        $document->save($outputFile);
        $document->close();
```

## Ajouter une info-bulle au formulaire

La classe Document fournit une collection nommée Form qui gère les champs de formulaire dans un document PDF.
 Pour ajouter une info-bulle à un champ de formulaire, utilisez la classe Field AlternateName. Adobe Acrobat utilise le « nom alternatif » comme info-bulle de champ.

Les extraits de code suivants montrent comment ajouter une info-bulle à un champ de formulaire avec PHP.

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // Définir l'info-bulle pour le champ texte
    $textBoxField->setAlternateName("Info-bulle de la zone de texte");

    // enregistrer le document PDF
    $document->save($outputFile);
    $document->close();
```