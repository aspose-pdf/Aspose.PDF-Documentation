---
title: Travailler avec un Portfolio en PDF
linktitle: Portfolio
type: docs
weight: 40
url: fr/cpp/portfolio/
description: Créez un Portfolio PDF avec Aspose.PDF pour C++. Vous devez utiliser un fichier Microsoft Excel, un document Word et un fichier image pour créer un Portfolio PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Comment créer un Portfolio PDF

Aspose.PDF permet de créer des documents de Portfolio PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Ajoutez un fichier dans un objet Document.Collection après l'avoir obtenu avec la classe [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Une fois les fichiers ajoutés, utilisez la méthode Save de la classe Document pour enregistrer le document de portfolio.

L'exemple suivant utilise un fichier Microsoft Excel, un document Word et un fichier image pour créer un Portfolio PDF.

Le code ci-dessous aboutit au portfolio suivant.

### Un Portfolio PDF créé avec Aspose.PDF

![Un Portfolio PDF créé avec Aspose.PDF pour C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // Instancier l'objet Document
    auto pdfDocument = MakeObject<Document>();

    // Instancier l'objet Collection de document
    pdfDocument->set_Collection(MakeObject<Collection>());

    // Obtenir les fichiers à ajouter au portfolio
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // Fournir la description des fichiers
    excel->set_Description(u"Fichier Excel");
    word->set_Description(u"Fichier Word");
    image->set_Description(u"Fichier Image");

    // Ajouter des fichiers à la collection de documents
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // Enregistrer le document Portfolio
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```


## Extraire les fichiers du portfolio PDF

Les portefeuilles PDF vous permettent de rassembler du contenu provenant de diverses sources (par exemple, fichiers PDF, Word, Excel, JPEG) dans un conteneur unifié. Les fichiers originaux conservent leurs identités individuelles mais sont assemblés dans un fichier de portefeuille PDF. Les utilisateurs peuvent ouvrir, lire, éditer et formater chaque fichier composant indépendamment des autres fichiers composants.

Aspose.PDF permet la création de documents de portefeuille PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Il offre également la capacité d'extraire des fichiers d'un portefeuille PDF.

L'extrait de code suivant vous montre les étapes pour extraire des fichiers d'un portefeuille PDF.

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir un document
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // Obtenir la collection de fichiers intégrés
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // Itérer à travers chaque fichier du portefeuille
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // Enregistrer le fichier extrait à un emplacement
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // Fermer l'objet du flux
    fileStream->Close();
    }
}
```

![Extraire des fichiers d'un portefeuille PDF](working-with-pdf-portfolio_2.jpg)

## Supprimer des fichiers d'un portefeuille PDF

Pour supprimer des fichiers d'un portefeuille PDF, essayez d'utiliser les lignes de code suivantes.

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Charger le portefeuille PDF source
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```