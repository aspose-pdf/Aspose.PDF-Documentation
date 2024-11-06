---
title: Comment signer numériquement un PDF
linktitle: Signer numériquement un PDF
type: docs
weight: 10
url: fr/cpp/digitally-sign-pdf-file/
description: Signez numériquement des documents PDF en utilisant C++. Vérifiez ou validez les PDF signés numériquement en utilisant C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Signer un PDF avec des signatures numériques

Vous pouvez signer le document PDF pour confirmer son contenu, ou vous pouvez approuver le document avec Aspose.PDF.

Aspose.PDF pour C++ prend en charge la fonctionnalité de signer numériquement les fichiers PDF en utilisant la classe SignatureField. Vous pouvez également certifier un fichier PDF avec un certificat PKCS12. Quelque chose de similaire à [Ajouter des signatures et de la sécurité dans Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Utilisez la classe [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) pour signer votre PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// Chaîne pour le nom du chemin.

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // Utilisez PKCS7/PKCS7Detached
























// objets

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// Enregistrez le fichier PDF de sortie

signature->Save(outFile);
}
```

## Ajouter un horodatage à la signature numérique

### Comment signer numériquement un PDF avec horodatage

Aspose.PDF pour C++ prend en charge la signature numérique du PDF avec un serveur d'horodatage ou un service Web.

Les horodatages sont utilisés pour indiquer la date et l'heure à laquelle vous avez signé le document. L'horodatage fiable prouve que le contenu de vos PDFs existait à un moment spécifique et n'a pas changé depuis lors.

Utilisez la classe [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) pour ajouter un horodatage de confiance aux signatures numériques ou aux documents.

Veuillez consulter l'extrait de code suivant qui obtient un horodatage et l'ajoute au document PDF :

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {


// Chaîne pour le nom de chemin.

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");


auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // Utilisateur/Mot de passe peuvent
























// être omis

pkcs->set_TimestampSettings(timestampSettings);


System::Drawing::Rectangle rect(100, 100, 200, 100);

// Créez l'un des trois types de signature

signature->Sign(1, u"Raison de la signature", u"Contact", u"Emplacement", true, rect, pkcs);

// Enregistrez le fichier PDF de sortie

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```