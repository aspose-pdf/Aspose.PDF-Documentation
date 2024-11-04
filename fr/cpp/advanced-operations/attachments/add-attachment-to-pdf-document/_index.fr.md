---
title: Ajouter une pièce jointe au document PDF
linktitle: Ajouter une pièce jointe au document PDF
type: docs
weight: 10
url: /cpp/add-attachment-to-pdf-document/
description: Cette page décrit comment ajouter une pièce jointe à un fichier PDF avec la bibliothèque Aspose.PDF pour C++
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les pièces jointes peuvent contenir une grande variété d'informations et peuvent être de différents types de fichiers. Cet article explique comment ajouter une pièce jointe à un fichier PDF.

1. Créez un nouveau projet C++.
1. Ajoutez une référence à la DLL Aspose.PDF.
1. Créez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Créez un objet [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) avec le fichier que vous ajoutez, et la description du fichier.
1. Ajouter l'objet [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) à la collection [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), avec la méthode Add de la collection.

La collection [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) contient toutes les pièces jointes dans le fichier PDF. Le fragment de code suivant vous montre comment ajouter une pièce jointe dans un document PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// Ouvrir le document

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// Configurer le nouveau fichier à ajouter en tant que pièce jointe

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"Fichier texte d'exemple");


// Ajouter la pièce jointe à la collection de pièces jointes du document

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// Enregistrer la nouvelle sortie

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```