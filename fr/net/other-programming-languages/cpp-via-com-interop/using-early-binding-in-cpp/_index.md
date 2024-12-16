---
title: Utilisation du liage précoce en CPP
type: docs
weight: 10
url: /fr/net/using-early-binding-in-cpp/
---

## Prérequis

{{% alert color="primary" %}}

Veuillez enregistrer Aspose.PDF pour .NET avec COM Interop, veuillez consulter l'article intitulé [Utiliser Aspose.pdf pour .NET via COM Interop](/pdf/fr/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## Exemple

{{% alert color="primary" %}}

Voici un exemple simple de code C++ pour extraire du texte des fichiers PDF en utilisant COM Interop avec liage précoce. Avant d'exécuter l'exemple, faites attention à ce que :

- **#import** *typelib.tlb* fait en sorte que le compilateur C++ génère 2 fichiers : *typelib.tlh* et *typelib.tli*. Par défaut, ces fichiers sont générés une seule fois, vous devez donc recompiler entièrement le projet pour obtenir de nouvelles versions de ces fichiers.
- souvent, l'importation d'un seul fichier TLB entraîne un grand nombre d'erreurs de compilation.
{{% /alert %}}
- Souvent, importer un seul fichier TLB conduit à un grand nombre d'erreurs de compilation.

```cpp
// Bibliothèques de types référencées croisées :
```

et comporte une ou plusieurs **#import**. Copiez-les simplement dans votre code avant d'importer la bibliothèque de types principale et faites-le dans le ***même*** ordre. Ainsi, vous éviterez le premier type de problème. Le type de problème suivant provient du fait que l'environnement C++ a un grand nombre de macros, de fonctions prédéfinies, etc., qui peuvent entrer en conflit avec les méthodes de la bibliothèque de types. Par exemple, GetType est déjà largement utilisé en C++ mais aussi Aspose.PDF l'utilise. J'ai trouvé que les attributs **rename** et **auto_rename** de la directive **#import** sont très pratiques pour éviter les avertissements et les erreurs possibles.
{{% alert color="primary" %}}

- parfois, les classes dans les espaces de noms **uses** entrent en conflit avec les noms dans la bibliothèque de types, donc dans de tels cas, le nom complet de la classe doit être utilisé au lieu de **using namespace**. Par exemple, voyez comment StringToBSTR est appelé dans l'extrait de code ci-dessous.
{{% /alert %}}

Pour plus de détails, veuillez consulter [ce](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) post.
Pour plus de détails, veuillez consulter [ce](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) article.

Exemple en C++

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^liaisonPrécoce(String ^fichier)
{
    String ^texte;
    // créer ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"Erreur survenue");
    }
    else
    {
        // définir la licence
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // obtenir le Document
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(fichier).ToPointer());

        comHelperPtr.Release();

        // créer Absorber
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // parcourir le texte
        docPtr->GetPages()->Accept_4(absorberPtr);

        // récupérer le texte
        BSTR texteExtrait = absorberPtr->GetText();
        texte = gcnew String(texteExtrait);
        docPtr.Release();
        absorberPtr.Release();
    }
    return texte;
}

int main(array<System::String ^> ^args)
{
    CoInitialize(NULL);
    if (args->Length != 1)
    {
        Console::WriteLine("Paramètres manquants\nUsage:testCOM <fichier pdf>");
        return 0;
    }

    String ^texte = liaisonPrécoce(args[0]);
    CoUninitialize();
    Console::WriteLine("Texte extrait:");
    Console::WriteLine("---\n{0}", texte != nullptr ? texte->Trim() : "<vide>");
    Console::WriteLine("---");
    return 0;
}
```

