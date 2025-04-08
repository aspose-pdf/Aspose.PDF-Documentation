---
title: Tambahkan Gambar ke PDF menggunakan C#
linktitle: Tambahkan Gambar
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/add-image-to-existing-pdf-file/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang sudah ada menggunakan pustaka C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image to PDF using C#",
    "alternativeHeadline": "Add Images PDFs in C#",
    "abstract": "Fungsi baru dalam pustaka Aspose.PDF memungkinkan pengguna untuk dengan mudah menambahkan gambar ke file PDF yang sudah ada menggunakan C#. Fitur ini menyederhanakan manipulasi PDF dengan memungkinkan penempatan dan skala gambar yang tepat langsung dalam dokumen, memastikan integrasi berkualitas tinggi dan kontrol atas elemen visual. Dengan dukungan untuk berbagai format dan konfigurasi gambar, alat ini meningkatkan fleksibilitas manajemen konten PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Image to PDF, C#, Aspose.PDF, PDF document generation, image compression, image aspect ratio, PDF file manipulation, add image method, XImage class, clipping mask",
    "wordcount": "1921",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2025-04-08",
    "description": "Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang sudah ada menggunakan pustaka C#."
}
</script>

## Tambahkan Gambar dalam File PDF yang Ada

Setiap halaman PDF berisi properti Resources dan Contents. Resources dapat berupa gambar dan formulir misalnya, sementara konten diwakili oleh sekumpulan operator PDF. Setiap operator memiliki nama dan argumennya. Contoh ini menggunakan operator untuk menambahkan gambar ke file PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Untuk menambahkan gambar ke file PDF yang sudah ada:

- Buat objek Document dan buka dokumen PDF input.
- Ambil halaman yang ingin Anda tambahkan gambar.
- Tambahkan gambar ke koleksi Resources halaman.
- Gunakan operator untuk menempatkan gambar di halaman:
- Gunakan operator GSave untuk menyimpan keadaan grafis saat ini.
- Gunakan operator ConcatenateMatrix untuk menentukan di mana gambar akan ditempatkan.
- Gunakan operator Do untuk menggambar gambar di halaman.
- Terakhir, gunakan operator GRestore untuk menyimpan keadaan grafis yang diperbarui.
- Simpan file.
Potongan kode berikut menunjukkan cara menambahkan gambar dalam dokumen PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where image needs to be added
        var page = document.Pages[1];

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "AddImage.jpg", FileMode.Open))
        {
            // Add image to Images collection of Page Resources
            page.Resources.Images.Add(imageStream);

            // Using GSave operator: this operator saves the current graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GSave());

            // Create Rectangle and Matrix objects to define image positioning
            var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
            var matrix = new Aspose.Pdf.Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });

            // Using ConcatenateMatrix operator: defines how the image must be placed
            page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

            // Retrieve the added image and use Do operator to draw it
            var ximage = page.Resources.Images[page.Resources.Images.Count];
            page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

            // Using GRestore operator: this operator restores the graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
        }

        // Save PDF document
        document.Save(dataDir + "AddImage_out.pdf");
    }
}
```

{{% alert color="primary" %}}

Secara default, kualitas JPEG diatur ke 100%. Untuk menerapkan kompresi dan kualitas yang lebih baik, gunakan overload berikut:

{{% /alert %}}

- overload metode Replace ditambahkan ke kelas XImageCollection: public void Replace(int index, Stream stream, int quality)
- overload metode Add ditambahkan ke kelas XImageCollection: public void Add(Stam stream, int quality)

## Tambahkan Gambar dalam File PDF yang Ada (Facade)

Ada juga cara alternatif yang lebih mudah untuk menambahkan Gambar ke file PDF. Anda dapat menggunakan metode [AddImage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) dari kelas [PdfFileMend](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend). Metode [AddImage](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) memerlukan gambar yang akan ditambahkan, nomor halaman di mana gambar perlu ditambahkan dan informasi koordinat. Setelah itu, simpan file PDF yang diperbarui menggunakan metode Close. Potongan kode berikut menunjukkan cara menambahkan gambar dalam file PDF yang sudah ada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDFUsingPdfFileMender()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add first page with specified size
        var page = document.Pages.Add();
        page.SetPageSize(Aspose.Pdf.PageSize.A3.Height, Aspose.Pdf.PageSize.A3.Width);

        // Add second page
        page = document.Pages.Add();

        // Create PdfFileMend object
        var mender = new Aspose.Pdf.Facades.PdfFileMend(document);

        // Add image to the first page using the mender
        mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);

        // Save PDF document
        document.Save(dataDir + "AddImageMender_out.pdf");
    }
}
```

Terkadang, perlu untuk memotong gambar sebelum menyisipkannya ke dalam PDF. Anda dapat menggunakan metode `AddImage()` untuk mendukung penambahan gambar yang dipotong:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");
    var outputPdfFileName = dataDir + "Example-add-image-mender.pdf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (var imgStream = File.OpenRead(imageFileName))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document to the specified file path
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## Tempatkan gambar di halaman dan pertahankan (kontrol) rasio aspek

Jika kita tidak mengetahui dimensi gambar, ada kemungkinan besar mendapatkan gambar yang terdistorsi di halaman. Contoh berikut menunjukkan salah satu cara untuk menghindari hal ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Load the image
    using (var bitmap = System.Drawing.Image.FromFile(dataDir + "InputImage.jpg"))
    {
        // Get the original width and height of the image
        int width = bitmap.Width;
        int height = bitmap.Height;

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Define the scaled width and height while preserving the aspect ratio
            int scaledWidth = 400;
            int scaledHeight = scaledWidth * height / width;

            // Add the image to the page
            page.AddImage(dataDir + "InputImage.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));

            // Save PDF document
            document.Save(dataDir + "PreserveAspectRatio.pdf");
        }
    }
}
```

Terkadang, gambar besar mengalami masalah skala saat ditambahkan ke PDF. Potongan kode berikut menskalakan gambar sesuai dengan dimensi halaman PDF, memastikan gambar pas dengan baik dan terlihat lebih baik.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();
    var file = dataDir + "AddImageAccordingToPage.jpg";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var pdfImageSection = document.Pages.Add();
        using (var stream = new FileStream(file, FileMode.Open))
        {
            // Open bitmap
            using (var img = new Bitmap(stream))
            {
                //Scale image according to page dimensions
                using (var scaledImg = ScaleImage(img, (int)pdfImageSection.PageInfo.Width, (int)pdfImageSection.PageInfo.Height))
                {
                    using (var ms = new MemoryStream())
                    {
                        scaledImg.Save(ms, ImageFormat.Jpeg);
                        ms.Seek(0, SeekOrigin.Begin);
                        var image = new Aspose.Pdf.Image
                        {
                            ImageStream = ms
                        };

                        // Add the image to the page
                        pdfImageSection.Paragraphs.Add(image);

                        // Save PDF document
                        document.Save("AddImageAccordingToPage.pdf");
                    }
                }
            }
        }
    }
}

private static Image ScaleImage(Image image, int maxWidth, int maxHeight)
{
    var ratioX = (double)maxWidth / image.Width;
    var ratioY = (double)maxHeight / image.Height;
    var ratio = Math.Min(ratioX, ratioY);
    var newWidth = (int)(image.Width * ratio);
    var newHeight = (int)(image.Height * ratio);
    var newImage = new Bitmap(newWidth, newHeight);
    using (var graphics = System.Drawing.Graphics.FromImage(newImage))
    {
        graphics.DrawImage(image, 0, 0, newWidth, newHeight);
    }
    return newImage;
}
```

## Identifikasi apakah gambar di dalam PDF berwarna atau Hitam & Putih

Berbagai jenis kompresi dapat diterapkan pada gambar untuk mengurangi ukurannya. Jenis kompresi yang diterapkan pada gambar tergantung pada ColorSpace dari gambar sumber yaitu jika gambar berwarna (RGB), maka terapkan kompresi JPEG2000, dan jika hitam & putih, maka kompresi JBIG2/JBIG2000 harus diterapkan. Oleh karena itu, mengidentifikasi setiap jenis gambar dan menggunakan jenis kompresi yang sesuai akan menghasilkan output terbaik/yang dioptimalkan.

File PDF dapat berisi elemen Teks, Gambar, Grafik, Lampiran, Anotasi, dll dan jika file PDF sumber berisi gambar, kita dapat menentukan ruang warna gambar dan menerapkan kompresi yang sesuai untuk gambar guna mengurangi ukuran file PDF. Potongan kode berikut menunjukkan langkah-langkah untuk mengidentifikasi apakah gambar di dalam PDF berwarna atau Hitam & Putih.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageTypesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Counters for grayscale and RGB images
    int grayscaled = 0;
    int rgb = 0;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            Console.WriteLine("--------------------------------");
            var abs = new Aspose.Pdf.ImagePlacementAbsorber();
            page.Accept(abs);

            // Get the count of images on the current page
            Console.WriteLine("Total Images = {0} on page number {1}", abs.ImagePlacements.Count, page.Number);

            // Iterate through all the image placements on the page
            int image_counter = 1;
            foreach (Aspose.Pdf.ImagePlacement ia in abs.ImagePlacements)
            {
                // Determine the color type of the image
                var colorType = ia.Image.GetColorType();
                switch (colorType)
                {
                    case Aspose.Pdf.ColorType.Grayscale:
                        ++grayscaled;
                        Console.WriteLine("Image {0} is Grayscale...", image_counter);
                        break;
                    case Aspose.Pdf.ColorType.Rgb:
                        ++rgb;
                        Console.WriteLine("Image {0} is RGB...", image_counter);
                        break;
                }
                image_counter += 1;
            }
        }
    }
}
```

## Kontrol Kualitas Gambar

Dimungkinkan untuk mengontrol kualitas gambar yang ditambahkan ke file PDF. Gunakan metode [Replace](https://reference.aspose.com/pdf/id/net/aspose.pdf.ximagecollection/replace/methods/1) yang di-overload dalam kelas [XImageCollection](https://reference.aspose.com/pdf/id/net/aspose.pdf/ximagecollection).

Potongan kode berikut menunjukkan cara mengonversi semua gambar dokumen menjadi JPEG yang menggunakan kualitas 80% untuk kompresi.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImagesInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            int idx = 1;
            // Iterate through all images in the page's resources
            foreach (Aspose.Pdf.XImage image in page.Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save the image as JPEG with 80% quality
                    image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
                    // Replace the image in the page's resources
                    page.Resources.Images.Replace(idx, imageStream, 80);
                    idx = idx + 1;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceImages_out.pdf");
    }
}
```

## Dukungan penerapan Topeng Pemotongan pada Gambar

Menempatkan bentuk vektor di atas gambar bitmap dasar berfungsi sebagai topeng, hanya mengekspos bagian dari desain dasar yang sejajar dengan bentuk vektor. Semua area di luar bentuk akan disembunyikan.

Potongan kode memuat PDF, membuka dua file gambar, dan menerapkan gambar tersebut sebagai topeng stensil pada dua gambar pertama di halaman pertama PDF.

Topeng stensil dapat ditambahkan dengan metode 'XImage.AddStencilMask(Stream maskStream)':

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>