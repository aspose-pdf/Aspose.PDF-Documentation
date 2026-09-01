---
title: Modification d'AcroForm
linktitle: Modification d'AcroForm
type: docs
weight: 45
url: /java/modifying-form/
description: Modifiez les champs AcroForm dans les documents PDF à l'aide d'Aspose.PDF pour Java, notamment en effaçant le texte, en définissant des limites, en stylisant les champs et en supprimant des champs.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modifier et personnaliser les champs du formulaire PDF avec Java
Abstract: Cet article explique comment modifier le contenu AcroForm à l'aide d'Aspose.PDF pour Java. Il couvre la suppression du texte des ressources de formulaire Typewriter, la définition et la lecture des limites de longueur des champs de texte, la modification de l'apparence de la police des champs de formulaire et la suppression de champs spécifiques par nom.
---
La maintenance des formulaires implique souvent à la fois des modifications au niveau des champs et le nettoyage des ressources de page liées au formulaire.


## 
Texte clair dans les ressources de formulaire intégré



Utilisez cet exemple lorsque le contenu du formulaire Typewriter doit être vidé sans supprimer les objets du formulaire eux-mêmes.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les ressources de formulaires de page et localisez les formulaires Typewriter.
1. Effacez les fragments de texte absorbés et enregistrez le document.


```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
Définir une limite de longueur de champ de texte



Utilisez cet exemple lorsqu'un champ de texte ne doit accepter qu'un nombre limité de caractères.


1. 
Créez une façade [FormEditor] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) et liez le PDF source.

1. 
Définissez la longueur maximale du champ cible.
1. Enregistrez le document mis à jour.


```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
Obtenir une limite de longueur de champ de texte



Utilisez cet exemple lorsque vous devez inspecter la longueur maximale actuelle d’un champ de texte.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez au champ cible à partir de la collection de formulaires.
1. Lisez la limite de [TextBoxField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) et affichez-la.


```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## 
Changer la police d'un champ de formulaire



Utilisez cet exemple lorsqu'un champ de texte existant doit utiliser une police ou une apparence différente.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez à la cible [TextBoxField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) et définissez une nouvelle apparence par défaut.
1. Enregistrez le PDF mis à jour.


```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## 
Supprimer un champ de formulaire par son nom



Utilisez cet exemple lorsqu'un champ spécifique doit être supprimé de l'AcroForm.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Supprimez le champ cible du formulaire par son nom.
1. Enregistrez le document mis à jour.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
