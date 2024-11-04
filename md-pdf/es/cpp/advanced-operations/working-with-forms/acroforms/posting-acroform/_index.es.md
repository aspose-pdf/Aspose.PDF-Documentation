---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /cpp/posting-acroform-data/
description: Puede importar y exportar datos de formularios a y desde un archivo XML con el espacio de nombres Aspose.Pdf.Facades en Aspose.PDF para C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm es un tipo importante del documento PDF. No solo puedes crear y editar un AcroForm usando [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades), sino también importar y exportar datos del formulario a un archivo XML. El namespace Aspose.Pdf.Facades en Aspose.PDF para C++ te permite implementar otra característica de AcroForm, que te ayuda a enviar datos de un AcroForm a una página web externa. Esta página web luego lee las variables enviadas y utiliza estos datos para su posterior procesamiento. Esta característica es útil en los casos en los que no solo deseas mantener los datos en el archivo PDF, sino que quieres enviarlos a tu servidor y luego guardarlos en una base de datos, etc.

{{% /alert %}}

## Detalles de implementación

En este artículo, hemos tratado de crear un AcroForm usando [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) y la clase [FormEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/). También hemos añadido un botón de envío y configurado su URL de destino.

Los siguientes fragmentos de código te muestran cómo crear el formulario y luego recibir los datos enviados en la página web.
```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // String _dataDir("C:\\Samples\\");
    // Crear una instancia de la clase FormEditor y vincular archivos pdf de entrada y salida
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // Crear campos de AcroForm - He creado solo dos campos por simplicidad
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // Agregar un botón de envío y establecer la URL de destino
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // Guardar el archivo pdf de salida
    editor->Save();
}
```