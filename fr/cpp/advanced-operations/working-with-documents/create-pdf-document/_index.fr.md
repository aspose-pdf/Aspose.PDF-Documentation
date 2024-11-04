---
title: Créer un document PDF
linktitle: Créer PDF
type: docs
weight: 10
url: /cpp/create-pdf-document/
description: Cet article décrit comment créer et formater le document PDF avec Aspose.PDF pour C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Nous sommes toujours à la recherche d'un moyen de générer des documents PDF et de travailler avec eux dans des projets C++ de manière plus précise, exacte et efficace. Avoir des fonctions faciles à utiliser à partir d'une bibliothèque nous permet de suivre plus de travail, et moins sur les détails chronophages de la tentative de génération de PDF, que ce soit en C++.

## Générer un PDF en utilisant C++

L'API Aspose.PDF pour C++ vous permet de créer et de lire des fichiers PDF en utilisant C++. L'API peut être utilisée dans une variété d'applications C++ y compris WinForms, et plusieurs autres. Dans cet article, nous allons montrer comment utiliser l'API Aspose.PDF pour C++ pour générer et lire facilement des fichiers PDF dans les applications C++.

### Comment créer un fichier PDF simple

Pour créer un fichier PDF en utilisant C++, les étapes suivantes peuvent être utilisées.

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)  
1. Ajoutez un objet [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à la collection 'Pages' de l'objet Document  
1. Ajoutez [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) à la collection [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) de la page  
1. Enregistrez le document PDF résultant  

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Add text to new page
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Save updated PDF
    document->Save(_dataDir + outputFileName);
}
```
## Créer un document PDF consultable

Aspose.PDF pour C++ vous permet de créer des PDFs à partir de zéro et de manipuler ceux existants.  
Lorsque vous ajoutez des éléments texte à un PDF, le PDF résultant est consultable. Cependant, si nous convertissons une image contenant du texte en un fichier PDF, le contenu à l'intérieur du PDF n'est pas consultable. Cependant, comme solution de contournement, nous pouvons utiliser l'OCR sur le fichier résultant pour le rendre consultable. Par conséquent, vous devez d'abord installer Tesseract-OCR sur votre système, et vous aurez une application console tesseract.

Voici le code complet pour accomplir cette exigence :

```cpp
void CreateSearchableDocument() {
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```