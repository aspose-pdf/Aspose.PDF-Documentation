---
title: Menambahkan Teks ke PDF menggunakan C#
linktitle: Menambahkan Teks ke PDF
type: docs
weight: 10
url: /id/net/add-text-to-pdf-file/
description: Artikel ini menjelaskan berbagai aspek bekerja dengan teks dalam Aspose.PDF. Pelajari cara menambahkan teks ke PDF, menambahkan fragmen HTML, atau menggunakan font OTF khusus.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/add-text-to-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Teks ke PDF menggunakan C#",
    "alternativeHeadline": "Cara Menambahkan Teks ke PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen PDF",
    "keywords": "pdf, c#, menambahkan teks ke pdf",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan berbagai aspek bekerja dengan teks dalam Aspose.PDF. Pelajari cara menambahkan teks ke PDF, menambahkan fragmen HTML, atau menggunakan font OTF khusus."
}
</script>
Kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Untuk menambahkan teks ke file PDF yang ada:

1. Buka PDF masukan menggunakan objek Dokumen.
2. Dapatkan halaman tertentu di mana Anda ingin menambahkan teks.
3. Buat objek TextFragment dengan teks masukan bersama dengan properti teks lainnya. Objek TextBuilder yang dibuat dari halaman tertentu – tempat Anda ingin menambahkan teks – memungkinkan Anda untuk menambahkan objek TextFragment ke halaman menggunakan metode AppendText.
4. Panggil metode Save objek Dokumen dan simpan file PDF keluaran.

## Menambahkan Teks

Potongan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang ada.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "input.pdf");

// Dapatkan halaman tertentu
Page pdfPage = (Page)pdfDocument.Pages[1];

// Buat fragmen teks
TextFragment textFragment = new TextFragment("teks utama");
textFragment.Position = new Position(100, 600);

// Atur properti teks
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// Buat objek TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);

// Tambahkan fragmen teks ke halaman PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// Simpan dokumen PDF hasil.
pdfDocument.Save(dataDir);
```
## Memuat Font dari Stream

Potongan kode berikut menunjukkan cara memuat Font dari objek Stream saat menambahkan teks ke dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// Memuat file PDF masukan
Document doc = new Document(dataDir + "input.pdf");
// Membuat objek pembuat teks untuk halaman pertama dokumen
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Membuat fragmen teks dengan string contoh
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // Memuat font TrueType ke dalam objek stream
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // Mengatur nama font untuk string teks
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Menentukan posisi untuk Fragmen Teks
        textFragment.Position = new Position(10, 10);
        // Menambahkan teks ke TextBuilder agar dapat ditempatkan di atas file PDF
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // Menyimpan dokumen PDF hasil.
    doc.Save(dataDir);
}
```
## Menambahkan Teks menggunakan TextParagraph

Potongan kode berikut menunjukkan bagaimana menambahkan teks dalam dokumen PDF menggunakan kelas [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buka dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman dari objek Document
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// Buat paragraf teks
TextParagraph paragraph = new TextParagraph();
// Setel indentasi baris berikutnya
paragraph.SubsequentLinesIndent = 20;
// Tentukan lokasi untuk menambahkan TextParagraph
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// Tentukan mode pembungkusan kata
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// Buat fragmen teks
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// Tambahkan fragmen ke paragraf
paragraph.AppendLine(fragment1);
// Tambahkan paragraf
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// Simpan dokumen PDF hasil.
doc.Save(dataDir);
```
## Menambahkan Tautan ke TextSegment

Sebuah halaman PDF mungkin terdiri dari satu atau lebih objek TextFragment, di mana setiap objek TextFragment dapat memiliki satu atau lebih instance TextSegment. Untuk mengatur tautan hyperlink untuk TextSegment, properti Hyperlink dari kelas [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) dapat digunakan sambil menyediakan objek dari instance Aspose.Pdf.WebHyperlink. Silakan coba menggunakan potongan kode berikut untuk mencapai persyaratan ini.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buat instansi dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman file PDF
Page page1 = doc.Pages.Add();
// Buat instansi TextFragment
TextFragment tf = new TextFragment("Contoh Fragment Teks");
// Atur penyelarasan horizontal untuk TextFragment
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// Buat textsegment dengan teks contoh
TextSegment segment = new TextSegment(" ... Teks Segmen 1...");
// Tambahkan segmen ke koleksi segmen dari TextFragment
tf.Segments.Add(segment);
// Buat TextSegment baru
segment = new TextSegment("Tautan ke Google");
// Tambahkan segmen ke koleksi segmen dari TextFragment
tf.Segments.Add(segment);
// Atur hyperlink untuk TextSegment
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// Atur warna latar depan untuk segmen teks
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// Atur pemformatan teks sebagai miring
segment.TextState.FontStyle = FontStyles.Italic;
// Buat objek TextSegment lainnya
segment = new TextSegment("TextSegment tanpa hyperlink");
// Tambahkan segmen ke koleksi segmen dari TextFragment
tf.Segments.Add(segment);
// Tambahkan TextFragment ke koleksi paragraf dari objek halaman
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// Simpan dokumen PDF yang dihasilkan.
doc.Save(dataDir);
```
## Gunakan Font OTF

Aspose.PDF untuk .NET menawarkan fitur untuk menggunakan font Custom/TrueType saat membuat/manipulasi konten file PDF sehingga konten file ditampilkan menggunakan konten selain font sistem default. Mulai rilis Aspose.PDF untuk .NET 10.3.0, kami telah menyediakan dukungan untuk Font Tipe Terbuka.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buat instansi dokumen baru
Document pdfDocument = new Document();
// Tambahkan halaman ke koleksi halaman file PDF
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// Buat instansi TextFragment dengan teks sampel
TextFragment fragment = new TextFragment("Sample Text in OTF font");
// Temukan font di dalam direktori font sistem
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// Atau Anda bahkan bisa menentukan jalur font OTF di direktori sistem
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// Tentukan untuk menanamkan font di dalam file PDF, agar ditampilkan dengan benar,
// Bahkan jika font spesifik tidak terpasang/hadir di mesin target
fragment.TextState.Font.IsEmbedded = true;
// Tambahkan TextFragment ke koleksi paragraf dari instansi Halaman
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// Simpan dokumen PDF hasil.
pdfDocument.Save(dataDir);
```
## Menambahkan String HTML menggunakan DOM

Kelas Aspose.Pdf.Generator.Text memiliki properti yang disebut IsHtmlTagSupported yang memungkinkan penambahan tag/konten HTML ke dalam file PDF. Konten yang ditambahkan dirender dalam tag HTML asli daripada muncul sebagai string teks biasa. Untuk mendukung fitur serupa dalam Model Objek Dokumen (DOM) baru dari namespace Aspose.Pdf, kelas HtmlFragment telah diperkenalkan.

Instansi [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) dapat digunakan untuk menentukan konten HTML yang harus ditempatkan di dalam file PDF. Mirip dengan TextFragment, HtmlFragment adalah objek tingkat paragraf dan dapat ditambahkan ke koleksi paragraf objek Halaman. Cuplikan kode berikut menunjukkan langkah-langkah untuk menempatkan konten HTML di dalam file PDF menggunakan pendekatan DOM.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Instansiasi objek Dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman file PDF
Page page = doc.Pages.Add();
// Instansiasi HtmlFragment dengan konten HTML
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
// Atur informasi margin bawah
title.Margin.Bottom = 10;
// Atur informasi margin atas
title.Margin.Top = 200;
// Tambahkan Fragmen HTML ke koleksi paragraf halaman
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// Simpan file PDF
doc.Save(dataDir);
```
Potongan kode berikut menunjukkan langkah-langkah cara menambahkan daftar terurut HTML ke dalam dokumen:

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Jalur ke dokumen keluaran.
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// Instansiasi objek Document
Document doc = new Document();
// Instansiasi objek HtmlFragment dengan fragmen HTML yang sesuai
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>Pertama</li><li>Kedua</li><li>Ketiga</li><li>Keempat</li><li>Kelima</li></ul>Teks setelah daftar.<br/>Baris berikutnya<br/>Baris terakhir</body>`");
// Tambahkan Halaman dalam Koleksi Halaman
Page page = doc.Pages.Add();
// Tambahkan HtmlFragment di dalam halaman
page.Paragraphs.Add(t);
// Simpan berkas PDF hasil
doc.Save(outFile);
```

Anda juga dapat mengatur pemformatan string HTML menggunakan objek TextState sebagai berikut:

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
HtmlFragment html = new HtmlFragment("beberapa teks");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
Jika Anda mengatur nilai atribut teks melalui markup HTML dan kemudian menyediakan nilai yang sama dalam properti TextState, maka properti dari instansi TextState akan menimpa parameter HTML. Cuplikan kode berikut menunjukkan perilaku yang dijelaskan.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instansiasi objek Dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman file PDF
Page page = doc.Pages.Add();
// Instansiasi HtmlFragment dengan konten HTML
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Tabel berisi teks</i></b></p>");
// Font-family dari 'Verdana' akan direset ke 'Arial'
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// Atur informasi margin bawah
title.Margin.Bottom = 10;
// Atur informasi margin atas
title.Margin.Top = 400;
// Tambahkan Fragmen HTML ke koleksi paragraf halaman
page.Paragraphs.Add(title);
// Simpan file PDF
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// Simpan file PDF
doc.Save(dataDir);
```
## Catatan Kaki dan Catatan Akhir (DOM)

Catatan Kaki menunjukkan catatan dalam teks makalah Anda dengan menggunakan nomor superskrip berturut-turut. Catatan sebenarnya diindentasi dan dapat muncul sebagai catatan kaki di bagian bawah halaman.

### Menambahkan Catatan Kaki

Dalam sistem referensi catatan kaki, tunjukkan referensi dengan:

- meletakkan angka kecil di atas garis tipe langsung setelah materi sumber. Angka ini disebut pengenal catatan. Ini terletak sedikit di atas garis teks.
- meletakkan nomor yang sama, diikuti dengan kutipan dari sumber Anda, di bagian bawah halaman. Pencatatan kaki harus bersifat numerik dan kronologis: referensi pertama adalah 1, kedua adalah 2, dan seterusnya.

Keuntungan dari pencatatan kaki adalah pembaca dapat dengan mudah menurunkan mata mereka ke halaman untuk menemukan sumber referensi yang menarik bagi mereka.

Silakan ikuti langkah-langkah yang ditentukan di bawah ini untuk membuat Catatan Kaki:

- Buat instance Dokumen
- Buat objek Halaman
- Buat objek Fragmen Teks
- Buat instance Catatan dan berikan nilai ke properti TextFragment.FootNote
- Buat instance Note dan lewatkan nilai ke properti TextFragment.FootNote
- Tambahkan TextFragment ke koleksi paragraf dari instance halaman

### Gaya garis kustom untuk FootNote

Contoh berikut menunjukkan cara menambahkan Footnote ke bagian bawah halaman Pdf dan mendefinisikan gaya garis kustom.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Path ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buat instance Dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman PDF
Page page = doc.Pages.Add();
// Buat objek GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Atur lebar garis menjadi 2
graph.LineWidth = 2;
// Atur warna untuk objek grafik
graph.Color = Aspose.Pdf.Color.Red;
// Atur nilai array dash menjadi 3
graph.DashArray = new int[] { 3 };
// Atur nilai fase dash menjadi 1
graph.DashPhase = 1;
// Atur gaya garis footnote untuk halaman sebagai grafik
page.NoteLineStyle = graph;
// Buat instance TextFragment
TextFragment text = new TextFragment("Hello World");
// Atur nilai FootNote untuk TextFragment
text.FootNote = new Note("foot note untuk teks tes 1");
// Tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
page.Paragraphs.Add(text);
// Buat TextFragment kedua
text = new TextFragment("Aspose.Pdf for .NET");
// Atur FootNote untuk fragmen teks kedua
text.FootNote = new Note("foot note untuk teks tes 2");
// Tambahkan fragmen teks kedua ke koleksi paragraf file PDF
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// Simpan dokumen PDF hasil.
doc.Save(dataDir);
```
Kita dapat mengatur format Label Catatan Kaki (pengenal catatan) menggunakan objek TextState sebagai berikut:

```csharp
TextFragment text = new TextFragment("test text 1");
text.FootNote = new Note("foot note for test text 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### Sesuaikan label Catatan Kaki

Secara default, nomor Catatan Kaki bertambah mulai dari 1. Namun, kita mungkin memiliki kebutuhan untuk mengatur label Catatan Kaki kustom. Untuk mencapai kebutuhan ini, silakan coba menggunakan cuplikan kode berikut

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buat instance Dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman PDF
Page page = doc.Pages.Add();
// Buat objek GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Atur lebar garis menjadi 2
graph.LineWidth = 2;
// Atur warna untuk objek grafik
graph.Color = Aspose.Pdf.Color.Red;
// Atur nilai array dash menjadi 3
graph.DashArray = new int[] { 3 };
// Atur nilai fase dash menjadi 1
graph.DashPhase = 1;
// Atur gaya garis catatan kaki untuk halaman sebagai grafik
page.NoteLineStyle = graph;
// Buat instance TextFragment
TextFragment text = new TextFragment("Hello World");
// Atur nilai Catatan Kaki untuk TextFragment
text.FootNote = new Note("foot note for test text 1");
// Tentukan label kustom untuk Catatan Kaki
text.FootNote.Text = " Aspose(2015)";
// Tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## Menambahkan Gambar dan Tabel ke Catatan Kaki

Dalam versi rilis sebelumnya, dukungan Catatan Kaki disediakan tetapi hanya berlaku untuk objek TextFragment. Namun mulai rilis Aspose.PDF untuk .NET 10.7.0, Anda juga dapat menambahkan Catatan Kaki ke objek lain di dalam dokumen PDF seperti Tabel, Sel, dll. Cuplikan kode berikut menunjukkan langkah-langkah untuk menambahkan Catatan Kaki ke objek TextFragment dan kemudian menambahkan objek Gambar dan Tabel ke koleksi paragraf bagian Catatan Kaki.

```csharp

// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("some text");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("footnote text");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("Row 1 Cell 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// Simpan dokumen PDF yang dihasilkan.
doc.Save(dataDir);
```
## Cara Membuat Catatan Akhir

Catatan Akhir adalah sitiran sumber yang mengarahkan pembaca ke tempat tertentu di akhir makalah di mana mereka dapat menemukan sumber dari informasi atau kata-kata yang dikutip atau disebutkan dalam makalah tersebut. Saat menggunakan catatan akhir, kalimat yang Anda kutip atau parafrasekan atau materi yang diringkas diikuti oleh nomor superskrip.

Contoh berikut menunjukkan cara menambahkan Catatan Akhir di halaman Pdf.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buat instance Dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman PDF
Page page = doc.Pages.Add();
// Buat instance TextFragment
TextFragment text = new TextFragment("Halo Dunia");
// Setel nilai FootNote untuk TextFragment
text.EndNote = new Note("catatan akhir contoh");
// Tentukan label khusus untuk FootNote
text.EndNote.Text = " Aspose(2015)";
// Tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// Simpan dokumen PDF yang dihasilkan.
doc.Save(dataDir);
```
## Teks dan Gambar sebagai Paragraf InLine

Tata letak default dari file PDF adalah tata letak alir (Atas-Kiri ke Bawah-Kanan). Oleh karena itu, setiap elemen baru yang ditambahkan ke file PDF ditambahkan dalam aliran kanan bawah. Namun, kita mungkin memiliki kebutuhan untuk menampilkan berbagai elemen halaman, yaitu Gambar dan Teks pada level yang sama (satu setelah yang lain). Salah satu pendekatan bisa dengan membuat instansi Tabel dan menambahkan kedua elemen ke dalam objek sel masing-masing. Namun, pendekatan lain bisa dengan paragraf InLine. Dengan mengatur properti IsInLineParagraph dari Gambar dan Teks sebagai true, paragraf-paragraf ini akan muncul sebagai inline dengan elemen halaman lainnya.

Potongan kode berikut menunjukkan cara menambahkan teks dan Gambar sebagai paragraf InLine dalam file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instansiasi instansi Dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman dari instansi Dokumen
Page page = doc.Pages.Add();
// Buat TextFragmnet
TextFragment text = new TextFragment("Hello World.. ");
// Tambahkan fragmen teks ke koleksi paragraf dari objek Halaman
page.Paragraphs.Add(text);
// Buat instansi gambar
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// Atur gambar sebagai paragraf InLine sehingga muncul tepat setelah
// Objek paragraf sebelumnya (TextFragment)
image.IsInLineParagraph = true;
// Tentukan jalur file gambar
image.File = dataDir + "aspose-logo.jpg";
// Atur Tinggi gambar (opsional)
image.FixHeight = 30;
// Atur Lebar Gambar (opsional)
image.FixWidth = 100;
// Tambahkan gambar ke koleksi paragraf dari objek halaman
page.Paragraphs.Add(image);
// Inisialisasi ulang objek TextFragment dengan konten yang berbeda
text = new TextFragment(" Hello Again..");
// Atur TextFragment sebagai paragraf InLine
text.IsInLineParagraph = true;
// Tambahkan TextFragment yang baru dibuat ke koleksi paragraf dari halaman
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## Tentukan Spasi Karakter saat Menambahkan Teks

Teks dapat ditambahkan di dalam koleksi paragraf file PDF menggunakan instance TextFragment atau dengan menggunakan objek TextParagraph dan bahkan Anda dapat menstempel teks di dalam PDF menggunakan kelas TextStamp. Saat menambahkan teks, kita mungkin perlu menentukan spasi karakter untuk objek teks. Untuk mencapai kebutuhan ini, properti baru bernama properti CharacterSpacing telah diperkenalkan. Silakan lihat pendekatan berikut untuk memenuhi kebutuhan ini.

Pendekatan berikut menunjukkan langkah-langkah untuk menentukan spasi karakter saat menambahkan teks di dalam dokumen PDF.

### Menggunakan TextBuilder dan TextFragment

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Membuat instance Dokumen
Document pdfDocument = new Document();
// Menambahkan halaman ke koleksi halaman Dokumen
Page page = pdfDocument.Pages.Add();
// Membuat instance TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Membuat instance fragmen teks dengan konten sampel
TextFragment wideFragment = new TextFragment("Teks dengan spasi karakter yang ditingkatkan");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// Menentukan spasi karakter untuk TextFragment
wideFragment.TextState.CharacterSpacing = 2.0f;
// Menentukan posisi TextFragment
wideFragment.Position = new Position(100, 650);
// Menambahkan TextFragment ke instance TextBuilder
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// Menyimpan dokumen PDF hasil.
pdfDocument.Save(dataDir);
```
### Menggunakan TextParagraph

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buat instansi Dokumen
Document pdfDocument = new Document();
// Tambahkan halaman ke koleksi halaman Dokumen
Page page = pdfDocument.Pages.Add();
// Buat instansi TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Instansiasi instansi TextParagraph
TextParagraph paragraph = new TextParagraph();
// Buat instansi TextState untuk menentukan nama dan ukuran font
TextState state = new TextState("Arial", 12);
// Tentukan jarak karakter
state.CharacterSpacing = 1.5f;
// Tambahkan teks ke objek TextParagraph
paragraph.AppendLine("Ini adalah paragraf dengan jarak karakter", state);
// Tentukan posisi untuk TextParagraph
paragraph.Position = new Position(100, 550);
// Tambahkan TextParagraph ke instansi TextBuilder
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// Simpan dokumen PDF hasil.
pdfDocument.Save(dataDir);
```
### Menggunakan TextStamp

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buat instansi Dokumen
Document pdfDocument = new Document();
// Tambahkan halaman ke koleksi halaman Dokumen
Page page = pdfDocument.Pages.Add();
// Buat instansi TextStamp dengan teks contoh
TextStamp stamp = new TextStamp("Ini adalah cap teks dengan spasi karakter");
// Tentukan nama font untuk objek Stamp
stamp.TextState.Font = FontRepository.FindFont("Arial");
// Tentukan ukuran font untuk TextStamp
stamp.TextState.FontSize = 12;
// Tentukan spasi karakter sebagai 1f
stamp.TextState.CharacterSpacing = 1f;
// Atur XIndent untuk Stamp
stamp.XIndent = 100;
// Atur YIndent untuk Stamp
stamp.YIndent = 500;
// Tambahkan cap teks ke instansi halaman
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// Simpan dokumen PDF hasil.
pdfDocument.Save(dataDir);
```

## Membuat Dokumen PDF Multi-Kolom

Dalam majalah dan koran, kita sering melihat berita ditampilkan dalam beberapa kolom di halaman tunggal daripada buku di mana paragraf teks kebanyakan dicetak di seluruh halaman dari posisi kiri ke kanan. Banyak aplikasi pengolah dokumen seperti Microsoft Word dan Adobe Acrobat Writer memungkinkan pengguna untuk membuat beberapa kolom di satu halaman dan kemudian menambahkan data ke dalamnya.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) juga menawarkan fitur untuk membuat beberapa kolom di dalam halaman dokumen PDF.
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) juga menawarkan fitur untuk membuat beberapa kolom di dalam halaman dokumen PDF.

Pengaturan jarak kolom berarti ruang antara kolom dan jarak default antara kolom adalah 1,25cm. Jika lebar kolom tidak ditentukan, maka [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) menghitung lebar setiap kolom secara otomatis menurut ukuran halaman dan jarak kolom.

Contoh di bawah ini diberikan untuk mendemonstrasikan pembuatan dua kolom dengan objek Grafik (Garis) dan mereka ditambahkan ke koleksi paragraf FloatingBox, yang kemudian ditambahkan ke koleksi paragraf dari instansi Halaman.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// Tentukan informasi margin kiri untuk file PDF
doc.PageInfo.Margin.Left = 40;
// Tentukan informasi margin kanan untuk file PDF
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// Tambahkan garis ke koleksi paragraf dari objek bagian
page.Paragraphs.Add(graph1);

// Tentukan koordinat untuk garis
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// Buat variabel string dengan teks yang mengandung tag html

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> Bagaimana Menghindari penipuan uang</<strong> "
+ "</font>";
// Buat paragraf teks yang berisi teks HTML

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// Tambahkan empat kolom di bagian
box.ColumnInfo.ColumnCount = 2;
// Atur jarak antara kolom
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("Oleh Seorang Googler (Blog Resmi Google)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// Buat objek grafik untuk menggambar garis
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// Tentukan koordinat untuk garis
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// Tambahkan garis ke koleksi paragraf dari objek bagian
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// Simpan file PDF
doc.Save(dataDir);
```
## Bekerja dengan Custom Tab Stops

Tab Stop adalah titik berhenti untuk tabulasi. Dalam pengolahan kata, setiap baris berisi sejumlah tab stop yang ditempatkan pada interval reguler (misalnya, setiap setengah inci). Namun, ini dapat diubah, karena sebagian besar pengolah kata memungkinkan Anda untuk menetapkan tab stop di mana pun Anda inginkan. Ketika Anda menekan tombol Tab, kursor atau titik sisipan melompat ke tab stop berikutnya, yang itu sendiri tidak terlihat. Meskipun tab stop tidak ada dalam file teks, pengolah kata tetap melacaknya sehingga dapat bereaksi dengan benar terhadap tombol Tab.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) memungkinkan pengembang untuk menggunakan tab stop kustom dalam dokumen PDF. Kelas Aspose.Pdf.Text.TabStop digunakan untuk mengatur TAB stop kustom di kelas [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) juga menawarkan beberapa jenis pemimpin tab yang sudah ditentukan sebagai enumerasi bernama, TabLeaderType yang nilai dan deskripsi yang sudah ditentukan diberikan di bawah ini:
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) juga menawarkan beberapa jenis tab leader yang telah ditentukan sebelumnya sebagai enumerasi yang bernama, TabLeaderType dengan nilai yang telah ditentukan dan deskripsinya diberikan di bawah ini:

|**Jenis Tab Leader**|**Deskripsi**|
| :- | :- |
|None|Tanpa tab leader|
|Solid|Tab leader padat|
|Dash|Tab leader garis putus-putus|
|Dot|Tab leader titik|

Berikut adalah contoh cara mengatur TAB stops kustom.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("Ini adalah contoh pembentukan tabel dengan TAB stops", ts);
TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```
## Cara Menambahkan Teks Transparan pada PDF

Sebuah file PDF berisi Objek Gambar, Teks, Grafik, lampiran, Anotasi dan saat membuat TextFragment, Anda dapat mengatur informasi warna latar depan, latar belakang serta pemformatan teks. Aspose.PDF untuk .NET mendukung fitur untuk menambahkan teks dengan saluran warna Alpha. Cuplikan kode berikut menunjukkan cara menambahkan teks dengan warna transparan.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buat instance Document
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman file PDF
Aspose.Pdf.Page page = doc.Pages.Add();

// Buat objek Graph
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// Buat instance persegi panjang dengan dimensi tertentu
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// Buat objek warna dari saluran warna Alpha
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Tambahkan persegi panjang ke koleksi bentuk dari objek Graph
canvas.Shapes.Add(rect);
// Tambahkan objek grafik ke koleksi paragraf dari objek halaman
page.Paragraphs.Add(canvas);
// Atur nilai untuk tidak mengubah posisi objek grafik
canvas.IsChangePosition = false;

// Buat instance TextFragment dengan nilai contoh
TextFragment text = new TextFragment("teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan ");
// Buat objek warna dari saluran Alpha
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// Atur informasi warna untuk instance teks
text.TextState.ForegroundColor = color;
// Tambahkan teks ke koleksi paragraf dari instance halaman
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## Tentukan LineSpacing untuk Font

Setiap font memiliki persegi abstrak, yang tingginya adalah jarak yang dimaksudkan antara baris teks dalam ukuran huruf yang sama.
Setiap font memiliki kotak abstrak, yang tingginya adalah jarak yang dimaksudkan antara baris teks dalam ukuran tipe yang sama.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// Muat file PDF masukan
Document doc = new Document();
//Buat TextFormattingOptions dengan LineSpacingMode.FullSize
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// Buat objek pembangun teks untuk halaman pertama dokumen
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Buat fragmen teks dengan string contoh
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // Muat font TrueType ke dalam objek stream
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // Tetapkan nama font untuk string teks
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Tentukan posisi untuk Fragmen Teks
        textFragment.Position = new Position(100, 600);
        //Tetapkan TextFormattingOptions dari fragmen saat ini ke yang telah ditentukan(sehingga mengarah ke LineSpacingMode.FullSize)
        textFragment.TextState.FormattingOptions = formattingOptions;
        // Tambahkan teks ke TextBuilder agar dapat ditempatkan di atas file PDF
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // Simpan dokumen PDF hasil
    doc.Save(dataDir);
}
```
## Mendapatkan Lebar Teks Secara Dinamis

Terkadang, diperlukan untuk mendapatkan lebar teks secara dinamis. Aspose.PDF untuk .NET mencakup dua metode untuk pengukuran lebar string. Anda dapat memanggil metode [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) dari kelas Aspose.Pdf.Text.Font atau Aspose.Pdf.Text.TextState (atau keduanya). Cuplikan kode di bawah ini menunjukkan cara menggunakan fungsionalitas ini.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("Pengukuran string font tidak sesuai!");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("Pengukuran string font tidak sesuai!");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("Pengukuran string font dan state tidak cocok!");
}
```

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
```

