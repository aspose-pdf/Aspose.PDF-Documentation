---  
title: Changer la taille des pages PDF par programmation  
linktitle: Changer la taille des pages PDF  
type: docs  
weight: 40  
url: /fr/cpp/change-page-size/  
description: Modifier la taille des pages de votre fichier PDF en utilisant la bibliothèque C++.  
lastmod: "2021-12-08"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---  

Le PDF est un format imprimable à mise en page statique, c'est pourquoi il est devenu répandu dans la vie professionnelle.

Cependant, il peut y avoir des tâches où vous devez redimensionner votre document PDF car la taille de la page est plus grande que celle du papier. Mais comment ?

Ne vous inquiétez pas. Sur cette page, vous trouverez un moyen de résoudre votre tâche.

Mais d'abord, souvenons-nous qu'il existe une série de tailles de pages.

Il existe deux séries de tailles de pages largement adoptées dans le monde.  
Bien sûr, il existe de nombreux formats, mais il y a ceux les plus couramment utilisés.  
La première est les formats de papier ISO. Série A4 est utilisée pour l'impression standard et la papeterie. Le papier de format Lettre est utilisé pour les affiches, les diagrammes muraux, etc. Les États-Unis, le Canada et en partie le Mexique ont adopté la deuxième série de tailles de pages et sont aujourd'hui les seuls pays industrialisés où les formats de papier standard ISO ne sont pas encore largement utilisés.

Voyons maintenant comment Aspose.PDF vous invite à redimensionner la page à l'aide de la bibliothèque C++.

## Changer la taille de la page PDF

Aspose.PDF pour С++ vous permet de changer la taille des pages PDF avec de simples lignes de code dans vos applications С++. Ce sujet explique comment mettre à jour/modifier les dimensions (taille) des pages d'un fichier PDF existant.

La classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) contient la méthode SetPageSize(...) qui vous permet de définir la taille de la page. L'extrait de code ci-dessous met à jour les dimensions des pages en quelques étapes simples :

1. Chargez le fichier PDF source.
1. Obtenez les pages dans l'objet [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. Obtenez une page donnée.
1. Appelez la méthode SetPageSize(..) pour mettre à jour ses dimensions.
1. Appelez la méthode Save(..) de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) pour générer le fichier PDF avec les dimensions de page mises à jour.

Le code suivant montre comment changer les dimensions de la page PDF à la taille A4.

```cpp
void ChangePageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");
    String outputFileName("UpdateDimensions_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obtenir une page particulière
    auto pdfPage = document->get_Pages()->idx_get(1);

    // Définir la taille de la page comme A4 (11.7 x 8.3 pouces) et dans Aspose.Pdf, 1 pouce = 72 points
    // Donc les dimensions A4 en points seront (842.4, 597.6)
    pdfPage->SetPageSize(597.6, 842.4);
    // Enregistrer le document mis à jour
    document->Save(_dataDir + outputFileName);
}
```

## Obtenir la taille de la page PDF

Vous pouvez lire la taille de la page PDF d'un fichier PDF existant en utilisant Aspose.PDF pour С++. Le code d'exemple suivant montre comment lire les dimensions des pages PDF en utilisant C++.

```cpp
void GetPDFPageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obtenir une page particulière
    auto page = document->get_Pages()->idx_get(1);

    // Obtenir les informations de hauteur et de largeur de la page
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
    // Faire pivoter la page à un angle de 90 degrés
    page->set_Rotate(Rotation::on90);
    // Obtenir les informations de hauteur et de largeur de la page
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```