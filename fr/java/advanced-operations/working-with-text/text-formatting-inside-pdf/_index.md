---
title: Formater le texte PDF en Java
linktitle: Formatage du texte dans un PDF
type: docs
weight: 70
url: /java/text-formatting-inside-pdf/
description: Découvrez comment formater le texte dans des documents PDF en Java à l'aide d'options d'espacement, de notes, de listes, de disposition sur plusieurs colonnes et de style.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formater et styliser le texte dans les fichiers PDF avec Java
Abstract: Cet article explique comment formater le texte dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'espacement des lignes, l'espacement des caractères, les listes à puces et numérotées, les notes de bas de page et de fin, le contenu des paragraphes en ligne, la disposition sur plusieurs colonnes, les sauts de page forcés et les taquets de tabulation personnalisés.
---
Aspose.PDF pour Java propose des contrôles de formatage du texte pour l'espacement, les listes, les notes, la mise en page en ligne et la composition multi-colonnes.


## 
Définir un espacement de ligne simple



Utilisez cet exemple lorsque le texte d’un paragraphe doit utiliser une valeur d’interligne fixe.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Chargez ou préparez le texte source et créez un `TextFragment`.
1. Définissez l'espacement des lignes, ajoutez le fragment à la page et enregistrez le document.


```java
public static void specifyLineSpacingSimpleCase(Path outputFile) throws Exception {
        try (Document document = new Document()) {
            Page page = document.getPages().add();

            Path loremPath = dataDir.resolve("lorem.txt");
            String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

            TextFragment textFragment = new TextFragment(text);
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setLineSpacing(16);
            page.getParagraphs().add(textFragment);

            document.save(outputFile.toString());
        }
    }
```

## 
Comparez les modes d'espacement des lignes avec une police personnalisée



Utilisez cet exemple lorsque l’espacement des lignes doit être testé avec différents modes de formatage pour la même police.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Chargez la police personnalisée et préparez deux fragments avec des modes d'espacement des lignes différents.
1. Ajoutez les deux fragments à la page et enregistrez le PDF.


```java
public static void specifyLineSpacingSpecificCase(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Path fontFile = dataDir.resolve("HPSimplified.ttf");
        Path loremPath = dataDir.resolve("lorem.txt");
        String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

        try (InputStream fontStream = Files.newInputStream(fontFile)) {
            Font font = FontRepository.openFont(fontStream, FontTypes.TTF);

            TextFragment fragment1 = new TextFragment(text);
            fragment1.getTextState().setFont(font);
            fragment1.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment1.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FontSize);
            page.getParagraphs().add(fragment1);

            TextFragment fragment2 = new TextFragment(text);
            fragment2.getTextState().setFont(font);
            fragment2.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment2.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);
            page.getParagraphs().add(fragment2);
        }

        document.save(outputFile.toString());
    }
}
```

## 
Définir l'espacement des caractères avec des fragments de texte



Utilisez cet exemple lorsque le même texte doit être affiché avec des valeurs d'espacement des caractères différentes.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez des fragments de texte avec la méthode d'assistance pour plusieurs valeurs d'espacement.
1. Ajoutez les fragments à la page et enregistrez le document.


```java
public static void characterSpacingUsingTextFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.getParagraphs().add(makeCharacterSpacingFragment(2.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(1.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(0.75f));

        document.save(outputFile.toString());
    }
}

private static TextFragment makeCharacterSpacingFragment(float spacing) {
    TextFragment fragment = new TextFragment("Sample Text with character spacing");
    fragment.getTextState().setFont(FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize(14);
    fragment.getTextState().setCharacterSpacing(spacing);
    return fragment;
}
```

## 
Définir l'espacement des caractères à l'intérieur d'un paragraphe de texte



Utilisez cet exemple lorsque l’espacement des caractères doit être appliqué à l’intérieur d’un paragraphe de texte délimité.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TextParagraph` avec un rectangle cible et des options d'habillage.
1. Ajoutez le fragment de texte stylisé et enregistrez le PDF.


```java
public static void characterSpacingUsingTextParagraph(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(100, 700, 500, 750, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        TextFragment fragment = new TextFragment("Sample Text with character spacing");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(14);
        fragment.getTextState().setCharacterSpacing(2.0f);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
Créer une liste à puces avec HTML



Utilisez cet exemple lorsqu'un formatage de liste non ordonné doit être produit à partir d'un balisage HTML.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Construisez la chaîne de liste HTML.
1. Ajoutez-le en tant que `HtmlFragment` et enregistrez le document.


```java
public static void createBulletListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ul><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ul>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## 
Créer une liste numérotée avec HTML



Utilisez cet exemple lorsque le formatage de liste ordonnée doit être produit à partir du balisage HTML.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Construisez la chaîne de liste HTML ordonnée.
1. Ajoutez-le en tant que `HtmlFragment` et enregistrez le document.


```java
public static void createNumberedListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ol><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ol>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## 
Créer une liste à puces avec LaTeX



Utilisez cet exemple lorsque le formatage de liste non ordonnée doit être rendu à partir du balisage TeX.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Préparez la chaîne de liste TeX avec l'environnement `itemize`.
1. Ajoutez-le en tant que `TeXFragment` et enregistrez le PDF.


```java
public static void createBulletListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{itemize}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{itemize}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## 
Créer une liste numérotée avec LaTeX



Utilisez cet exemple lorsque le formatage de liste ordonnée doit être rendu à partir du balisage TeX.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Préparez la chaîne de liste TeX avec l'environnement `enumerate`.
1. Ajoutez-le en tant que `TeXFragment` et enregistrez le PDF.


```java
public static void createNumberedListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{enumerate}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{enumerate}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## 
Créer une liste à puces avec des paragraphes de texte



Utilisez cet exemple lorsqu'une liste à puces manuelle doit être créée à partir de fragments de texte brut.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TextParagraph` et ajoutez des fragments préfixés par une puce.
1. Ajoutez le paragraphe à la page et enregistrez le document.


```java
public static void createBulletList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (String item : items) {
            TextFragment fragment = new TextFragment("- " + item);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
Créer une liste numérotée avec des paragraphes de texte



Utilisez cet exemple lorsqu'une liste numérotée manuelle doit être construite à partir de fragments de texte brut.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TextParagraph` et ajoutez des fragments numérotés.
1. Ajoutez le paragraphe à la page et enregistrez le document.


```java
public static void createNumberedList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (int i = 0; i < items.length; i++) {
            TextFragment fragment = new TextFragment((i + 1) + ". " + items[i]);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une note de bas de page de base



Utilisez cet exemple lorsqu'un fragment de texte doit faire référence à une simple note de bas de page.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez le fragment de texte principal et attribuez un `Note` comme note de bas de page.
1. Ajoutez n'importe quel texte de continuation en ligne et enregistrez le document.


```java
public static void addFootnote(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        page.getParagraphs().add(textFragment);

        TextFragment inlineText = new TextFragment(" This is another text after footnote in the same paragraph.");
        inlineText.setInLineParagraph(true);
        inlineText.getTextState().setFont(FontRepository.findFont("Arial"));
        inlineText.getTextState().setFontSize(14);
        page.getParagraphs().add(inlineText);

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une note de bas de page avec un style de texte personnalisé



Utilisez cet exemple lorsque le contenu d’une note de bas de page doit utiliser ses propres paramètres de police, de taille et de couleur.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez le fragment de texte principal et configurez une note de bas de page stylisée.
1. Joignez la note et enregistrez le PDF.


```java
public static void addFootnoteCustomTextStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);

        Note note = new Note("This is the footnote content with custom text style.");
        TextState noteTextState = new TextState();
        noteTextState.setFont(FontRepository.findFont("Times New Roman"));
        noteTextState.setFontSize(10);
        noteTextState.setForegroundColor(Color.getRed());
        noteTextState.setFontStyle(FontStyles.Italic);
        note.setTextState(noteTextState);
        textFragment.setFootNote(note);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une note de bas de page avec un texte de marqueur personnalisé



Utilisez cet exemple lorsque le marqueur de note de bas de page visible doit être remplacé par du texte personnalisé.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Attribuez la note de bas de page au fragment de texte principal et remplacez son texte de marqueur.
1. Ajoutez le contenu restant et enregistrez le document.


```java
public static void addFootnoteCustomText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        textFragment.getFootNote().setText("***");
        page.getParagraphs().add(textFragment);

        TextFragment anotherText = new TextFragment(" This is another text without footnote.");
        anotherText.getTextState().setFont(FontRepository.findFont("Arial"));
        anotherText.getTextState().setFontSize(14);
        page.getParagraphs().add(anotherText);

        document.save(outputFile.toString());
    }
}
```

## 
Personnaliser la ligne de séparation des notes de bas de page



Utilisez cet exemple lorsque la ligne qui sépare les notes de bas de page du contenu de la page doit être explicitement stylisée.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Configurez le style de ligne de note de page via `GraphInfo`.
1. Ajoutez des fragments de texte avec des notes de bas de page et enregistrez le document.


```java
public static void addFootnoteWithCustomLineStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        GraphInfo graphInfo = new GraphInfo();
        graphInfo.setLineWidth(2);
        graphInfo.setColor(Color.getRed());
        graphInfo.setDashArray(new int[] {3});
        graphInfo.setDashPhase(1);
        page.setNoteLineStyle(graphInfo);

        TextFragment text1 = new TextFragment("This is a sample text with a footnote.");
        text1.setFootNote(new Note("foot note for text 1"));
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment("This is yet another sample text with a footnote.");
        text2.setFootNote(new Note("foot note for text 2"));
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une note de bas de page avec le contenu de l'image et du tableau



Utilisez cet exemple lorsque la note de bas de page elle-même doit contenir un contenu riche tel que des images, du texte et des tableaux.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un objet `Note` avec une image, du texte en ligne et un tableau.
1. Attachez-le au fragment de texte principal et enregistrez le document.


```java
public static void addFootnoteWithImageAndTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text = new TextFragment("This is a sample text with a footnote.");
        page.getParagraphs().add(text);

        Note note = new Note();

        Image imageNote = new Image();
        imageNote.setFile(dataDir.resolve("logo.jpg").toString());
        imageNote.setFixHeight(20);
        imageNote.setFixWidth(20);
        note.getParagraphs().add(imageNote);

        TextFragment textNote = new TextFragment("This is the footnote content.");
        textNote.getTextState().setFontSize(20);
        textNote.setInLineParagraph(true);
        note.getParagraphs().add(textNote);

        Table table = new Table();
        table.getRows().add().getCells().add("Cell 1,1");
        table.getRows().add().getCells().add("Cell 1,2");
        note.getParagraphs().add(table);

        text.setFootNote(note);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une note de fin



Utilisez cet exemple lorsqu'un fragment de texte doit faire référence au contenu d'une note de fin au lieu d'une note de bas de page.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Attribuez une note de fin au fragment de texte principal et ajoutez le corps du texte de support.
1. Enregistrez le document avec le contenu de la note de fin générée.


```java
public static void addEndnote(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}

private static String loremText() throws Exception {
    Path loremPath = dataDir.resolve("lorem.txt");
    return Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum sample text not found.";
}
```

## 
Ajouter une note de fin avec un texte de marqueur personnalisé



Utilisez cet exemple lorsque le marqueur de note de fin doit utiliser une étiquette visible personnalisée.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Attribuez une note de fin au fragment de texte principal et remplacez son texte de marqueur.
1. Ajoutez le texte restant du document et enregistrez le PDF.


```java
public static void addEndnoteCustomText(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        textFragment.getEndNote().setText("***");
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}
```

## 
Forcer le contenu du tableau sur une nouvelle page



Utilisez cet exemple lorsque le contenu formaté doit explicitement commencer sur une nouvelle page.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un tableau et remplissez ses lignes.
1. Configurez le tableau pour qu'il commence sur une nouvelle page et enregistrez le document.


```java
public static void forceNewPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Table table = new Table();
        table.setColumnWidths("150 150 150");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));

        for (int i = 0; i < 5; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Row " + (i + 1) + " - Col 1");
            row.getCells().add("Row " + (i + 1) + " - Col 2");
            row.getCells().add("Row " + (i + 1) + " - Col 3");
        }

        table.setInNewPage(true);
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
Mélanger le contenu en ligne dans un flux de paragraphe



Utilisez cet exemple lorsque le texte et les images doivent continuer dans le même flux de paragraphes.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Ajoutez le premier fragment de texte, puis une image en ligne, puis un autre fragment de texte en ligne.
1. Ajoutez n’importe quel paragraphe autonome suivant et enregistrez le document.


```java
public static void usingInlineParagraphProperty(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment1 = new TextFragment("This is the first part of the paragraph. ");
        fragment1.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment1.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment1);

        Image image = new Image();
        image.setInLineParagraph(true);
        image.setFile(dataDir.resolve("logo.jpg").toString());
        image.setFixHeight(30);
        image.setFixWidth(30);
        page.getParagraphs().add(image);

        TextFragment fragment2 = new TextFragment("This is the second part of the same paragraph.");
        fragment2.setInLineParagraph(true);
        fragment2.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment2.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment2);

        TextFragment fragment3 = new TextFragment("This is a new paragraph.");
        fragment3.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment3.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment3);

        document.save(outputFile.toString());
    }
}
```

## 
Créer une mise en page de texte multicolonne



Utilisez cet exemple lorsque le texte de style article doit s’étendre sur plusieurs colonnes.


1. 
Créez un nouveau document PDF et configurez les marges des pages.

1. 
Ajoutez le contenu du titre et créez un `FloatingBox` multi-colonnes.
1. Remplissez-le de texte et enregistrez le PDF final.


```java
public static void createMultiColumnPdf(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(40);
        document.getPageInfo().getMargin().setRight(40);
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500.0, 2.0);
        page.getParagraphs().add(graph1);
        graph1.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 2.0f, 500.0f, 2.0f}));

        String html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>";
        page.getParagraphs().add(new HtmlFragment(html));

        FloatingBox box = new FloatingBox();
        box.getColumnInfo().setColumnCount(2);
        box.getColumnInfo().setColumnSpacing("5");
        box.getColumnInfo().setColumnWidths("105 105");

        TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
        text1.getTextState().setFontSize(8);
        text1.getTextState().setLineSpacing(2);
        box.getParagraphs().add(text1);

        text1.getTextState().setFontSize(10);
        text1.getTextState().setFontStyle(FontStyles.Italic);

        com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50.0, 10.0);
        graph2.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 10.0f, 100.0f, 10.0f}));
        box.getParagraphs().add(graph2);

        String loremText = loremText();
        box.getParagraphs().add(new TextFragment(loremText.repeat(5)));
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```

## 
Créez du texte aligné avec des taquets de tabulation personnalisés



Utilisez cet exemple lorsque le texte doit s’aligner comme un simple tableau en utilisant des positions de taquet de tabulation.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Configurez les taquets de tabulation avec les paramètres d'alignement et de repère.
1. Créez les fragments de texte qui utilisent ces taquets de tabulation et enregistrez le document.

```java
public static void customTabStops(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TabStops tabStops = new TabStops();
        TabStop tabStop1 = tabStops.add(100);
        tabStop1.setAlignmentType(TabAlignmentType.Right);
        tabStop1.setLeaderType(TabLeaderType.Solid);

        TabStop tabStop2 = tabStops.add(200);
        tabStop2.setAlignmentType(TabAlignmentType.Center);
        tabStop2.setLeaderType(TabLeaderType.Dash);

        TabStop tabStop3 = tabStops.add(300);
        tabStop3.setAlignmentType(TabAlignmentType.Left);
        tabStop3.setLeaderType(TabLeaderType.Dot);

        TextFragment header = new TextFragment("This is an example of forming table with TAB stops", tabStops);
        TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);

        TextFragment text2 = new TextFragment("#$TABdata21 ", tabStops);
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data22 "));
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data23"));

        page.getParagraphs().add(header);
        page.getParagraphs().add(text0);
        page.getParagraphs().add(text1);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```
