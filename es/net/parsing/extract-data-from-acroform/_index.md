---
title:  Extraer datos de AcroForm usando C#
linktitle:  Extraer datos de AcroForm
type: docs
weight: 50
url: es/net/extract-data-from-acroform/
description: Aspose.PDF facilita la extracción de datos de campos de formulario desde archivos PDF. Aprende cómo extraer datos de AcroForms y guardarlos en formato JSON, XML o FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer campos de formulario de un documento PDF

Así como te permite generar campos de formulario y llenar campos de formulario, Aspose.PDF para .NET facilita la extracción de datos de campos de formulario o información sobre campos de formulario desde archivos PDF.

En el código de muestra a continuación demostramos cómo iterar a través de cada página en un PDF para extraer información sobre todos los AcroForm en el PDF así como los valores de los campos de formulario. Este código de muestra presupone que no conoces el nombre de los campos de formulario de antemano.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // Obtener valores de todos los campos
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("Nombre del Campo : {0} ", formField.PartialName);
        Console.WriteLine("Valor : {0} ", formField.Value);
    }
}
```
Si conoce el nombre de los campos del formulario de los que desea extraer valores, entonces puede usar el indexador en la colección Documents.Form para recuperar rápidamente estos datos. Mire al final de este artículo para ver un código de ejemplo sobre cómo usar esa función.

## Recuperar el valor del campo del formulario por título

La propiedad Value del campo del formulario permite obtener el valor de un campo particular. Para obtener el valor, obtenga el campo del formulario de la colección Form del objeto Document. Este ejemplo selecciona un TextBoxField y recupera su valor usando la propiedad Value.

## Extraer campos de formulario de documento PDF a JSON

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## Extraer Datos a XML desde un Archivo PDF

La clase Form permite exportar datos a un archivo XML desde el archivo PDF utilizando el método ExportXml. Para exportar datos a XML, necesitas crear un objeto de la clase Form y luego llamar al método ExportXml usando el objeto FileStream. Finalmente, puedes cerrar el objeto FileStream y desechar el objeto Form. El siguiente fragmento de código te muestra cómo exportar datos a un archivo XML.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// Abrir documento
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// Crear archivo xml.
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// Exportar datos
form.ExportXml(xmlOutputStream);
// Cerrar flujo de archivo
xmlOutputStream.Close();

// Cerrar el documento
form.Dispose();
```
## Exportar Datos a FDF desde un Archivo PDF

La clase Form permite exportar datos a un archivo FDF desde el archivo PDF usando el método ExportFdf. Para exportar datos a FDF, necesitas crear un objeto de la clase Form y luego llamar al método ExportFdf usando el objeto FileStream. Finalmente, puedes guardar el archivo PDF usando el método Save de la clase Form. El siguiente fragmento de código te muestra cómo exportar datos a un archivo FDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Abrir documento
form.BindPdf(dataDir + "input.pdf");

// Crear archivo fdf.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// Exportar datos
form.ExportFdf(fdfOutputStream);

// Cerrar flujo de archivo
fdfOutputStream.Close();

// Guardar documento actualizado
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## Exportar Datos a XFDF desde un Archivo PDF

La clase Form te permite exportar datos a un archivo XFDF desde el archivo PDF utilizando el método ExportXfdf. Para exportar datos a XFDF, necesitas crear un objeto de la clase Form y luego llamar al método ExportXfdf usando el objeto FileStream. Finalmente, puedes guardar el archivo PDF utilizando el método Save de la clase Form. El siguiente fragmento de código te muestra cómo exportar datos a un archivo XFDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Abrir Documento
form.BindPdf(dataDir + "input.pdf");

// Crear archivo xfdf.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// Exportar datos
form.ExportXfdf(xfdfOutputStream);

// Cerrar flujo de archivo
xfdfOutputStream.Close();

// Guardar documento actualizado
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```

