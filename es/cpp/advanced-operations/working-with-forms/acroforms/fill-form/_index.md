---
title: Rellenar AcroForm
linktitle: Rellenar AcroForm
type: docs
weight: 20
url: es/cpp/fill-form/
description: Esta sección explica cómo rellenar un campo de formulario en un documento PDF con Aspose.PDF para C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los documentos PDF son los mejores y realmente el tipo de archivo preferido para crear Formularios.

Este tema explica cómo rellenar formularios PDF usando Aspose.PDF para C++.

Aspose.PDF para C++ te permite rellenar un campo de formulario, obtener el campo de la colección Form del objeto Document.

Veamos el siguiente ejemplo de cómo resolver esta tarea:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // Obtener un campo
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Modificar valor del campo
    textBoxField->set_Value(u"Valor a ser llenado en el campo");

    // Guardar documento actualizado
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```