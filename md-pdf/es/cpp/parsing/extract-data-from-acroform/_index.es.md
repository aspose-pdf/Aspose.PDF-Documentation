---
title:  Extraer datos de AcroForm
linktitle:  Extraer datos de AcroForm
type: docs
weight: 50
url: /cpp/extract-data-from-acroform/
description: Aspose.PDF facilita la extracción de datos de campos de formulario de archivos PDF. Aprende cómo extraer datos de AcroForms y guardarlos en formato XML o FDF.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer campos de formulario del documento PDF

Aspose.PDF para C++ te permite no solo crear campos de formulario y rellenarlos, sino que también facilita la extracción de datos de campos de formulario o información de campos de formulario de archivos PDF.

En el ejemplo de código a continuación, demostramos cómo iterar sobre cada página en PDF para extraer información sobre todos los AcroForms en PDF así como los valores de los campos de formulario. Este ejemplo de código asume que no conoces los nombres de los campos de formulario de antemano.

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // String para nombre de ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nombre de archivo
    String infilename("StudentInfoFormElectronic.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Obtener valores de todos los campos
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Nombre del campo :" << formField->get_PartialName() << std::endl;
        std::cout << "Valor : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extraer Datos a XML desde un Archivo PDF

La clase [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) te permite exportar datos a un archivo XML desde el archivo PDF usando el método ExportXml. Para exportar datos a XML, necesitas crear un objeto de la clase Form y luego llamar al método ExportXml usando el objeto FileStream. Luego debes cerrar el objeto FileStream y disponer del objeto Form.

El siguiente fragmento de código muestra cómo exportar datos a un archivo XML.

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // Exportar datos
    form->ExportXml(fdfOutputStream);

    // Cerrar flujo de archivo
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Exportar datos a FDF desde un archivo PDF

La clase [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) te permite exportar datos a un archivo FDF desde el archivo PDF usando el método ExportFdf. Para exportar datos a FDF, necesitas crear un objeto de la clase Form y luego llamar al método ExportFdf usando el objeto FileStream. Después, puedes guardar el archivo PDF usando el método Save de la clase Form.

El siguiente fragmento de código te muestra cómo exportar datos a un archivo FDF.

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Exportar datos
    form->ExportFdf(fdfOutputStream);

    // Cerrar flujo de archivo
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Exportar Datos a XFDF desde un Archivo PDF

Aspose PDF para C++ con la clase [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) te permite exportar datos a un archivo XFDF desde el archivo PDF usando el método ExportXfdf. Para exportar datos a XFDF, necesitas crear un objeto de la clase Form y luego llamar al método ExportXfdf usando el objeto FileStream.

Al final, puedes guardar el archivo PDF usando el método Save de la clase Form.

El siguiente fragmento de código te muestra cómo exportar datos a un archivo XFDF.

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Exportar datos
    form->ExportXfdf(fdfOutputStream);

    // Cerrar flujo de archivo
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```