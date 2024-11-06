---
title: Extraer Datos de AcroForm usando C++
linktitle: Extraer Datos AcroForm
type: docs
weight: 30
url: es/cpp/extract-form/
description: Esta sección explica cómo extraer formularios de su documento PDF con Aspose.PDF para C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Valores de todos los Campos del Documento PDF

Para obtener valores de todos los campos en un documento PDF, necesita navegar a través de todos los campos del formulario y luego obtener el valor usando la propiedad Value. Obtenga cada campo de la colección Form, en el tipo de campo base llamado Field y acceda a su propiedad Value.

Los siguientes fragmentos de código muestran cómo obtener los valores de todos los campos de un documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // Obtener valores de todos los campos
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"Nombre del Campo : {0} ", formField->get_PartialName());
        Console::WriteLine(u"Valor : {0} ", formField->get_Value());
    }
}
```

## Obtener el Valor de un Campo Individual de un Documento PDF

La propiedad Value del campo de formulario te permite obtener el valor de un campo en particular. Para obtener el valor, obtén el campo de formulario de la colección Form del objeto Document. Este ejemplo selecciona un [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field) y recupera su valor usando la propiedad Value.

El siguiente fragmento de código muestra cómo obtener los valores de los campos individuales en un documento PDF.

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // Obtener un campo
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Obtener valor del campo
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

Para obtener la URL del botón de envío, usa las siguientes líneas de código.

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## Obtener campos de formulario de una región específica del archivo PDF

A veces, puedes saber dónde está un campo de formulario en un documento, pero no tener su nombre. Por ejemplo, si todo lo que tienes para guiarte es un esquema de un formulario impreso. Con Aspose.PDF para C++, esto no es un problema. Puedes averiguar qué campos están en una región determinada de un archivo PDF. Para obtener campos de formulario de una región específica de un archivo PDF:

1. Abre el archivo PDF usando el objeto Document.
1. Crea un objeto rectángulo para obtener campos en esa área.
1. Obtén el formulario de la colección de formularios del documento.
1. Muestra nombres y valores de los campos.

El siguiente fragmento de código muestra cómo obtener campos de formulario en una región rectangular específica de un archivo PDF.


```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // Abrir archivo pdf
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // Crear objeto rectángulo para obtener campos en esa área
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // Obtener campos en el área rectangular
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // Mostrar nombres de campos y valores
    for(auto field : fields)
    {
        // Mostrar propiedades de ubicación de imagen para todas las ubicaciones
        Console::WriteLine(u"Nombre del campo: {0} - Valor del campo: {1}", field->get_FullName(), field->get_Value());
    }
}
```