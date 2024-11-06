---
title:  Extraer datos de AcroForm
linktitle:  Extraer datos de AcroForm
type: docs
weight: 50
url: es/java/extract-data-from-acroform/
description: Los AcroForms existen en muchos documentos PDF. Este artículo tiene como objetivo ayudarle a entender cómo extraer datos de AcroForms usando Java y Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer campos de formulario del documento PDF

Aspose.PDF para Java no solo le permite crear y completar campos de formulario, sino que también facilita la extracción de datos de campos de formulario o información de campos de formulario de archivos PDF.

Supongamos que no conocemos los nombres de los campos de formulario de antemano. Entonces deberíamos iterar sobre cada página en el PDF para extraer información sobre todos los AcroForms en el PDF, así como los valores de los campos de formulario. Para acceder al formulario necesitamos usar el método [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // Obtener valores de todos los campos
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("Nombre del Campo :" + formField.getPartialName());
        System.out.println("Valor : " + formField.getValue());
    }
}
```


Si conoces los nombres de los campos de formulario de los que deseas extraer valores, entonces puedes usar el indexador en la colección Documents.Form para recuperar rápidamente estos datos.

## Recuperar el valor del campo de formulario por título

La propiedad Value del campo de formulario te permite obtener el valor de un campo en particular. Para obtener el valor, obtén el campo de formulario de la [colección de campos de formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Este ejemplo selecciona un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) y recupera su valor utilizando el método [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```


## Extraer campos de formulario de un documento PDF a JSON

Para exportar datos de formularios a JSON, recomendamos usar la biblioteca de terceros como [Gson](https://github.com/google/gson). Los siguientes fragmentos muestran cómo exportar `Name` y `Value` a JSON:

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

En este ejemplo usamos una clase adicional

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```


## Extraer Datos a XML desde un Archivo PDF

La clase Form permite exportar datos a un archivo XML desde un archivo PDF utilizando el método ExportXml. Para exportar datos a XML, necesitas crear un objeto de la clase Form y luego llamar al método ExportXml utilizando el objeto FileStream. Finalmente, puedes cerrar el objeto FileStream y disponer del objeto Form. El siguiente fragmento de código te muestra cómo exportar datos a un archivo XML.

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // Abrir documento
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // Crear archivo XML.
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // Exportar datos
        form.exportXml(xmlOutputStream);

        // Cerrar flujo de archivo
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // Cerrar el documento
    form.dispose();
    ;
}
```


## Exportar Datos a FDF desde un Archivo PDF

Para exportar datos de formularios PDF a un archivo XFDF, podemos usar el método [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) en la clase [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Por favor, tenga en cuenta que es una clase de `com.aspose.pdf.facades`. A pesar del nombre similar, esta clase tiene un propósito ligeramente diferente.

Para exportar datos a FDF, necesitas crear un objeto de la clase `Form` y luego llamar al método `exportXfdf` usando el objeto `OutputStream`. El siguiente fragmento de código te muestra cómo exportar datos a un archivo XFDF.

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Exportar datos
            form.exportFdf(fdfOutputStream);

            // Cerrar flujo de archivo
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: manejar excepción
            e.printStackTrace();
        }

    }
```


## Exportar Datos a XFDF desde un Archivo PDF

Para exportar datos de formularios PDF a un archivo XFDF, podemos usar el método [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) en la clase [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Para exportar datos a XFDF, necesitas crear un objeto de la clase `Form` y luego llamar al método `exportXfdf` usando el objeto `OutputStream`. 
El siguiente fragmento de código te muestra cómo exportar datos a un archivo XFDF.

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Exportar datos
            form.exportXfdf(fdfOutputStream);

            // Cerrar el flujo del archivo
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: manejar la excepción
            e.printStackTrace();
        }
    }
```