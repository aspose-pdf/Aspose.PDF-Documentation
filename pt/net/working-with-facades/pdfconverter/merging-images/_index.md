---
title: Mesclar imagens
type: docs
weight: 20
url: pt/net/merge-images/
description: Esta seção explica como mesclar imagens e é possível salvar no formato Tiff.
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF 21.4 permite combinar imagens. O método [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) verifica o conteúdo de uma pasta específica e trabalha com o tipo especificado de arquivos nela. Ao trabalhar com a mesclagem de imagens, especificamos 'inputImagesStreams', Formato de Imagem e Modo de Mesclagem de Imagem (como exemplo - vertical) do nosso arquivo. Em seguida, salvamos nosso resultado em FileOutputStream.

Siga o próximo trecho de código para resolver sua tarefa:

## Mesclar Imagens

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

O segundo exemplo funciona da mesma forma que o anterior, mas as imagens mescladas serão salvas horizontalmente.

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

No terceiro exemplo, vamos mesclar as imagens centralizando-as. Duas horizontalmente, duas verticalmente.

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

Também, o Aspose.PDF para Java oferece a oportunidade de combinar imagens e salvá-las no formato Tiff, usando o [Método MergeImagesAsTiff](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).

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

Para salvar as imagens mescladas como uma imagem em uma página PDF, colocamos elas no imageStream, colocamos o resultado na página com o método addImage, onde especificamos as coordenadas onde queremos colocá-las.

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