---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
weight: 40
url: /cpp/modifing-form/
description: Modificar formularios en su archivo PDF con la biblioteca Aspose.PDF para C++. Puede agregar o eliminar campos en un formulario existente, obtener y establecer el límite de campo, etc.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener o Establecer el Límite de Campo

El método SetFieldLimit(field, limit) de la clase FormEditor le permite establecer un límite de campo, el número máximo de caracteres que se pueden ingresar en un campo.

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

De manera similar, Aspose.PDF tiene un método que obtiene el límite de campo utilizando el enfoque DOM. El siguiente fragmento de código muestra los pasos.

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Límite: {0}", textBoxField->get_MaxLen());        
}
```

También puede establecer y obtener el mismo valor utilizando el espacio de nombres *Aspose.PDF.Facades* usando el siguiente fragmento de código.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Agregar campo con límite
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Agregar campo con límite
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Límite: {0}", form->GetFieldLimit(u"textbox1"));
}
```
## Establecer fuente personalizada para el campo de formulario

Los campos de formulario en archivos PDF de Adobe pueden configurarse para usar fuentes predeterminadas específicas. En las primeras versiones de Aspose.PDF, solo se admitían las 14 fuentes predeterminadas. Las versiones posteriores permitieron a los desarrolladores aplicar cualquier fuente. Para establecer y actualizar la fuente predeterminada utilizada para los campos de formulario, use la clase DefaultAppearance (Font font, double size, Color color). Esta clase se encuentra bajo el espacio de nombres Aspose.PDF.InteractiveFeatures. Para usar este objeto, utilice la propiedad DefaultAppearance de la clase Field.

El siguiente fragmento de código muestra cómo establecer la fuente predeterminada para los campos de formulario PDF.

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // Obtener un campo de formulario específico del documento
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Crear objeto de fuente
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // Establecer la información de la fuente para el campo de formulario

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // Guardar documento actualizado
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## Eliminar campos de un formulario existente

Todos los campos del formulario están contenidos en la colección Form del objeto Document. Esta colección ofrece diferentes métodos que gestionan los campos del formulario, incluido el método Delete. Si deseas eliminar un campo en particular, pasa el nombre del campo como un parámetro al método Delete y luego guarda el documento PDF actualizado. El siguiente fragmento de código muestra cómo eliminar un campo en particular de un documento PDF.

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // Eliminar un campo en particular por nombre
    document->get_Form()->Delete(u"textbox1");
    
    // Guardar documento modificado
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```