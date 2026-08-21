---
title: Manipuler des documents PDF en Java
linktitle: Manipuler un document PDF
type: docs
weight: 20
url: /java/manipulate-pdf-document/
description: Découvrez comment valider, structurer et modifier des documents PDF en Java, y compris la gestion de la table des matières et les vérifications PDF/A.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validez, restructurez et aplatissez des documents PDF avec Java
Abstract: Cet article explique comment manipuler des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la validation de la conformité PDF/A, l'ajout et la personnalisation d'une table des matières, le masquage ou la personnalisation des numéros de page de la table des matières, l'attribution d'un script d'expiration et l'aplatissement des champs de formulaire interactifs.
---
Aspose.PDF pour Java inclut des opérations de structure de document qui vont au-delà de la simple édition de pages.


## 
Valider la conformité PDF/A-1a



Utilisez cet exemple lorsque vous devez vérifier si un document répond à la norme d'archivage PDF/A-1a.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Exécutez la validation par rapport à la cible [PdfFormat] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) requise.
1. Enregistrez le rapport de validation dans le chemin de sortie spécifié.


```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## 
Valider la conformité PDF/A-1b



Cette variation valide le même document source par rapport au niveau de conformité PDF/A-1b.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Appelez la méthode de validation avec la valeur [PdfFormat] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) pour PDF/A-1b.
1. Écrivez le résultat de la validation dans le fichier de rapport de sortie.


```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## 
Ajouter une table des matières



Utilisez cette approche lorsque le document doit inclure une page de table des matières générée avec des liens vers des pages de contenu.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Insérez une nouvelle TOC [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et configurez sa [TocInfo] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Créez des entrées [Heading] (https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) qui pointent vers les pages de destination.

1. 
Enregistrez le document mis à jour.


```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## 
Personnaliser les niveaux et le formatage de la table des matières



Cet exemple montre comment attribuer différents paramètres visuels à plusieurs niveaux de table des matières.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ajoutez une table des matières [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et configurez le tableau de format [TocInfo] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).

1. 
Créez des exemples d'entrées [Heading] (https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) avec différents niveaux.

1. 
Enregistrez le document avec la table des matières formatée.


```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 
Masquer les numéros de page dans la table des matières



Utilisez cet exemple lorsque la table des matières doit afficher les titres des entrées sans numéros de page.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une table des matières [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et désactivez les numéros de page dans [TocInfo] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).

1. 
Créez l'entrée [Heading] (https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) requise et ajoutez-la à la page de contenu.

1. 
Enregistrez le document mis à jour.


```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## 
Personnaliser les préfixes des numéros de page de la table des matières

Cet exemple ajoute un préfixe personnalisé aux numéros de page affichés dans la table des matières générée.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Insérez une table des matières [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et définissez le préfixe du numéro de page souhaité dans [TocInfo] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).

1. 
Créez des entrées [Heading] (https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) qui pointent vers chaque page.

1. 
Enregistrez le document mis à jour.

```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Ajouter un script d'expiration PDF



Utilisez cette approche lorsque le document doit exécuter JavaScript à l'ouverture et afficher un avertissement d'expiration après une date spécifique.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez tout contenu requis.

1. 
Créez une [JavascriptAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) avec la logique d'expiration.

1. 
Attribuez le script comme action d'ouverture de document et enregistrez le fichier de sortie.

```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## Aplatir un formulaire PDF à remplir



Cet exemple convertit les champs de formulaire interactifs en contenu de page statique afin que le document résultant ne soit plus modifiable en tant que formulaire.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Vérifiez si le document contient des widgets de formulaire.

1. 
Aplatissez chaque [Field] (https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) représenté par une [WidgetAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Enregistrez le document aplati.

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
