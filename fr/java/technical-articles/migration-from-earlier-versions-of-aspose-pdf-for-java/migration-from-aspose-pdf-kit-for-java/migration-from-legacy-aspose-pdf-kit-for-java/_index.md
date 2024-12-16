---
title: Migration depuis Aspose.Pdf.Kit pour Java hérité
type: docs
weight: 10
url: /fr/java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Le composant actuel Aspose.PDF.Kit pour Java fournissait les fonctionnalités pour manipuler les fichiers PDF existants. Cependant, ce composant sera bientôt abandonné en tant que produit distinct car nous avons transféré toutes ses classes et énumérations sous le package **com.aspose.pdf.facades** de la nouvelle version autoportée d'Aspose.PDF pour Java (4.x.x). Désormais, cette seule version autoportée offre la possibilité de créer ainsi que de manipuler des fichiers PDF existants.

{{% /alert %}}

## Support pour le code hérité

Pendant toute l'activité de migration, nous avons définitivement pris en compte l'impact de cette activité sur les clients existants et nous avons fait de notre mieux pour minimiser cet impact autant que possible.
 En outre, nous nous sommes également concentrés sur la compatibilité ascendante de la nouvelle version autoportée afin que la base de code des clients existants nécessite des changements minimes. Bien que la nouvelle version autoportée fournisse le Document Object Model (DOM) sous le package com.aspose.pdf pour créer et manipuler des fichiers PDF existants, si vous souhaitez continuer à utiliser votre code hérité développé avec Aspose.PDF.Kit pour Java, vous n'avez qu'à importer le package **com.aspose.pdf.facades** et votre code devrait fonctionner (*sauf pour la mise à jour des références de classe explicites*).

L'extrait de code suivant vous montre comment exécuter votre code existant Aspose.PDF.Kit pour Java avec le nouveau Aspose.PDF autoporté pour Java.

```java

 import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // charger un fichier PDF existant

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("TITRE: " + fileInfo.getTitle());

            System.out.println("AUTEUR:" + fileInfo.getAuthor());

            System.out.println("DATE DE CRÉATION:" + fileInfo.getCreationDate());

            System.out.println("CRÉATEUR:" + fileInfo.getCreator());

            System.out.println("MOTS CLÉS:" + fileInfo.getKeywords());

            System.out.println("DATE DE MODIFICATION:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## Utilisation de la classe ReplaceTextStrategy

Afin de migrer le code pour la classe ReplaceTextStrategy, la méthode **setScope(..)** a été mise à jour en **setReplaceScope(..)**. Veuillez consulter l'extrait de code suivant.

```java

 // instancier l'objet PdfContentEditor

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// lier le fichier PDF source

editor.bindPdf("input.pdf");

// créer une stratégie de remplacement de texte

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// définir l'alignement pour le remplacement de texte

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// définir le champ d'application pour le remplacement de texte

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// définir la stratégie de remplacement

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test","replaced");

// enregistrer le fichier mis à jour

editor.save("TxtReplaceTest.pdf");
```