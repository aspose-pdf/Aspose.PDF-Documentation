---
title: Travailler avec les opérateurs PDF en Java
linktitle: Travailler avec des opérateurs
type: docs
weight: 90
url: /java/working-with-operators/
description: Découvrez comment utiliser les opérateurs PDF de bas niveau en Java pour la manipulation de flux de contenu, le placement d'images, la réutilisation de XForm et le nettoyage de graphiques.
lastmod: "2026-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Utiliser des opérateurs PDF de bas niveau pour le contrôle du flux de contenu en Java
Abstract: Cet article explique comment utiliser les opérateurs PDF de bas niveau dans Aspose.PDF pour Java. Apprenez à placer des images avec précision, à dessiner du contenu XForm réutilisable et à supprimer des opérateurs graphiques des pages PDF.
---
## Introduction aux opérateurs PDF et à leur utilisation



Un opérateur est un mot-clé PDF spécifiant une action à effectuer, comme peindre une forme graphique sur la page. Un mot-clé opérateur se distingue d'un objet nommé par l'absence de caractère solidus initial (2Fh). Les opérateurs n'ont de sens qu'à l'intérieur du flux de contenu.



Un flux de contenu est un objet flux PDF dont les données sont constituées d'instructions décrivant les éléments graphiques à peindre sur une page. Plus de détails sur les opérateurs PDF peuvent être trouvés dans la [spécification PDF] (https://opensource.adobe.com/dc-acrobat-sdk-docs/).



Utilisez cette page lorsque vous avez besoin d'un contrôle direct sur un flux de contenu PDF en Java, par exemple en plaçant une image avec des mathématiques matricielles explicites, en réutilisant le même graphique plusieurs fois via un XForm ou en supprimant des instructions de dessin de bas niveau d'une page.


## 
Ajouter une image avec les opérateurs PDF

Utilisez des opérateurs de bas niveau lorsque le placement des images doit être contrôlé précisément au niveau du flux de contenu plutôt que via des API de mise en page de niveau supérieur.


1. 
Ouvrez le PDF source avec [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et obtenez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Ajoutez le flux d'images d'entrée aux ressources de la page et conservez le nom de la ressource renvoyé.

1. 
Créez un [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) qui définit la zone cible et construisez une [Matrice] (https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) à partir de ses limites.

1. 
Utilisez [GSave] (https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) pour conserver l'état graphique actuel, [ConcatenateMatrix] (https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) pour positionner l'image, [Do] (https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) pour la peindre et [GRestore] (https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) pour restaurer l'état antérieur.
1. Enregistrez le document PDF mis à jour.


```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## 
Dessiner du contenu XForm réutilisable sur une page



Utilisez cette approche lorsque la même image ou le même graphique doit être rendu plusieurs fois sans dupliquer la ressource dans le fichier PDF.


1. 
Ouvrez le PDF source avec [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), récupérez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et accédez à sa [OperatorCollection] (https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).

1. 
Enveloppez le contenu de la page existante avec [GSave] (https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) et [GRestore] (https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) afin que les transformations ultérieures ne s'infiltrent pas dans le flux de contenu d'origine.
1. Créez une ressource [XForm] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/), ajoutez l'image aux ressources du formulaire et utilisez [ConcatenateMatrix] (https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) plus [Do] (https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) pour dessiner l'image à l'intérieur du formulaire.

1. 
Placez le même formulaire sur plusieurs coordonnées de page en ajoutant une matrice de traduction et en exécutant le nom du formulaire avec l'opérateur `Do`.

1. 
Restaurez l’état graphique et enregistrez le PDF de sortie.


```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## 
Supprimer les opérateurs graphiques d'une page



Utilisez cet exemple lorsqu'une page contient des opérateurs de dessin vectoriel qui doivent être supprimés directement du flux de contenu.

1. Open the source PDF with [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and get the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Iterate through the page content operators and collect instances of [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/), and [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).

1. 
Delete the collected operators from the page contents and save the updated PDF.



This technique removes the targeted drawing instructions only. If the page also contains related text labels or other non-graphic operators, those items remain in the content stream and may need a separate cleanup pass.


```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## 
Related Topics

- [Opérations PDF avancées en Java](/pdf/java/advanced-operations/)

- 
[Travailler avec des images en PDF en utilisant Java](/pdf/java/working-with-images/)

- 
[Gérer les pages PDF en Java](/pdf/java/working-with-pages/)

- 
[Travailler avec des graphiques vectoriels en Java](/pdf/java/working-with-vector-graphics/)
