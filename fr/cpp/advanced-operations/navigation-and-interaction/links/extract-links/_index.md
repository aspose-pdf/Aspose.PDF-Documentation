---
title: Extraire des liens à partir du fichier PDF
linktitle: Extraire des liens
type: docs
weight: 30
url: fr/cpp/extract-links/
description: Extraire des liens à partir de PDF avec C#. Ce sujet vous explique comment extraire des liens en utilisant la classe AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire des liens à partir du fichier PDF

Les liens sont représentés comme des annotations dans un fichier PDF, donc pour extraire des liens, extrayez tous les objets [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).

1. Créez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
2. Obtenez la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) dont vous souhaitez extraire les liens.
3. Utilisez la classe [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) pour extraire tous les objets [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) de la page spécifiée.
1. Passez l'objet [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) à la méthode Accept de l'objet Page.
1. Obtenez toutes les annotations de lien sélectionnées dans un objet IList en utilisant la propriété Selected de l'objet [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).

Le fragment de code suivant vous montre comment extraire des liens d'un fichier PDF.

```cpp
void ExtractLinksFromThePDFFile() {
   
    // Charger le fichier PDF
    String _dataDir("C:\\Samples\\");

    // Créer une instance de Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Annotation localisée : {0}", annot->get_Rect());
    }
}
```