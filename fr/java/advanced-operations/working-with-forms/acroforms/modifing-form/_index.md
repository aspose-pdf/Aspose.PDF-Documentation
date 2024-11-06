---
title: Modification des AcroForms
linktitle: Modification des AcroForms
type: docs
weight: 40
url: fr/java/modifing-form/
description: Cette section explique comment modifier les formulaires dans votre document PDF avec Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Définir une police de champ de formulaire personnalisée

Les champs de formulaire dans les fichiers PDF Adobe peuvent être configurés pour utiliser des polices par défaut spécifiques. Aspose.PDF permet aux développeurs d'appliquer n'importe quelle police comme police par défaut pour un champ, qu'il s'agisse de l'une des 14 polices de base ou d'une police personnalisée. Pour définir et mettre à jour la police par défaut utilisée pour les champs de formulaire, Aspose.PDF dispose de la classe DefaultAppearance (Font font, double size, Color color). Cette classe est accessible via com.aspose.pdf.DefaultAppearance. Pour utiliser cet objet, utilisez la méthode setDefaultAppearance(..) de la classe Field.

Le code suivant vous montre comment définir la police par défaut pour un champ de formulaire PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // Obtenir un champ de formulaire particulier du document
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // Créer un objet police
        Font font = FontRepository.findFont("ComicSansMS");

        // Définir les informations de la police pour le champ de formulaire
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## Get/Set FieldLimit

La méthode SetFieldLimit de la classe FormEditor vous permet de définir une limite de champ, le nombre maximum de caractères pouvant être saisis dans un champ.

```java
    public static void GettingMaximumFieldLimit()
    {
        // Obtenir la limite maximale de champ en utilisant DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("Limite: " +field.getMaxLen());
    }
```

Vous pouvez également obtenir la même valeur en utilisant l'espace de noms Aspose.PDF.Facades avec le code suivant.

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // Obtenir la limite maximale de champ en utilisant Facades
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("Limite: " + form.getFieldLimit("textbox1"));
    }
```

De même, Aspose.PDF dispose d'une méthode qui obtient la limite de champ en utilisant l'approche DOM.
 Le code suivant montre les étapes.

```java
    public static void SettingMaximumFieldLimit()
    {
        // Obtenir la limite maximale de champ en utilisant le DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Limite : " +field.getMaxLen());       
    }
```

## Supprimer un champ de formulaire particulier d'un document PDF

Tous les champs de formulaire sont contenus dans la collection Form de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Cette collection fournit différentes méthodes qui gèrent les champs de formulaire, y compris la méthode de suppression. Si vous souhaitez supprimer un champ particulier, passez le nom du champ en tant que paramètre à la méthode de suppression, puis enregistrez le document PDF mis à jour.

Le code suivant montre comment supprimer un champ nommé d'un document PDF.

```java
    public static void DeleteParticularFormField()
    {    
        // Ouvrir un document
        Document pdfDocument = new Document("input.pdf");

        // Supprimer un champ nommé par son nom
        pdfDocument.getForm().delete("textbox1");

        // Enregistrer le PDF modifié
        pdfDocument.save("output.pdf");
    }
```

## Modifier un champ de formulaire dans un document PDF

La collection Form de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) vous permet de gérer les champs de formulaire dans un document PDF.

Pour modifier un champ de formulaire, obtenez le champ de la collection Form et définissez ses propriétés. Ensuite, enregistrez le document PDF mis à jour.

Le fragment de code suivant montre comment modifier un champ de formulaire existant dans un document PDF.

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // Obtenez un champ
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modifier la valeur du champ
        textBoxField.setValue("Valeur Mise à Jour");

        // Définir le champ comme lecture seule
        textBoxField.setReadOnly(true);

        // Enregistrez le document mis à jour
        pdfDocument.save("output.pdf");
    }
```

### Déplacer un champ de formulaire vers un nouvel emplacement dans un fichier PDF

Si vous souhaitez déplacer un champ de formulaire vers un nouvel emplacement sur une page PDF, commencez par obtenir l'objet champ, puis spécifiez une nouvelle valeur pour sa méthode setRect.
 Un objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) avec de nouvelles coordonnées est attribué à la méthode setRect(..). Ensuite, enregistrez le PDF mis à jour en utilisant la méthode save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Le code suivant vous montre comment déplacer un champ de formulaire vers un nouvel emplacement.

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // Ouvrir un document
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // Obtenir un champ
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modifier l'emplacement du champ
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // Enregistrer le document modifié
        pdfDocument.save("output.pdf");
    }
}
```