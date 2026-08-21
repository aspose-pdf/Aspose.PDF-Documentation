---
title: Annotations interactives utilisant Java
linktitle: Annotations interactives
type: docs
weight: 60
url: /java/interactive-annotations/
description: Découvrez comment ajouter, inspecter et supprimer des annotations de lien dans des documents PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Travaillez avec des annotations PDF interactives en Java.
Abstract: Cet article explique comment utiliser des annotations de liens interactifs dans des fichiers PDF à l'aide d'Aspose.PDF pour Java. Il couvre la localisation du texte, la création d'une annotation de lien sur la zone de texte correspondante, la lecture des annotations de lien existantes et leur suppression.
---
Les annotations interactives de cette section se concentrent sur les flux de travail basés sur des liens et des boutons qui répondent aux actions de l'utilisateur dans une visionneuse PDF.


## 
Ajouter une annotation de lien



Utilisez cet exemple lorsque vous devez placer un lien cliquable sur le texte trouvé sur la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Localisez le fragment de texte cible et créez une [LinkAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) sur son rectangle.
1. Attribuez une [GoToURIAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) et enregistrez le document mis à jour.


```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
Obtenir des annotations de lien



Cet exemple analyse la collection d'annotations de page et indique l'emplacement de chaque annotation de lien.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations sur la page cible.
1. Filtrez les annotations par [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` et imprimez leurs rectangles.


```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 
Supprimer les annotations du lien



Utilisez cette approche lorsque les annotations de liens existantes doivent être supprimées de la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Collectez les annotations dont le type est [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`.
1. Supprimez les annotations collectées et enregistrez le fichier de sortie.


```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une annotation de ligne



Cet exemple crée une annotation de ligne interactive avec des styles de flèches, des paramètres de bordure et une note contextuelle.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [LineAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) avec des points de début et de fin.
1. Configurez son apparence et son annotation contextuelle, puis enregistrez le document.


```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));

        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des boutons de navigation



Utilisez cet exemple lorsque le PDF doit inclure des boutons de page précédente et de page suivante pour une navigation interactive.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et assurez-vous que le document contient les pages requises.

1. 
Créez des contrôles [ButtonField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) avec des actions de navigation prédéfinies.
1. Ajoutez les boutons à la collection de formulaires et enregistrez le document mis à jour.


```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un bouton d'impression



Cet exemple crée un bouton qui déclenche la commande d'impression lorsque l'utilisateur clique dessus.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Créez un [ButtonField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) et attribuez l'action prédéfinie d'impression.
1. Configurez la bordure et l'arrière-plan du bouton, ajoutez-les au formulaire et enregistrez le document.

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
