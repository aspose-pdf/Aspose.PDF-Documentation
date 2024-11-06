---
title: Ajouter un Numéro de Page au PDF avec C++
linktitle: Ajouter un Numéro de Page
type: docs
weight: 100
url: fr/cpp/add-page-number/
description: Aspose.PDF pour C++ vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant la classe PageNumber Stamp.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Comment Ajouter des Numéros de Page à un PDF Existant

Tous les documents doivent avoir des numéros de page. Le numéro de page facilite la localisation de différentes parties du document pour le lecteur.
**Aspose.PDF pour C++** vous permet d'ajouter des numéros de page avec PageNumberStamp.

Les étapes suivantes et le code exemple illustrent comment ajouter des étiquettes de numérotation de pages à un document PDF existant en utilisant l'élément de page [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) pour ajouter automatiquement des numéros de page à un PDF.

Étapes pour Ajouter des Numéros de Page à un Document PDF Existant :

Pour ajouter un tampon de numéro de page, vous devez créer un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) et un objet [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) en utilisant les propriétés requises.

Après cela, vous pouvez appeler la méthode [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) de [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) pour ajouter le tampon dans le PDF.

Vous pouvez également définir les attributs de police du tampon de numéro de page.

L'extrait de code suivant vous montre comment ajouter des numéros de page dans un fichier PDF.

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer un tampon de numéro de page
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// Si le tampon est en arrière-plan
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Page # de " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// Définir les propriétés du texte
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // Ajouter le tampon à une page particulière
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // Enregistrer le document de sortie
    document->Save(_dataDir+ outputFileName);
}
```

## Exemple en Direct

[Ajouter des numéros de page PDF](https://products.aspose.app/pdf/page-number) est une application web gratuite en ligne qui vous permet d'examiner comment fonctionne la fonctionnalité d'ajout de numéros de page.

[![Comment ajouter un numéro de page dans un PDF en utilisant C++](page_number.png)](https://products.aspose.app/pdf/page-number)

## Ajouter/Supprimer la numérotation Bates

La **numérotation Bates** (également connue sous le nom de tamponnage Bates) est utilisée dans les domaines juridique, médical et commercial pour placer des numéros d'identification et/ou des marques de date/heure sur des images et des documents lorsqu'ils sont numérisés ou traités, par exemple, pendant la phase de découverte des préparations pour un procès ou pour identifier des reçus commerciaux. Ce processus fournit l'identification, la protection et la numérotation consécutive automatique des images ou des documents.

Aspose.PDF a pour l'instant un support limité pour la numérotation Bates. Cette fonctionnalité sera mise à jour en fonction des demandes des clients.

### Comment supprimer la numérotation Bates

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // Enregistrer le document de sortie
    document->Save(_dataDir + outputFileName);
}
```