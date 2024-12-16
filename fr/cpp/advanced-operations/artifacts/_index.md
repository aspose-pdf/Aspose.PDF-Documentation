---
title: Travailler avec des Artifacts en C++
linktitle: Travailler avec des Artifacts
type: docs
weight: 110
url: /fr/cpp/artifacts/
description: Cette page décrit comment travailler avec la classe Artifact en utilisant Aspose.PDF pour C++. Les extraits de code montrent comment ajouter une image d'arrière-plan aux pages PDF et comment obtenir chaque filigrane sur la première page d'un fichier PDF.
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Comment obtenir un filigrane dans un PDF ?

**Qu'est-ce qu'un artifact dans un PDF ?**

Selon la référence PDF / UA ISO, le contenu qui n'est pas important ou qui n'apparaît pas en arrière-plan ne porte pas d'informations pertinentes, doit être marqué comme un artifact pour que les technologies d'assistance puissent l'ignorer.
Si les artifacts ne peuvent pas être identifiés dans le programme de création, cela doit être fait manuellement en utilisant Aspose.PDF pour C++.

La classe [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) contient les propriétés suivantes :

- **Artifact.Type** – obtient le type d'artifact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
- **Artifact.Subtype** – obtient le sous-type d'artéfact (prend en charge les valeurs de l'énumération Artifact.ArtifactSubtype où les valeurs incluent Arrière-plan, Pied de page, En-tête, Indéfini, Filigrane).

{{% alert color="primary" %}}

Veuillez noter que les filigranes créés avec Adobe Acrobat ont le type Pagination et le sous-type Filigrane.

{{% /alert %}}

- **Artifact.Contents** – Obtient une collection d'opérateurs internes de l'artéfact. Son type pris en charge est System.Collections.ICollection.
- **Artifact.Form** – Obtient le XForm d'un artéfact (si XForm est utilisé). Les artéfacts de filigrane, d'en-tête et de pied de page contiennent XForm qui montre tous les contenus de l'artéfact.
- **Artifact.Image** – Obtient l'image d'un artéfact (si une image est présente, sinon null).
- **Artifact.Text** – Obtient le texte d'un artéfact.
- **Artifact.Rectangle** – Obtient la position d'un artéfact sur la page.
- **Artifact.Rotation** – Obtient la rotation d'un artéfact (en degrés, une valeur positive indique une rotation dans le sens inverse des aiguilles d'une montre).
- **Artifact.Opacity** – Obtient l'opacité d'un artéfact. Les valeurs possibles sont dans la plage 0...1, où 1 est complètement opaque.

Pour un exemple de travail avec des artefacts dans un fichier PDF, prenons un filigrane.

Un filigrane créé avec le support d'Adobe Acrobat est appelé un artefact (comme décrit dans 14.8.2.2 Présentation du contenu et artefacts de la spécification PDF). Pour travailler avec des artefacts, Aspose.PDF contient 2 classes :
[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) et [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Afin d'obtenir tous les artefacts sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a la propriété Artifacts. Ce sujet montre comment travailler avec un artefact de filigrane dans des fichiers PDF.

Le fragment de code suivant montre comment obtenir chaque filigrane sur la première page d'un fichier PDF avec C++ :

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```
Les images d'arrière-plan peuvent être utilisées pour ajouter des filigranes ou des designs exclusifs aux documents PDF. Aspose.PDF pour C++ utilise la classe [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) pour ajouter une image d'arrière-plan à l'objet page.

Le prochain extrait de code vous montre comment ajouter une image d'arrière-plan aux pages PDF avec l'objet BackgroundArtifact :

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>();

    // Ajouter un MakeObject<page à l'objet document
    auto page = pdfDocument->get_Pages()->Add();

    // Créer un objet Background Artifact
    auto background = MakeObject<BackgroundArtifact>();

    // Spécifier l'image pour l'objet backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Ajouter BackgroundArtifact à la collection d'artefacts de la page
    page->get_Artifacts()->Add(background);

    // Enregistrer le PDF modifié
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### Exemples de programmation : Obtenir des filigranes

L'extrait de code suivant montre comment obtenir chaque filigrane sur la première page d'un fichier PDF.

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // Itérer et obtenir le sous-type, le texte et l'emplacement de l'artéfact
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### Exemples de programmation : Compter les artéfacts d'un type particulier

Pour calculer le nombre total d'artéfacts d'un type particulier (par exemple, le nombre total de filigranes), utilisez le code suivant :

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // Si le type d'artéfact est filigrane, augmenter le compteur
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"La page contient {0} filigranes", count);
}
```