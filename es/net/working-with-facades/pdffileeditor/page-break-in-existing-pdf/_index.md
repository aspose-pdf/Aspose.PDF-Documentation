---
title: Salto de Página en PDF existente
type: docs
weight: 30
url: es/net/page-break-in-existing-pdf/
description: Esta sección explica cómo insertar saltos de página en un PDF existente utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Como diseño predeterminado, los contenidos dentro de los archivos PDF se añaden en un diseño de Arriba-Izquierda a Abajo-Derecha. Una vez que los contenidos superan el margen inferior de la página, se produce el salto de página. Sin embargo, puede que te encuentres con la necesidad de insertar un salto de página dependiendo de la necesidad. Se ha añadido un método llamado AddPageBreak(...) en la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) para cumplir con este requisito.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/addpagebreak)

- src es documento fuente/ruta al documento/corriente con documento fuente
- dest es documento de destino/ruta donde se guardará el documento/corriente donde se guardará el documento
- PageBreak es un arreglo de objetos de salto de página. Tiene dos propiedades: índice de la página donde se debe colocar el salto de página y posición vertical del salto de página en la página.

## Ejemplo 1 (Agregar salto de página)

```csharp
public static void PageBrakeExample01()
{
    // Instanciar instancia de Documento
    Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
    // Instanciar instancia de Documento en blanco
    Document dest = new Document();
    // Crear objeto PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[]
    {
        new PdfFileEditor.PageBreak(1, 450)
    });
    // Guardar archivo resultante
    dest.Save(_dataDir + "PageBreak_out.pdf");
}
```
## Ejemplo 2

```csharp
public static void PageBrakeExample02()
{
    // Crear objeto PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();

    fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf",
        _dataDir + "PageBreakWithDestPath_out.pdf",
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
}
```

## Ejemplo 3

```csharp
public static void PageBrakeExample03()
{
    Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
    Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(src, dest,
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
    dest.Close();
    src.Close();
}
```