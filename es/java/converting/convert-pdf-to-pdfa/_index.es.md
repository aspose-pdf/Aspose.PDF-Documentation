---
title: Convertir PDF a formatos PDF/A
linktitle: Convertir PDF a formatos PDF/A
type: docs
weight: 100
url: /java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF a un archivo PDF conforme con PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Java** le permite convertir un archivo PDF a un archivo PDF conforme con PDF/A. Antes de hacerlo, el archivo debe ser validado. Este artículo explica cómo.

Tenga en cuenta que seguimos Adobe Preflight para validar la conformidad con PDF/A. Todas las herramientas en el mercado tienen su propia "representación" de la conformidad con PDF/A. Por favor, consulte este artículo sobre [herramientas de validación de PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) como referencia. Elegimos productos de Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

Antes de convertir el PDF a un archivo conforme con PDF/A, valide el PDF utilizando el método de validación.
 El resultado de la validación se almacena en un archivo XML y luego este resultado también se pasa al método de conversión. También puedes especificar la acción para los elementos que no se pueden convertir usando la enumeración [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Conversión de PDF a PDF/A_1b

El siguiente fragmento de código muestra cómo convertir archivos PDF a PDF compatible con PDF/A-1b.

```java
// Abrir documento
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convertir a documento compatible con PDF/A
// Durante el proceso de conversión, también se realiza la validación
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// Guardar documento de salida
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

Para realizar solo la validación, utiliza la siguiente línea de código:

```java
// Abrir documento
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// Validar PDF para PDF/A-1a
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("Válido");
} else {
    System.out.println("No válido");
}
document.close();
```

## Conversión de PDF a PDF/A_3b

Desde [Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java), la API también admite la conversión de archivos PDF al formato PDF/A_3b.

```java
// Abrir documento
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convertir a documento compatible con PDF/A
// Durante el proceso de conversión, también se realiza la validación
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// Guardar documento de salida
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## Conversión de PDF a PDF/A_3a

Desde [Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java), la API también admite la conversión de archivos PDF al formato PDF/A_3a.

```java
// Abrir documento
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convertir a documento compatible con PDF/A
// Durante el proceso de conversión, también se realiza la validación
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// Guardar documento de salida
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## PDF to PDF/A_2a Conversion

A partir del lanzamiento de [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java), la API ofrece la funcionalidad de convertir archivos PDF al formato PDF/A3.

```java
    public static void ConvertPDFtoPDFa2a() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convertir a documento compatible con PDF/A
        // Durante el proceso de conversión, también se realiza la validación
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Guardar documento de salida
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF to PDF/A_3U Conversion

A partir del lanzamiento de Aspose.PDF for Java 17.2.0, la API ofrece la funcionalidad de convertir archivos PDF al formato PDF/A_3U.

```java
    public static void ConvertPDFtoPDFa3u() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convertir a documento compatible con PDF/A
        // Durante el proceso de conversión, también se realiza la validación
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Guardar documento de salida
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## Crear PDF/A-3 y adjuntar archivo XML

Aspose.PDF para Java ofrece la función de convertir archivos PDF al formato PDF/A y también admite la capacidad de agregar archivos como adjuntos a documentos PDF. En caso de que tenga el requisito de adjuntar archivos al formato de conformidad PDF/A, le recomendamos usar el valor PDF_A_3A de la enumeración com.aspose.pdf.PdfFormat. El PDF/A_3a es el formato que proporciona la función de adjuntar cualquier formato de archivo como un adjunto a un archivo compatible con PDF/A. Sin embargo, una vez que el archivo está adjunto, debe convertirlo nuevamente al formato Pdf-3a para corregir los metadatos. Por favor, observe el siguiente fragmento de código.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // añadir página al archivo PDF
        doc.getPages().add();
        // cargar archivo XML
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "Archivo xml de muestra");
        // Añadir adjunto a la colección de adjuntos del documento
        doc.getEmbeddedFiles().add(fileSpecification);
        // realizar la conversión a PDF/A_3a
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* o PDF_A_3B */, ConvertErrorAction.Delete);
        // guardar archivo PDF final
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF para Java te presenta una aplicación en línea gratuita ["PDF a PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a PDF/A con Aplicación Gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}