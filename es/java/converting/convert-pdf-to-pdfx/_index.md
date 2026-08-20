---
title: Convierta PDF a PDF/A, PDF/E y PDF/X en Java
linktitle: Convierta PDF a PDF/A, PDF/E y PDF/X
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-16"
description: Aprenda a convertir archivos PDF a PDF/A, PDF/E y PDF/X en Java con Aspose.PDF para flujos de trabajo de archivo, ingeniería, accesibilidad e impresión.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a formatos PDF/x
Abstract: Este artículo explica cómo validar y convertir documentos PDF a formatos PDF/A, PDF/E y PDF/X utilizando Aspose.PDF para Java. Cubre la generación de registros, la preservación de archivos adjuntos para PDF/A-3, la sustitución de fuentes faltantes, el etiquetado automático, la configuración del perfil ICC y la configuración de intención de salida.
---
Aspose.PDF para Java puede validar y convertir archivos PDF estándar en estándares PDF orientados al archivo y al intercambio.


## 
Convertir PDF a PDF/A



Utilice este ejemplo cuando deba convertir un PDF estándar en un documento de archivo compatible con PDF/A.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Llame a `document.convert(...)` con [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` y [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Escriba el registro de validación en un archivo XML complementario para que los problemas de cumplimiento se registren durante la conversión.

1. 
Guarde la salida PDF/A validada.


```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## 
Convertir PDF a PDF/E



Utilice este ejemplo cuando deba convertir un PDF al estándar PDF/E orientado a la ingeniería.


1. 
Cree [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) para [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` y la ruta del archivo de registro deseada.
1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Llame a `document.convert(options)` para que la conversión de cumplimiento se ejecute con el objeto de opciones preparado.

1. 
Guarde el archivo PDF compatible resultante.


```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## 
Convertir PDF a PDF/X



Utilice este ejemplo cuando deba convertir un PDF al estándar PDF/X orientado a impresión.

1. Cree [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) para [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` y la ruta del archivo de registro deseada.

1. 
Configure un [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) como `FOGRA39` para que el perfil de color de destino de impresión se incruste en la configuración de conversión.

1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y llame a `document.convert(options)`.

1. 
Guarde la salida PDF/X convertida.

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
