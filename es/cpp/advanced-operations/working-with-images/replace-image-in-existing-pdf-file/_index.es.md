---
title: Reemplazar Imagen en Archivo PDF Existente usando C++
linktitle: Reemplazar Imagen
type: docs
weight: 70
url: /cpp/replace-image-in-existing-pdf-file/
description: Esta sección describe cómo reemplazar una imagen en un archivo PDF existente usando la biblioteca ++.
lastmod: "2021-12-18"
---

El método Replace de la colección de Imágenes permite reemplazar una imagen en un archivo PDF existente.

La colección de Imágenes se puede encontrar en la colección de Recursos de una página. Para reemplazar una imagen:

1. Abra el archivo PDF usando el objeto Document.
2. Reemplace una imagen en particular, guarde el archivo PDF actualizado usando el método Save del objeto Document.

El siguiente fragmento de código le muestra cómo reemplazar una imagen en un archivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // Reemplazar una imagen en particular
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // Guardar archivo PDF actualizado
    document->Save(_dataDir + u"output.pdf");
}
```