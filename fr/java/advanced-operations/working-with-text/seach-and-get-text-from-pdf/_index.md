---
title: Rechercher et Obtenir du Texte à partir des Pages d'un Document PDF
linktitle: Rechercher et Obtenir du Texte
type: docs
weight: 60
url: fr/java/search-and-get-text-from-pdf/
description: Cet article explique comment utiliser divers outils pour rechercher et obtenir du texte à partir de documents PDF. Nous pouvons rechercher avec une expression régulière à partir de pages particulières ou de l'ensemble des pages.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Rechercher et Obtenir du Texte à partir de Toutes les Pages d'un Document PDF

TextFragmentAbsorber vous permet de trouver du texte, correspondant à une phrase particulière, à partir de toutes les pages d'un document PDF.

Pour rechercher du texte dans l'ensemble du document, appelez la méthode accept() de la collection [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 Le [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) méthode prend un objet TextFragmentAbsorber comme paramètre, qui renvoie une collection d'objets TextFragment. Parcourez tous les fragments pour obtenir leurs propriétés, par exemple Texte, Position, XIndent, YIndent, NomPolice, TaillePolice, EstAccessible, EstIntégré, EstSous-ensemble, CouleurPremierPlan, etc.

Le snippet de code suivant montre comment rechercher dans l'ensemble du document et afficher toutes les correspondances dans une console.

```java
// Ouvrir le document
Document pdfDocument = new Document("input.pdf");

// Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Accepter l'absorbeur pour toutes les pages
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obtenir les fragments de texte extraits dans la collection
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Parcourir les fragments
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Texte :- " + textFragment.getText());
    System.out.println("Position :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Police - Nom :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Police - EstAccessible :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Police - EstIntégré - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Police - EstSous-ensemble :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Taille de police :- " + textFragment.getTextState().getFontSize());
    System.out.println("Couleur du premier plan :- " + textFragment.getTextState().getForegroundColor());
}
```

Pour rechercher du texte sur une page particulière et obtenir les propriétés qui lui sont associées, fournissez l'index de la page :

```java
// Accepter l'absorbeur pour la première page du document
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Rechercher et obtenir des segments de texte à partir des pages du PDF

Pour rechercher des segments de texte sur toutes les pages d'un document, obtenez les objets TextFragment d'un document.

TextFragmentAbsorber vous permet de trouver du texte, correspondant à une phrase particulière, sur toutes les pages d'un document PDF. Pour rechercher du texte dans l'ensemble du document, appelez la méthode [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) de la collection [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection). La méthode [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) prend un objet TextFragmentAbsorber en paramètre, qui renvoie une collection d'objets TextFragment.

{{% alert color="primary" %}}

Lorsque la collection TextFragmentCollection a été récupérée du document, parcourez-la pour obtenir la collection TextSegmentCollection de chaque objet TextFragment.
 Après cela, vous pouvez obtenir les propriétés de l'objet TextSegment individuel.

{{% /alert %}}

Le fragment de code suivant montre comment rechercher des segments de texte sur toutes les pages.

```java
// Ouvrir le document
Document pdfDocument = new Document("input.pdf");

// Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche entrée
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Accepter l'absorbeur pour la première page du document
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obtenir les fragments de texte extraits dans la collection
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Boucle à travers les fragments de texte
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // Itérer à travers les segments de texte
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("Texte :- " + textSegment.getText());
        System.out.println("Position :- " + textSegment.getPosition());
        System.out.println("XIndent :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndent :- " + textSegment.getPosition().getYIndent());
        System.out.println("Police - Nom :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("Police - EstAccessible :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("Police - EstIntégrée - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("Police - EstSous-ensemble :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("Taille de la police :- " + textSegment.getTextState().getFontSize());
        System.out.println("Couleur de premier plan :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

Pour rechercher un segment de texte spécifique et obtenir les propriétés associées, spécifiez l'index de la page pour la page que vous souhaitez rechercher :

```java
// Accepter l'absorbeur pour la première page du document.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Rechercher et obtenir du texte des pages en utilisant une expression régulière

TextFragmentAbsorber vous aide à rechercher et à récupérer du texte de toutes les pages d'un document, basé sur une expression régulière.

Pour rechercher et obtenir du texte d'un document :

1. Passez le terme de recherche comme une expression régulière au constructeur de TextFragmentAbsorber.
1. Définissez la propriété TextSearchOptions de l'objet TextFragmentAbsorber.
   Cette propriété nécessite un objet TextSearchOptions : passez true à son constructeur lors de la création d'un nouvel objet.
1. Pour récupérer le texte correspondant de toutes les pages, appelez la méthode [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) de la collection [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection).

   TextFragmentAbsorber renvoie un TextFragmentCollection contenant tous les fragments correspondant aux critères spécifiés par l'expression régulière.

Le fragment de code suivant montre comment rechercher toutes les pages d'un document et obtenir du texte basé sur une expression régulière.

```java
// Ouvre un document
Document pdfDocument = new Document("source.pdf");

// Crée un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche saisie
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // comme 1999-2000

// Définit l'option de recherche de texte pour spécifier l'utilisation d'expressions régulières
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// Accepte l'absorbeur pour la première page du document
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obtient les fragments de texte extraits dans la collection
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Parcourt les fragments
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Texte :- " + textFragment.getText());
    System.out.println("Position :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Police - Nom :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Police - EstAccessible :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Police - EstIntégrée - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Police - EstSous-ensemble :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Taille de la police :- " + textFragment.getTextState().getFontSize());
    System.out.println("Couleur de premier plan :- " + textFragment.getTextState().getForegroundColor());
}
```


Pour rechercher du texte sur une page particulière et obtenir ses propriétés, spécifiez l'index de la page :

```java
// Accepter l'absorbeur pour la première page du document.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

Afin de rechercher une chaîne en majuscules ou en minuscules, vous pouvez envisager d'utiliser une expression régulière.

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

Exemple :

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```