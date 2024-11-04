---
title: Extraire et Enregistrer une Pièce Jointe
linktitle: Extraire et Enregistrer une Pièce Jointe
type: docs
weight: 20
url: /cpp/extract-and-save-an-attachment/
description: Aspose.PDF pour C++ vous permet d'obtenir toutes les pièces jointes d'un document PDF. De plus, vous pouvez obtenir une pièce jointe individuelle de votre document.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenez Toutes les Pièces Jointes

Avec Aspose.PDF, il est possible d'obtenir toutes les pièces jointes d'un document PDF. Ceci est utile soit lorsque vous souhaitez enregistrer les documents séparément du PDF, soit si vous avez besoin de retirer les pièces jointes d'un PDF.

Pour obtenir toutes les pièces jointes d'un fichier PDF :

1. Loop à travers la collection [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). La collection [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) contient toutes les pièces jointes. Chaque élément de cette collection représente un objet [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Chaque itération de la boucle foreach à travers la collection [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) renvoie un objet [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification).
1. Une fois l'objet disponible, récupérez soit toutes les propriétés du fichier joint soit le fichier lui-même.

Les extraits de code suivants montrent comment obtenir toutes les pièces jointes d'un document PDF.

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // Ouvrir le document
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // Obtenir la collection de fichiers intégrés
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // Obtenir le nombre de fichiers intégrés
 Console::WriteLine(u"Total files : {0}", embeddedFiles->get_Count());

 int count = 1;

 // Boucle à travers la collection pour obtenir toutes les pièces jointes
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

  // Vérifier si l'objet paramètre contient les paramètres
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"CheckSum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Creation Date: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Modification Date: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Size: {0}", fileSpecification->get_Params()->get_Size());
  }

  // Obtenir la pièce jointe et l'écrire dans un fichier ou un flux
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## Obtenir une pièce jointe individuelle

Afin d'obtenir une pièce jointe individuelle, nous pouvons spécifier l'index de la pièce jointe dans l'objet `EmbeddedFiles` de l'instance Document. Veuillez essayer d'utiliser l'extrait de code suivant.

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // Obtenir un fichier intégré particulier
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // Obtenir les propriétés du fichier
    Console::WriteLine(u"Nom: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Type MIME: {0}", fileSpecification->get_MIMEType());

    // Vérifier si l'objet paramètre contient les paramètres
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"CheckSum: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Date de création: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Date de modification: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Taille: {0}",
        fileSpecification->get_Params()->get_Size());
    }


    // Obtenir la pièce jointe et écrire dans un fichier ou un flux
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```