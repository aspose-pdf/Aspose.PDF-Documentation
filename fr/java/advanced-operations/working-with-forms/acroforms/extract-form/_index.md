---
title: Extraire les données des AcroForms
linktitle: Extraire les données des AcroForms
type: docs
weight: 30
url: /fr/java/extract-form/
description: Cette section explique comment extraire des formulaires de votre document PDF avec Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir la valeur d'un champ individuel du document PDF

La méthode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier.

Pour obtenir la valeur, récupérez le champ de formulaire de la collection Form de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cet exemple sélectionne un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) et récupère sa valeur en utilisant la méthode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // Ouvrir un document
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // Obtenir un champ
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Obtenir le nom du champ
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // Obtenir la valeur du champ
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## Obtenir les valeurs de tous les champs dans un document PDF

Pour obtenir les valeurs de tous les champs dans un document PDF, vous devez naviguer à travers tous les champs de formulaire et ensuite obtenir la valeur en utilisant la [méthode getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--). Obtenez chaque champ de la collection Form en utilisant la méthode [getForm()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et récupérez la liste des champs de formulaire dans un tableau Field en utilisant getFields() et parcourez le tableau pour obtenir la valeur des champs.

Le code suivant montre comment obtenir les valeurs de tous les champs dans un document PDF.

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // Ouvrir le document
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("Champ de formulaire : " + fields[i].getFullName());
            System.out.println("Champ de formulaire : " + fields[i].getValue());
        }

    }
}
```


## Obtenir les Champs de Formulaire d'une Région Spécifique d'un Fichier PDF

Dans certains cas, il est nécessaire d'obtenir des données non pas de l'ensemble du formulaire, mais, par exemple, uniquement du quart supérieur gauche de la feuille imprimée.  
Avec Aspose.PDF pour Java, ce n'est pas un problème. Vous pouvez spécifier une région pour filtrer les champs qui sont en dehors de la région donnée du fichier PDF. Pour obtenir les champs de formulaire d'une zone spécifique d'un fichier PDF :

1. Ouvrez le fichier PDF en utilisant l'objet Document.
1. Obtenez le formulaire à partir de la collection Forms du document.
1. Spécifiez la région rectangulaire et passez-la à la méthode [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) de l'objet Form. Une collection [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field) est retournée.
1. Utilisez cela pour manipuler les champs.

Le code suivant montre comment obtenir les champs de formulaire dans une région rectangulaire spécifique d'un fichier PDF.

```java
public static void GetValuesFromSpecificRegion() {
    // Ouvrir le fichier pdf
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // Créer un objet rectangle pour obtenir les champs dans cette zone
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // Obtenir le formulaire PDF
    com.aspose.pdf.Form form = doc.getForm();

    // Obtenir les champs dans la zone rectangulaire
    Field[] fields = form.getFieldsInRect(rectangle);

    // Afficher les noms et valeurs des champs
    for (Field field : fields)
    {
        // Afficher les propriétés de placement de l'image pour tous les placements
        System.out.println("Nom du Champ: " + field.getFullName() + "-" + "Valeur du Champ: " + field.getValue());
    }
}
```