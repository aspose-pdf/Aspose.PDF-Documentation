---
title: Obtenez la Résolution et les Dimensions des Images Intégrées en C++
linktitle: Obtenez la Résolution et les Dimensions
type: docs
weight: 40
url: fr/cpp/get-resolution-and-dimensions-of-embedded-images/
description: Cette section montre les détails pour obtenir la résolution et les dimensions des images intégrées
lastmod: "2021-12-18"
---

Ce sujet explique comment utiliser les classes d'opérateurs dans l'espace de noms Aspose.PDF qui fournissent la capacité d'obtenir des informations de résolution et de dimension sur les images sans avoir à les extraire.

Il existe différentes façons de réaliser cela. Cet article explique comment utiliser une `arraylist` et les [classes de placement d'images](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement).

1. Tout d'abord, chargez le fichier PDF source (avec des images).
1. Ensuite, créez un objet ArrayList pour contenir les noms des images dans le document.
1. Obtenez les images en utilisant la propriété Page.Resources.Images.
1. Créez un objet pile pour contenir l'état graphique de l'image et utilisez-le pour suivre les différents états de l'image.
1. Créer un objet ConcatenateMatrix qui définit la transformation actuelle. Il prend également en charge le redimensionnement, la rotation et l'inclinaison de tout contenu. Il concatène la nouvelle matrice avec la précédente. Veuillez noter que nous ne pouvons pas définir la transformation à partir de zéro, mais seulement modifier la transformation existante.
1. Parce que nous pouvons modifier la matrice avec ConcatenateMatrix, nous pourrions également avoir besoin de revenir à l'état d'image original. Utilisez [l'opérateur GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) et [l'opérateur GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/). Ces opérateurs sont associés, ils doivent donc être appelés ensemble. Par exemple, si vous effectuez un travail graphique avec des transformations complexes et revenez enfin aux transformations initiales, l'approche sera quelque chose comme ceci :

Le code suivant vous montre comment obtenir les dimensions et la résolution d'une image sans extraire l'image du document PDF.

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // Charger le fichier PDF source
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // Définir la résolution par défaut pour l'image
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // Définir l'objet de liste de tableaux qui contiendra les noms d'images
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // Insérer un objet dans la pile
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // Obtenir tous les opérateurs sur la première page du document
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // Utiliser les opérateurs GSave/GRestore pour rétablir les transformations précédemment définies
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // Instancier l'objet ConcatenateMatrix car il définit la matrice de transformation actuelle.
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // Créer l'opérateur Do qui dessine des objets à partir des ressources. Il dessine des objets Form et des objets Image
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // Enregistrer l'état précédent et pousser l'état actuel en haut de la pile
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // Supprimer l'état actuel et restaurer le précédent
            graphicsState->Pop();
        }
        else if (opCtm != nullptr)
        {
            auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
                (float)opCtm->get_Matrix()->get_A(),
                (float)opCtm->get_Matrix()->get_B(),
                (float)opCtm->get_Matrix()->get_C(),
                (float)opCtm->get_Matrix()->get_D(),
                (float)opCtm->get_Matrix()->get_E(),
                (float)opCtm->get_Matrix()->get_F());

            // Multiplier la matrice actuelle par la matrice d'état
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            continue;
        }
        else if (opDo != nullptr)
        {
            // Dans le cas où il s'agit d'un opérateur de dessin d'image
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // Créer un objet XImage pour contenir les images de la première page PDF
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // Obtenir les dimensions de l'image
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // Obtenir les informations de hauteur et de largeur de l'image
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // Calculer la résolution basée sur les informations ci-dessus
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // Afficher les informations de dimension et de résolution de chaque image
                Console::Write(_dataDir);
                Console::Write(u" image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```