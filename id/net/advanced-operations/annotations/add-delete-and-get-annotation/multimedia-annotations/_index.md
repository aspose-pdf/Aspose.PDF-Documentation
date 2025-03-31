---
title: Anotasi Multimedia PDF menggunakan C#
linktitle: Anotasi Multimedia
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/multimedia-annotation/
description: Aspose.PDF for .NET memungkinkan Anda untuk menambahkan, mendapatkan, dan menghapus anotasi multimedia dari dokumen PDF Anda.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Multimedia Annotation using C#",
    "alternativeHeadline": "Enable Multimedia Annotations in PDF with C#",
    "abstract": "Aspose.PDF for .NET memperkenalkan kemampuan anotasi multimedia yang canggih, memungkinkan pengguna untuk dengan mudah menambahkan, mengambil, dan menghapus berbagai jenis multimedia dalam dokumen PDF. Fitur ini mendukung anotasi layar, suara, dan media kaya, meningkatkan interaktivitas dokumen dan memungkinkan integrasi konten video eksternal, catatan audio, dan media tertanam, menjadikan dokumen PDF lebih dinamis dan menarik.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF multimedia annotation, Aspose.PDF, C# PDF features, screen annotation, sound annotation, rich media annotation, widget annotations, 3D annotation, document navigation, multimedia file embedding",
    "wordcount": "2247",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Anotasi dalam dokumen PDF terdapat dalam koleksi Annotations objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Koleksi ini berisi semua anotasi untuk halaman individu tersebut saja: setiap halaman memiliki koleksi Annotations-nya sendiri. Untuk menambahkan anotasi ke halaman tertentu, tambahkan ke koleksi Annotations halaman tersebut menggunakan metode Add.

Gunakan kelas [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) dalam namespace Aspose.PDF.InteractiveFeatures.Annotations untuk menyertakan file SWF sebagai anotasi dalam dokumen PDF. Anotasi layar menentukan area halaman di mana klip media dapat diputar.

Ketika Anda perlu menambahkan tautan video eksternal dalam dokumen PDF, Anda dapat menggunakan [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
Anotasi Film berisi grafik animasi dan suara yang ditampilkan di layar komputer dan melalui speaker.

Anotasi [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) akan serupa dengan anotasi teks kecuali bahwa alih-alih catatan teks, ia berisi suara yang direkam dari mikrofon komputer atau diimpor dari file. Ketika anotasi diaktifkan, suara akan diputar. Anotasi akan berperilaku seperti anotasi teks dalam banyak hal, dengan ikon yang berbeda (secara default, sebuah speaker) untuk menunjukkan bahwa ia mewakili suara.

Namun, ketika ada kebutuhan untuk menyematkan media di dalam dokumen PDF, Anda perlu menggunakan [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

Metode/properti berikut dari kelas RichMediaAnnotation dapat digunakan.

- Stream CustomPlayer { set; }: Memungkinkan pengaturan pemutar yang digunakan untuk memutar video.
- string CustomFlashVariables { set; }: Memungkinkan untuk mengatur variabel yang diteruskan ke aplikasi flash. Baris ini adalah set pasangan “key=value” yang dipisahkan dengan ‘&'.
- void AddCustomData(strig name, Stream data): Tambahkan data tambahan untuk pemutar. Misalnya source=video.mp4&autoPlay=true&scale=100.
- ActivationEvent ActivateOn { get; set}: Event mengaktifkan pemutar; nilai yang mungkin adalah Click, PageOpen, PageVisible.
- void SetContent(Stream stream, string name): Set data video/audio yang akan diputar.
- void Update(): Buat struktur data dari anotasi. Metode ini harus dipanggil terakhir.
- void SetPoster(Stream): Set poster video yaitu gambar yang ditampilkan ketika pemutar tidak aktif.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Tambahkan Anotasi Layar

Potongan kode berikut menunjukkan cara menambahkan Anotasi Layar ke file PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddScreenAnnotationWithMedia()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (cument = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Path to the media file (SWF)
        var mediaFile = dataDir + "input.swf";

        // Create Screen Annotation
        var screenAnnotation = new Aspose.Pdf.Annotations.ScreenAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(170, 190, 470, 380),
            mediaFile);

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(screenAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddScreenAnnotationWithMedia_out.pdf");
    }
}
```

## Tambahkan Anotasi Suara

Potongan kode berikut menunjukkan cara menambahkan Anotasi Suara ke file PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSoundAnnotation()
{
    // Open PDF document
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        var mediaFile = dataDir + "file_example_WAV_1MG.wav";

        // Create Sound Annotation
        var soundAnnotation = new Aspose.Pdf.Annotations.SoundAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(20, 700, 60, 740),
            mediaFile)
        {
            Color = Aspose.Pdf.Color.Blue,
            Title = "John Smith",
            Subject = "Sound Annotation demo",
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(20, 700, 60, 740))
        };

        document.Pages[1].Annotations.Add(soundAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddSoundAnnotation_out.pdf");
    }
}
```

## Tambahkan RichMediaAnnotation

Potongan kode berikut menunjukkan cara menambahkan RichMediaAnnotation ke file PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRichMediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
        Page page = document.Pages.Add();

        // Define video and poster names
        const string videoName = "file_example_MP4_480_1_5MG.mp4";
        const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        string skinName = "SkinOverAllNoFullNoCaption.swf";

        // Create RichMediaAnnotation
        var rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600));

        // Specify the stream containing the video player code
        rma.CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp, "Players", "Videoplayer.swf"), FileMode.Open, FileAccess.Read);

        // Compose flash variables line for the player
        rma.CustomFlashVariables = $"source={videoName}&skin={skinName}";

        // Add skin code
        rma.AddCustomData(skinName, new FileStream(Path.Combine(pathToAdobeApp, skinName), FileMode.Open, FileAccess.Read));

        // Set poster for the video
        rma.SetPoster(new FileStream(Path.Combine(dataDir, posterName), FileMode.Open, FileAccess.Read));

        // Set video content
        using (Stream fs = new FileStream(Path.Combine(dataDir, videoName), FileMode.Open, FileAccess.Read))
        {
            rma.SetContent(videoName, fs);
        }

        // Set type of the content (video)
        rma.Type = RichMediaAnnotation.ContentType.Video;

        // Activate player by click
        rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

        // Update annotation data
        rma.Update();

        // Add annotation to the page
        page.Annotations.Add(rma);

        // Save PDF document
        document.Save(dataDir + "RichMediaAnnotation_out.pdf");
    }
}
```

### Dapatkan MultimediaAnnotation

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan MultimediaAnnotation dari dokumen PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMultimediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get multimedia annotations (Screen, Sound, RichMedia)
        var mediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Screen
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Sound
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.Annotation>();

        // Iterate through the annotations and print their details
        foreach (var ma in mediaAnnotations)
        {
            Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
        }
    }
}
```

### Hapus MultimediaAnnotation

Potongan kode berikut menunjukkan cara Menghapus MultimediaAnnotation dari file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolyAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get RichMedia annotations
        var richMediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.RichMediaAnnotation>();

        // Delete each RichMedia annotation
        foreach (var rma in richMediaAnnotations)
        {
            document.Pages[1].Annotations.Delete(rma);
        }

        // Save PDF document
        document.Save(dataDir + "DeletePolyAnnotation_out.pdf");
    }
}
```

## Tambahkan Anotasi Widget

Formulir interaktif menggunakan [Widget Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) untuk mewakili penampilan bidang dan untuk mengelola interaksi pengguna.
Kami menggunakan elemen formulir ini yang ditambahkan ke PDF untuk memudahkan memasukkan, mengirim informasi, atau melakukan beberapa interaksi pengguna lainnya.

Anotasi Widget adalah representasi grafis dari bidang formulir di halaman tertentu, jadi kami tidak dapat membuatnya langsung sebagai anotasi.

Setiap Anotasi Widget akan memiliki grafik yang sesuai (penampilan) tergantung pada jenisnya. Setelah dibuat, aspek visual tertentu dapat diubah, seperti gaya batas dan warna latar belakang.
Properti lain seperti warna teks dan font dapat diubah melalui bidang, setelah terpasang pada salah satu.

Dalam beberapa kasus, Anda mungkin ingin bidang muncul di lebih dari satu halaman, mengulangi nilai yang sama. Dalam hal itu, bidang yang biasanya hanya memiliki satu widget mungkin memiliki beberapa widget yang terpasang: TextField, ListBox, ComboBox, dan CheckBox biasanya memiliki tepat satu, sementara RadioGroup memiliki beberapa widget, satu untuk setiap tombol radio.
Seseorang yang mengisi formulir dapat menggunakan salah satu dari widget tersebut untuk memperbarui nilai bidang, dan ini tercermin di semua widget lainnya juga.

Setiap bidang formulir untuk setiap tempat dalam dokumen mewakili satu Anotasi Widget. Data spesifik lokasi dari Anotasi Widget ditambahkan ke halaman tertentu. Setiap bidang formulir memiliki beberapa variasi. Sebuah tombol dapat berupa tombol radio, kotak centang, atau tombol tekan. Widget pilihan dapat berupa kotak daftar atau kotak kombo.

Dalam contoh ini, kita akan belajar bagaimana menambahkan tombol tekan untuk navigasi dalam dokumen.

### Tambahkan Tombol ke Dokumen

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPrintButton()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Define the rectangle for the button
        var rect = new Aspose.Pdf.Rectangle(72, 748, 164, 768);

        // Create a button field
        var printButton = new Aspose.Pdf.Forms.ButtonField(page, rect)
        {
            AlternateName = "Print current document",
            Color = Aspose.Pdf.Color.Black,
            PartialName = "printBtn1",
            NormalCaption = "Print Document"
        };

        // Set the border style for the button
        var border = new Aspose.Pdf.Annotations.Border(printButton)
        {
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
            Width = 2
        };
        printButton.Border = border;

        // Set the border and background color characteristics
        printButton.Characteristics.Border = System.Drawing.Color.FromArgb(255, 0, 0, 255);
        printButton.Characteristics.Background = System.Drawing.Color.FromArgb(255, 0, 191, 255);

        // Add the button to the form
        document.Form.Add(printButton);

        // Save PDF document
        document.Save(dataDir + "PrintButton_out.pdf");
    }
}
```

Tombol ini memiliki batas dan mengatur latar belakang. Juga kami mengatur nama tombol (Name), tooltip (AlternateName), label (NormalCaption), dan warna teks label (Color).

### Menggunakan Aksi Navigasi Dokumen

Ada contoh yang lebih kompleks dari penggunaan Anotasi Widget - navigasi dokumen dalam dokumen PDF. Ini mungkin diperlukan untuk menyiapkan presentasi dokumen PDF.

Contoh ini menunjukkan cara membuat 4 tombol:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNavigationButtons()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "JSON Fundamenals.pdf"))
    {
        // Create an array of button fields
        var buttons = new Aspose.Pdf.Forms.ButtonField[4];

        // Define alternate names and normal captions for the buttons
        var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
        var normalCaptions = new[] { "First", "Prev", "Next", "Last" };

        // Define predefined actions for the buttons
        PredefinedAction[] actions = {
            PredefinedAction.FirstPage,
            PredefinedAction.PrevPage,
            PredefinedAction.NextPage,
            PredefinedAction.LastPage
        };

        // Define border and background colors
        var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
        var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);

        // We should create the buttons without attaching them to the page.
        for (var i = 0; i < 4; i++)
        {
            buttons[i] = new Aspose.Pdf.Forms.ButtonField(document, new Aspose.Pdf.Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
            {
                AlternateName = alternateNames[i],
                Color = Aspose.Pdf.Color.White,
                NormalCaption = normalCaptions[i],
                OnActivated = new Aspose.Pdf.Annotations.NamedAction(actions[i])
            };

            // Set the border style for the button
            buttons[i].Border = new Aspose.Pdf.Annotations.Border(buttons[i])
            {
                Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
                Width = 2
            };

            // Set the border and background color characteristics
            buttons[i].Characteristics.Border = clrBorder;
            buttons[i].Characteristics.Background = clrBackGround;
        }

        // Duplicate the array of buttons on each page in the document
        for (var pageIndex = 1; pageIndex <= document.Pages.Count; pageIndex++)
        {
            for (var i = 0; i < 4; i++)
            {
                document.Form.Add(buttons[i], $"btn{pageIndex}_{i + 1}", pageIndex);
            }
        }

        // Save PDF document
        document.Save(dataDir + "NavigationButtons_out.pdf");

        // We call Form.Add method with the following parameters: field, name, and the index of the pages that this field will be added to.
        // And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

        document.Form["btn1_1"].ReadOnly = true;
        document.Form["btn1_2"].ReadOnly = true;

        document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
        document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
    }
}
```

Untuk informasi lebih rinci dan kemungkinan fitur ini lihat juga [Bekerja dengan Formulir](/pdf/id/net/acroforms/).

Dalam dokumen PDF, Anda dapat melihat dan mengelola konten 3D berkualitas tinggi yang dibuat dengan perangkat lunak CAD 3D atau pemodelan 3D dan disematkan dalam dokumen PDF. Dapat memutar elemen 3D ke segala arah seolah-olah Anda memegangnya di tangan Anda.

Mengapa Anda membutuhkan tampilan 3D dari gambar sama sekali?

Selama beberapa tahun terakhir, teknologi telah membuat terobosan besar di semua bidang berkat pencetakan 3D. Teknologi pencetakan 3D dapat diterapkan untuk mengajarkan keterampilan teknologi dalam konstruksi, teknik mesin, desain sebagai alat utama. Teknologi ini berkat munculnya perangkat pencetakan pribadi dapat berkontribusi pada pengenalan bentuk baru organisasi proses pendidikan, meningkatkan motivasi, dan pembentukan kompetensi yang diperlukan dari lulusan dan pengajar.

Tugas utama pemodelan 3D adalah ide objek atau objek masa depan karena, untuk merilis objek, Anda perlu pemahaman tentang fitur desainnya secara detail untuk regenerasi berturut-turut dalam desain industri atau arsitektur.

## Tambahkan Anotasi 3D

Anotasi 3D ditambahkan menggunakan model yang dibuat dalam format U3D.

1. Buat [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) baru.
1. Muat data model 3D yang diinginkan (dalam kasus kami "Ring.u3d") untuk membuat [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent).
1. Buat objek [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) dan tautkan ke dokumen dan 3DContent.
1. Atur objek pdf3dArtWork:

    - 3DLightingScheme - (kami akan mengatur `CAD` dalam contoh)
    - 3DRenderMode - (kami akan mengatur `Solid` dalam contoh)
    - Isi `ViewArray`, buat setidaknya satu [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) dan tambahkan ke array.

1. Atur 3 parameter dasar dalam anotasi:
    - `page` di mana anotasi akan ditempatkan.
    - `rectangle`, di dalam mana anotasi.
    - dan objek `3dArtWork`.
1. Untuk presentasi yang lebih baik dari objek 3D, atur bingkai Batas.
1. Atur tampilan default (misalnya - TOP).
1. Tambahkan beberapa parameter tambahan: nama, poster pratinjau, dll.
1. Tambahkan Anotasi ke [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Simpan hasilnya.

### Contoh

Silakan periksa potongan kode berikut untuk menambahkan Anotasi 3D.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Add3dAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Load 3D content
        var pdf3DContent = new Aspose.Pdf.Annotations.PDF3DContent(dataDir + "Ring.u3d");

        // Create 3D artwork
        var pdf3dArtWork = new Aspose.Pdf.Annotations.PDF3DArtwork(document, pdf3DContent)
        {
            LightingScheme = new Aspose.Pdf.Annotations.PDF3DLightingScheme(Aspose.Pdf.Annotations.LightingSchemeType.CAD),
            RenderMode = new Aspose.Pdf.Annotations.PDF3DRenderMode(Aspose.Pdf.Annotations.RenderModeType.Solid),
        };

        // Define matrices for different views
        var topMatrix = new Aspose.Pdf.Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Aspose.Pdf.Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);

        // Add views to the 3D artwork
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        // Add page
        var page = document.Pages.Add();

        // Create a 3D annotation
        var pdf3dAnnotation = new Aspose.Pdf.Annotations.PDF3DAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.Border = new Aspose.Pdf.Annotations.Border(pdf3dAnnotation);
        pdf3dAnnotation.SetDefaultViewIndex(1);
        pdf3dAnnotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.NoZoom;
        pdf3dAnnotation.Name = "Ring.u3d";

        // Set preview image if needed
        // pdf3dAnnotation.SetImagePreview(dataDir + "sample_3d.png");

        // Add the 3D annotation to the page
        document.Pages[1].Annotations.Add(pdf3dAnnotation);

        // Save PDF document
        document.Save(dataDir + "Add3dAnnotation_out.pdf");
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