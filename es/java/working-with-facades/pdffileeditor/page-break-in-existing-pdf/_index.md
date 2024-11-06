---
title: Salto de Página en un PDF Existente
type: docs
weight: 30
url: es/java/page-break-in-existing-pdf/
description: Esta sección explica cómo insertar saltos de página en un PDF existente usando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Como diseño predeterminado, los contenidos dentro de los archivos PDF se agregan en un diseño de Arriba-Izquierda a Abajo-Derecha. Una vez que los contenidos superan el margen inferior de la página, se produce el salto de página. Sin embargo, puede que tenga un requisito para insertar un salto de página dependiendo de la necesidad. Un método llamado AddPageBreak(...) se ha añadido en la clase [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) para cumplir con este requisito.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- src es el documento fuente/ruta al documento/flujo con documento fuente
- dest es el documento de destino/ruta donde el documento será guardado/flujo donde el documento será guardado
- PageBreak es un array de objetos de salto de página. Tiene dos propiedades: índice de la página donde se debe colocar el salto de página y posición vertical del salto de página en la página.

## Ejemplo 1 (Agregar salto de página)

```java
   public static void PageBrakeExample01() {
        // Instanciar instancia de Documento
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // Instanciar instancia de Documento en blanco
        Document dest = new Document();
        // Crear objeto PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // Guardar archivo resultante
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## Ejemplo 2

```java
  public static void PageBrakeExample02() {
        // Crear objeto PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## Ejemplo 3

```java
 public static void PageBrakeExample03() {
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```