---
title: Métadonnées de fichier PDF
type: docs
weight: 20
url: fr/cpp/pdf-file-metadata/
---

## Obtenir/Configurer les informations du fichier PDF

Afin d'obtenir des informations spécifiques d'un fichier PDF, vous devez d'abord appeler la méthode **get_Info()** de la classe Document. Une fois l'objet DocumentInfo récupéré, vous pouvez obtenir les valeurs des propriétés individuelles. De plus, vous pouvez également définir les propriétés en utilisant les méthodes respectives de la classe DocumentInfo. Le code suivant démontre comment obtenir/configurer les informations du fichier PDF en utilisant Aspose.PDF pour C++ :

{{% alert color="primary" %}}

Veuillez noter que vous ne pouvez pas définir de valeurs pour les champs **Application** et **Producer**, car Aspose Ltd. et Aspose.PDF pour C++ x.x.x seront affichés pour ces champs.

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // Obtenir les informations du document
    auto docInfo = pdfDocument->get_Info();
    // Afficher les informations du document
    Console::WriteLine(u"Auteur : {0}", docInfo->get_Author());
    Console::WriteLine(u"Date de création : {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Mots-clés : {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Date de modification : {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Sujet : {0}", docInfo->get_Subject());
    Console::WriteLine(u"Titre : {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // Spécifier les informations du document
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"Informations sur le PDF");
    docInfo->set_Title (u"Définir les informations du document PDF");

    // Enregistrer le document de sortie
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## Obtenir/Configurer les Métadonnées XMP à partir d'un Fichier PDF

Aspose.PDF pour C++ vous permet d'accéder aux métadonnées XMP d'un fichier PDF ainsi que de les configurer. Pour obtenir/configurer les métadonnées d'un fichier PDF :

1. Créez un objet Document et ouvrez le fichier PDF d'entrée.
1. Obtenez/Configurez les métadonnées du fichier en utilisant les méthodes respectives.

Le code suivant vous montre comment obtenir/configurer les métadonnées à partir du fichier PDF.

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // Obtenir les propriétés
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // Définir les propriétés
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // Enregistrer le document
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // le préfixe xmlns a été supprimé
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // Enregistrer le document
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```