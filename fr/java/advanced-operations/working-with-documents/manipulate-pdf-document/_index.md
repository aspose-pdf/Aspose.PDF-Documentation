---
title: Manipuler le document PDF
linktitle: Manipuler le document PDF
type: docs
weight: 30
url: /fr/java/manipulate-pdf-document/
description: Cet article contient des informations sur la façon de valider un document PDF pour la norme PDF A, comment travailler avec le TOC, comment définir la date d'expiration du PDF et comment déterminer la progression de la génération du fichier PDF.
lastmod: "2021-06-05"
---

## Valider le document PDF pour la norme PDF A (A 1A et A 1B)

Pour valider un document PDF pour la compatibilité PDF/A-1a ou PDF/A-1b, utilisez la méthode [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Cette méthode vous permet de spécifier le nom du fichier dans lequel le résultat doit être enregistré et le type de validation requis dans l'énumération [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) : PDF_A_1A ou PDF_A_1B.

Le format de sortie XML est un format personnalisé d'Aspose.
 L'XML contient une collection de balises avec le nom Problem; chaque balise contient les détails d'un problème particulier. L'attribut ObjectID de la balise Problem représente l'ID de l'objet particulier auquel ce problème est lié. L'attribut Clause représente une règle correspondante dans la spécification PDF.

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Valider le PDF pour PDF/A-1a
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // Enregistrer le fichier PDF mis à jour
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## Travailler avec la table des matières

### Ajouter une table des matières à un PDF existant

La classe ListSection dans le package aspose.pdf vous permet de créer une table des matières lors de la création d'un document PDF à partir de zéro. Pour ajouter des titres, qui sont des éléments de la table des matières, utilisez la classe [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading).

Pour ajouter une table des matières à un fichier PDF existant, utilisez la classe [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) dans le package com.aspose.pdf. Le package com.aspose.pdf peut à la fois créer de nouveaux fichiers PDF et manipuler des fichiers PDF existants. Pour ajouter un sommaire à un PDF existant, utilisez le package com.aspose.pdf.

Le code suivant montre comment créer une table des matières dans un fichier PDF existant.

```java
public static void AddTOCtoExistingPDF() {
    // Charger un fichier PDF existant
    Document document = new Document(_dataDir + "sample.pdf");

    // Accéder à la première page du fichier PDF
    Page tocPage = document.getPages().insert(1);

    // Créer un objet pour représenter les informations du sommaire
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("Table des Matières");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // Définir le titre pour le sommaire
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // Créer des objets string qui seront utilisés comme éléments du sommaire
    String[] titles = new String[4];
    titles[0] = "Première page";
    titles[1] = "Deuxième page";
    titles[2] = "Troisième page";
    titles[3] = "Quatrième page";
    for (int i = 0; i < 4; i++) {
      // Créer un objet Heading
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // Spécifier la page de destination pour l'objet heading
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // Page de destination
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // Coordonnée de destination
      segment2.setText(titles[i]);

      // Ajouter le heading à la page contenant le sommaire
      tocPage.getParagraphs().add(heading2);
    }
    // Sauvegarder le document mis à jour
    document.save("TOC_Output_Java.pdf");
  }
```
### Définir différents TabLeaderType pour différents niveaux de TOC

Aspose.PDF permet également de définir différents TabLeaderType pour différents niveaux de TOC. Vous devez définir la propriété LineDash de FormatArray avec la valeur appropriée de l'énumération TabLeaderType comme suit.

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // définir le LeaderType

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("Table Des Matières");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // Ajouter la section de liste à la collection de sections du document Pdf

    tocPage.setTocInfo(tocInfo);

    // Définir le format de la liste à quatre niveaux en définissant les marges de gauche et
    // les paramètres de format de texte de chaque niveau

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // Créer une section dans le document Pdf
    Page page = document.getPages().add();

    // Ajouter quatre titres dans la section
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("Exemple de Titre" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // Ajouter le titre dans la Table Des Matières.
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // enregistrer le PDF
    document.save(outFile);
  }
```

### Masquer les numéros de page dans la table des matières

Dans le cas où vous ne souhaitez pas afficher les numéros de page avec les titres dans la table des matières, vous pouvez utiliser la propriété [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) de la classe [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) comme faux. Veuillez vérifier l'extrait de code suivant pour masquer les numéros de page dans la table des matières :

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // Ajouter la section de liste à la collection de sections du document PDF
    tocPage.setTocInfo(tocInfo);

    // Définir le format de la liste à quatre niveaux en définissant les marges de gauche et
    // les paramètres de format de texte de chaque niveau

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // Ajouter quatre titres dans la section
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("ceci est le titre de niveau " + Level);
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### Personnaliser les numéros de page lors de l'ajout de TOC

Il est courant de personnaliser la numérotation des pages dans la table des matières lors de l'ajout de celle-ci à un document PDF. Par exemple, nous pouvons avoir besoin d'ajouter un préfixe avant le numéro de page comme P1, P2, P3 et ainsi de suite. Dans ce cas, Aspose.PDF pour Java fournit la propriété PageNumbersPrefix de la classe TocInfo qui peut être utilisée pour personnaliser les numéros de page comme montré dans l'exemple de code suivant.

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // Charger un fichier PDF existant
    Document doc = new Document(inFile);
    // Accéder à la première page du fichier PDF
    Page tocPage = doc.getPages().insert(1);
    // Créer un objet pour représenter les informations du TOC
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table des Matières");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // Définir le titre pour le TOC
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // Créer un objet Heading
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // Spécifier la page de destination pour l'objet heading
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // Page de destination
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // Coordonnée de destination
      segment2.setText("Page " + i);
      // Ajouter le heading à la page contenant le TOC
      tocPage.getParagraphs().add(heading2);
    }

    // Enregistrer le document mis à jour
    doc.save(outFile);
  }
```


## Ajouter des Couches au Fichier PDF

Les couches peuvent être utilisées dans les documents PDF de nombreuses manières. Vous pourriez avoir un fichier multilingue que vous souhaitez distribuer et vous souhaitez que le texte dans chaque langue apparaisse sur des couches différentes, avec le design de fond apparaissant sur une couche séparée. Vous pourriez également créer des documents avec une animation qui apparaît sur une couche séparée. Un exemple pourrait être d'ajouter un accord de licence à votre fichier, et vous ne voulez pas qu'un utilisateur voie le contenu avant d'accepter les termes de l'accord.

Aspose.PDF pour Java prend en charge l'ajout de couches aux fichiers PDF.

Pour travailler avec des couches dans des fichiers PDF, utilisez les membres d'API suivants.

La classe [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) représente une couche et contient les propriétés suivantes :

- **Name** – le nom de la couche.
- **Id** – l'ID de la couche.
- **Contents** – une liste d'opérateurs de couche.

Une fois que les objets [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) ont été définis, ajoutez-les à la collection Layers de l'objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 Le code ci-dessous montre comment ajouter des calques à un document PDF.

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "Ligne Rouge");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "Ligne Verte");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "Ligne Bleue");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## Définir l'expiration du PDF

La fonctionnalité d'expiration de PDF définit la durée de validité d'un fichier PDF. À une date particulière, si quelqu'un essaie d'y accéder, une fenêtre pop-up s'affiche, expliquant que le fichier a expiré et qu'il en a besoin d'un nouveau.

Aspose.PDF vous permet de définir l'expiration lors de la création et de l'édition de fichiers PDF.

L'extrait de code ci-dessous montre comment définir la date d'expiration pour un fichier PDF. Vous devez utiliser JavaScript car les fichiers enregistrés par des composants tiers (par exemple OwnerGuard) ne peuvent pas être visualisés sur d'autres stations de travail sans cet utilitaire.

Le fichier PDF peut être créé en utilisant PDF OwnerGuard avec un fichier existant ayant une date d'expiration. Mais le nouveau fichier ne peut être ouvert que sur une station de travail qui a PDF OwnerGuard installé. Les stations de travail sans PDF OwnerGuard afficheront une ExpirationFeatureError. Par exemple, PDF Reader ouvre le fichier si OwnerGuard est installé, mais Adobe Acrobat renvoie une erreur.

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('Le fichier est expiré. Vous avez besoin d'un nouveau.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```