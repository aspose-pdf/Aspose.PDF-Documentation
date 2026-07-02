---
title:  Extraer datos de AcroForm
linktitle:  Extraer datos de AcroForm
type: docs
weight: 50
url: /es/androidjava/extract-data-from-acroform/
description: AcroForms existen en muchos documentos PDF. Este artículo tiene como objetivo ayudarle a comprender cómo extraer datos de AcroForms con Aspose.PDF.
lastmod: "2026-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer campos de formulario de un documento PDF

Aspose.PDF for Android via Java no solo le permite crear y rellenar campos de formulario, sino que también facilita la extracción de datos de campos de formulario o información de campos de formulario de archivos PDF.

Supongamos que no conocemos los nombres de los campos del formulario de antemano. Entonces debemos iterar sobre cada página del PDF para extraer información sobre todos los AcroForms en el PDF, así como los valores de los campos del formulario. Para acceder al formulario necesitamos usar [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) método.

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```

Si conoce el nombre de los campos de formulario de los que desea extraer valores, puede usar el indexador en la colección Documents.Form para recuperar rápidamente estos datos.

## Recuperar el valor del campo de formulario por título

La propiedad Value del campo de formulario le permite obtener el valor de un campo en particular. Para obtener el valor, obtenga el campo de formulario de la [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objeto’s [colección de campos de formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). Este ejemplo selecciona un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) y recupera su valor usando el [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) método.

```java

    public void extractFormDataByName () {
        // Open document
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

## Extraer datos a XML de un archivo PDF

La clase Form le permite exportar datos a un archivo XML desde el archivo PDF mediante el método ExportXml. Para exportar datos a XML, necesita crear un objeto de la clase Form y luego llamar al método ExportXml utilizando el objeto FileStream. Finalmente, puede cerrar el objeto FileStream y disponer del objeto Form. El siguiente fragmento de código le muestra cómo exportar datos a un archivo XML.

```java
public void extractFormFieldsToXML () {
        // Open document
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
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## Exportar datos a FDF desde un archivo PDF

Para exportar los datos de formularios PDF a un archivo XFDF, podemos usar el [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) método en el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) clase.

Tenga en cuenta, que es una clase de `com.aspose.pdf.facades`. A pesar del nombre similar, esta clase tiene un propósito ligeramente diferente.

Para exportar datos a FDF, necesita crear un objeto de `Form` clase y luego llame al `exportXfdf` método usando el `OutputStream` objeto. El siguiente fragmento de código le muestra cómo exportar datos a un archivo XFDF.

```java
public void extractFormExportFDF () {
        // Open document
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

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Exportar datos a XFDF desde un archivo PDF

Para exportar los datos de formularios PDF a un archivo XFDF, podemos usar el [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) método en el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) clase.

Para exportar datos a XFDF, necesitas crear un objeto de `Form` clase y luego llame al `exportXfdf` método usando el `OutputStream` objeto. 
El siguiente fragmento de código le muestra cómo exportar datos a un archivo XFDF.

```java
    public void extractFormExportXFDF () {
        // Open document
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

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

