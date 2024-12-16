---
title: Créer AcroForms - Créer un PDF remplissable en Java
linktitle: Créer AcroForms
type: docs
weight: 10
url: /fr/java/create-forms/
description: Cette section explique comment créer des AcroForms à partir de zéro dans vos documents PDF avec Aspose.PDF pour Java.
lastmod: "2021-06-05"
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

### Ajout de TextBoxField

Un champ de texte est un élément de formulaire qui permet à un destinataire de saisir du texte dans votre formulaire.
 Cela serait utilisé chaque fois que vous souhaitez permettre à l'utilisateur la liberté de taper ce qu'il veut.

Les extraits de code suivants montrent comment ajouter un TextBoxField à un document PDF.

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Créer un champ
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Ajouter le champ au document
        pdfDocument.getForm().add(textBoxField, 1);

        // Enregistrer le PDF modifié
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## Ajout de RadioButtonField

Un bouton radio est le plus souvent utilisé pour les questions à choix multiple, dans le scénario où une seule réponse peut être sélectionnée.

Les extraits de code suivants montrent comment ajouter [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) dans un document PDF.

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // ajouter une page au fichier PDF
        pdfDocument.getPages().add();

        // instancier l'objet RadioButtonField avec le numéro de page comme argument
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // ajouter la première option du bouton radio et spécifier également son origine à l'aide d'un objet Rectangle
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // ajouter la deuxième option du bouton radio
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // ajouter le bouton radio à l'objet formulaire de l'objet Document
        pdfDocument.getForm().add(radio);
        // enregistrer le fichier PDF
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


Le fragment de code suivant montre les étapes pour ajouter [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) avec trois options et les placer à l'intérieur des cellules du tableau.

```java
public static void AddingRadioButtonAdvanced() {
        Document doc = new Document();
        Page page = doc.getPages().add();
        Table table = new Table();
        table.setColumnWidths("120 120 120");
        page.getParagraphs().add(table);
        Row r1 = table.getRows().add();
        Cell c1 = r1.getCells().add();
        Cell c2 = r1.getCells().add();
        Cell c3 = r1.getCells().add();

        RadioButtonField rf = new RadioButtonField(page);
        rf.setPartialName("radio");
        doc.getForm().add(rf, 1);

        RadioButtonOptionField opt1 = new RadioButtonOptionField();
        RadioButtonOptionField opt2 = new RadioButtonOptionField();
        RadioButtonOptionField opt3 = new RadioButtonOptionField();

        opt1.setOptionName("Item1");
        opt2.setOptionName("Item2");
        opt3.setOptionName("Item3");

        opt1.setWidth(15);
        opt1.setHeight(15);
        opt2.setWidth(15);
        opt2.setHeight(15);
        opt3.setWidth(15);
        opt3.setHeight(15);

        rf.add(opt1);
        rf.add(opt2);
        rf.add(opt3);

        opt1.setBorder(new Border(opt1));
        opt1.getBorder().setWidth(1);
        opt1.getBorder().setStyle(BorderStyle.Solid);
        opt1.getCharacteristics().setBorder(Color.getBlack());
        opt1.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt1.setCaption(new TextFragment("Item1"));
        opt2.setBorder(new Border(opt2));
        opt2.getBorder().setWidth(1);
        opt2.getBorder().setStyle(BorderStyle.Solid);
        opt2.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt2.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt2.setCaption(new TextFragment("Item2"));
        opt3.setBorder(new Border(opt3));
        opt3.getBorder().setWidth(1);
        opt3.getBorder().setStyle(BorderStyle.Solid);
        opt3.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt3.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt3.setCaption(new TextFragment("Item3"));
        c1.getParagraphs().add(opt1);
        c2.getParagraphs().add(opt2);
        c3.getParagraphs().add(opt3);

        doc.save("RadioButtonField.pdf");
    }
```


## Ajout de légende à RadioButtonField

Le code suivant montre comment ajouter une légende qui sera associée à [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) :

```java
public static void AddingCaptionToRadioButtonField() {
        // Charger le formulaire PDF source
        com.aspose.pdf.facades.Form form1 = new com.aspose.pdf.facades.Form(_dataDir + "RadioButtonField.pdf");
        Document document = new Document(_dataDir + "RadioButtonField.pdf");
        for (String item : form1.getFieldNames()) {
            System.out.println(item.toString());
            if (item.contains("radio1")) {
                RadioButtonField field0 = (RadioButtonField) document.getForm().get(item);
                RadioButtonOptionField fieldoption = new RadioButtonOptionField();
                fieldoption.setOptionName("Yes");
                fieldoption.setPartialName("Yesname");

                var updatedFragment = new TextFragment("test123");
                updatedFragment.getTextState().setFont(FontRepository.findFont("Arial"));
                updatedFragment.getTextState().setFontSize(10);
                updatedFragment.getTextState().setLineSpacing(6.32f);

                // Créer un objet TextParagraph
                TextParagraph par = new TextParagraph();

                // Définir la position du paragraphe
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // Spécifier le mode de retour à la ligne
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // Ajouter un nouveau TextFragment au paragraphe
                par.appendLine(updatedFragment);

                // Ajouter le TextParagraph en utilisant TextBuilder
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## Ajout d'un champ ComboBox

Une Combo Box est un champ de formulaire qui ajoutera un menu déroulant à votre document.

Les extraits de code suivants montrent comment ajouter un champ [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) dans un document PDF.

```java
public static void AddingComboboxField() {
        // créer un objet Document
        Document doc = new Document();
        // ajouter une page à l'objet document
        doc.getPages().add();
        // instancier un objet ComboBox Field
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // ajouter une option à la ComboBox
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // ajouter l'objet combo box à la collection de champs de formulaire de l'objet document
        doc.getForm().add(combo);
        // enregistrer le document PDF
        doc.save("ComboBox_Added.pdf");
    }
```

## Ajouter une info-bulle au formulaire

La classe Document fournit une collection nommée Form qui gère les champs de formulaire dans un document PDF.
 Pour ajouter une info-bulle à un champ de formulaire, utilisez la classe Field AlternateName. Adobe Acrobat utilise le « nom alternatif » comme info-bulle de champ.

Les extraits de code suivants montrent comment ajouter une info-bulle à un champ de formulaire avec Java.

```java
public static void AddTooltipToFormField() {
        // Charger le formulaire PDF source
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // Obtenir un champ
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // Définir l'info-bulle pour le champ de texte
        textBoxField.setAlternateName("Info-bulle de la boîte de texte");

        // Enregistrer le document modifié
        doc.save("output.pdf");
    }
```