---
title: Obtenir et Définir les Propriétés de Page
type: docs
weight: 30
url: /fr/php-java/get-and-set-page-properties/
description: Ce sujet explique comment obtenir des nombres dans un fichier PDF, obtenir les propriétés de page et déterminer la couleur de la page en utilisant Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
---

Aspose.PDF pour PHP via Java vous permet de lire et définir les propriétés des pages dans un fichier PDF dans vos applications Java. Cette section montre comment obtenir le nombre de pages dans un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés de page.

## Obtenir le Nombre de Pages dans un Fichier PDF

Lorsque vous travaillez avec des documents, vous souhaitez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne prend pas plus de deux lignes de code.

Pour obtenir le nombre de pages dans un fichier PDF :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Ensuite, les pages du document sont récupérées. Une tentative est faite pour obtenir le nombre de pages à partir des pages récupérées.

Le code suivant montre comment obtenir le nombre de pages d'un fichier PDF.


```php

    // Ouvrir le document
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Obtenir le nombre de pages
    $responseData = $responseData . "Nombre de pages : " + $pages->size();
```

### Obtenez le nombre de pages sans enregistrer le document

À moins que le fichier PDF ne soit enregistré et que tous les éléments ne soient effectivement placés à l'intérieur du fichier PDF, nous ne pouvons pas obtenir le nombre de pages d'un document particulier (car nous ne pouvons pas être certains du nombre de pages dans lesquelles tous les éléments seront logés). Cependant, à partir de la version Aspose.PDF pour PHP via Java, nous avons introduit une méthode nommée [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) qui offre la fonctionnalité d'obtenir le nombre de pages d'un document PDF, sans enregistrer le fichier. Ainsi, nous pouvons obtenir des informations sur le nombre de pages à la volée. Veuillez essayer d'utiliser le code suivant pour répondre à cette exigence.

```php

    // Ouvrir le document
    $document = new Document($inputFile);      

    // ajouter une page à la collection de pages du fichier PDF
    $page = $document->getPages()->add();
    
    // créer une boucle pour ajouter 300 instances de TextFragment
    for ($i=0; $i < 300; $i++) { 
       // ajouter TextFragment à la collection de paragraphes de la première page du PDF
       $page->getParagraphs()->add(new TextFragment("Test de comptage des pages"));
    }
    
    // traiter les paragraphes pour obtenir des informations sur le nombre de pages
    $document->processParagraphs();

    $pages = $document->getPages();

    // Obtenir le nombre de pages
    $responseData = $responseData . "Nombre de pages : " + $pages->size();
```


## Obtenir les propriétés de la page

Chaque page d'un fichier PDF a un certain nombre de propriétés, telles que la largeur, la hauteur, les boîtes de fond perdu, de recadrage et de coupe. Aspose.PDF vous permet d'accéder à ces propriétés.

### **Comprendre les propriétés de la page : la différence entre les propriétés Artbox, BleedBox, CropBox, MediaBox, TrimBox et Rect**

- **Boîte de médias**: La boîte de médias est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, Lettre US, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d'autres termes, la boîte de médias détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de fond perdu**: Si le document a un fond perdu, le PDF aura également une boîte de fond perdu.
 Bleed est la quantité de couleur (ou illustration) qui dépasse le bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et découpé à la taille ("rogné"), l'encre ira jusqu'au bord de la page. Même si la page est mal rognée - coupée légèrement en dehors des repères de coupe - aucun bord blanc n'apparaîtra sur la page.

- **Boîte de rognage**: La boîte de rognage indique la taille finale d'un document après impression et rognage.
- **Boîte d'art**: La boîte d'art est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Boîte de découpe**: La boîte de découpe est la taille de "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seuls les contenus de la boîte de découpe sont affichés dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Limites de page.
- **Page.Rect**: l'intersection (rectangle couramment visible) du MediaBox et du DropBox. La figure ci-dessous illustre ces propriétés.

Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Accéder aux propriétés de la page

Le fragment de code suivant obtient des propriétés telles que ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Numéro de page et Rotation pour une page spécifique du document. Il stocke ensuite les données extraites dans des variables distinctes et les concatène dans une chaîne de réponse.

1. Créer un nouvel objet Document en utilisant la variable $inputFile.
1. Obtenez la collection de pages du document en utilisant la méthode getPages().
1. Obtenez une page spécifique de la collection de pages en utilisant la méthode get_Item().
1. Extraire diverses propriétés (ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Numéro de page, Rotation) de l'objet de page spécifique et les stocker dans des variables distinctes.
1. Le code concatène les valeurs de propriété extraites en chaînes de réponse distinctes ($responseData1, $responseData2, etc.).
1. Ensuite, il tente de récupérer le nombre de pages en utilisant la méthode size() sur l'objet $pages, mais la variable $pages n'est pas définie.

Le snippet de code suivant montre comment obtenir les propriétés d'une page.

```php

   // Ouvrir le document
    $document = new Document($inputFile);

    // Obtenir la collection de pages
    $pageCollection = $document->getPages();

    // Obtenir une page spécifique
    $page = $pageCollection->get_Item(1);

    // Obtenir les propriétés de la page
    $responseData1 = "ArtBox : Hauteur = " . $page->getArtBox()->getHeight()
        . ", Largeur = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Hauteur = " . $page->getBleedBox()->getHeight() . ", Largeur = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Hauteur = " . $page->getCropBox()->getHeight() . ", Largeur = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Hauteur = " . $page->getMediaBox()->getHeight() . ", Largeur = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Hauteur = " . $page->getTrimBox()->getHeight() . ", Largeur = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Hauteur = " . $page->getRect()->getHeight() . ", Largeur = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Numéro de page :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Rotation :-" . $page->getRotate() . PHP_EOL;

    // Obtenir le nombre de pages
    $responseData8 = $responseData8 . "Nombre de pages : " . $pages->size();
```


## Déterminer la couleur de la page

La classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) fournit les propriétés liées à une page particulière dans un document PDF, y compris le type de couleur - RGB, noir et blanc, niveaux de gris ou indéfini - que la page utilise.

Toutes les pages des fichiers PDF sont contenues par la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). La propriété [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) spécifie la couleur des éléments sur la page. Pour obtenir ou déterminer les informations de couleur pour une page PDF particulière, utilisez la propriété [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) de l'objet de classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

Le code suivant montre comment itérer à travers chaque page d'un fichier PDF pour obtenir des informations sur la couleur.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Itérer à travers toutes les pages du fichier PDF
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // Obtenir les informations de type de couleur pour une page PDF particulière
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="Page # -" . $pageCount . " est en noir et blanc..";
                break;
            case 1:
                $responseData ="Page # -" . $pageCount . " est en niveaux de gris...";
                break;
            case 0:
                $responseData ="Page # -" . $pageCount . " est en RGB..";
                break;
            case 3:
                $responseData ="Page # -" . $pageCount . " La couleur est indéfinie..";
                break;
        }
    }
```