---
title: Concatenar documentos PDF
type: docs
weight: 10
url: /java/concatenate-pdf-documents/
description: Esta sección explica cómo concatenar documentos PDF con com.aspose.pdf.facades utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Concatenar archivos PDF usando rutas de archivos (Facades)

El método concatenate de la clase [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) se puede usar para concatenar dos archivos PDF. El método concatenate te permite pasar tres parámetros: primer PDF de entrada, segundo PDF de entrada y PDF de salida. El PDF de salida final contiene ambos archivos PDF de entrada.

El siguiente fragmento de código te muestra cómo concatenar archivos PDF usando rutas de archivos.

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // Crear objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Concatenar archivos
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


En algunos casos, cuando hay muchos esquemas, los usuarios pueden desactivarlos configurando **CopyOutlines** en false y mejorar el rendimiento de la concatenación.

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // Crear objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Concatenar archivos
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## Concatenar múltiples archivos PDF usando MemoryStreams

El método [Concatenate]https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) toma los archivos PDF de origen y el archivo PDF de destino como parámetros.
 Estos parámetros pueden ser rutas a los archivos PDF en el disco o podrían ser MemoryStreams. Ahora, para este ejemplo, primero crearemos dos flujos de archivos para leer los archivos PDF desde el disco. Luego convertiremos estos archivos en matrices de bytes. Estas matrices de bytes de los archivos PDF se convertirán en MemoryStreams. Una vez que obtengamos los MemoryStreams de los archivos PDF, podremos pasarlos al método de concatenación y fusionarlos en un único archivo de salida.

El siguiente fragmento de código te muestra cómo concatenar múltiples archivos PDF usando MemoryStreams:

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // Crear dos flujos de archivos para leer archivos pdf
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // Crear matrices de bytes para mantener el contenido de los archivos PDF
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // Leer el contenido del archivo PDF en matrices de bytes
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Ahora, primero convertir matrices de bytes en MemoryStreams y luego concatenar esos streams
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // Crear instancia de la clase PdfFileEditor para concatenar streams
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // Concatenar ambos MemoryStreams de entrada y guardar en un MemoryStream de salida
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convertir MemoryStream de nuevo a matriz de bytes
                        byte[] data = pdfStream.ToArray();
                        // Crear un FileStream para guardar el archivo PDF de salida
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // Escribir el contenido de la matriz de bytes en el flujo de archivo de salida
                        output.Write(data, 0, data.Length);
                        // Cerrar archivo de salida
                        output.Close();
                    }
                }
            }
            // Cerrar archivos de entrada
            fs1.Close();
            fs2.Close();
        }
```

## Concatenar Array de Archivos PDF Usando Rutas de Archivos (Facades)

Si desea concatenar múltiples archivos PDF, puede usar la sobrecarga del método de concatenación, que le permite pasar un array de rutas de archivos PDF. El resultado final se guarda como un archivo fusionado creado a partir de todos los archivos en el array.

El siguiente fragmento de código le muestra cómo concatenar un array de archivos PDF usando rutas de archivos.

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // Crear objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Array de archivos
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // Concatenar archivos
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## Concatenar Array de Archivos PDF Usando Streams (Facades)

La concatenación de un array de archivos PDF no se limita solo a archivos que residen en el disco.
 También puedes concatenar un array de archivos PDF desde flujos. Si deseas concatenar múltiples archivos PDF, puedes usar la sobrecarga apropiada del método Concatenate. Primero, necesitas crear un array de flujos de entrada y un flujo para el PDF de salida y luego llamar al método Concatenate. La salida se guardará en el flujo de salida.

El siguiente fragmento de código te muestra cómo concatenar un array de archivos PDF usando flujos.

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // Crear objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Array de flujos
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // Flujo de salida
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // Concatenar archivo
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## Concatenar Formularios PDF y mantener los nombres de los campos únicos

La clase [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) en el espacio de nombres [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) ofrece la capacidad de concatenar los archivos PDF.
 Ahora, si los archivos Pdf que se van a concatenar tienen campos de formulario con nombres de campo similares, Aspose.PDF proporciona la función para mantener los campos en el archivo Pdf resultante como únicos y también puede especificar el sufijo para hacer que los nombres de los campos sean únicos. El método [KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) de PdfFileEditor como verdadero hará que los nombres de los campos sean únicos cuando se concatenen formularios Pdf. Además, el método [UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) de PdfFileEditor se puede usar para especificar el formato definido por el usuario del sufijo que se agrega al nombre del campo para que sea único cuando los formularios se concatenan. Esta cadena debe contener la subcadena %NUM% que se reemplazará por números en el archivo resultante.

Por favor, vea el siguiente fragmento de código simple para lograr esta funcionalidad.

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // Establecer las rutas de archivo de entrada y salida

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // Instanciar objeto PdfFileEditor
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // Para mantener Id de campo único para todos los campos
                KeepFieldsUnique = true,
                // Formato del sufijo que se agrega al nombre del campo para hacerlo único cuando los formularios se concatenan.
                UniqueSuffix = "_%NUM%"
            };

            // Concatenar los archivos en un archivo Pdf resultante
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## Concatenar Insertar página en blanco

Una vez que los archivos PDF se hayan fusionado, podemos insertar una página en blanco al comienzo del documento en la que podemos crear un Índice. Para cumplir con este requisito, podemos cargar el archivo fusionado en un objeto Document y necesitamos llamar al método Page.Insert(…) para insertar una página en blanco.

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // Crear objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // Concatenar archivos
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```