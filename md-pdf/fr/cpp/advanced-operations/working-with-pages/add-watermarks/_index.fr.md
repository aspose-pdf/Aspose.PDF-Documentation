---
title: Ajouter un filigrane au PDF en utilisant C++
linktitle: Ajouter un filigrane
type: docs
weight: 90
url: /cpp/add-watermarks/
description: Cet article explique les fonctionnalités de travail avec les artefacts et l'obtention de filigranes dans les PDFs de manière programmatique avec le C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Un filigrane est une image translucide qui contient généralement un logo ou un sceau pour identifier qui a créé le document ou l'image.

**Aspose.PDF for C++** permet d'ajouter des filigranes à votre document PDF en utilisant la classe Artifact. Veuillez consulter cet article pour résoudre votre tâche.

Un filigrane créé avec Adobe Acrobat est appelé un artefact (comme décrit dans 14.8.2.2 Contenu réel et artefacts de la spécification PDF). Pour travailler avec des artefacts, Aspose.PDF dispose de deux classes : [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) et [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Pour obtenir tous les artefacts sur une page particulière, la classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a la propriété Artifacts. Ce sujet explique comment travailler avec les artefacts dans les fichiers PDF.

## Travailler avec des Artefacts

La classe [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) contient les propriétés suivantes :

**Artifact.Type** – obtient le type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactType où les valeurs incluent Background, Layout, Page, Pagination et Undefined).
**Artifact.Subtype** – obtient le sous-type d'artefact (prend en charge les valeurs de l'énumération Artifact.ArtifactSubtype où les valeurs incluent Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Veuillez noter que les filigranes créés avec Adobe Acrobat ont le type Pagination et le sous-type Watermark.

{{% /alert %}}

**Artifact.Contents** – Obtient une collection d'opérateurs internes d'artefact. Son type pris en charge est System.Collections.ICollection.
**Artifact.Form** – Obtient le XForm d'un artefact (si XForm est utilisé). Les artefacts de filigrane, d'en-tête et de pied de page contiennent XForm qui montre tous les contenus de l'artefact.

**Artifact.Image** – Obtient l'image d'un artefact (si une image est présente, sinon null).**Artifact.Text** – Obtient le texte d'un artefact.  
**Artifact.Rectangle** – Obtient la position d'un artefact sur la page.  
**Artifact.Rotation** – Obtient la rotation d'un artefact (en degrés, une valeur positive indique une rotation dans le sens antihoraire).  
**Artifact.Opacity** – Obtient l'opacité d'un artefact. Les valeurs possibles sont dans la plage 0…1, où 1 est complètement opaque.

## Exemples de programmation : Comment ajouter un filigrane sur des fichiers PDF

Le code suivant montre comment obtenir chaque filigrane sur la première page d'un fichier PDF avec C++.

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```