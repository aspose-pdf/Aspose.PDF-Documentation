---
title: Travailler avec les opérateurs en C++
linktitle: Travailler avec les opérateurs
type: docs
weight: 170
url: fr/cpp/operators/
description: Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF en C++. Les classes d'opérateurs offrent d'excellentes fonctionnalités pour la manipulation de PDF.
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction aux opérateurs PDF et leur utilisation

Un opérateur est un mot-clé PDF spécifiant une action à effectuer, comme peindre une forme graphique sur la page. Un mot-clé opérateur se distingue d'un objet nommé par l'absence d'un caractère solidus initial (2Fh). Les opérateurs n'ont de sens qu'à l'intérieur du flux de contenu.

Un flux de contenu est un objet flux PDF dont les données consistent en instructions décrivant les éléments graphiques à peindre sur une page. Plus de détails sur les opérateurs PDF peuvent être trouvés dans la [spécification PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Détails de l'implémentation

Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF. L'exemple sélectionné ajoute une image dans un fichier PDF pour illustrer le concept. Pour ajouter une image dans un fichier PDF, différents opérateurs sont nécessaires. Cet exemple utilise [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix), [Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do), et [GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore).

- L'opérateur **GSave** sauvegarde l'état graphique actuel du PDF.
- L'opérateur **ConcatenateMatrix** (concaténer la matrice) est utilisé pour définir comment une image doit être placée sur la page PDF.
- L'opérateur **Do** dessine l'image sur la page.
- L'opérateur **GRestore** restaure l'état graphique.

Pour ajouter une image dans un fichier PDF :

1. Créez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) et ouvrez le document PDF d'entrée.
1. Obtenez la page particulière à laquelle l'image va être ajoutée.
1. Ajoutez l'image dans la collection de Ressources de la page.
1. Utilisez les opérateurs pour placer l'image sur la page :
   - Tout d'abord, utilisez l'opérateur GSave pour enregistrer l'état graphique actuel.
   - Ensuite, utilisez l'opérateur ConcatenateMatrix pour spécifier où l'image doit être placée.
   - Utilisez l'opérateur Do pour dessiner l'image sur la page.
1. Enfin, utilisez l'opérateur GRestore pour enregistrer l'état graphique mis à jour.

Le code suivant montre comment utiliser les opérateurs PDF.

```cpp
void ExampleUsingOperators()
{
    // Open document
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // Set coordinates
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // Get the page where image needs to be added
    auto page = document->get_Pages()->idx_get(1);

    // Load image into stream
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // Add image to Images collection of Page Resources
    page->get_Resources()->get_Images()->Add(imageStream);

    // Using GSave operator: this operator saves current graphics state
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Create Rectangle and Matrix objects
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // Using Do operator: this operator draws image
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // Using GRestore operator: this operator restores graphics state
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // Save updated document
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```
## Dessiner XForm sur la Page en utilisant des Opérateurs

Ce sujet démontre comment utiliser les opérateurs GSave/GRestore, l'opérateur ConcatenateMatrix pour positionner un xForm et l'opérateur Do pour dessiner un xForm sur une page.

Le code ci-dessous enveloppe le contenu existant d'un fichier PDF avec la paire d'opérateurs GSave/GRestore. Cette approche aide à obtenir l'état graphique initial à la fin des contenus existants. Sans cette approche, des transformations indésirables pourraient rester à la fin de la chaîne d'opérateurs existante.

```cpp
void DrawXFormOnPageUsingOperators() {
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // L'échantillon démontre
    // Utilisation des opérateurs GSave/GRestore
    // Utilisation de l'opérateur ConcatenateMatrix pour positionner xForm
    // Utilisation de l'opérateur Do pour dessiner xForm sur la page

    // Envelopper les contenus existants avec la paire d'opérateurs GSave/GRestore
    // ceci est pour obtenir l'état graphique initial à la fin des contenus existants
    // sinon il pourrait rester des transformations indésirables à la fin de la chaîne d'opérateurs existante
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Ajouter l'opérateur d'enregistrement de l'état graphique pour effacer correctement l'état graphique après les nouvelles commandes
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Créer xForm

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Définir largeur et hauteur de l'image
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // Charger l'image dans le flux
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // Ajouter l'image à la collection Images des Ressources XForm
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // Utilisation de l'opérateur Do : cet opérateur dessine l'image
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Placer le formulaire aux coordonnées x=100 y=500
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // Dessiner le formulaire avec l'opérateur Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Placer le formulaire aux coordonnées x=100 y=300
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // Dessiner le formulaire avec l'opérateur Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Restaurer l'état graphique avec GRestore après le GSave
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## Supprimer des objets graphiques en utilisant des classes d'opérateurs

Les classes d'opérateurs offrent de grandes fonctionnalités pour la manipulation de PDF. Lorsqu'un fichier PDF contient des graphiques qui ne peuvent pas être supprimés en utilisant la méthode [DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380) de la classe [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor), les classes d'opérateurs peuvent être utilisées pour les supprimer à la place.

Le code suivant montre comment supprimer des graphiques. Veuillez noter que si le fichier PDF contient des étiquettes de texte pour les graphiques, elles pourraient persister dans le fichier PDF en utilisant cette approche. Par conséquent, recherchez les opérateurs graphiques pour une méthode alternative afin de supprimer de telles images.

```cpp
void RemoveGraphicsObjects() {
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // Opérateurs de peinture de chemin utilisés
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```