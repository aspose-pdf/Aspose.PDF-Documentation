---
title: Créer AcroForm - Créer un PDF remplissable en Java
linktitle: Créer un AcroForm
type: docs
weight: 10
url: /java/create-form/
description: Créez des champs AcroForm à partir de zéro dans des documents PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créez des champs AcroForm interactifs dans des fichiers PDF avec Java
Abstract: Cet article explique comment créer des champs AcroForm à l'aide d'Aspose.PDF pour Java. Il couvre les zones de texte, les champs de texte multi-widgets, les boutons radio, les zones de liste déroulante, les cases à cocher, les zones de liste, les champs de signature et les champs de codes-barres pour les formulaires PDF interactifs.
---
Aspose.PDF pour Java vous permet de créer une large gamme de types de champs AcroForm à partir de zéro.


## 
Créer un champ de zone de texte



Utilisez cet exemple lorsque vous devez ajouter un champ de saisie de texte sur une seule ligne à un nouveau formulaire PDF.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [TextBoxField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) avec un rectangle cible et configurez son apparence.
1. Ajoutez le champ au formulaire et enregistrez le document.


```java
public static void addTextBoxField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rectangle = new Rectangle(10, 600, 110, 620, true);
        TextBoxField textBoxField = new TextBoxField(page, rectangle);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");
        textBoxField.setDefaultAppearance(new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()));

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField, 1);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un champ de zone de texte avec plusieurs widgets



Utilisez cet exemple lorsque la même valeur de champ de texte doit apparaître à plusieurs positions sur la page.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Définissez plusieurs rectangles et apparences pour les widgets de champ.
1. Créez le [TextBoxField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/), configurez chaque widget et enregistrez le document.


```java
public static void addTextBoxFieldNt(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle[] rects = {
                new Rectangle(10, 600, 110, 620, true),
                new Rectangle(10, 630, 110, 650, true),
                new Rectangle(10, 660, 110, 680, true)
        };

        DefaultAppearance[] defaultAppearances = {
                new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()),
                new DefaultAppearance("Helvetica", 12, Color.getDarkGreen().toRgb()),
                new DefaultAppearance(FontRepository.findFont("Calibri"), 14, Color.getDarkMagenta().toRgb())
        };

        TextBoxField textBoxField = new TextBoxField(page, rects);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Some text");

        int index = 0;
        for (WidgetAnnotation widget : textBoxField) {
            widget.setDefaultAppearance(defaultAppearances[index]);
            index++;
        }

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un champ de bouton radio



Utilisez cet exemple lorsque le formulaire doit permettre à l'utilisateur de choisir une option parmi un ensemble prédéfini.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [RadioButtonField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) et ajoutez les options requises.
1. Ajoutez le champ au formulaire et enregistrez le PDF.


```java
public static void addRadioButton(Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();

        RadioButtonField radio = new RadioButtonField(document.getPages().get_Item(1));
        radio.addOption("Option 1", new Rectangle(100, 640, 120, 680, true));
        radio.addOption("Option 2", new Rectangle(140, 640, 160, 680, true));

        document.getForm().add(radio);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un champ de zone de liste déroulante



Utilisez cet exemple lorsque l'utilisateur doit choisir une valeur dans une liste déroulante.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [ComboBoxField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) et ajoutez ses options sélectionnables.
1. Définissez la sélection par défaut et enregistrez le document.


```java
public static void addComboBox(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ComboBoxField combo = new ComboBoxField(page, new Rectangle(100, 640, 150, 656, true));
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        combo.setSelected(3);

        document.getForm().add(combo);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un champ de case à cocher



Utilisez cet exemple lorsque le formulaire nécessite une option vrai ou faux telle que le consentement ou la sélection de fonctionnalités.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [CheckboxField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) et configurez son apparence.
1. Ajoutez la case à cocher au formulaire et enregistrez le fichier de sortie.


```java
public static void addCheckboxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 620, 100, 650, true));
        checkbox.getCharacteristics().setBackground(Color.getAqua().toRgb());
        checkbox.setStyle(BoxStyle.Circle);

        document.getForm().add(checkbox);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un champ de zone de liste



Utilisez cet exemple lorsque le formulaire doit afficher plusieurs choix disponibles dans une liste visible.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [ListBoxField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) et ajoutez les options disponibles.
1. Ajoutez le champ au formulaire et enregistrez le document.


```java
public static void addListBoxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ListBoxField listBox = new ListBoxField(page, new Rectangle(50, 650, 100, 700, true));
        listBox.setPartialName("list");
        listBox.addOption("Red");
        listBox.addOption("Green");
        listBox.addOption("Blue");

        document.getForm().add(listBox);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un champ de signature



Utilisez cet exemple lorsque le document doit réserver une zone visible pour une signature numérique.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [SignatureField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) dans le rectangle requis.
1. Ajoutez le champ au formulaire et enregistrez le PDF de sortie.


```java
public static void addSignatureField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        SignatureField signatureField = new SignatureField(page, new Rectangle(100, 700, 200, 800, true));
        signatureField.setPartialName("Signature1");
        document.getForm().add(signatureField);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un champ de code-barres



Utilisez cet exemple lorsque le formulaire doit afficher des données lisibles par machine dans un champ de code-barres.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [BarcodeField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) et ajoutez la valeur du code-barres.
1. Ajoutez le champ au formulaire et enregistrez le document.

```java
public static void addBarcodeField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        BarcodeField barcode = new BarcodeField(page, new Rectangle(100, 700, 200, 740, true));
        barcode.setPartialName("Barcode1");
        barcode.addBarcode("1234567890");
        document.getForm().add(barcode);
        document.save(outputFile.toString());
    }
}
```
