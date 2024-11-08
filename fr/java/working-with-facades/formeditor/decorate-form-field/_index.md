---
title: Décorer un Champ de Formulaire dans un PDF
type: docs
weight: 20
url: /fr/java/decorate-form-field/
description: Cette section explique comment décorer un champ de formulaire dans un PDF en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Décorer un Champ de Formulaire Particulier dans un Fichier PDF Existant

La méthode [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) présente dans la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) permet de décorer un champ de formulaire particulier dans un fichier PDF.
 Si vous souhaitez décorer un champ particulier, vous devez passer le nom du champ à cette méthode. Cependant, avant d'appeler cette méthode, vous devez créer des objets des classes [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) et [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Après cela, vous pouvez définir n'importe quel attribut fourni par l'objet [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Une fois que vous avez défini les attributs, vous pouvez appeler la méthode [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) et enfin enregistrer le PDF mis à jour en utilisant la méthode Save de la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Le code suivant vous montre comment décorer un champ de formulaire particulier.

```java
public static void DecorateField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade cityDecoration = new FormFieldFacade();
        cityDecoration.setFont(FontStyle.Courier);
        cityDecoration.setFontSize(12);
        cityDecoration.setBorderColor(Color.BLACK);
        cityDecoration.setBorderWidth(2);

        editor.setFacade(cityDecoration);
        editor.decorateField("City");
        editor.save(_dataDir + "Sample-Form-02.pdf");
    }
```

## Décorer Tous les Champs d'un Type Particulier dans un Fichier PDF Existant

La méthode [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) vous permet de décorer tous les champs de formulaire d'un type particulier dans un fichier PDF en une seule fois.
 Si vous souhaitez décorer tous les champs d'un type particulier, vous devez passer le type de champ à cette méthode. Cependant, avant d'appeler cette méthode, vous devez créer des objets des classes [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) et [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Après cela, vous pouvez définir tous les attributs fournis par l'objet [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Une fois que vous avez défini les attributs, vous pouvez appeler la méthode [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) et enfin enregistrer le PDF mis à jour en utilisant la méthode Save de la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Le code suivant vous montre comment décorer tous les champs d'un type particulier.

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        // Définir l'alignement au centre pour le champ de texte
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        editor.decorateField(FieldType.Text);
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```