---
title: Convertir archivo PDF a PDF/A 
linktitle: Convertir archivo PDF a PDF/A 
type: docs
weight: 180
url: /androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: Este tema muestra cómo Aspose.PDF para Java permite convertir un archivo PDF a un archivo PDF compatible con PDF/A.  
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF le permite convertir un archivo PDF a un archivo PDF compatible con PDF/A. Antes de hacerlo, el archivo debe ser validado. Este artículo explica cómo.

Tenga en cuenta que seguimos Adobe Preflight para validar la conformidad con PDF/A. Todas las herramientas del mercado tienen su propia "representación" de la conformidad con PDF/A. Consulte este artículo sobre [herramientas de validación de PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) como referencia. Elegimos productos de Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

Antes de convertir el PDF a un archivo compatible con PDF/A, valide el PDF usando el método de validación.
 El resultado de la validación se almacena en un archivo XML y luego este resultado también se pasa al método de conversión. También puedes especificar la acción para los elementos que no pueden ser convertidos usando la enumeración [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

{{% alert color="primary" %}}

Prueba en línea. Puedes verificar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Conversión de PDF a PDF/A_1b

El siguiente fragmento de código muestra cómo convertir archivos PDF a PDF compatibles con PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir a documento compatible con PDF/A
        // Durante el proceso de conversión, también se realiza la validación
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Guardar documento de salida
        document.save(pdfaFileName.toString());
    }
```

Para realizar solo la validación, use la siguiente línea de código:

```java
public void ValidatePDF_A_1B() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validar como documento compatible con PDF/A

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("El documento es válido");
        }
        else {
            resultMessage.setText("El documento no es válido");
        }
    }
```

## Conversión de PDF a PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir a documento compatible con PDF/A
        // Durante el proceso de conversión, también se realiza la validación
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Guardar documento de salida
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Conversión de PDF a PDF/A_3a

```java
public void convertPDFtoPDFa3a() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir a un documento compatible con PDF/A
        // Durante el proceso de conversión, también se realiza la validación
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Guardar documento de salida
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Conversión de PDF a PDF/A_2a

```java
public void convertPDFtoPDFa2a() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir a un documento compatible con PDF/A
        // Durante el proceso de conversión, también se realiza la validación
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Guardar documento de salida
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## Conversión de PDF a PDF/A_3U

```java
 public void convertPDFtoPDFa3u() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir a documento compatible con PDF/A
        // Durante el proceso de conversión, también se realiza la validación
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Guardar documento de salida
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Crear PDF/A-3 y adjuntar archivo XML

Aspose.PDF para Android a través de Java ofrece la función de convertir archivos PDF al formato PDF/A y también soporta las capacidades de agregar archivos como un adjunto al documento PDF.
 En caso de que tenga un requisito para adjuntar archivos al formato de cumplimiento PDF/A, le recomendamos usar el valor PDF_A_3A de la enumeración com.aspose.pdf.PdfFormat. El PDF/A_3a es el formato que proporciona la función para adjuntar cualquier formato de archivo como un adjunto a un archivo compatible con PDF/A. Sin embargo, una vez que el archivo está adjunto, debe convertirlo nuevamente al formato Pdf-3a, para corregir los metadatos. Por favor, eche un vistazo al siguiente fragmento de código.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir a documento compatible con PDF/A
        // Durante el proceso de conversión, también se realiza la validación
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Guardar documento de salida
        try {
            // cargar archivo XML
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Archivo xml de muestra");
            // Agregar adjunto a la colección de adjuntos del documento
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```