---
title: Anotasi Multimedia PDF menggunakan C#
linktitle: Anotasi Multimedia
type: docs
weight: 40
url: id/net/multimedia-annotation/
description: Aspose.PDF untuk .NET memungkinkan Anda untuk menambahkan, mendapatkan, dan menghapus anotasi multimedia dari dokumen PDF Anda.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotasi Multimedia PDF menggunakan C#",
    "alternativeHeadline": "Cara menambahkan Anotasi Multimedia dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, anotasi multimedia, anotasi layar, anotasi suara, anotasi widget, anotasi 3D",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET memungkinkan Anda untuk menambahkan, mendapatkan, dan menghapus anotasi multimedia dari dokumen PDF Anda."
}
</script>

Anotasi dalam dokumen PDF terkandung dalam koleksi Annotations dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Koleksi ini berisi semua anotasi untuk halaman tersebut saja: setiap halaman memiliki koleksi Annotations sendiri. Untuk menambahkan anotasi ke halaman tertentu, tambahkan ke koleksi Annotations halaman tersebut menggunakan metode Add.

Gunakan kelas [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) dalam namespace Aspose.PDF.InteractiveFeatures.Annotations untuk memasukkan file SWF sebagai anotasi dalam dokumen PDF. Anotasi layar menentukan wilayah halaman di mana klip media dapat diputar.

Ketika Anda perlu menambahkan tautan video eksternal dalam dokumen PDF, Anda dapat menggunakan [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
Anotasi Film mengandung grafis animasi dan suara yang akan dipresentasikan di layar komputer dan melalui speaker.

Anotasi [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) sebanding dengan anotasi teks kecuali bahwa bukan catatan teks, ia berisi suara yang direkam dari mikrofon komputer atau diimpor dari file.
Sebuah [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) seharusnya analog dengan anotasi teks kecuali daripada catatan teks, ia mengandung suara yang direkam dari mikrofon komputer atau diimpor dari file.

Namun, ketika ada kebutuhan untuk menyematkan media di dalam dokumen PDF, Anda perlu menggunakan [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

Berikut adalah metode/properti dari kelas RichMediaAnnotation yang dapat digunakan.

- Stream CustomPlayer { set; }: Memungkinkan pengaturan pemutar yang digunakan untuk memutar video.
- string CustomFlashVariables { set; }: Memungkinkan untuk mengatur variabel yang diteruskan ke aplikasi flash. Baris ini adalah set pasangan “key=value” yang dipisahkan dengan ‘&'.
- void AddCustomData(strig name, Stream data): Menambahkan data tambahan untuk pemutar. Misalnya source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: Event mengaktifkan pemutar; nilai yang mungkin adalah Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Mengatur data video/audio yang akan diputar.
- void SetContent(Stream stream, string name): Mengatur data video/audio untuk diputar.
- void Update(): Membuat struktur data anotasi. Metode ini harus dipanggil terakhir.
- void SetPoster(Stream): Mengatur poster video yaitu gambar yang ditampilkan ketika pemutar tidak aktif

Kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Tambahkan Anotasi Layar

Kode berikut menunjukkan cara menambahkan Anotasi Layar ke file PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;


namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // Jalur ke direktori dokumen.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // Muat file PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // Buat Anotasi Layar
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## Tambahkan Anotasi Suara

Berikut adalah cuplikan kode yang menunjukkan cara menambahkan Anotasi Suara ke file PDF:

```csharp
        public static void AddSoundAnnotation()
        {
            // Memuat file PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // Membuat Anotasi Suara
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "Demo Anotasi Suara",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## Tambahkan RichMediaAnnotation

Berikut adalah cuplikan kode yang menunjukkan cara menambahkan RichMediaAnnotation ke file PDF:
Potongan kode berikut menunjukkan cara menambahkan RichMediaAnnotation ke file PDF:

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //beri nama pada data video. Data ini akan disematkan ke dalam dokumen dengan nama ini dan dirujuk dari variabel flash dengan nama ini.
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //kita juga menggunakan skin untuk pemutar video
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //di sini kita harus menentukan aliran yang berisi kode pemutar video
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //susun baris variabel flash untuk pemutar. Harap dicatat bahwa pemutar yang berbeda mungkin memiliki format baris variabel flash yang berbeda. Rujuk ke dokumentasi untuk pemutar Anda.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //tambahkan kode skin.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //atur poster untuk video
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //atur konten video
            rma.SetContent(videoName, fs);

            //tentukan tipe konten (video)
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //aktifkan pemutar dengan klik
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //perbarui data anotasi. Metode ini harus dipanggil setelah semua penugasan/pengaturan. Metode ini menginisialisasi struktur data anotasi dan menyematkan data yang dibutuhkan.
            rma.Update();

            //tambahkan anotasi di halaman.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### Dapatkan MultimediaAnnotation

Silakan coba menggunakan potongan kode berikut untuk mendapatkan MultimediaAnnotation dari dokumen PDF.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // Memuat file PDF
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### Hapus MultimediaAnnotation

Potongan kode berikut menunjukkan cara Menghapus MultimediaAnnotation dari file PDF.

```csharp
        public static void DeletePolyAnnotation()
        {
            // Memuat file PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```
## Tambahkan Anotasi Widget

Formulir interaktif menggunakan [Anotasi Widget](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) untuk merepresentasikan tampilan dari bidang dan untuk mengelola interaksi pengguna.
Kami menggunakan elemen formulir ini yang ditambahkan ke PDF untuk memudahkan memasukkan, mengirimkan informasi, atau melakukan beberapa interaksi pengguna lainnya.

Anotasi Widget adalah representasi grafis dari suatu bidang formulir pada halaman tertentu, sehingga kami tidak dapat membuatnya secara langsung sebagai anotasi.

Setiap Anotasi Widget akan memiliki grafis (tampilan) yang sesuai tergantung pada tipe nya. Setelah dibuat, beberapa aspek visual tertentu dapat diubah, seperti gaya batas dan warna latar belakang.
Properti lain seperti warna teks dan font dapat diubah melalui bidang, setelah terlampir pada salah satunya.

Dalam beberapa kasus, Anda mungkin ingin suatu bidang muncul di lebih dari satu halaman, mengulangi nilai yang sama.
Dalam beberapa kasus, Anda mungkin ingin sebuah bidang muncul di lebih dari satu halaman, mengulang nilai yang sama.
Seseorang yang mengisi formulir dapat menggunakan salah satu widget tersebut untuk memperbarui nilai bidang, dan ini tercermin di semua widget lain juga.

Setiap bidang formulir untuk setiap tempat dalam dokumen mewakili satu Widget Anotasi. Data spesifik lokasi dari Widget Anotasi ditambahkan ke halaman tertentu. Setiap bidang formulir memiliki beberapa variasi. Tombol dapat berupa tombol radio, kotak centang, atau tombol tekan. Widget pilihan bisa berupa kotak daftar atau kotak kombinasi.

Dalam contoh ini, kita akan belajar cara menambahkan tombol-tombol untuk navigasi dalam dokumen.

### Tambahkan Tombol ke Dokumen

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "Cetak dokumen saat ini",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "Cetak Dokumen"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
Tombol ini memiliki batas dan mengatur latar belakang. Juga kami menetapkan nama tombol (Nama), tooltip (NamaAlternatif), label (KeteranganNormal), dan warna teks label (Warna).

### Menggunakan aksi navigasi dokumen

Ada contoh yang lebih kompleks dari penggunaan Anotasi Widget - navigasi dokumen dalam dokumen PDF. Ini mungkin diperlukan untuk menyiapkan presentasi dokumen PDF.

Contoh ini menunjukkan cara membuat 4 tombol:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
var normalCaptions = new[] { "First", "Prev", "Next", "Last" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

Kita harus membuat tombol-tombol tersebut tanpa melampirkannya ke halaman.
Kita harus membuat tombol-tombol tanpa melampirkannya ke halaman.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

Kita harus menduplikasi array tombol ini di setiap halaman dalam dokumen.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

Kami memanggil [Form.Add method](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) dengan parameter berikut: field, name, dan indeks halaman yang akan ditambahkan field tersebut.
Kami memanggil [Metode Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) dengan parameter berikut: field, nama, dan indeks halaman tempat field ini akan ditambahkan.

Dan untuk mendapatkan hasil penuh, kita perlu menonaktifkan tombol "First" dan "Prev" di halaman pertama serta tombol "Next" dan "Last" di halaman terakhir.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

Untuk informasi lebih detail dan kemungkinan fitur ini, lihat juga [Bekerja dengan Formulir](/pdf/net/acroforms/).

Dalam dokumen PDF, Anda dapat melihat dan mengelola konten 3D berkualitas tinggi yang dibuat dengan perangkat lunak CAD 3D atau pemodelan 3D dan tertanam dalam dokumen PDF. Dapat memutar elemen 3D ke semua arah seolah-olah Anda sedang memegangnya di tangan.

Mengapa Anda memerlukan tampilan gambar 3D sama sekali?

Selama beberapa tahun terakhir, teknologi telah membuat terobosan besar di semua area berkat pencetakan 3D.
Dalam beberapa tahun terakhir, teknologi telah membuat terobosan besar di semua area berkat pencetakan 3D. dan guru.

Tugas utama dari pemodelan 3D adalah gagasan tentang objek masa depan atau objek karena, untuk mengeluarkan objek, Anda memerlukan pemahaman tentang fitur desainnya secara detail untuk regenerasi berurutan dalam desain industri atau arsitektur.

## Tambahkan Anotasi 3D

Anotasi 3D ditambahkan menggunakan model yang dibuat dalam format U3D.

1. Buat dokumen baru [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Muat data model 3D yang diinginkan (dalam kasus kami "Ring.u3d") untuk membuat [KontenPDF3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)
1. Buat objek [KaryaSeni3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) dan hubungkan ke dokumen dan Konten3D
1. Atur objek karyaSeniPDF3D:

    - SkemaPencahayaan3D - (kami akan mengatur `CAD` dalam contoh)
    - ModeRender3D - (kami akan mengatur `Solid` dalam contoh)
    - Isi `ViewArray`, buat setidaknya satu [Tampilan 3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) dan tambahkan ke array.
- Isi `ViewArray`, buat setidaknya satu [Tampilan 3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) dan tambahkan ke dalam array.

1. Atur 3 parameter dasar dalam anotasi:
   - `page` di mana anotasi akan ditempatkan,
   - `rectangle`, di dalamnya anotasi,
   - dan objek `3dArtWork`.
1. Untuk presentasi objek 3D yang lebih baik, atur Bingkai Batas
1. Atur tampilan default (contohnya - ATAS)
1. Tambahkan beberapa parameter tambahan: nama, poster pratinjau dll.
1. Tambahkan Anotasi ke [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. Simpan hasilnya

### Contoh

Silakan periksa cuplikan kode berikut untuk menambahkan Anotasi 3D.

```csharp
    public static void Add3dAnnotation()
    {
    // Muat file PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Name = "Ring.u3d";
    //atur gambar pratinjau jika diperlukan
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
Contoh kode ini menunjukkan model seperti ini:

![Demo Anotasi 3D](3d_demo.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
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

