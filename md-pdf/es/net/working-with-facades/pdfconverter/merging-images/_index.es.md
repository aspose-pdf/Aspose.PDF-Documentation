---
title: Unir imágenes
type: docs
weight: 20
url: /net/merge-images/
description: Esta sección explica cómo unir imágenes, y es posible guardar en formato Tiff.
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF 21.4 permite combinar imágenes. El método [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) verifica el contenido de una carpeta específica y trabaja con el tipo de archivos especificado en ella. Al trabajar con la fusión de imágenes, especificamos 'inputImagesStreams', Formato de Imagen y Modo de Fusión de Imagen (como ejemplo - vertical) de nuestro archivo. Luego guardamos nuestro resultado en FileOutputStream.

Siga el siguiente fragmento de código para resolver su tarea:

## Unir Imágenes

```csharp
public static class ExamplePdfConverter
    {
        private static readonly string _dataDir = @"C:\Samples\Facades\PdfConverter\";
        public static void MergeImages01()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
            {
                FileStream outputStream = new FileStream(_dataDir+"merged_images.jpg", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }
```

El segundo ejemplo funciona igual que el anterior, pero las imágenes fusionadas se guardarán horizontalmente.

```csharp
public static void MergeImages02()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Horizontal, 1, 1))
            {
                FileStream outputStream = new FileStream(_dataDir + "merged_images.jpg", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }
```

En el tercer ejemplo, fusionaremos las imágenes centrando las mismas. Dos horizontalmente, dos verticalmente.

```csharp
public static void MergeImages03()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Center, 2, 2))
            {
                FileStream outputStream = new FileStream(_dataDir + "merged_images.jpg", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }

```

También, Aspose.PDF para Java le ofrece la oportunidad de combinar imágenes y guardarlas en el formato Tiff, utilizando el [Método MergeImagesAsTiff](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).

```csharp
public static void MergeImages04()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImagesAsTiff(fileStreams))
            {
                FileStream outputStream = new FileStream(_dataDir + "merged_images.tiff", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }
```

Para guardar las imágenes combinadas como una sola imagen en la página del PDF, las colocamos en el imageStream, colocamos el resultado en la página con el método addImage, donde especificamos las coordenadas donde queremos colocarlas.

```csharp
   public static void MergeImages05()
        {
            var fileStreams = Directory.GetFiles(_dataDir, "cat*.jpg")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
            {
                MemoryStream outputStream = new MemoryStream();
                inputStream.CopyTo(outputStream);
                var document = new Document();
                var pages = document.Pages.Add();
                pages.AddImage(outputStream, new Rectangle(10,120,400,720));
                document.Save(_dataDir + "merged_images.pdf");
            }

        }
```