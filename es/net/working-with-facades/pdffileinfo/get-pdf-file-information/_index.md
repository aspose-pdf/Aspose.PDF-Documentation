---
title: Obtener información del archivo PDF
type: docs
weight: 50
url: /es/net/get-pdf-file-information/
description: Esta sección explica cómo obtener información de archivos PDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Para obtener información específica de un archivo PDF, necesitas crear un objeto de la clase [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Después de eso, puedes obtener los valores de las propiedades individuales como Asunto, Título, Palabras clave y Creador, etc.

El siguiente fragmento de código muestra cómo obtener la información del archivo PDF.

```csharp
 public static void GetPdfInfo()
        {
            // Abrir documento
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // Obtener información del PDF
            Console.WriteLine("Asunto: {0}", fileInfo.Subject);
            Console.WriteLine("Título: {0}", fileInfo.Title);
            Console.WriteLine("Palabras clave: {0}", fileInfo.Keywords);
            Console.WriteLine("Creador: {0}", fileInfo.Creator);
            Console.WriteLine("Fecha de creación: {0}", fileInfo.CreationDate);
            Console.WriteLine("Fecha de modificación: {0}", fileInfo.ModDate);
            // Encontrar si es un PDF válido y si también está encriptado
            Console.WriteLine("Es PDF válido: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("Está encriptado: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("Ancho de la página:{0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("Altura de la página:{0}", fileInfo.GetPageHeight(1));
        }
```

## Obtener Información Meta

Para obtener información, utilizamos la propiedad [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header). Con 'Hashtable' obtenemos todos los valores posibles.

```csharp
public static void GetMetaInfo()
        {
            // Crear instancia del objeto PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // Recuperar todos los atributos personalizados existentes
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // Recuperar un atributo personalizado
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```