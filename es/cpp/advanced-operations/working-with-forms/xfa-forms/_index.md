---
title: Trabajando con Formularios XFA usando C++
linktitle: Formularios XFA
type: docs
weight: 20
url: /es/cpp/xfa-forms/
description: Aspose.PDF para C++ API te permite trabajar con campos XFA y XFA Acroform en un documento PDF. El Aspose.PDF.Facades.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA Forms es la Arquitectura de Formularios XML, una familia de especificaciones XML propietarias que fueron propuestas y desarrolladas por JetForm para mejorar el manejo de formularios web. También se puede usar en archivos PDF a partir de la especificación PDF 1.5.

Rellena campos XFA con la clase [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) de [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades).

## Rellenar campos XFA

El siguiente fragmento de código muestra cómo rellenar campos en un formulario XFA.

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // Cargar formulario XFA
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // Obtener nombres de los campos del formulario XFA
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Establecer valores de los campos

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // Guardar el documento actualizado
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## Convertir XFA a AcroForm

{{% alert color="primary" %}}

Probar en línea
Puede verificar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Los formularios dinámicos se basan en una especificación XML conocida como XFA, la "Arquitectura de Formularios XML". La información sobre el formulario (en lo que respecta a un PDF) es muy vaga: especifica que existen campos, con propiedades y eventos JavaScript, pero no especifica ningún renderizado.

Actualmente, PDF admite dos métodos diferentes para integrar datos y formularios PDF:

- AcroForms (también conocidos como formularios Acrobat), introducidos e incluidos en la especificación de formato PDF 1.2.
- Formularios de Arquitectura de Formularios XML de Adobe (XFA), introducidos en la especificación de formato PDF 1.5 como una característica opcional (La especificación XFA no está incluida en la especificación PDF, solo se hace referencia a ella.)

No podemos extraer o manipular páginas de Formularios XFA, porque el contenido del formulario se genera en tiempo de ejecución (durante la visualización del formulario XFA) dentro de la aplicación que intenta mostrar o renderizar el formulario XFA. Aspose.PDF tiene una característica que permite a los desarrolladores convertir formularios XFA a AcroForms estándar.

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // Set the form fields type as standard AcroForm
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // Save the resultant PDF
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## Obtener propiedades del campo XFA

Para acceder a las propiedades del campo, primero use Document.Form.XFA.Teamplate para acceder a la plantilla del campo. El siguiente fragmento de código muestra los pasos para obtener las coordenadas X e Y de un campo de formulario XFA.

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Set field values
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // Get field position
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // Get field position
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // Save the updated document
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```