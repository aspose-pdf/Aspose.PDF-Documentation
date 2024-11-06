---
title: Remplacer le texte dans un PDF
linktitle: Remplacer le texte dans un PDF
type: docs
weight: 40
url: fr/java/replace-text-in-a-pdf-document/
description: En savoir plus sur les différentes manières de remplacer et supprimer du texte d'un PDF. Aspose.PDF permet de remplacer du texte dans une région particulière ou avec une expression régulière.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Remplacer le texte sur toutes les pages d'un document PDF

{{% alert color="primary" %}}

Vous pouvez essayer de trouver et remplacer le texte dans le document en utilisant Aspose.PDF et obtenir les résultats en ligne à ce [lien](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Pour remplacer le texte sur toutes les pages d'un document PDF en utilisant [Aspose.PDF for Java](https://products.aspose.com/pdf/java):

1. Utilisez d'abord [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) pour trouver la phrase particulière à remplacer.

1. Ensuite, parcourez tous les [TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--) pour remplacer le texte et modifier d'autres attributs.

1. Enfin, enregistrez le PDF de sortie en utilisant la méthode [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) de la classe Document.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche saisie
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // Accepter l'absorbeur pour la première page du document
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // Obtenir les fragments de texte extraits dans une collection
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // Parcourir les fragments
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // Mettre à jour le texte et d'autres propriétés
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // Enregistrer le fichier PDF mis à jour
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## Remplacer le texte dans une région particulière de la page

Pour remplacer le texte dans une région particulière de la page, nous devons d'abord instancier l'objet TextFragmentAbsorber, spécifier la région de la page en utilisant [TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-) puis parcourir tous les TextFragments pour remplacer le texte. Une fois ces opérations terminées, nous avons seulement besoin de sauvegarder le PDF de sortie en utilisant la méthode save de l'objet Document.

Le code suivant vous montre comment remplacer le texte dans toutes les pages d'un document PDF.

```java
public static void ReplaceTextInParticularRegion(){
    // charger le fichier PDF
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // instancier l'objet TextFragment Absorber
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // rechercher le texte dans les limites de la page
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // spécifier la région de la page pour les options de recherche de texte
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // rechercher le texte de la première page du fichier PDF
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // parcourir chaque TextFragment
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // remplacer le texte par "---"
        tf.setText("---");
    }

    // Enregistrer le fichier PDF mis à jour
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## Remplacer le texte basé sur une expression régulière

Si vous voulez remplacer certaines phrases basées sur une expression régulière, vous devez d'abord trouver toutes les phrases correspondant à cette expression régulière particulière en utilisant TextFragmentAbsorber. Vous devrez passer l'expression régulière en tant que paramètre au constructeur de TextFragmentAbsorber. Vous devez également créer un objet TextSearchOptions qui spécifie si l'expression régulière est utilisée ou non. Une fois que vous avez les phrases correspondantes dans TextFragments, vous devez les parcourir toutes et les mettre à jour selon vos besoins. Enfin, vous devez enregistrer le PDF mis à jour en utilisant la méthode Save de l'objet Document.

Le code suivant vous montre comment remplacer du texte basé sur une expression régulière.

```java
public static void ReplaceTextWithRegularExpression() {
    // charger le fichier PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Créez un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // comme 1999-2000

    // Définir l'option de recherche de texte pour spécifier l'utilisation des expressions régulières
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // Accepter l'absorbeur pour la première page du document
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obtenez les fragments de texte extraits dans la collection
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Parcourir les fragments
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Mettre à jour le texte et autres propriétés
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // Enregistrer le fichier PDF mis à jour
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## Remplacer les polices dans un fichier PDF existant

Aspose.PDF pour Java prend en charge la capacité de remplacer le texte dans un document PDF. Cependant, parfois, vous avez besoin de remplacer uniquement la police utilisée dans le document PDF. Ainsi, au lieu de remplacer le texte, seule la police utilisée est remplacée. L'une des surcharges du constructeur TextFragmentAbsorber accepte un objet TextEditOptions comme argument et nous pouvons utiliser la valeur RemoveUnusedFonts de l'énumération TextEditOptions.FontReplace pour répondre à nos besoins.

Le code suivant montre comment remplacer la police dans un document PDF.

```java
public static void ReplaceFonts() {
    // Instancier l'objet Document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Rechercher des fragments de texte et définir l'option d'édition pour supprimer les polices inutilisées
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // Accepter l'absorbeur pour toutes les pages du document
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // parcourir tous les TextFragments
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // si le nom de la police est ArialMT, remplacer le nom de la police par Arial
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // Enregistrer le fichier PDF mis à jour
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### Utiliser une Police Non-Anglaise (Japonais) Lors du Remplacement de Texte

Le code suivant montre comment remplacer du texte par des caractères japonais. Veuillez noter que pour ajouter du texte japonais, vous devez utiliser une police qui prend en charge les caractères japonais (par exemple MSGothic).

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // Instancier un objet Document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Changeons chaque mot "page" par du texte japonais avec une police spécifique
    // TakaoMincho qui peut être installée dans le système
    // De plus, il peut s'agir d'une autre police qui prend en charge les hiéroglyphes
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // Créer une instance des options de recherche de texte
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // Accepter l'absorbeur pour toutes les pages du document
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obtenir les fragments de texte extraits dans une collection
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // Parcourir les fragments
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Mettre à jour le texte et d'autres propriétés
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // Enregistrer le document mis à jour
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## Le remplacement de texte doit réorganiser automatiquement le contenu de la page

Aspose.PDF pour Java prend en charge la fonctionnalité de recherche et de remplacement de texte dans le fichier PDF. Cependant, récemment, certains clients ont rencontré des problèmes lors du remplacement de texte lorsqu'un TextFragment particulier est remplacé par un contenu plus petit et que des espaces supplémentaires sont affichés dans le PDF résultant ou dans le cas où le TextFragment est remplacé par une chaîne plus longue, les mots se chevauchent avec le contenu existant de la page. Donc, la nécessité était d'introduire un mécanisme pour que, une fois le texte d'un document PDF remplacé, le contenu soit réorganisé.

Afin de répondre aux scénarios mentionnés ci-dessus, Aspose.PDF pour Java a été amélioré de sorte qu'aucun problème de ce type n'apparaisse lors du remplacement de texte dans le fichier PDF. Le code suivant montre comment remplacer du texte dans le fichier PDF et le contenu de la page doit être réorganisé automatiquement.

```java
public static void RearrangeContent() {
    // Charger le fichier PDF source
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Créer un objet TextFragment Absorber avec une expression régulière
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    //Vous pouvez également spécifier l'option ReplaceAdjustment.WholeWordsHyphenation pour envelopper le texte sur la ligne suivante ou actuelle
    //si la ligne actuelle devient trop longue ou courte après le remplacement :
    //textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // Accepter l'absorbeur pour toutes les pages du document
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obtenir les fragments de texte extraits dans la collection
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Remplacer chaque TextFragment
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Définir la police du fragment de texte à remplacer
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // Définir la taille de la police
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // Remplacer le texte par une chaîne plus longue que l'espace réservé
        textFragment.setText("Ceci est une chaîne plus longue pour le test de cette fonctionnalité");
    }
    // Enregistrer le PDF résultant
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## Rendu des symboles remplaçables lors de la création de PDF

Les symboles remplaçables sont des symboles spéciaux dans une chaîne de texte qui peuvent être remplacés par le contenu correspondant lors de l'exécution. Les symboles remplaçables actuellement pris en charge par le nouveau modèle objet de document du namespace Aspose.PDF sont `$P`, `$p,` `\n`, `\r`. Les symboles `$p` et `$P` sont utilisés pour gérer la numérotation des pages lors de l'exécution. `$p` est remplacé par le numéro de la page où se trouve la classe actuelle de paragraphe. `$P` est remplacé par le nombre total de pages dans le document. Lors de l'ajout de [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) à la collection de paragraphes des documents PDF, il ne prend pas en charge le saut de ligne à l'intérieur du texte. Cependant, afin d'ajouter du texte avec un saut de ligne, veuillez utiliser [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) avec [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph) :

- utilisez "\r\n" ou Environment.NewLine dans TextFragment au lieu d'un simple "\n" ;
- créez un objet TextParagraph.
 Il ajoutera du texte avec une séparation de ligne ;
- ajouter le TextFragment avec TextParagraph.AppendLine ;
- ajouter le TextParagraph avec TextBuilder.AppendParagraph.

```java
public static void RenderingReplaceableSymbols() {
    // charger le fichier PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // Initialiser un nouveau TextFragment avec du texte contenant les marqueurs de nouvelle ligne requis
    TextFragment textFragment = new TextFragment("Nom du demandeur : " + System.lineSeparator() + " Joe Smoe");

    // Définir les propriétés du fragment de texte si nécessaire
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

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

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## Symboles remplaçables dans la zone d'en-tête/pied de page

Les symboles remplaçables peuvent également être placés à l'intérieur de la section En-tête/Pied de page d'un fichier PDF. Veuillez consulter l'extrait de code suivant pour plus de détails sur la façon d'ajouter un symbole remplaçable dans la section de pied de page.

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // Assigner l'instance marginInfo à la propriété Margin de sec1.PageInfo
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // Instancier un paragraphe de texte qui stockera le contenu à afficher comme en-tête
    TextFragment t1 = new TextFragment("titre du rapport");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("Nom_Rapport");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // Créer un objet HeaderFooter pour la section
    HeaderFooter hfFoot = new HeaderFooter();

    // Définir l'objet HeaderFooter sur pied de page impair et pair
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // Ajouter un paragraphe de texte contenant le numéro de page actuel sur le nombre total de pages
    TextFragment t3 = new TextFragment("Généré à la date du test");
    TextFragment t4 = new TextFragment("nom du rapport ");
    TextFragment t5 = new TextFragment("Page $p de $P");

    // Instancier un objet Table
    Table tab2 = new Table();

    // Ajouter le tableau dans la collection de paragraphes de la section souhaitée
    hfFoot.getParagraphs().add(tab2);

    // Définir les largeurs de colonnes du tableau
    tab2.setColumnWidths("165 172 165");

    // Créer des rangées dans le tableau puis des cellules dans les rangées
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // Définir l'alignement vertical du texte comme aligné au centre
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // Ajouter le tableau dans la collection de paragraphes de la section souhaitée
    page.getParagraphs().add(table);

    // Définir la bordure par défaut de la cellule à l'aide de l'objet BorderInfo
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // Définir la bordure du tableau à l'aide d'un autre objet BorderInfo personnalisé
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // Créer des rangées dans le tableau puis des cellules dans les rangées
    Row row1 = table.getRows().add();

    row1.getCells().add("col1");
    row1.getCells().add("col2");
    row1.getCells().add("col3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Java est une compilation de chaque composant Java offert par Aspose. Elle est compilée sur une"
                                + CRLF
                                + "base quotidienne pour s'assurer qu'elle contient les versions les plus récentes de chacun de nos composants Java. "
                                + CRLF
                                + "base quotidienne pour s'assurer qu'elle contient les versions les plus récentes de chacun de nos composants Java. "
                                + CRLF
                                + "En utilisant Aspose.Total for Java, les développeurs peuvent créer une large gamme d'applications.");
            else
                c1 = row.getCells().add("élément1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## Supprimer tout le texte du document PDF

### Supprimer tout le texte en utilisant des opérateurs

Dans certaines opérations sur le texte, vous devez supprimer tout le texte du document PDF et pour cela, vous devez généralement définir le texte trouvé comme une chaîne vide. Le point est que changer le texte pour une multitude de fragments de texte entraîne un certain nombre de vérifications et d'opérations d'ajustement de position du texte. Elles sont essentielles dans les scénarios d'édition de texte. La difficulté est que vous ne pouvez pas déterminer combien de fragments de texte seront supprimés dans le scénario où ils sont traités dans une boucle.

Par conséquent, nous recommandons d'utiliser une autre approche pour le scénario de suppression de tout le texte des pages PDF. Veuillez considérer l'extrait de code suivant qui fonctionne très rapidement.

```java
public static void RemoveAllTextUsingOperators() {
    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Boucle à travers toutes les pages du document PDF
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // Sélectionner tout le texte sur la page
        page.getContents().accept(operatorSelector);
        // Supprimer tout le texte
        page.getContents().delete(operatorSelector.getSelected());
    }
    // Enregistrer le document
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```