---
title: Optimiser PDF avec C++
linktitle: Optimiser PDF
type: docs
weight: 30
url: /cpp/optimize-pdf/
description: Optimiser un fichier PDF, réduire toutes les images, diminuer la taille du PDF, désintégrer les polices, activer la réutilisation du contenu des pages, supprimer ou aplatir les annotations avec C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Tout d'abord, toute optimisation de PDF que vous faites est pour l'utilisateur. Dans les PDF, l'optimisation pour l'utilisateur consiste principalement à réduire la taille de vos PDF afin d'augmenter leur vitesse de chargement. C'est la tâche la plus populaire.
Nous pouvons utiliser plusieurs techniques pour optimiser le PDF, mais les plus essentielles :

- Optimiser le contenu des pages pour la navigation en ligne
- Réduire ou compresser toutes les images
- Activer la réutilisation du contenu des pages
- Fusionner les flux en double
- Désintégrer les polices
- Supprimer les objets inutilisés
- Supprimer les champs de formulaire aplatissants
- Supprimer ou aplatir les annotations

## Optimiser le document PDF pour le Web

Lorsque vous êtes confronté à la tâche d'optimiser le contenu de votre document PDF pour un meilleur classement dans les moteurs de recherche, Aspose.PDF pour C++ a une solution.

1. Ouvrez le document d'entrée dans un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Utilisez la méthode [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda).
1. Enregistrez le document optimisé en utilisant la méthode Save.

Le code suivant montre comment optimiser un document PDF pour le web.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//Optimiser le document PDF pour le Web
void OptimizeForWeb() {
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String outfilename("OptimizeDocument_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>();

    // Effectuer certaines opérations (ajouter des pages, des images, etc.)
    // ...

    // Optimiser pour le web
    document->Optimize();

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
}
```

## Réduire la taille du PDF

La méthode [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) vous permet de réduire la taille du document en éliminant les informations inutiles. Par défaut, cette méthode fonctionne comme suit :

- Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées
- Les ressources égales sont fusionnées en un seul objet
- Les objets inutilisés sont supprimés

L'extrait ci-dessous est un exemple. Notez, cependant, que cette méthode ne peut pas garantir la réduction du document.

```cpp
void ReduceSizePDF() {

    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String outfilename("ShrinkDocument_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>();
    // Effectuer certaines opérations (ajouter des pages, des images, etc.)
    // ...

    // Optimiser le document PDF. Notez, cependant, que cette méthode ne peut pas garantir la réduction du document
    document->OptimizeResources();

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
}
```

## Gestion de la stratégie d'optimisation

Nous pouvons également personnaliser la stratégie d'optimisation. Actuellement, la méthode [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) utilise 5 techniques. Ces techniques peuvent être appliquées en utilisant la méthode OptimizeResources() avec le paramètre [OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/).

### Réduction ou Compression de Toutes les Images

Pour optimiser les images dans votre document PDF, nous utiliserons [Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization). Pour résoudre le problème de l'optimisation des images, nous avons les options suivantes : réduire la qualité des images et/ou changer leur résolution. Dans tous les cas, [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/) devrait être appliqué. Dans l'exemple suivant, nous réduisons les images en diminuant [ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e) à 50.

```cpp
void CompressImage() {
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialiser OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Définir l'option CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Définir l'option ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // Optimiser le document PDF en utilisant OptimizationOptions
    document->OptimizeResources(optimizationOptions); 
    // Enregistrer le document mis à jour
    document->Save(_dataDir + outfilename);
}
```
Pour définir l'image à une résolution plus basse, réglez [ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6) sur true et [MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e) sur la valeur correspondante.

```cpp
void ResizeImagesWithLowerResolution() {
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialiser OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Régler l'option CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Régler l'option ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Régler l'option ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Régler l'option MaxResolution
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // Optimiser le document PDF en utilisant OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Enregistrer le document mis à jour
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF pour C++ vous offre également un contrôle sur le paramètre d'exécution. Aujourd'hui, nous pouvons utiliser deux algorithmes - Standard et Rapide. Pour contrôler le temps d'exécution, nous devons définir une propriété [Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4).

L'extrait suivant démontre l'algorithme Rapide :

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialiser OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Définir l'option CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Définir l'option ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Définir l'option ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Définir la version de compression d'image à rapide
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // Optimiser le document PDF en utilisant OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Enregistrer le document mis à jour
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### Suppression des objets inutilisés

Parfois, vous pouvez avoir besoin de supprimer certains objets inutilisés de votre document PDF qui ne sont pas référencés sur les pages. Cela peut se produire, par exemple, lorsqu'une page est supprimée de l'arborescence des pages du document, mais que l'objet de la page lui-même n'est pas supprimé. Supprimer ces objets ne rend pas le document invalide mais le réduit. Consultez le prochain extrait de code :

```cpp
void RemovingUnusedObject() { 
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialiser OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Définir l'option RemoveUsedObject
    optimizationOptions->set_RemoveUnusedObjects(true);

    // Optimiser le document PDF à l'aide d'OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Enregistrer le document mis à jour
    document->Save(_dataDir + outfilename); 
}
```

### Suppression des flux non utilisés

Parfois, le document contient des flux de ressources non utilisés. Ces flux ne sont pas des “objets non utilisés” car ils sont référencés à partir d'un dictionnaire de ressources de page. Ainsi, ils ne sont pas supprimés avec une méthode de “suppression des objets non utilisés”. Mais ces flux ne sont jamais utilisés avec le contenu de la page. Cela peut se produire dans des cas où une image a été supprimée de la page mais pas des ressources de la page. De plus, cette situation se produit souvent lorsque des pages sont extraites du document et que les pages du document ont des ressources “communes”, c'est-à-dire le même objet Resources. Le contenu des pages est analysé afin de déterminer si un flux de ressources est utilisé ou non. Les flux non utilisés sont supprimés. Cela diminue parfois la taille du document. L'utilisation de cette technique est similaire à l'étape précédente :

```cpp
void RemovingUnusedStreams() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set RemoveUsedStreams option
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### Liaison des flux en double

Certains documents peuvent contenir plusieurs flux de ressources en double (comme des images, par exemple). Cela peut se produire, par exemple, lorsqu'un document est concaténé avec lui-même. Le document de sortie contient deux copies indépendantes du même flux de ressources. Nous analysons tous les flux de ressources et les comparons. Si les flux sont dupliqués, ils sont fusionnés, c'est-à-dire qu'une seule copie est conservée. Les références sont modifiées en conséquence, et les copies de l'objet sont supprimées. Dans certains cas, cela aide à réduire la taille du document.

```cpp
void LinkingDuplicateStreams() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set LinkDuplcateStreams option
    optimizationOptions->set_LinkDuplcateStreams(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

De plus, nous pouvons utiliser les paramètres [AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8). Si cette propriété est définie sur true, le contenu de la page sera réutilisé lors de l'optimisation du document pour des pages identiques.

```cpp
void AllowReusePageContent() { 
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialiser OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Définir l'option AllowReusePageContent
    optimizationOptions->set_AllowReusePageContent(true);

    // Optimiser le document PDF en utilisant OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Sauvegarder le document mis à jour
    document->Save(_dataDir + outfilename); 
}
```

### Désintégration des Polices

Lorsque vous créez une version PDF de votre fichier de conception personnel, une copie de toutes les polices nécessaires est ajoutée au fichier PDF lui-même. C'est l'intégration. Peu importe où ce PDF est ouvert, que ce soit sur votre ordinateur, l'ordinateur d'un ami ou celui de votre fournisseur d'impression, toutes les polices correctes seront présentes et s'afficheront correctement.

Cependant, si le document utilise des polices intégrées, cela signifie que toutes les données de police sont stockées dans le document. L'avantage est que le document est visible que la police soit installée ou non sur la machine de l'utilisateur. Mais l'intégration des polices rend le document plus volumineux. La méthode de désintégration des polices supprime toutes les polices intégrées. Ainsi, la taille du document diminue, mais le document lui-même peut devenir illisible si la police correcte n'est pas installée.

```cpp
void UnembedFonts() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set AllowReusePageContent option
    optimizationOptions->set_UnembedFonts(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

Les ressources d'optimisation appliquent ces méthodes au document. Si l'une de ces méthodes est appliquée, la taille du document diminuera très probablement. Si aucune de ces méthodes n'est appliquée, la taille du document ne changera pas, ce qui est évident.

## Moyens supplémentaires pour réduire la taille d'un document PDF

### Suppression ou aplatissement des annotations

La présence d'annotations dans votre document PDF augmente naturellement sa taille. Les annotations peuvent être supprimées lorsqu'elles ne sont pas nécessaires. Lorsqu'elles sont nécessaires mais ne nécessitent pas d'édition supplémentaire, elles peuvent être aplaties. Ces deux techniques réduiront la taille du fichier.

```cpp
void FlatteningAnnotation() {
    // Chaîne pour le chemin d'accès
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("OptimizeDocument.pdf");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("OptimizeDocument_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Aplatir les annotations
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // Enregistrer le document mis à jour
    document->Save(_dataDir + outfilename);
}
```

### Suppression des champs de formulaire

Supprimer les formulaires de votre PDF optimisera également votre document. Si le document PDF contient des AcroForms, nous pouvons essayer de réduire la taille du fichier en aplatissant les champs de formulaire.

```cpp
void FlatteningFormFields() {
    // Chaîne pour le chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("OptimizeFormField.pdf");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("OptimizeFormField_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Aplatir les champs de formulaire
    // Aplatir les formulaires
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // Enregistrer le document mis à jour
    document->Save(_dataDir + outfilename);
}
```

### Convertir un PDF de l'espace colorimétrique RVB en niveaux de gris

Un fichier PDF comprend du texte, des images, des pièces jointes, des annotations, des graphiques et d'autres objets. Vous pouvez rencontrer l'exigence de convertir un PDF de l'espace colorimétrique RGB en niveaux de gris afin qu'il soit plus rapide lors de l'impression de ces fichiers PDF. De plus, lorsque le fichier est converti en niveaux de gris, la taille du document est également réduite, mais cela peut tout aussi bien entraîner une diminution de la qualité du document. Cette fonctionnalité est actuellement prise en charge par la fonctionnalité de pré-vol d'Adobe Acrobat, mais lorsqu'il s'agit d'automatisation de bureau, Aspose.PDF est une solution ultime pour offrir de tels avantages pour les manipulations de documents. Pour accomplir cette exigence, le code suivant peut être utilisé.

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("OptimizeDocument.pdf");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("Test-gray_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // Obtenir une instance d'une page particulière dans le PDF
        auto page = document->get_Pages()->idx_get(idxPage);
        // Convertir l'image de l'espace colorimétrique RGB en espace colorimétrique GrayScale
        strategy->Convert(page);
    }
    // Enregistrer le fichier résultant
    document->Save(_dataDir + outfilename); 
}
```
### Compression FlateDecode

Aspose.PDF pour C++ offre le support de la compression FlateDecode pour la fonctionnalité d'optimisation de PDF.
Pour optimiser l'image en utilisant la compression FlateDecode, définissez les options d'optimisation sur Flate.
Le code ci-dessous montre comment utiliser l'option dans l'optimisation pour stocker des images avec la compression **FlateDecode** :

```cpp
void FlatDecodeCompression() {
 // Chaîne pour le nom du chemin
 String _dataDir("C:\\Samples\\");

 // Chaîne pour le nom du fichier d'entrée
 String infilename("FlateDecodeCompression.pdf");
 // Chaîne pour le nom du fichier de sortie
 String outfilename("FlateDecodeCompression_out.pdf");

 // Ouvrir le document
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Initialiser OptimizationOptions
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // Pour optimiser l'image en utilisant la compression FlateDecode, définissez les options d'optimisation sur Flate
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // Optimiser le document PDF en utilisant OptimizationOptions
 document->OptimizeResources(optimizationOptions);

 // Enregistrer le document mis à jour
 document->Save(_dataDir + outfilename);
}
```

### **Stocker une image dans XImageCollection**

Aspose.PDF pour C++ offre la possibilité de stocker de nouvelles images dans [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) avec une compression FlateDecode. Pour activer cette option, vous pouvez utiliser le drapeau **ImageFilterType.Flate**. Le code suivant montre comment utiliser cette fonctionnalité :

```cpp
void StoreImageInXImageCollection() {

 // Chaîne pour le nom du chemin
 String _dataDir("C:\\Samples\\");

 // Chaîne pour le nom du fichier de sortie
 String outfilename("FlateDecodeCompression_out.pdf");

 // Ouvrir le document
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // Définir les coordonnées
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // Utilisation de l'opérateur ConcatenateMatrix (concaténer matrice) : définit comment l'image doit être placée
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```