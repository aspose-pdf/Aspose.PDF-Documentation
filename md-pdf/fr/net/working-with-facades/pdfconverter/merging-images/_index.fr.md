---
title: Fusionner des images 
type: docs
weight: 20
url: /net/merge-images/
description: Cette section explique comment fusionner des images, et il est possible de sauvegarder au format Tiff.
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF 21.4 vous permet de combiner des images. La méthode [Fusionner des images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) vérifie le contenu d'un dossier spécifique et fonctionne avec le type de fichiers spécifié. Lorsqu'on travaille avec la fusion d'images, on spécifie 'inputImagesStreams', le format de l'image et le mode de fusion d'image (par exemple - vertical) de notre fichier. Ensuite, nous enregistrons notre résultat dans FileOutputStream.

Suivez l'extrait de code suivant pour résoudre votre tâche :

## Fusionner des images

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

Le deuxième exemple fonctionne de la même manière que le précédent, mais les images fusionnées seront enregistrées horizontalement.

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

Dans le troisième exemple, nous allons fusionner les images en les centrant. Deux horizontalement, deux verticalement.

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

Aussi, Aspose.PDF pour Java vous offre la possibilité de combiner des images et de les enregistrer au format Tiff, en utilisant la méthode [MergeImagesAsTiff](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).

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

Pour enregistrer les images fusionnées comme une seule image sur la page PDF, nous les plaçons dans le imageStream, plaçons le résultat sur la page avec la méthode addImage, où nous spécifions les coordonnées où nous voulons les placer.

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