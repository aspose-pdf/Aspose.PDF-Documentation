---
title: Travailler avec des documents PDF dans Qt
type: docs
weight: 130
url: /cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qt est un cadre de développement d'applications multiplateforme qui permet de créer une variété d'applications de bureau, mobiles, web et de systèmes embarqués. Dans cet article, nous verrons comment vous pouvez intégrer notre bibliothèque PDF C++ pour travailler avec des documents PDF dans vos applications Qt.

## Utilisation de Aspose.PDF pour C++ dans Qt

Afin d'utiliser Aspose.PDF pour C++ dans votre application Qt sur le système d'exploitation Windows, téléchargez la dernière version de l'API depuis la section [téléchargements](https://downloads.aspose.com/pdf/cpp). Une fois l'API téléchargée, vous pouvez utiliser l'une des options suivantes pour l'utiliser avec Qt.

- Utiliser Qt Creator
- Utiliser Visual Studio

Ici, nous allons démontrer comment intégrer et utiliser Aspose.PDF pour C++ dans une application console Qt en utilisant Qt Creator.

### Créer une application console Qt

{{% alert color="primary" %}}

Cet article suppose que vous avez correctement installé l'environnement de développement Qt et Qt Creator.

{{% /alert %}}

- Ouvrez Qt Creator et créez une nouvelle *Qt Console Application*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- Sélectionnez l'option QMake dans le menu déroulant *Build System*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- Sélectionnez le kit approprié et terminez l'assistant.

À ce stade, vous devriez avoir une application console Qt exécutable qui devrait se compiler sans problème.

### Intégrer Aspose.PDF pour l'API C++ avec Qt

- Extrayez l'archive Aspose.PDF pour C++ que vous avez téléchargée plus tôt
- Copiez les dossiers *Aspose.Pdf.Cpp* et *CodePorting.Native.Cs2Cpp_vc14_20.4* du package extrait de Aspose.PDF pour C++ à la racine du projet. Votre projet devrait ressembler à l'image suivante.

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- Pour ajouter des chemins vers les dossiers lib et include, cliquez avec le bouton droit sur le projet dans le panneau LHS et sélectionnez *Add Library*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- Sélectionnez l'option Bibliothèque externe et parcourez les chemins pour inclure et libérer les dossiers un par un.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- Une fois terminé, votre fichier de projet .pro contiendra les entrées suivantes :

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- Compilez l'application et vous avez terminé avec l'intégration.

### Créer un document PDF dans Qt

Maintenant qu'Aspose.PDF pour C++ a été intégré à Qt, nous sommes prêts à créer un document PDF avec du texte et à l'enregistrer sur le disque. Pour ce faire :

- Incluez les en-têtes suivants dans main.cpp

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```

- Insérez le code suivant dans la fonction principale pour générer un document PDF et l'enregistrer sur le disque

```cpp

    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;
    
    QString text = "Bonjour le monde";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```