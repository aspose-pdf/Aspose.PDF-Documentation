---
title: Migration de votre code vers Aspose.PDF pour Java 2.5.0
type: docs
weight: 10
url: /java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Dans cet article, nous avons essayé de mettre en évidence certaines des zones d'un code existant d'Aspose.PDF pour Java afin de le rendre compatible avec la dernière version publiée.

{{% /alert %}}

## Détails

Avec la sortie d'Aspose.PDF pour Java 2.5.0, il y a eu de nombreux changements dans la structure de l'API et la construction des classes. La plupart des noms des membres de classe ont été mis à jour, certains membres de classe existants ont été supprimés et quelques méthodes et propriétés supplémentaires ont été ajoutées aux classes existantes. Juste pour vous donner un bref aperçu des changements, nous allons examiner le code simple suivant, basé sur les versions d'Aspose.PDF pour Java publiées avant la 2.5.0.

Dans ce code simple, nous allons ajouter un hyperlien et un lien vers la page dans le même document PDF.

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}


//Instancier un objet Pdf en appelant son constructeur vide

Pdf pdf1 = new Pdf();

//Créer une section dans l'objet Pdf

Section sec1 = pdf1.getSections().add();

//Créer un paragraphe de texte avec la référence d'une section

Text text1 = new Text(sec1);

//Ajouter le paragraphe de texte dans la collection de paragraphes de la section

sec1.getParagraphs().add(text1);

//Ajouter un segment de texte dans le paragraphe de texte

Segment segment1 = text1.getSegments().add("ceci est un lien local");

//Définir le texte dans le segment de texte pour être souligné

segment1.getTextInfo().setUnderLine(true);


//Définir le type de lien du segment de texte sur Local

//Attribuer l'ID du paragraphe souhaité comme ID cible pour le segment de texte

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

//Créer un paragraphe de texte à lier avec le segment de texte

Text text3 = new Text(sec1, "informations sur le produit 1 ...");

//Ajouter le paragraphe de texte à la collection de paragraphes de la section

sec1.getParagraphs().add(text3);

//Définir ce paragraphe comme le premier afin qu'il puisse être affiché dans une page séparée

//dans le document

text3.setFirstParagraph(true);

//Définir l'ID de ce segment de texte sur "product1"

text3.setID("product1");


// enregistrer le fichier PDF

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```


Lorsque vous utilisez les versions antérieures à Aspose.PDF pour Java 2.5.0, le code peut être exécuté avec succès et un document PDF résultant contenant un hyperlien vers une page au sein du même document peut être généré. Mais, lorsque le même code est compilé avec la version 2.5.0, vous remarquerez un certain nombre d'erreurs car il y a eu des changements dans les membres de la classe et aussi certaines méthodes dans les classes ont été supprimées. Commençons maintenant par la modification du code pour la version 2.5.0

Utilisez `import aspose.pdf.*`; au lieu de `import com.aspose.pdf.elements.*`; pour inclure le package.

Pour l'initialisation de la licence, veuillez mettre à jour votre code existant de

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

à

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo** ne contient plus de méthode **setUnderLine(...)**. Veuillez essayer d'utiliser **TextInfo.setIsUnderline(...)** ** à la place **.**

La classe nommée **HyperLinkToLocalPdf** a été supprimée. Veuillez donc mettre à jour votre code existant comme suit

{{% alert color="primary" %}}
**//Définir le type de lien du segment de texte sur Local**

```java

 //Assigner l'identifiant du paragraphe souhaité comme identifiant cible pour le segment de texte

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

par

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

Le nom de méthode **setFirstParagraph** a été supprimé de la classe Text.
 Ainsi, pour afficher le segment de texte dans une nouvelle page, vous devez créer un nouvel objet Section et ajouter l'objet texte à la section nouvellement créée. Comme par défaut chaque section est affichée sur une nouvelle page, il n'est donc pas nécessaire d'appeler une méthode comme **sec2.setIsNewPage(true**)**;

## Méthode de sauvegarde mise à jour

La méthode de sauvegarde dans la classe Pdf qui prenait un objet FileOutputStream comme argument a été supprimée. Dans la nouvelle version, vous pouvez utiliser l'une des méthodes surchargées suivantes de sauvegarde.

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

Après avoir effectué toutes les modifications spécifiées ci-dessus, lors de l'utilisation de Aspose.PDF pour Java 2.5.0, le code sera compilé et exécuté sans afficher de messages d'erreur. Le code mis à jour complet est spécifié ci-dessous.

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

//Instancier un objet Pdf en appelant son constructeur vide

Pdf pdf1 = new Pdf();

//Créer une section dans l'objet Pdf

Section sec1 = pdf1.getSections().add();

//Créer un paragraphe de texte avec la référence d'une section

Text text1 = new Text(sec1);

//Ajouter le paragraphe de texte dans la collection de paragraphes de la section

sec1.getParagraphs().add(text1);

//Ajouter un segment de texte dans le paragraphe de texte

Segment segment1 = text1.getSegments().add("ceci est un lien local");

//Définir le texte dans le segment de texte pour être souligné

segment1.getTextInfo().setIsUnderline(true);


//Définir le type de lien du segment de texte à Local

//Attribuer l'identifiant du paragraphe souhaité comme identifiant cible pour le segment de texte

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// ajouter une nouvelle section qui contiendra l'objet texte avec l'ID "Product 1"

Section sec2 = pdf1.getSections().add();

//Créer un paragraphe de texte à lier avec le segment de texte

Text text3 = new Text(sec1,"infos produit 1 ...");

//Ajouter le paragraphe de texte à la collection de paragraphes de la section

sec2.getParagraphs().add(text3);

//Définir l'identifiant de ce segment de texte sur "product1"

text3.setID("product1");


// sauvegarder le fichier PDF

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## Conclusion

Dans le sujet ci-dessus, nous avons expliqué certaines des classes et méthodes qui ont été modifiées dans la nouvelle version. Pour une liste complète de toutes les classes et de leurs membres, veuillez visiter [Aspose.PDF pour Java Référence API](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html)

Pour en savoir plus sur Aspose et ses produits, veuillez cliquer ici <http://www.aspose.com/>