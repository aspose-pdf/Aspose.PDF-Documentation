---
title: Ajouter du texte au PDF en Java
linktitle: Ajouter du texte au PDF
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: Découvrez comment ajouter du texte, des fragments HTML, des listes, des liens et des polices personnalisées aux documents PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajoutez du texte, des liens, du HTML et des polices aux fichiers PDF avec Java
Abstract: Cet article explique comment ajouter et styliser du texte dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'insertion de texte simple, la disposition des paragraphes, les hyperliens, le texte de droite à gauche, le style des polices, la transparence, les bordures, les fragments HTML et LaTeX, le texte dégradé et les polices personnalisées chargées à partir de fichiers ou de flux.
---
Aspose.PDF pour Java prend en charge l'insertion de texte brut, la mise en page avancée, le style, les dégradés, HTML, LaTeX et les polices personnalisées.


## 
Ajouter un simple fragment de texte



Utilisez cet exemple lorsqu'une courte chaîne de texte doit être placée à des coordonnées de page fixes.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TextFragment` et définissez sa position.
1. Ajoutez-le à la page et enregistrez le document.


```java
public static void addTextSimpleCase(Path outputFile) {
      try (Document document = new Document()) {
          Page page = document.getPages().add();

          TextFragment textFragment = new TextFragment("Hello, Aspose!");
          textFragment.setPosition(new Position(100, 600));

          page.getParagraphs().add(textFragment);
          document.save(outputFile.toString());
      }
  }
```

## 
Ajouter un paragraphe à l'intérieur d'un rectangle



Utilisez cet exemple lorsqu’un bloc de texte plus grand doit être placé à l’intérieur d’une zone délimitée.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Chargez le texte source et configurez un rectangle `TextParagraph` et un mode d'habillage.
1. Ajoutez le fragment via `TextBuilder` et enregistrez le PDF.


```java
public static void addParagraph(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setFirstLineIndent(20);
        paragraph.setRectangle(new Rectangle(80, 800, 400, 200, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.DiscretionaryHyphenation);

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des paragraphes avec différents paramètres de retrait



Utilisez cet exemple lorsque la première ligne et les lignes suivantes doivent utiliser des règles d'indentation différentes.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Préparez le fragment de texte partagé et créez plusieurs objets `TextParagraph`.
1. Configurez l'indentation pour chaque paragraphe, ajoutez-les et enregistrez le document.


```java
public static void addParagraphsIndents(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph1 = new TextParagraph();
        paragraph1.setFirstLineIndent(20);
        paragraph1.setRectangle(new Rectangle(80, 800, 300, 50, true));
        paragraph1.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph1.appendLine(fragment);
        builder.appendParagraph(paragraph1);

        TextParagraph paragraph2 = new TextParagraph();
        paragraph2.setSubsequentLinesIndent(20);
        paragraph2.setRectangle(new Rectangle(320, 800, 500, 50, true));
        paragraph2.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph2.appendLine(fragment);
        builder.appendParagraph(paragraph2);

        document.save(outputFile.toString());
    }
}
```

## 
Insérer du texte avec un saut de ligne manuel



Utilisez cet exemple lorsqu'un fragment de texte doit contenir une nouvelle ligne explicite.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TextFragment` contenant un saut de ligne et configurez son style.
1. Ajoutez-le via un `TextParagraph` et enregistrez le PDF.


```java
public static void addNewLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());

        TextParagraph paragraph = new TextParagraph();
        paragraph.appendLine(textFragment);
        paragraph.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 
Inspecter les sauts de ligne détectés



Utilisez cet exemple lorsque vous devez examiner la sortie de notification liée à la mise en page du texte et au retour à la ligne.


1. 
Créez un nouveau document PDF et activez la journalisation des notifications.

1. 
Ajoutez plusieurs longs fragments de texte à la page.
1. Inspectez les notifications et enregistrez le document.


```java
public static void determineLineBreak(Path outputFile) {
    try (Document document = new Document()) {
        document.setEnableNotificationLogging(true);

        Page page = document.getPages().add();
        for (int i = 0; i < 4; i++) {
            TextFragment text = new TextFragment(
                    "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
                            + "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                            + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                            + "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                            + "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
                            + "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                            + "culpa qui officia deserunt mollit anim id est laborum.");
            text.getTextState().setFontSize(20);
            page.getParagraphs().add(text);
        }

        System.out.println(document.getPages().get_Item(1).getNotifications());
        document.save(outputFile.toString());
    }
}
```

## 
Mesurer dynamiquement la largeur du texte



Utilisez cet exemple lorsque les largeurs de caractères et de chaînes doivent être mesurées avant que les décisions de mise en page ne soient prises.


1. 
Résolvez la police cible et créez un `TextState`.

1. 
Mesurez les caractères et comparez les résultats des API d’état de police et de texte.
1. Affichez toutes les incohérences pour validation.


```java
public static void getTextWidthDynamically(Path outputFile) {
    Font font = FontRepository.findFont("Arial");
    TextState textState = new TextState();
    textState.setFont(font);
    textState.setFontSize(14);

    if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    if (Math.abs(textState.measureString("z") - 7.0) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++) {
        double fontMeasure = font.measureString(String.valueOf(c), 14);
        double textStateMeasure = textState.measureString(String.valueOf(c));
        if (Math.abs(fontMeasure - textStateMeasure) > 0.001) {
            System.out.println("Font and state string measuring doesn't match!");
        }
    }
}
```

## 
Ajouter du texte avec un segment de lien hypertexte



Utilisez cet exemple lorsqu'une partie d'un fragment de texte doit se comporter comme un lien Web.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TextFragment` avec plusieurs objets `TextSegment`.
1. Attribuez un lien hypertexte et un style au segment cible, puis enregistrez le document.


```java
public static void addTextWithHyperlink(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Sample Text Fragment");
        fragment.getSegments().add(new TextSegment(" ... Text Segment 1..."));

        TextSegment segment = new TextSegment("Link to Aspose");
        fragment.getSegments().add(segment);
        segment.setHyperlink(new WebHyperlink("https://products.aspose.com/pdf"));
        segment.getTextState().setForegroundColor(Color.getBlue());
        segment.getTextState().setFontStyle(FontStyles.Italic);

        fragment.getSegments().add(new TextSegment("TextSegment without hyperlink"));

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter du texte de droite à gauche



Utilisez cet exemple lorsque le document doit afficher le contenu du script de droite à gauche avec un alignement approprié.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TextFragment` avec le texte RTL cible et configurez sa police et son alignement.
1. Ajoutez-le à la page et enregistrez le PDF.


```java
public static void addTextWithRtlText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment(
                "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية.");
        textFragment.getTextState().setFont(FontRepository.findFont("Tahoma"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.setHorizontalAlignment(HorizontalAlignment.Right);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Ajoutez du texte stylisé et des segments de type formule



Utilisez cet exemple lorsque du texte normal et des segments de type indice doivent utiliser différents états de texte dans une seule sortie.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Construisez le fragment stylisé principal et composez la formule avec des segments auxiliaires.
1. Ajoutez les deux fragments à la page et enregistrez le document.


```java
public static void addTextWithFontStyling(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment formula = new TextFragment();
        TextFragment textFragment = new TextFragment("Hello, Aspose!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textFragment.getTextState().setUnderline(true);
        textFragment.setHorizontalAlignment(HorizontalAlignment.Left);

        TextState textStateLetters = new TextState();
        textStateLetters.setFont(FontRepository.findFont("Arial"));
        textStateLetters.setFontSize(14);
        textStateLetters.setForegroundColor(Color.getBlue());
        textStateLetters.setFontStyle(FontStyles.Bold);

        TextState textStateIndex = new TextState();
        textStateIndex.setFont(FontRepository.findFont("Arial"));
        textStateIndex.setFontSize(14);
        textStateIndex.setForegroundColor(Color.getDarkRed());
        textStateIndex.setSubscript(true);

        Position position = new Position(100, 500);
        addSegment(formula, "S = a", textStateLetters, position);
        addSegment(formula, "2n", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+1", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+2", textStateIndex, position);
        formula.setHorizontalAlignment(HorizontalAlignment.Left);

        page.getParagraphs().add(textFragment);
        page.getParagraphs().add(formula);
        document.save(outputFile.toString());
    }
}

private static void addSegment(TextFragment formula, String text, TextState state, Position position) {
    TextSegment segment = new TextSegment(text);
    segment.setTextState(state);
    segment.setPosition(position);
    formula.getSegments().add(segment);
}
```

## 
Ajouter du texte souligné



Utilisez cet exemple lorsqu'un fragment de texte doit visiblement utiliser le style souligné.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez le fragment de texte, configurez sa police et son état de soulignement, et définissez sa position.
1. Ajoutez-le avec `TextBuilder` et enregistrez le résultat.


```java
public static void addUnderlineText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextBuilder textBuilder = new TextBuilder(page);

        TextFragment fragment = new TextFragment("Hello, ASPOSE.PDF!");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(10);
        fragment.getTextState().setUnderline(true);
        fragment.setPosition(new Position(10, 800));
        textBuilder.appendText(fragment);

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter du texte transparent sur une forme colorée



Utilisez cet exemple lorsque le texte doit apparaître en transparence au-dessus d'un graphique d'arrière-plan.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Dessinez la forme d'arrière-plan et créez un fragment de texte semi-transparent.
1. Ajoutez les deux éléments à la page et enregistrez le document.


```java
public static void addTextTransparent(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph canvas = new com.aspose.pdf.drawing.Graph(100.0, 400.0);
        com.aspose.pdf.drawing.Rectangle rectangle = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
        rectangle.getGraphInfo().setFillColor(Color.fromArgb(128, 0xC5, 0xB5, 0xFF));
        canvas.getShapes().addItem(rectangle);
        canvas.setChangePosition(false);
        page.getParagraphs().add(canvas);

        TextFragment text = new TextFragment(
                "This is the transparent text. This is the transparent text. This is the transparent text.");
        text.getTextState().setForegroundColor(Color.fromArgb(30, 0, 255, 0));
        page.getParagraphs().add(text);

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter du texte invisible



Utilisez cet exemple lorsque du texte consultable ou masqué doit être présent sans rendu visible.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Ajoutez un fragment de texte visible et un deuxième fragment avec le drapeau invisible activé.
1. Enregistrez le document.


```java
public static void addTextInvisible(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text1 = new TextFragment(
            "This is the visible text. This is the visible text. This is the visible text.");
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment(
            "This is the invisible text. This is the invisible text. This is the invisible text.");
        text2.getTextState().setInvisible(true);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter du texte avec une bordure rectangulaire



Utilisez cet exemple lorsque le texte doit être dessiné avec son rectangle englobant.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un style `TextFragment` et activez le dessin de la bordure du rectangle de texte.
1. Ajoutez-le avec `TextBuilder` et enregistrez le PDF.


```java
public static void addTextBorder(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample text with border.");
        textFragment.setPosition(new Position(10, 700));
        textFragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrokingColor(Color.getDarkRed());
        textFragment.getTextState().setDrawTextRectangleBorder(true);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter du texte barré



Utilisez cet exemple lorsque le texte doit utiliser un formatage barré.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un fragment de texte stylisé avec le barré activé.
1. Ajoutez-le à la page et enregistrez le document.


```java
public static void addStrikeoutText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample strikeout text.");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrikeOut(true);
        textFragment.getTextState().setFontStyle(FontStyles.Bold);
        textFragment.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## 
Appliquer un ombrage dégradé axial au texte



Utilisez cet exemple lorsque le texte doit utiliser un remplissage en dégradé linéaire au lieu d'une couleur unie.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez le fragment de texte et attribuez un dégradé axial à sa couleur de premier plan.
1. Ajoutez-le à la page et enregistrez le PDF.


```java
public static void applyGradientAxialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Appliquer un ombrage dégradé radial au texte



Utilisez cet exemple lorsque le texte doit utiliser un remplissage en dégradé radial.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez le fragment de texte et attribuez un dégradé radial à sa couleur de premier plan.
1. Ajoutez-le à la page et enregistrez le document.


```java
public static void applyGradientRadialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter du texte au format HTML en ligne



Utilisez cet exemple lorsque le formatage en exposant et en indice doit être inséré via le balisage HTML.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `HtmlFragment` avec le balisage en ligne requis.
1. Ajoutez-le à la page et enregistrez le PDF.


```java
public static void addTextHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        HtmlFragment textFragment = new HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un fragment de texte LaTeX



Utilisez cet exemple lorsque le contenu mathématique ou au format TeX doit être rendu dans le PDF.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Créez un `TeXFragment` avec l'expression requise.
1. Ajoutez-le à la page et enregistrez le document.


```java
public static void addTextLatexFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TeXFragment textFragment = new TeXFragment(
                "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un fragment HTML riche



Utilisez cet exemple lorsque la page doit afficher du contenu HTML structuré tel que des titres, des paragraphes et des liens.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Préparez la chaîne de contenu HTML et créez un `HtmlFragment`.
1. Ajoutez-le à la page et enregistrez le PDF.


```java
public static void addHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un fragment HTML avec un état de texte remplacé



Utilisez cet exemple lorsque le contenu HTML importé doit hériter d’une configuration de police et de couleur contrôlée.


1. 
Créez un nouveau document PDF et ajoutez une page.

1. 
Préparez le contenu HTML et créez le `HtmlFragment`.
1. Attribuez un `TextState` personnalisé, ajoutez le fragment et enregistrez le document.


```java
public static void addHtmlFragmentOverrideTextState(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        TextState textState = new TextState();
        textState.setFont(FontRepository.findFont("Arial"));
        textState.setFontSize(14);
        textState.setForegroundColor(Color.getRed());
        htmlFragment.setTextState(textState);

        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Utiliser une police personnalisée chargée à partir d'un fichier



Utilisez cet exemple lorsque le texte doit utiliser une police chargée directement à partir d’un chemin de fichier de police.


1. 
Résolvez le chemin du fichier de police personnalisé.

1. 
Créez un fragment de texte et chargez la police via `FontRepository.openFont`.
1. Appliquez les paramètres de police et enregistrez le document.


```java
public static void useCustomFontFromFile(Path outputFile) {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Hello, Aspose!");
        fragment.setPosition(new Position(100, 600));
        fragment.getTextState().setFont(FontRepository.openFont(fontPath.toString()));
        fragment.getTextState().setFontSize(24);
        fragment.getTextState().setForegroundColor(Color.getBlue());
        fragment.getTextState().setFontStyle(FontStyles.Italic);

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## 
Utiliser une police personnalisée chargée à partir d'un flux



Utilisez cet exemple lorsqu'une police personnalisée doit être ouverte à partir d'un flux et intégrée dans le PDF.


1. 
Ouvrez le fichier de police sous forme de flux et chargez-le avec `FontRepository`.

1. 
Créez le fragment de texte et attribuez la police intégrée.
1. Ajoutez le fragment à la page et enregistrez le document.

```java
public static void useCustomFontFromStream(Path outputFile) throws Exception {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (InputStream fontStream = Files.newInputStream(fontPath)) {
        Font font = FontRepository.openFont(fontStream, FontTypes.OTF);
        font.setEmbedded(true);

        try (Document document = new Document()) {
            Page page = document.getPages().add();

            TextFragment fragment = new TextFragment("Hello, Aspose!");
            fragment.setPosition(new Position(100, 600));
            fragment.getTextState().setFont(font);
            fragment.getTextState().setFontSize(14);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setFontStyle(FontStyles.Italic);

            page.getParagraphs().add(fragment);
            document.save(outputFile.toString());
        }
    }
}
```
