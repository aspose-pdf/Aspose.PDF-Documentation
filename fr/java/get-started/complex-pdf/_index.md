---
title: Créer un PDF complexe
linktitle: Créer un PDF complexe
type: docs
weight: 30
url: /java/complex-pdf-example/
description: Aspose.PDF for Java vous permet de créer des documents PDF plus complexes contenant des images, des fragments de texte et des tableaux dans un seul fichier.
lastmod: "2026-09-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un PDF complexe à l'aide de Java
Abstract: Cet article montre comment créer un PDF plus complexe en Java à l'aide d'Aspose.PDF. L'exemple ajoute une image, un en-tête mis en forme, un bloc de texte descriptif et un tableau avec des cellules d’en-tête mises en forme et des lignes d’horaires générées, puis enregistre le résultat sous forme de document PDF.
---
L'exemple [Hello World](/pdf/java/hello-world-example/) présente les étapes de base de la création d’un PDF. Cet exemple reprend ces étapes et crée un document plus riche combinant des graphiques, du texte et du contenu tabulaire.

Pour créer un document PDF plus complexe en Java :

1. Créez un objet [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Ajoutez une image à la [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) avec `page.addImage(...)` et un rectangle de destination [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).

1. Créez un objet [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) pour l’en-tête et définissez sa police, sa taille de police, son alignement et sa [`Position`](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/).
1. Créez un deuxième objet [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) pour le paragraphe de description.

1. Créez un tableau [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) avec des bordures, des marges internes de cellule et un style d’en-tête.

1. Ajoutez les lignes d’horaires générées au tableau [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/).

1. Ajoutez le tableau [`Table`](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) à la collection de paragraphes de la page [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Enregistrez l’objet [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) au format PDF.

Le code Java suivant est basé sur `GetStartedExamples.java`.

```java
public static void complexExample(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));

        TextFragment header = new TextFragment("New ferry routes in Fall 2029");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
                + "Ferry service is operating at half capacity and on a reduced schedule. "
                + "Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        page.getParagraphs().add(createScheduleTable());

        document.save(outputFile.toString());
    }
}
```

Cet exemple utilise une méthode auxiliaire pour préparer le tableau des horaires, mettre en forme l’en-tête et générer les heures de départ :

```java
private static Table createScheduleTable() {
    Table table = new Table();
    table.setColumnWidths("200 200");
    table.setBorder(new BorderInfo(BorderSide.Box, 1.0f, Color.getDarkSlateGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
    table.setDefaultCellPadding(new MarginInfo(4.5, 4.5, 4.5, 4.5));
    table.getMargin().setBottom(10);
    table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

    Row headerRow = table.getRows().add();
    Cell departsCityCell = headerRow.getCells().add("Departs City");
    Cell departsIslandCell = headerRow.getCells().add("Departs Island");
    styleHeaderCell(departsCityCell);
    styleHeaderCell(departsIslandCell);

    Duration time = Duration.ofHours(6);
    Duration increment = Duration.ofMinutes(30);
    for (int index = 0; index < 10; index++) {
        Row dataRow = table.getRows().add();
        dataRow.getCells().add(formatTime(time));
        time = time.plus(increment);
        dataRow.getCells().add(formatTime(time));
    }

    return table;
}
```
