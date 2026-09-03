---
title: Convertir PDF a PDF/A, PDF/E y PDF/X en Java
linktitle: Convertir PDF a PDF/A, PDF/E y PDF/X
type: docs
weight: 120
url: /es/java/convert-pdf-to-pdf_x/
lastmod: "2026-09-03"
description: Aprenda cómo convertir archivos PDF a PDF/A, PDF/E y PDF/X en Java con Aspose.PDF para flujos de trabajo de archivado, ingeniería, accesibilidad e impresión.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a formatos PDF/x
Abstract: Este artículo explica cómo validar y convertir documentos PDF a los formatos PDF/A, PDF/E y PDF/X usando Aspose.PDF for Java. Cubre la generación de registros, la preservación de adjuntos para PDF/A-3, la sustitución de fuentes faltantes, el etiquetado automático, la configuración del perfil ICC y la configuración de la intención de salida.
---
Aspose.PDF for Java puede validar y convertir archivos PDF estándar en estándares PDF de archivo e intercambio.

## Convertir PDF a PDF/A

Utilice este ejemplo cuando un PDF estándar deba convertirse en un documento de archivo compatible con PDF/A.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Llamar `document.convert(...)` con [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` y [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Escriba el registro de validación en un archivo XML adjunto para que los problemas de cumplimiento se registren durante la conversión.
1. Guarde la salida PDF/A validada.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Convertir PDF a PDF/E

Utilice este ejemplo cuando se deba convertir un PDF al estándar PDF/E orientado a la ingeniería.

1. Crear [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) para [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` y la ruta del archivo de registro deseada.
1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Llamar `document.convert(options)` por lo tanto, la conversión de cumplimiento se ejecuta con el objeto de opciones preparado.
1. Guarde el archivo PDF conforme resultante.

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

## Convertir PDF a PDF/X

Utilice este ejemplo cuando un PDF debe convertirse al estándar PDF/X orientado a la impresión.

1. Crear [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) para [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` y la ruta del archivo de registro deseada.
1. Configure un [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) como `FOGRA39` por lo que el perfil de color de destino de impresión se incrusta en la configuración de conversión.
1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instanciar y llamar `document.convert(options)`.
1. Guarde la salida PDF/X convertida.

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
