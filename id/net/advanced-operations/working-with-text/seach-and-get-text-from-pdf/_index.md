---
title: Mencari dan Mendapatkan Teks dari Halaman PDF
linktitle: Mencari dan Mendapatkan Teks
type: docs
weight: 60
url: id/net/search-and-get-text-from-pdf/
description: Artikel ini menjelaskan cara menggunakan berbagai alat untuk mencari dan mendapatkan teks dari Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mencari dan Mendapatkan Teks dari Halaman PDF",
    "alternativeHeadline": "Alat untuk mencari dan mendapatkan teks dari Halaman PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, mencari teks, mendapatkan teks dari pdf",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan cara menggunakan berbagai alat untuk mencari dan mendapatkan teks dari Aspose.PDF untuk .NET."
}
</script>

Potongan kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Mencari dan Mendapatkan Teks dari Semua Halaman Dokumen PDF

Kelas [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) memungkinkan Anda untuk menemukan teks, yang cocok dengan frase tertentu, dari semua halaman dokumen PDF. Untuk mencari teks dari seluruh dokumen, Anda perlu memanggil metode Accept dari koleksi Halaman. Metode [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) mengambil objek TextFragmentAbsorber sebagai parameter, yang mengembalikan koleksi objek TextFragment. Anda dapat mengulang semua fragmen dan mendapatkan properti mereka seperti Teks, Posisi (XIndent, YIndent), NamaFont, UkuranFont, IsAccessible, IsEmbedded, IsSubset, WarnaLatarDepan, dll.

Potongan kode berikut menunjukkan cara mencari teks dari semua halaman.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Buat objek TextAbsorber untuk menemukan semua instansi frase pencarian masukan
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// Terima absorber untuk semua halaman
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Dapatkan fragmen teks yang diekstraksi
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Ulangi melalui fragmen
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Teks : {0} ", textFragment.Text);
    Console.WriteLine("Posisi : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Nama : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Ukuran Font : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Warna Latar Depan : {0} ", textFragment.TextState.ForegroundColor);
}
```
Jika Anda perlu mencari teks di dalam halaman tertentu dari PDF, silakan tentukan nomor halaman dari koleksi halaman instansi Dokumen dan panggil metode Accept pada halaman tersebut (seperti yang ditunjukkan pada baris kode di bawah ini).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Terima absorber untuk halaman tertentu
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Mencari dan Mendapatkan Segmen Teks dari Semua Halaman Dokumen PDF

Untuk mencari segmen teks dari semua halaman, Anda pertama-tama perlu mendapatkan objek TextFragment dari dokumen.
Untuk mencari segmen teks dari semua halaman, Anda pertama-tama perlu mendapatkan objek TextFragment dari dokumen.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Buat objek TextAbsorber untuk menemukan semua contoh frase pencarian yang dimasukkan
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// Terima absorber untuk semua halaman
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Dapatkan fragmen teks yang diekstrak
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Loop melalui fragmen
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("Teks : {0} ", textSegment.Text);
        Console.WriteLine("Posisi : {0} ", textSegment.Position);
        Console.WriteLine("Indent X : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("Indent Y : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("Font - Nama : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("Font - Dapat Diakses : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("Font - Tertanam : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Font - Subset : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Ukuran Font : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Warna Latar Depan : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```
Untuk mencari dan mendapatkan TextSegments dari halaman tertentu dalam PDF, Anda perlu menentukan indeks halaman tertentu saat memanggil metode Accept(..). Silakan lihat baris kode berikut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Terima absorber untuk semua halaman
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Cari dan Dapatkan Teks dari semua halaman menggunakan Ekspresi Reguler

TextFragmentAbsorber membantu Anda mencari dan mengambil teks, dari semua halaman, berdasarkan ekspresi reguler.
TextFragmentAbsorber membantu Anda mencari dan mengambil teks, dari semua halaman, berdasarkan ekspresi reguler.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Seperti 1999-2000

// Tetapkan opsi pencarian teks untuk menentukan penggunaan ekspresi reguler
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Terima absorber untuk semua halaman
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Dapatkan fragmen teks yang diekstrak
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Loop melalui fragmen
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Teks : {0} ", textFragment.Text);
    Console.WriteLine("Posisi : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Nama : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - Dapat Diakses : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - Tertanam : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - Subset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Ukuran Font : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Warna Latar Depan : {0} ", textFragment.TextState.ForegroundColor);
}
```
```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// Untuk mencari kecocokan tepat dari sebuah kata, Anda dapat mempertimbangkan menggunakan ekspresi reguler.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// Untuk mencari string dalam huruf besar atau huruf kecil, Anda dapat mempertimbangkan menggunakan ekspresi reguler.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// Untuk mencari semua string (menganalisis semua string) di dalam dokumen PDF, silakan coba menggunakan ekspresi reguler berikut.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// Temukan kecocokan string pencarian dan dapatkan apa pun setelah string tersebut hingga pemutusan baris.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// Silakan gunakan ekspresi reguler berikut untuk menemukan teks setelah kecocokan regex.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// Untuk mencari Hyperlink/URL di dalam dokumen PDF, silakan coba menggunakan ekspresi reguler berikut.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```
## Mencari Teks Berdasarkan Regex dan Menambahkan Hyperlink

Jika Anda ingin menambahkan hyperlink pada frasa teks berdasarkan ekspresi reguler, pertama temukan semua frasa yang cocok dengan ekspresi reguler tersebut menggunakan TextFragmentAbsorber dan tambahkan hyperlink pada frasa tersebut.

Untuk menemukan frasa dan menambahkan hyperlink di atasnya:

1. Masukkan ekspresi reguler sebagai parameter ke konstruktor TextFragmentAbsorber.
2. Buat objek TextSearchOptions yang menentukan apakah ekspresi reguler digunakan atau tidak.
3. Dapatkan frasa yang cocok ke dalam TextFragments.
4. Lakukan loop melalui hasil pencocokan untuk mendapatkan dimensi persegi panjangnya, ubah warna latar depan menjadi biru (opsional - agar terlihat seperti hyperlink dan buat link menggunakan metode CreateWebLink(..) kelas PdfContentEditor.
5. Simpan PDF yang telah diperbarui menggunakan metode Save dari objek Document.
Potongan kode berikut menunjukkan cara Anda mencari teks di dalam file PDF menggunakan ekspresi reguler dan menambahkan hyperlink pada hasil yang cocok.

```csharp
// Untuk contoh lengkap dan file data, silahkan pergi ke https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Buat objek absorber untuk menemukan semua contoh dari frasa pencarian masukan
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Aktifkan pencarian ekspresi reguler
absorber.TextSearchOptions = new TextSearchOptions(true);
// Buka dokumen
PdfContentEditor editor = new PdfContentEditor();
// Ikat file PDF sumber
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Terima absorber untuk halaman
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Loop melalui fragmen
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```
## Mencari dan Menggambar Persegi Panjang di Sekitar Setiap Fragmen Teks

Aspose.PDF untuk .NET mendukung fitur untuk mencari dan mendapatkan koordinat setiap karakter atau fragmen teks. Jadi, untuk memastikan tentang koordinat yang dikembalikan untuk setiap karakter, kita dapat mempertimbangkan untuk menyoroti (menambahkan persegi panjang) di sekitar setiap karakter.

Dalam kasus paragraf teks, Anda dapat menggunakan beberapa ekspresi reguler untuk menentukan pemisah paragraf dan menggambar persegi panjang di sekitarnya. Silakan lihat cuplikan kode berikut. Cuplikan kode berikut ini mendapatkan koordinat setiap karakter dan membuat persegi panjang di sekitar setiap karakter.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Buka dokumen
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```
## Sorot setiap karakter dalam dokumen PDF

{{% alert color="primary" %}}

Anda dapat mencoba mencari teks dalam dokumen menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di tautan ini [link](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF untuk .NET mendukung fitur untuk mencari dan mendapatkan koordinat dari setiap karakter atau fragmen teks. Jadi, untuk memastikan tentang koordinat yang dikembalikan untuk setiap karakter, kita dapat mempertimbangkan untuk menyoroti (menambahkan persegi panjang) di sekitar setiap karakter. Potongan kode berikut mendapatkan koordinat dari setiap karakter dan membuat persegi panjang di sekitar setiap karakter.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// Buat objek TextAbsorber untuk menemukan semua kata
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// Dapatkan fragmen teks yang diekstrak
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Loop melalui fragmen
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```
## Menambahkan dan Mencari Teks Tersembunyi

Terkadang kita ingin menambahkan teks tersembunyi dalam dokumen PDF dan kemudian mencari teks tersembunyi tersebut serta menggunakan posisinya untuk pengolahan lebih lanjut. Untuk kemudahan Anda, Aspose.PDF untuk .NET menyediakan kemampuan ini. Anda dapat menambahkan teks tersembunyi selama pembuatan dokumen. Anda juga dapat menemukan teks tersembunyi menggunakan TextFragmentAbsorber. Untuk menambahkan teks tersembunyi, atur TextState.Invisible menjadi ‘true’ untuk teks yang ditambahkan. TextFragmentAbsorber menemukan semua teks yang cocok dengan pola (jika ditentukan). Ini adalah perilaku default yang tidak dapat diubah. Untuk memverifikasi apakah teks yang ditemukan benar-benar tidak terlihat, properti TextState.Invisible dapat digunakan. Cuplikan kode di bawah ini menunjukkan cara menggunakan fitur ini.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//Membuat dokumen dengan teks tersembunyi
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("Ini adalah teks biasa.");
TextFragment frag2 = new TextFragment("Ini adalah teks tidak terlihat.");

//Atur properti teks - tidak terlihat
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//Mencari teks dalam dokumen
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //Lakukan sesuatu dengan fragmen
    Console.WriteLine("Teks '{0}' pada pos {1} tidak terlihat: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```
## Mencari Teks Dengan .NET Regex

Aspose.PDF untuk .NET menyediakan kemampuan untuk mencari dokumen menggunakan opsi Regex .NET standar. TextFragmentAbsorber dapat digunakan untuk tujuan ini seperti yang ditunjukkan pada contoh kode di bawah ini.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Membuat objek Regex untuk menemukan semua kata
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// Membuka dokumen
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// Mendapatkan halaman tertentu
Page page = document.Pages[1];

// Membuat objek TextAbsorber untuk menemukan semua instansi regex masukan
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// Menerima absorber untuk halaman
page.Accept(textFragmentAbsorber);

// Mendapatkan fragmen teks yang diekstrak
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Melakukan iterasi melalui fragmen
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
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

