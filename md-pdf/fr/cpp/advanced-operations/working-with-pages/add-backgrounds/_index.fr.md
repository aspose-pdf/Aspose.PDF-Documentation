---
title: Ajouter un arrière-plan au PDF avec C++
linktitle: Ajouter des arrière-plans
type: docs
weight: 110
url: /cpp/add-backgrounds/
descriptions: Ajouter une image d'arrière-plan à votre fichier PDF avec C++. Utilisez l'objet BackgroundArtifact.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Ajouter un arrière-plan aux fichiers PDF aide à améliorer la lisibilité générale du document. Le contenu du PDF est plus attrayant et les lecteurs le remarqueront si vous avez une bonne apparence du document. L'arrière-plan peut également être utilisé pour mettre en évidence les points forts du PDF.

Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane, ou un autre design subtil, aux documents. Dans Aspose.PDF pour С++, chaque document PDF est une collection de pages et chaque page contient une collection d'artefacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

Le fragment de code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact avec C++.

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // Créer un nouvel objet Document
    auto document = MakeObject<Document>();

    // Ajouter une nouvelle page à l'objet document
    auto page = document->get_Pages()->Add();

    // Créer un objet Background Artifact
    auto background = MakeObject<BackgroundArtifact>();

    // Spécifier l'image pour l'objet backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Ajouter backgroundartifact à la collection d'artifacts de la page
    page->get_Artifacts()->Add(background);

    // Enregistrer le document
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```