---
title: Créer des liens dans un fichier PDF avec C++
linktitle: Créer des liens
type: docs
weight: 10
url: /fr/cpp/create-links/
description: Cette section explique comment créer des liens dans votre document PDF avec C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Créer des liens

En ajoutant un lien vers une application dans un document, il est possible de lier des applications depuis un document. Cela est utile lorsque vous souhaitez que les lecteurs effectuent une certaine action à un moment spécifique dans un tutoriel, par exemple, ou pour créer un document riche en fonctionnalités. Pour créer un lien d'application :

1. [Créer un Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) objet.
1. Obtenez la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à laquelle vous souhaitez ajouter un lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Définissez les attributs du lien en utilisant l'objet [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. Définissez également la propriété Action de l'objet [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/).
1. Lors de la création de l'objet [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/), spécifiez l'application que vous souhaitez lancer.
1. Ajoutez le lien à la propriété [Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations) de l'objet Page.
1. Enfin, enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet Document.

L'extrait de code suivant montre comment créer un lien vers une application dans un fichier PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Créez une instance de Document
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // Ajoutez une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // Enregistrez le document mis à jour
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```
### Créer un lien de document PDF dans un fichier PDF

Aspose.PDF pour C++ vous permet d'ajouter un lien vers un fichier PDF externe afin que vous puissiez lier plusieurs documents ensemble. Pour créer un lien de document PDF :

1. Tout d'abord, créez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Ensuite, obtenez la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) particulière à laquelle vous souhaitez ajouter le lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Définissez les attributs du lien en utilisant l'objet [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. Définissez la propriété Action sur l'objet [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/).
1. Pendant la création de l'objet GoToRemoteAction, spécifiez le fichier PDF qui doit être lancé, ainsi que le numéro de page sur lequel il doit s'ouvrir.
1. Ajoutez le lien à la collection Annotations de l'objet Page.
1. Enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet Document.

L'extrait de code suivant montre comment créer un lien de document PDF dans un fichier PDF.

 ```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // Save updated document
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```