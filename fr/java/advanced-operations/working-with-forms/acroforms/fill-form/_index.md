---
title: Remplir les AcroForms
linktitle: Remplir les AcroForms
type: docs
weight: 20
url: /fr/java/fill-form/
description: Cette section explique comment remplir un champ de formulaire dans un document PDF avec Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les documents PDF sont merveilleux et vraiment le type de fichier préféré pour créer des formulaires.

Aspose.PDF pour Java vous permet de remplir un champ de formulaire, d'obtenir le champ de la collection de formulaires de l'objet Document.

Voyons l'exemple suivant pour résoudre cette tâche :

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Créer un champ
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Boîte de texte");

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

    
}
```