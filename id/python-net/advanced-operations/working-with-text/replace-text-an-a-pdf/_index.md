---
title: Ganti Teks dalam PDF melalui Python
linktitle: Ganti Teks dalam PDF
type: docs
weight: 40
url: /id/python-net/replace-text-in-pdf/
description: Pelajari lebih lanjut tentang berbagai cara mengganti dan menghapus teks dari Aspose.PDF untuk Python melalui pustaka .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ganti Teks dalam PDF",
    "alternativeHeadline": "Mengganti dan Menghapus Teks dalam File PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, ganti teks, hapus teks",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/replace-text-in-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Pelajari lebih lanjut tentang berbagai cara mengganti dan menghapus teks dari Aspose.PDF untuk Python melalui pustaka .NET."
}
</script>


## Ganti Teks di semua halaman dokumen PDF

{{% alert color="primary" %}}

Anda dapat mencoba menemukan dan mengganti teks dalam dokumen menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di [tautan ini](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Untuk mengganti teks di semua halaman dokumen PDF, Anda terlebih dahulu perlu menggunakan [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) untuk menemukan frasa tertentu yang ingin Anda ganti. Setelah itu, Anda perlu melalui semua TextFragments untuk mengganti teks dan mengubah atribut lainnya. Setelah Anda melakukan itu, Anda hanya perlu menyimpan PDF keluaran menggunakan metode Save dari objek Document. Kode berikut menunjukkan bagaimana mengganti teks di semua halaman dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat objek TextAbsorber untuk menemukan semua instance dari frasa pencarian masukan
    absorber = ap.text.TextFragmentAbsorber("format")

    # Terima absorber untuk semua halaman
    document.pages.accept(absorber)

    # Dapatkan fragmen teks yang diekstrak
    collection = absorber.text_fragments

    # Loop melalui fragmen
    for text_fragment in collection:
        # Perbarui teks dan properti lainnya
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # Simpan dokumen
    document.save(output_pdf)
```


## Ganti Teks di Wilayah Halaman Tertentu

Untuk mengganti teks di wilayah halaman tertentu, pertama-tama kita perlu membuat objek TextFragmentAbsorber, menentukan wilayah halaman menggunakan properti TextSearchOptions.Rectangle, dan kemudian mengiterasi melalui semua TextFragments untuk mengganti teks. Setelah operasi ini selesai, kita hanya perlu menyimpan PDF keluaran menggunakan metode Save dari objek Document. Cuplikan kode berikut menunjukkan cara mengganti teks di semua halaman dokumen PDF.

```python
// muat file PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// buat objek TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// mencari teks dalam batas halaman
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// tentukan wilayah halaman untuk Opsi Pencarian Teks
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// mencari teks dari halaman pertama file PDF
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// iterasi melalui setiap TextFragment
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // perbarui teks menjadi karakter kosong
    tf.Text = "";
}

// simpan file PDF yang telah diperbarui setelah penggantian teks
pdf.Save("c:/pdftest/TextUpdated.pdf");
```


## Mengganti Teks Berdasarkan Ekspresi Reguler

Jika Anda ingin mengganti beberapa frasa berdasarkan ekspresi reguler, Anda harus terlebih dahulu menemukan semua frasa yang cocok dengan ekspresi reguler tersebut menggunakan TextFragmentAbsorber. Anda harus melewatkan ekspresi reguler sebagai parameter ke konstruktor TextFragmentAbsorber. Anda juga perlu membuat objek TextSearchOptions yang menentukan apakah ekspresi reguler digunakan atau tidak. Setelah Anda mendapatkan frasa yang cocok dalam TextFragments, Anda perlu mengulangi semuanya dan memperbarui sesuai kebutuhan. Akhirnya, Anda perlu menyimpan PDF yang diperbarui menggunakan metode Save dari objek Document. Cuplikan kode berikut menunjukkan cara mengganti teks berdasarkan ekspresi reguler.

```python
// Untuk contoh lengkap dan file data, silahkan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Seperti 1999-2000

// Atur opsi pencarian teks untuk menentukan penggunaan ekspresi reguler
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Terima absorber untuk satu halaman
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// Dapatkan fragmen teks yang diekstraksi
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Ulangi fragmen
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Perbarui teks dan properti lainnya
    textFragment.Text = "Frasa Baru";
    // Atur ke instance dari objek.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```


## Ganti font dalam file PDF yang sudah ada

Aspose.PDF untuk Python via .NET mendukung kemampuan untuk mengganti teks dalam dokumen PDF. Namun, terkadang Anda memiliki kebutuhan untuk hanya mengganti font yang digunakan di dalam dokumen PDF. Jadi alih-alih mengganti teks, hanya font yang digunakan yang diganti. Salah satu overload dari konstruktor TextFragmentAbsorber menerima objek TextEditOptions sebagai argumen dan kita dapat menggunakan nilai RemoveUnusedFonts dari enumerasi TextEditOptions.FontReplace untuk memenuhi kebutuhan kita. Cuplikan kode berikut menunjukkan cara mengganti font di dalam dokumen PDF.

```python
// Untuk contoh lengkap dan file data, silakan pergi ke https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Memuat file PDF sumber
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Cari fragmen teks dan atur opsi edit sebagai hapus font yang tidak digunakan
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// Terima absorber untuk semua halaman
pdfDocument.Pages.Accept(absorber);
// Jelajahi semua TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // Jika nama font adalah ArialMT, ganti nama font dengan Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// Simpan dokumen yang diperbarui
pdfDocument.Save(dataDir);
```


## Penggantian Teks harus secara otomatis mengatur ulang Isi Halaman

Aspose.PDF untuk Python via .NET mendukung fitur untuk mencari dan mengganti teks di dalam file PDF. Namun, baru-baru ini beberapa pelanggan mengalami masalah selama penggantian teks ketika TextFragment tertentu diganti dengan konten yang lebih kecil dan beberapa spasi ekstra ditampilkan dalam PDF hasil atau jika TextFragment diganti dengan beberapa string yang lebih panjang, maka kata-kata tumpang tindih dengan konten halaman yang ada. Jadi dibutuhkan mekanisme yang setelah teks di dalam dokumen PDF diganti, konten harus diatur ulang.

Untuk mengatasi skenario yang disebutkan di atas, Aspose.PDF untuk Python via .NET telah ditingkatkan sehingga tidak ada masalah seperti itu muncul ketika mengganti teks di dalam file PDF. Cuplikan kode berikut menunjukkan cara mengganti teks di dalam file PDF dan isi halaman harus diatur ulang secara otomatis.

```python
// Untuk contoh lengkap dan file data, silakan pergi ke https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Memuat file PDF sumber
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Membuat objek TextFragment Absorber dengan ekspresi reguler
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Mengganti setiap TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Mengatur font dari fragmen teks yang diganti
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Mengatur ukuran font
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Mengganti teks dengan string yang lebih besar dari placeholder
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Menyimpan PDF hasil
doc.Save(dataDir);
```


## Merender Simbol yang Dapat Diganti selama Pembuatan PDF

Simbol yang dapat diganti adalah simbol khusus dalam string teks yang dapat diganti dengan konten yang sesuai saat waktu proses. Simbol yang dapat diganti saat ini didukung oleh Model Objek Dokumen baru dari namespace Aspose.PDF adalah `$P`, `$p,` `\n`, `\r`. `$p` dan `$P` digunakan untuk menangani penomoran halaman saat waktu proses. `$p` diganti dengan nomor halaman tempat kelas Paragraf saat ini berada. `$P` diganti dengan jumlah total halaman dalam dokumen. Saat menambahkan `TextFragment` ke koleksi paragraf dokumen PDF, itu tidak mendukung pemisah baris di dalam teks. Namun untuk menambahkan teks dengan pemisah baris, silakan gunakan `TextFragment` dengan `TextParagraph`:

- gunakan "\r\n" atau Environment.NewLine dalam TextFragment alih-alih "\n" tunggal;
- buat objek TextParagraph. Ini akan menambahkan teks dengan pemisahan baris;
- tambahkan TextFragment dengan TextParagraph.AppendLine;
- tambahkan TextParagraph dengan TextBuilder.AppendParagraph.

```python
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inisialisasi TextFragment baru dengan teks yang mengandung penanda baris baru yang diperlukan
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nama Pelamar: " + Environment.NewLine + " Joe Smoe");

// Atur properti text fragment jika diperlukan
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Buat objek TextParagraph
TextParagraph par = new TextParagraph();

// Tambah TextFragment baru ke paragraph
par.AppendLine(textFragment);

// Atur posisi paragraph
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Buat objek TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Tambahkan TextParagraph menggunakan TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```


## Simbol yang Dapat Diganti di Area Header/Footer

Simbol yang dapat diganti juga dapat ditempatkan di dalam bagian Header/Footer dari file PDF. Silakan lihat potongan kode berikut untuk detail tentang cara menambahkan simbol yang dapat diganti di bagian footer.

```python
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Tetapkan instance marginInfo ke properti Margin dari sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Instansiasi paragraf Teks yang akan menyimpan konten untuk ditampilkan sebagai header
TextFragment t1 = new TextFragment("judul laporan");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Nama_Laporan");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Buat objek HeaderFooter untuk bagian tersebut
HeaderFooter hfFoot = new HeaderFooter();
// Tetapkan objek HeaderFooter ke footer ganjil & genap
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Tambahkan paragraf teks yang berisi nomor halaman saat ini dari total jumlah halaman
TextFragment t3 = new TextFragment("Dibuat pada tanggal uji");
TextFragment t4 = new TextFragment("nama laporan ");
TextFragment t5 = new TextFragment("Halaman $p dari $P");

// Instansiasi objek tabel
Table tab2 = new Table();

// Tambahkan tabel dalam koleksi paragraf bagian yang diinginkan
hfFoot.Paragraphs.Add(tab2);

// Tetapkan lebar kolom tabel
tab2.ColumnWidths = "165 172 165";

// Buat baris dalam tabel dan kemudian sel dalam baris
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// Tetapkan penjajaran vertikal teks sebagai terpusat
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total untuk Java adalah kompilasi dari setiap komponen Java yang ditawarkan oleh Aspose. Ini dikompilasi pada a#$NL" + "dasar harian untuk memastikan bahwa itu berisi versi terbaru dari masing-masing komponen Java kami. #$NL " + "Menggunakan Aspose.Total untuk Java pengembang dapat membuat berbagai macam aplikasi. #$NL #$NL #$NP" + "Aspose.Total untuk Java adalah kompilasi dari setiap komponen Java yang ditawarkan oleh Aspose. Ini dikompilasi pada a#$NL" + "dasar harian untuk memastikan bahwa itu berisi versi terbaru dari masing-masing komponen Java kami. #$NL " + "Menggunakan Aspose.Total untuk Java pengembang dapat membuat berbagai macam aplikasi. #$NL #$NL #$NP" + "Aspose.Total untuk Java adalah kompilasi dari setiap komponen Java yang ditawarkan oleh Aspose. Ini dikompilasi pada a#$NL" + "dasar harian untuk memastikan bahwa itu berisi versi terbaru dari masing-masing komponen Java kami. #$NL " + "Menggunakan Aspose.Total untuk Java pengembang dapat membuat berbagai macam aplikasi. #$NL #$NL"))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Tambahkan tabel dalam koleksi paragraf bagian yang diinginkan
page.Paragraphs.Add(table);

// Tetapkan batas sel default menggunakan objek BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Tetapkan batas tabel menggunakan objek BorderInfo yang disesuaikan
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Buat baris dalam tabel dan kemudian sel dalam baris
Row row1 = table.Rows.Add();

row1.Cells.Add("kol1");
row1.Cells.Add("kol2");
row1.Cells.Add("kol3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total untuk Java adalah kompilasi dari setiap komponen Java yang ditawarkan oleh Aspose. Ini dikompilasi pada a" + CRLF + "dasar harian untuk memastikan bahwa itu berisi versi terbaru dari masing-masing komponen Java kami. " + CRLF + "dasar harian untuk memastikan bahwa itu berisi versi terbaru dari masing-masing komponen Java kami. " + CRLF + "Menggunakan Aspose.Total untuk Java pengembang dapat membuat berbagai macam aplikasi.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```


## Menghapus Font yang Tidak Digunakan dari File PDF

Aspose.PDF untuk Python via .NET mendukung fitur untuk menyematkan font saat membuat dokumen PDF, serta kemampuan untuk menyematkan font dalam file PDF yang ada. Mulai Aspose.PDF untuk Python via .NET 7.3.0, juga memungkinkan Anda untuk menghapus font duplikat atau yang tidak digunakan dari dokumen PDF.

Untuk mengganti font, gunakan pendekatan berikut:

1. Panggil kelas [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Panggil parameter TextEditOptions.FontReplace.RemoveUnusedFonts dari kelas TextFragmentAbsorber. (Ini menghapus font yang tidak digunakan selama penggantian font).
1. Atur font secara individual untuk setiap fragmen teks.

Cuplikan kode berikut mengganti font untuk semua fragmen teks dari semua halaman dokumen dan menghapus font yang tidak digunakan.

```python
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Memuat file PDF sumber
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Iterasi melalui semua TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Simpan dokumen yang diperbarui
doc.Save(dataDir);
```


## Hapus Semua Teks dari Dokumen PDF

### Hapus Semua Teks Menggunakan Operator

Dalam beberapa operasi teks, Anda perlu menghapus semua teks dari dokumen PDF dan untuk itu, Anda perlu mengatur teks yang ditemukan sebagai nilai string kosong biasanya. Poinnya adalah bahwa mengubah teks untuk banyak fragmen teks memicu sejumlah pemeriksaan dan operasi penyesuaian posisi teks. Mereka penting dalam skenario pengeditan teks. Kesulitannya adalah Anda tidak dapat menentukan berapa banyak fragmen teks yang akan dihapus dalam skenario di mana mereka diproses dalam sebuah loop.

Oleh karena itu, kami merekomendasikan menggunakan pendekatan lain untuk skenario menghapus semua teks dari halaman PDF. Silakan pertimbangkan potongan kode berikut yang bekerja sangat cepat.

```python
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// Loop melalui semua halaman Dokumen PDF
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // Pilih semua teks pada halaman
    page.Contents.Accept(operatorSelector);
    // Hapus semua teks
    page.Contents.Delete(operatorSelector.Selected);
}
// Simpan dokumen
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python melalui .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "Library Manipulasi PDF untuk Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>