---
title: Remplacer l'image dans un fichier PDF existant en utilisant C++
linktitle: Remplacer l'image
type: docs
weight: 70
url: /cpp/replace-image-in-existing-pdf-file/
description: Cette section décrit comment remplacer une image dans un fichier PDF existant en utilisant la bibliothèque C++.
lastmod: "2021-12-18"
---

La méthode Replace de la collection Images vous permet de remplacer une image dans un fichier PDF existant.

La collection Images peut être trouvée dans la collection Resources d'une page. Pour remplacer une image :

1. Ouvrez le fichier PDF en utilisant l'objet Document.
2. Remplacez une image particulière, enregistrez le fichier PDF mis à jour en utilisant la méthode Save de l'objet Document.

Le code suivant vous montre comment remplacer une image dans un fichier PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // Remplacer une image particulière
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // Enregistrer le fichier PDF mis à jour
    document->Save(_dataDir + u"output.pdf");
}
```