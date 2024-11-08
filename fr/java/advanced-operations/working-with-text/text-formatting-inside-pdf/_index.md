---
title: Formatage du texte dans un PDF
linktitle: Formatage du texte dans un PDF
type: docs
weight: 30
url: /fr/java/text-formatting-inside-pdf/
description: Cette page explique comment formater le texte dans votre fichier PDF. Il s'agit d'ajouter un retrait de ligne, d'ajouter une bordure de texte, de souligner le texte, d'ajouter une bordure autour du texte ajouté, de l'alignement du texte pour le contenu de la boîte flottante, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Comment ajouter un retrait de ligne au PDF

Aspose.PDF pour Java offre la propriété SubsequentLinesIndent dans la classe [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions). Elle peut être utilisée pour spécifier un retrait de ligne dans les scénarios de génération de PDF avec TextFragment et la collection Paragraphs.

Veuillez utiliser l'extrait de code suivant pour utiliser la propriété :

```java
public static void AddLineIndentToPDF() {
        // Créer un nouvel objet document
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux.");

        // Initialiser TextFormattingOptions pour le fragment de texte et spécifier
        // la valeur SubsequentLinesIndent
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Ligne2");
        page.getParagraphs().add(text);

        text = new TextFragment("Ligne3");
        page.getParagraphs().add(text);

        text = new TextFragment("Ligne4");
        page.getParagraphs().add(text);

        text = new TextFragment("Ligne5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## Comment ajouter une bordure de texte

Le code suivant montre comment ajouter une bordure à un texte en utilisant TextBuilder et en définissant la méthode DrawTextRectangleBorder de TextState :

```java
public static void AddTextBorder() {
    // Créer un nouvel objet document
    Document pdfDocument = new Document();
    // Obtenir une page particulière
    Page pdfPage = pdfDocument.getPages().add();
    // Créer un fragment de texte
    TextFragment textFragment = new TextFragment("texte principal");
    textFragment.setPosition(new Position(100, 600));
    // Définir les propriétés du texte
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // Utiliser setStrokingColor pour dessiner une bordure (tracé) autour du rectangle de texte
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // Utiliser la méthode setDrawTextRectangleBorder pour définir la valeur sur true
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // Enregistrer le document
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## Comment ajouter un texte souligné

Le code ci-dessous vous montre comment ajouter un texte souligné lors de la création d'un nouveau fichier PDF.

```java
public static void AddUnderlineText(){
    // Créer un objet de documentation
    Document pdfDocument = new Document();
    // Ajouter une page au document PDF
    Page page = pdfDocument.getPages().add();
    // Créer un TextBuilder pour la première page
    TextBuilder tb = new TextBuilder(page);
    // TextFragment avec texte d'exemple
    TextFragment fragment = new TextFragment("Texte avec décoration soulignée");
    // Définir la police pour TextFragment
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // Définir le formatage du texte comme souligné
    fragment.getTextState().setUnderline(true);
    // Spécifier la position où TextFragment doit être placé
    fragment.setPosition (new Position(10, 800));
    // Ajouter TextFragment au fichier PDF
    tb.appendText(fragment);

    // Enregistrer le document PDF résultant.
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## Comment ajouter une bordure autour du texte ajouté

Vous avez le contrôle sur l'apparence du texte que vous ajoutez. L'exemple ci-dessous montre comment ajouter une bordure autour d'un morceau de texte que vous avez ajouté en dessinant un rectangle autour de celui-ci. Découvrez-en plus sur la classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // Enregistrer le document PDF résultant.
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## Comment ajouter un saut de ligne

TextFragment ne supporte pas le saut de ligne à l'intérieur du texte.
 Cependant, afin d'ajouter du texte avec un saut de ligne, veuillez utiliser TextFragment avec TextParagraph :

- utilisez "\r\n" ou Environment.NewLine dans TextFragment au lieu de "\n" seul ;
- créez un objet TextParagraph. Il ajoutera du texte avec séparation de ligne ;
- ajoutez le TextFragment avec TextParagraph.AppendLine ;
- ajoutez le TextParagraph avec TextBuilder.AppendParagraph.  
Veuillez utiliser l'extrait de code ci-dessous.

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // Initialiser un nouveau TextFragment avec le texte contenant les marqueurs de nouvelle ligne requis
    TextFragment textFragment = new TextFragment("Nom du demandeur : " + System.lineSeparator() + " Joe Smoe");

    // Définir les propriétés du fragment de texte si nécessaire
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // Créer un objet TextParagraph
    TextParagraph par = new TextParagraph();

    // Ajouter un nouveau TextFragment au paragraphe
    par.appendLine(textFragment);

    // Définir la position du paragraphe
    par.setPosition (new Position(100, 600));

    // Créer un objet TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Ajouter le TextParagraph en utilisant TextBuilder
    textBuilder.appendParagraph(par);

    // Enregistrer le document PDF résultant.
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## Comment ajouter du texte barré

La classe TextState offre la possibilité de définir le formatage pour les TextFragments placés à l'intérieur d'un document PDF. Vous pouvez utiliser cette classe pour définir le formatage du texte comme Gras, Italique, Souligné et à partir de cette version, l'API a fourni la capacité de marquer le formatage du texte comme Barré. Veuillez essayer d'utiliser l'extrait de code suivant pour ajouter un TextFragment avec un formatage Barré.

Veuillez utiliser l'extrait de code complet :

```java
public static void AddStrikeOutText(){
    // Ouvrir le document
    Document pdfDocument = new Document();
    // Obtenir une page particulière
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // Créer un fragment de texte
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition (new Position(100, 600));

    // Définir les propriétés du texte
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // utiliser la méthode setStrikeOut pour activer le texte barré
    textFragment.getTextState().setStrikeOut(true);
    // Marquer le texte comme Gras
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // Créer un objet TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Ajouter le fragment de texte à la page PDF
    textBuilder.appendText(textFragment);

    // Enregistrer le document PDF résultant.
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## Appliquer un Ombrage en Dégradé au Texte

Le formatage du texte a été davantage amélioré dans l'API pour les scénarios d'édition de texte et vous pouvez maintenant ajouter du texte avec un espace colorimétrique à motifs dans le document PDF. La classe com.aspose.pdf.Color a été encore améliorée en introduisant de nouvelles méthodes `setPatternColorSpace`, qui peuvent être utilisées pour spécifier des couleurs d'ombrage pour le texte. Cette nouvelle méthode ajoute différents ombrages en dégradé au texte, par exemple l'ombrage axial, l'ombrage radial (Type 3) comme montré dans l'extrait de code suivant :

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // Créer une nouvelle couleur avec un espace colorimétrique à motifs
    textFragment.getTextState().setForegroundColor(foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


Pour appliquer un dégradé radial, vous pouvez utiliser la méthode `setPatternColorSpace` égale à `GradientRadialShading(startingColor, endingColor)` dans l'extrait de code ci-dessus.

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // Créer une nouvelle couleur avec un espace colorimétrique de motif
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## Comment aligner le texte par rapport au contenu flottant

Aspose.PDF prend en charge le réglage de l'alignement du texte pour les contenus à l'intérieur d'un élément de boîte flottante.
 Les propriétés d'alignement de l'instance Aspose.Pdf.FloatingBox peuvent être utilisées pour réaliser cela comme montré dans l'exemple de code suivant.

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center);
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top);
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf");        
}
```