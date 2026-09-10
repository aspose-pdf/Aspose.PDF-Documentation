---
title: Ajouter des en-têtes et des pieds de page PDF en Java
linktitle: Ajout d'un en-tête et d'un pied de page au PDF
type: docs
weight: 50
url: /java/add-headers-and-footers-of-pdf-file/
description: Découvrez comment ajouter des en-têtes et des pieds de page aux fichiers PDF en Java à l'aide de texte, d'images et de contenu structuré.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des en-têtes et des pieds de page aux fichiers PDF avec Java
Abstract: Cet article montre comment ajouter des en-têtes et des pieds de page aux documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre le texte, la numérotation des pages, le HTML, les images, les tableaux et le contenu des en-têtes et pieds de page basés sur LaTeX.
---
Aspose.PDF pour Java vous permet d'attribuer des objets `HeaderFooter` à chaque page et de les remplir avec différents types de contenu.


## 
Ajouter des en-têtes et des pieds de page de texte



Utilisez cet exemple lorsque vous avez besoin d'un contenu textuel simple en haut et en bas de chaque page.


1. 
Créez des objets [HeaderFooter] (https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) et ajoutez des fragments de texte.

1. 
Configurez les marges pour l'en-tête et le pied de page.
1. Appliquez-les à chaque page du PDF source et enregistrez le résultat.


```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des en-têtes et des pieds de page avec numérotation des pages



Utilisez cet exemple lorsque l'en-tête ou le pied de page doit afficher le numéro de page actuel et le nombre total de pages.


1. 
Créez des objets [HeaderFooter] (https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) avec des espaces réservés pour la numérotation des pages.

1. 
Configurez les marges pour les deux objets.
1. Apply them to each page and save the updated PDF.


```java
public static void usingHeaderAndFooterForPageNumbering(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Page $p from $P"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Page $p / $P"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Add HTML headers and footers



Use this example when header and footer content should include inline HTML formatting.


1. 
Create [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) objects and add [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) content.

1. 
Configure margins for placement.
1. Attribuez l'en-tête et le pied de page à chaque page et enregistrez le document.


```java
public static void addHeaderAndFooterAsHtml(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new HtmlFragment("This is an HTML <strong>Header</strong>"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new HtmlFragment("Powered by <i>Aspose.PDF</i>"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des en-têtes et des pieds de page d'image



Utilisez cet exemple lorsque l'en-tête et le pied de page doivent afficher une image sur chaque page.


1. 
Créez des objets [Image] (https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) et ajoutez-les aux conteneurs d'en-tête et de pied de page.

1. 
Configurez les marges et attribuez les conteneurs à chaque page.
1. Enregistrez le PDF mis à jour.


```java
public static void addHeaderAndFooterAsImage(Path inputFile, Path imageFile, Path outputFile) {
    Image headerImage = new Image();
    headerImage.setFile(imageFile.toString());
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(headerImage);

    Image footerImage = new Image();
    footerImage.setFile(imageFile.toString());
    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(footerImage);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            MarginInfo margin = new MarginInfo();
            margin.setLeft(50);
            header.setMargin(margin);
            footer.setMargin(margin);
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des en-têtes et des pieds de page basés sur des tableaux



Utilisez cet exemple lorsque le contenu de l’en-tête et du pied de page doit utiliser la disposition du tableau et le style du texte.


1. 
Créez les styles de texte et les objets de tableau requis.

1. 
Ajoutez les tables aux conteneurs [HeaderFooter] (https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/).
1. Appliquez l'en-tête et le pied de page à chaque page et enregistrez le document.


```java
public static void addHeaderAndFooterAsTable(Path inputFile, Path outputFile) {
    TextState textStateHeader = new TextState();
    textStateHeader.setFont(FontRepository.findFont("Arial"));
    textStateHeader.setFontSize(12);
    textStateHeader.setHorizontalAlignment(HorizontalAlignment.Center);

    TextState textStateFooter = new TextState();
    textStateFooter.setFont(FontRepository.findFont("Arial"));
    textStateFooter.setFontSize(12);
    textStateFooter.setHorizontalAlignment(HorizontalAlignment.Left);

    HeaderFooter header = new HeaderFooter();
    HeaderFooter footer = new HeaderFooter();

    Table tableHeader = new Table();
    tableHeader.setColumnWidths(String.valueOf(594 - header.getMargin().getLeft() - header.getMargin().getRight()));
    tableHeader.getRows().add().getCells().add("This is a Table Header", textStateHeader);

    Table table = new Table();
    table.setColumnWidths(String.valueOf(594 - footer.getMargin().getLeft() - footer.getMargin().getRight()));
    table.getRows().add().getCells().add("Powered by Aspose.PDF", textStateFooter);

    header.getParagraphs().add(tableHeader);
    footer.getParagraphs().add(table);
    footer.getMargin().setLeft(150);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des en-têtes et pieds de page LaTeX



Utilisez cet exemple lorsque l'en-tête et le pied de page doivent restituer le contenu TeX ou LaTeX.


1. 
Ouvrez le PDF source et déterminez le nombre total de pages.

1. 
Créez du contenu [TeXFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) pour l'en-tête et le pied de page de chaque page.
1. Attribuez le contenu et enregistrez le document.

```java
public static void addHeaderAndFooterAsLatex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int pageCount = document.getPages().size();
        for (int i = 1; i <= pageCount; i++) {
            HeaderFooter header = new HeaderFooter();
            header.getParagraphs().add(new TeXFragment("This is a LaTeX Header. \\today\\", true));

            HeaderFooter footer = new HeaderFooter();
            footer.getParagraphs().add(new TeXFragment("\\copyright\\ 2025 My Company -- Page \\thepage\\ is " + pageCount, true));

            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```
