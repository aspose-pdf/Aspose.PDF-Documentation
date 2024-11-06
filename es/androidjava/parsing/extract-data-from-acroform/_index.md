---
title:  Extraer datos de AcroForm 
linktitle:  Extraer datos de AcroForm
type: docs
weight: 50
url: es/androidjava/extract-data-from-acroform/
description: Los AcroForms existen en muchos documentos PDF. Este artículo tiene como objetivo ayudarte a entender cómo extraer datos de AcroForms con Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer campos de formulario de un documento PDF

Aspose.PDF para Android vía Java no solo te permite crear y rellenar campos de formulario, sino que también facilita la extracción de datos de los campos de formulario o información de los campos de formulario de archivos PDF.

Supongamos que no conocemos los nombres de los campos del formulario de antemano. Entonces deberíamos iterar sobre cada página en el PDF para extraer información sobre todos los AcroForms en el PDF así como los valores de los campos del formulario. Para acceder al formulario necesitamos usar el método [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
 public void extractFormFields () {
        // Abrir documento
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obtener valores de todos los campos
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Nombre del Campo: ");
            sb.append(formField.getPartialName());
            sb.append(" Valor: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```


Si conoces el nombre de los campos del formulario de los que deseas extraer valores, entonces puedes usar el indexador en la colección Documents.Form para recuperar rápidamente estos datos.

## Recuperar el valor del campo del formulario por título

La propiedad Value del campo del formulario te permite obtener el valor de un campo en particular. Para obtener el valor, obtén el campo del formulario de la [colección de campos de formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Este ejemplo selecciona un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) y recupera su valor usando el método [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java

    public void extractFormDataByName () {
        // Abrir documento
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```


## Extraer Datos a XML desde un Archivo PDF

La clase Form permite exportar datos a un archivo XML desde el archivo PDF usando el método ExportXml. Para exportar datos a XML, necesitas crear un objeto de la clase Form y luego llamar al método ExportXml usando el objeto FileStream. Finalmente, puedes cerrar el objeto FileStream y disponer del objeto Form. El siguiente fragmento de código te muestra cómo exportar datos a un archivo XML.

```java
public void extractFormFieldsToXML () {
        // Abrir documento
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // Crear archivo xml.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Exportar datos
            form.exportXml(xmlOutputStream);

            // Cerrar flujo de archivo
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Cerrar el documento
        form.dispose();
    }
```


## Exportar Datos a FDF desde un Archivo PDF

Para exportar los datos de formularios PDF a un archivo XFDF, podemos usar el método [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) en la clase [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Por favor, tenga en cuenta que es una clase de `com.aspose.pdf.facades`. A pesar del nombre similar, esta clase tiene un propósito ligeramente diferente.

Para exportar datos a FDF, necesita crear un objeto de la clase `Form` y luego llamar al método `exportXfdf` utilizando el objeto `OutputStream`. El siguiente fragmento de código le muestra cómo exportar datos a un archivo XFDF.

```java
public void extractFormExportFDF () {
        // Abrir documento
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Exportar datos
            form.exportFdf(fdfOutputStream);

            // Cerrar flujo de archivo
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Exportar Datos a XFDF desde un Archivo PDF

Para exportar los datos de formularios PDF a un archivo XFDF, podemos usar el método [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) en la clase [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Para exportar datos a XFDF, necesita crear un objeto de la clase `Form` y luego llamar al método `exportXfdf` usando el objeto `OutputStream`. El siguiente fragmento de código le muestra cómo exportar datos a un archivo XFDF.

```java
    public void extractFormExportXFDF () {
        // Abrir documento
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Exportar datos
            form.exportXfdf(fdfOutputStream);

            // Cerrar flujo de archivo
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```