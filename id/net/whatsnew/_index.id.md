---
title: What's new
linktitle: What's new
type: docs
weight: 10
url: /net/whatsnew/
description: Di halaman ini diperkenalkan fitur-fitur baru yang paling populer dalam Aspose.PDF untuk .NET yang telah diperkenalkan dalam rilis terbaru.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## Apa yang baru di Aspose.PDF 24.8

Mengonversi Dokumen PDF menjadi Format PDF/A-4

Sejak versi 24.8, telah dimungkinkan untuk mengonversi dokumen PDF menjadi PDF/A-4. Bagian 4 dari standar, berdasarkan PDF 2.0, diterbitkan pada akhir tahun 2020.

Potongan kode berikut menunjukkan cara mengonversi dokumen menjadi format PDF/A-4, dengan asumsi dokumen masukan adalah PDF 2.x.

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // Hanya dokumen PDF-2.x yang dapat dikonversi ke PDF/A-4
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
Potongan kode kedua ini menunjukkan cara mengonversi dokumen ke format PDF/A-4 ketika dokumen masukan adalah versi sebelumnya.

```cs
    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.Convert(Stream.Null, PdfFormat.v_2_0, ConvertErrorAction.Delete);

        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```

Sejak 24.8 kami memperkenalkan metode untuk meratakan konten transparan dalam dokumen PDF:

```cs
    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```

## Apa yang baru di Aspose.PDF 24.7

Membandingkan Dokumen PDF dengan Aspose.PDF untuk .NET

Sejak 24.7, dimungkinkan untuk membandingkan konten dokumen PDF dengan tanda anotasi dan output berdampingan:

Potongan kode pertama menunjukkan cara membandingkan halaman pertama dari dua dokumen PDF.
Potongan kode pertama menunjukkan cara membandingkan halaman pertama dari dua dokumen PDF.

```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

Potongan kode kedua memperluas cakupan untuk membandingkan seluruh konten dari dua dokumen PDF.

```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```
## Apa yang Baru di Aspose.PDF 24.4

Rilis ini mendukung penerapan masker pemotongan untuk gambar:

```cs
    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

Sejak 24.4 Anda dapat memilih sumber kertas berdasarkan ukuran halaman PDF di dialog cetak menggunakan API

Mulai dari Aspose.PDF 24.4 preferensi ini dapat diaktifkan dan dinonaktifkan menggunakan properti Document.PickTrayByPdfSize atau fasad PdfContentEditor:

```cs
    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("Hello world!"));

        // Atur bendera untuk memilih nampan kertas menggunakan ukuran halaman PDF
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
Dari rilis ini telah ditambahkan plugin Aspose.PDF Signature untuk .NET:

- Contoh dengan membuat bidang baru dan opsi:

```cs
    // membuat Signature
    var plugin = new Signature();
    // membuat objek SignOptions untuk menetapkan instruksi
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // menambahkan jalur file masukan
    opt.AddInput(new FileDataSource(inputPath));
    // menetapkan jalur file keluaran
    opt.AddOutput(new FileDataSource(outputPath));
    // menetapkan opsi tambahan
    opt.Reason = "alasan saya";
    opt.Contact = "kontak saya";
    opt.Location = "lokasi saya";
    // melakukan proses
    plugin.Process(opt);
```

- Contoh dengan bidang kosong yang sudah ada

```cs
    // membuat Signature
    var plugin = new Signature();
    // membuat objek SignOptions untuk menetapkan instruksi
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // menambahkan jalur file masukan dengan bidang tanda tangan kosong
    opt.AddInput(new FileDataSource(inputPath));
    // menetapkan jalur file keluaran
    opt.AddOutput(new FileDataSource(outputPath));
    // menetapkan nama bidang tanda tangan yang sudah ada
    opt.Name = "Signature1";
    // melakukan proses
    plugin.Process(opt);
```
## Apa yang baru di Aspose.PDF 24.3

Dari rilis ini ditambahkan plugin PDF/A Converter untuk .NET:

```cs
    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // Tambahkan berkas sumber
    options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // ganti dengan jalur berkas anda yang sebenarnya

    // Tambahkan jalur untuk menyimpan berkas yang dikonversi
    options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

    // Buat instansi plugin
    var plugin = new PdfAConverter();

    // Jalankan konversi
    plugin.Process(options);
```

- Implementasikan pencarian melalui daftar frasa dalam TextFragmentAbsorber:

```cs
    var regexes = new Regex[]
    {
    new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)+", RegexOptions.IgnoreCase),
    new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:?", RegexOptions.IgnoreCase),
    new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
    new Regex("Vested in:", RegexOptions.IgnoreCase),
    new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
    new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };
    var document = new Document(input);
    var absorber = new TextFragmentAbsorber(
    regexes,
    new TextSearchOptions(true)
    );
    document.Pages.Accept(absorber);
    // Dapatkan hasil
    var result = absorber.RegexResults
```
Sejak 24.3 mungkin untuk menambahkan bidang tanda tangan kosong di setiap halaman ke file PDF/A

```cs

    static void Main(string[] args)
    {
        try
        {
            var lic = new Aspose.Pdf.License();
            lic.SetLicense("Aspose.Total.lic");

            string source = "source.pdf";
            string fieldName = "signature_1234";
            string dest = "source_fieldNotInAllPages.pdf";
            addFieldSingle_NewCode(source, dest, fieldName, 1);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
        Console.ReadLine(); 
    }

    private static void addFieldSingle_NewCode(string source, string dest, string fieldName, int page)
    {
        File.Copy(source, dest, true);
        using (var fs = new FileStream(dest, FileMode.Open))
        {
            // Kode baru yang disarankan, menggunakan objek SignatureField (kode ini berfungsi dengan baik)
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // Tambahkan tampilan default untuk bidang tanda tangan
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // Bagaimana sekarang mendapatkan newAddedField terlihat di semua halaman?
            Aspose.Pdf.Annotations.Annotation addedField = null;
            foreach (Aspose.Pdf.Annotations.Annotation a in doc.Pages[1].Annotations)
            {
            if (a.FullName == fieldName)
                {
                    addedField = a;
                    break;
                }
            }
            if (addedField != null)
            {
                for (int p = 1; p <= doc.Pages.Count; p++)
                {
                    if (p == page) continue;
                    doc.Pages[p].Annotations.Add(addedField);
                }
            }

            doc.Save();
        }
        System.Diagnostics.Process.Start(dest);
    }
```
## Apa yang Baru di Aspose.PDF 24.2

Sejak 24.2 memungkinkan untuk mendapatkan data vektor dari file PDF

Telah diimplementasikan GraphicsAbsorber untuk mendapatkan data vektor dari dokumen:

```cs
var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## Apa yang Baru di Aspose.PDF 24.1

Sejak rilis 24.1 memungkinkan untuk mengimpor anotasi format FDF ke PDF:

```cs
    var fdfPath = Params.InputPath + "50745.fdf";
    var templatePath = Params.InputPath + "Empty.pdf";
    var outputPath = Params.OutputPath + "50745_form.pdf";

    using (var form = new Aspose.Pdf.Facades.Form(templatePath))
    {
        using (var fdfInputStream = new FileStream(fdfPath, FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }

        form.Save(outputPath);
    }
```

Juga, mendukung akses ke Kamus Halaman atau Katalog Dokumen.

Juga, mendukung akses ke Kamus Halaman atau Katalog Dokumen.

Berikut adalah contoh kode untuk DictionaryEditor:

- Menambahkan nilai baru

```cs
    // contoh nama kunci
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    var outputPath = "page_dictionary_editor.pdf";
    menggunakan (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new CosPdfName("data nama"));
        dictionaryEditor.Add(KEY_STRING, new CosPdfString("data string"));
        dictionaryEditor.Add(KEY_BOOL, new CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new CosPdfNumber(11.2));

        doc.Save(outputPath);
    }
```

- Menambahkan dan mengatur nilai ke kamus

```cs
    menggunakan (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Nama lama"));
        // atau
        dictionaryEditor[KEY_NAME] = new CosPdfName("Nama baru");
    }
```
- Dapatkan nilai dari kamus

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // atau 
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- Hapus nilai dari kamus

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## Apa yang baru di Aspose.PDF 23.12

Formulir dapat ditemukan dan teks dapat diganti menggunakan potongan kode berikut:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var absorber = new TextFragmentAbsorber();
            absorber.Visit(form);

            foreach (var fragment in absorber.TextFragments)
            {
                fragment.Text = "";
            }
        }
    }

    document.Save(output);
```            

Atau, formulir dapat dihapus sepenuhnya:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    for (int i = 1; i <= forms.Count; i++)
    {
        if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
        {
            forms.Delete(forms[i].Name);
        }
    }

    document.Save(output);
```            

Varian lain dari menghapus formulir:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var name = forms.GetFormName(form);
            forms.Delete(name);
        }
    }

    document.Save(output);
``` 

- Semua formulir dapat dihapus menggunakan potongan kode berikut:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- Implementasi konversi PDF ke Markdown:

```cs
    string markdownOutputFilePath = "output.md"
    string inputPdfPath = "input.pdf"
    using (Document doc = new Document(inputPdfPath))
    {
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.ResourcesDirectoryName = "images"; 
    doc.Save(markdownOutputFilePath, saveOptions);
    }
```

- Implementasi konversi OFD ke PDF:

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

Dari rilis ini ditambahkan plugin Merger:

```cs
    // Path ke file PDF yang digabungkan.
    var outputPath = "TestMerge.pdf";

    // Buat instance baru dari Merger.
    var merger = new Merger();

    // Buat MergeOptions.
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // Proses penggabungan PDF.
    merger.Process(opt);
```

Juga, dari rilis ini ditambahkan plugin ChatGPT:
Mulai dari rilis ini, telah ditambahkan plugin ChatGPT:

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Menambahkan jalur file keluaran.
    options.ApiKey = "Kunci API Anda."; // Anda perlu menyediakan kunci untuk mengakses API.
    options.MaxTokens = 1000; // Jumlah maksimum token yang dihasilkan dalam penyelesaian chat.

    // Menambahkan pesan permintaan.
    options.Messages.Add(new Message
    {
        Content = "Anda adalah asisten yang membantu.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "Berapa diameter pizza terbesar yang pernah dibuat?",
        Role = Role.User
    });

    // Memproses permintaan.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // Objek penyelesaian chat API ChatGPT.
    }
```

## Apa yang baru di Aspose.PDF 23.11
## Apa yang Baru di Aspose.PDF 23.11

Dari rilis ini, dimungkinkan untuk menghapus teks tersembunyi dari file PDF:

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // Opsi ini dapat digunakan untuk mencegah fragment teks lain bergerak setelah penggantian teks tersembunyi.
        textAbsorber.TextReplaceOptions = new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        document.Save(outputFile);
```

Sejak 23.11 mendukung untuk interupsi thread:

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        //ini adalah beberapa teks besar, menggunakan Lorem Ipsum dalam 8350 karakter untuk menyebabkan penangguhan
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // Timeout harus kurang dari waktu yang dibutuhkan untuk menyimpan dokumen lengkap (tanpa interupsi).
            Thread.Sleep(500);

            // Mengganggu proses
            monitor.Interrupt();

            // Menunggu interupsi...
            thread.Join();
        }
        private class RowSpanWorker
        {
            private readonly string outputPath;
            private readonly InterruptMonitor monitor;

            public RowSpanWorker(string outputPath, InterruptMonitor monitor)
            {
                this.outputPath = outputPath;
                this.monitor = monitor;
            }
            public void Work()
            {
                string text = InterruptMonitorTests.LongText;
                using (var doc = new Document())
                {
                    InterruptMonitor.ThreadLocalInstance = this.monitor;
                    var page = doc.Pages.Add();

                    var table = new Aspose.Pdf.Table
                    {
                        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
                    };

                    var row0 = table.Rows.Add();

                    // menambahkan sel yang membentang untuk dua baris dan berisi teks panjang-panjang
                    var cell00 = row0.Cells.Add(text);
                    cell00.RowSpan = 2;
                    cell00.IsWordWrapped = true;
                    row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
                    row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

                    var row1 = table.Rows.Add();
                    row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
                    row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

                    page.Paragraphs.Add(table);

                    try
                    {
                        doc.Save(this.outputPath);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex.Message);
                    }
                }
            }
        }
    }
```
## Apa yang Baru di Aspose.PDF 23.10

Pembaruan saat ini menyajikan tiga versi dari Menghapus tag dari PDF yang ditandai.

- Hapus beberapa elemen node dari documentElement (elemen pohon akar):

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
    if (documentElement.Children.Remove(structElement))
    {
        // elemen dihapus
        document.Save(outputPath);
    }

    // Anda juga dapat menghapus structElement itu sendiri
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- Hapus semua tag elemen yang ditandai dari dokumen, tetapi pertahankan elemen struktur:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var root = structure.Children[0];
    var queue = new Queue<Element>();
    queue.Enqueue(root);
    while(queue.TryDequeue(out var element))
    {
        foreach (var child in element.Children)
        {
            queue.Enqueue(child);
        }

        if (element is TextElement || element is FigureElement)
        {
            element.Remove();
        }
    }
```
- Hapus semua tag:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

Sejak 23.10 telah diimplementasikan fitur baru untuk mengukur tinggi karakter. Gunakan kode berikut untuk mengukur tinggi karakter.

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

Perhatikan bahwa pengukuran ini berdasarkan font yang tertanam dalam dokumen. Jika ada informasi untuk dimensi yang hilang, metode ini mengembalikan 0.

Juga, rilis ini menyediakan fitur untuk Menandatangani PDF menggunakan HASH yang telah ditandatangani:

```cs
    public void PDFNET_54566()
    {
        var inputPdf = "54566.pdf";
        var inputP12 = "54566.p12";
        var inputPfxPassword = "123456";
        var outputPdf = "54566_out.pdf";
        using (var sign = new PdfFileSignature())
        {
            sign.BindPdf(inputPdf);
            var pkcs7 = new PKCS7(inputP12, inputPfxPassword);
            pkcs7.CustomSignHash = CustomSignHash;
            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
            sign.Save(outputPdf);
        }
        using (var sign = new PdfFileSignature())
        {
            sign.BindPdf(outputPdf);
            Assert.IsTrue(sign.VerifySignature("Signature1"));
        }
    }

    private byte[] CustomSignHash(byte[] signableHash)
    {
        var inputP12 = "54566.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
```
Satu fitur baru lagi adalah Skala Halaman dalam Dialog Cetak Preset:

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## Apa yang baru di Aspose.PDF 23.9

Sejak 23.9 mendukung penghapusan anotasi anak dari bidang yang dapat diisi.

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation .PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## Apa yang baru di Aspose.PDF 23.8

Sejak 23.8 mendukung deteksi Pembaruan Inkremental.

Fungsi untuk mendeteksi Pembaruan Inkremental dalam dokumen PDF telah ditambahkan. Fungsi ini mengembalikan 'true' jika dokumen disimpan dengan pembaruan inkremental; jika tidak, ia mengembalikan 'false'.

```cs

    var path = "C:\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

Juga, 23.8 mendukung cara bekerja dengan bidang checkbox bersarang.
Juga, 23.8 mendukung cara untuk bekerja dengan bidang kotak centang bersarang.

- Buat bidang kotak centang multi-nilai:

```cs
    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // Tetapkan nilai opsi grup kotak centang pertama
    checkbox.ExportValue = "opsi 1";

    // Tambahkan opsi baru tepat di bawah yang sudah ada
    checkbox.AddOption("opsi 2");

    // Tambahkan opsi baru pada persegi panjang yang diberikan
    checkbox.AddOption("opsi 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // Pilih kotak centang yang ditambahkan
    checkbox.Value = "opsi 2";
    document.Save("checkbox_group.pdf");
    }
```

- Dapatkan dan tetapkan nilai kotak centang multi-nilai:

```cs
    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // Nilai yang diizinkan dapat diambil dari koleksi AllowedStates
    // Tetapkan nilai kotak centang menggunakan properti Value
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // nilai yang sebelumnya ditetapkan, contoh "opsi 1"

    // Nilai tersebut harus menjadi salah satu elemen dari AllowedStates
    checkbox.Value = "opsi 2";
    checkboxValue = checkbox.Value; // opsi 2

    // Hapus centang kotak dengan mengatur Value menjadi "Off" atau mengatur Checked menjadi false
    checkbox.Value = "Off";
    // atau, secara bergantian:
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
    }
```
## Apa yang Baru di Aspose.PDF 23.7

Dari Aspose.PDF 23.7 dukungan untuk menambahkan ekstraksi bentuk:

```cs
    public void PDFNET_46298()
    {
        var input1 = "46298_1.pdf";
        var input2 = "46298_2.pdf";

        var source = new Document(input1);
        var dest = new Document(input2);

        var graphicAbsorber = new GraphicsAbsorber();
        graphicAbsorber.Visit(source.Pages[1]);
        var area = new Rectangle(90, 250, 300, 400);
        dest.Pages[1].AddGraphics(graphicAbsorber.Elements, area);
    }
```

Juga mendukung kemampuan untuk mendeteksi Overflow saat menambahkan teks:

```cs
    var doc = new Document();
    var paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    var rectangle = new Rectangle(100, 600, 500, 700, false);
    var paragraph = new TextParagraph();
    var fragment = new TextFragment(paragraphContent);
    paragraph.VerticalAlignment = VerticalAlignment.Top;
    paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
    paragraph.Rectangle = rectangle;
    var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.TextState.FontSize -= 0.5f;
        isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
    }
    paragraph.AppendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.Pages.Add());
    builder.AppendParagraph(paragraph);
    doc.Save(output);
```
## Apa yang Baru di Aspose.PDF 23.6

Dari Aspose.PDF 23.6 mendukung penambahan plugin berikut:

- Aspose PdfConverter Html ke PDF
- Aspose PdfOrganizer Resize API
- Aspose PdfOrganizer Compress API

Perbarui Aspose.PdfForm 
- menambahkan fitur 'Ekspor "Nilai dari bidang di dokumen ke file CSV"
- menambahkan kemampuan untuk mengatur properti untuk bidang terpisah

Juga mendukung penambahan kemampuan untuk mengatur judul halaman HTML, Epub:

```cs
    var document = new Document(Params.InputPath + "53357.pdf");

    var htmlSaveOptions = new HtmlSaveOptions
    {
        ExplicitListOfSavedPages = new[] { 1 },
        SplitIntoPages = false,
        FixedLayout = true,
        CompressSvgGraphicsIfAny = false,
        SaveTransparentTexts = true,
        SaveShadowedTextsAsTransparentTexts = true,
        FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
        RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
        PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
        Title = "Judul untuk halaman"   // <-- ini ditambahkan
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```
## Apa yang Baru di Aspose.PDF 23.5

Sejak 23.5 mendukung untuk menambahkan opsi FontSize pada RedactionAnnotation. Gunakan cuplikan kode berikut untuk menyelesaikan tugas ini:

```cs

    Document doc = new Document(dataDir + "test_factuur.pdf");

    // Membuat instansi RedactionAnnotation untuk wilayah halaman tertentu
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // Teks yang akan dicetak pada anotasi redact
    annot.OverlayText = "(Unknown)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // Ulangi Teks Overlay di atas anotasi Redact
    annot.Repeat = false;
    // Properti baru di sini !
    annot.FontSize = 20;
    // Tambahkan anotasi ke koleksi anotasi halaman pertama
    doc.Pages[1].Annotations.Add(annot);
    // Meratakan anotasi dan mengedit konten halaman (yaitu menghapus teks dan gambar
    // Di bawah anotasi yang diredaksi)
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## Apa yang Baru di Aspose.PDF 23.4

Aspose.PDF mengumumkan rilis SDK .NET 7.

## Apa yang Baru di Aspose.PDF 23.3.1

Dari Aspose.PDF 23.3 mendukung penambahan plugin berikut:

- Aspose.PdfForm
- Aspose.PdfConverter PDF ke HTML
- Aspose.PdfConverter PDF ke XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator untuk Gambar

## Apa yang Baru di Aspose.PDF 23.3

Versi 23.3 memperkenalkan dukungan untuk menambahkan resolusi pada gambar. Dua metode dapat digunakan untuk menyelesaikan masalah ini:

```cs
    var table = new Table
            {
                ColumnWidths = "600"
            };

            for(var j = 0; j < 2; j ++)
            {
                var row = table.Rows.Add();
                var cell = row.Cells.Add();
                cell.Paragraphs.Add(new Image()
                {
                    IsApplyResolution = true,
                    File = imageFile
                });
            }

            page.Paragraphs.Add(table);
```

Dan pendekatan kedua:

```cs
    page.Paragraphs.Add(new Image()
            {
                IsApplyResolution = true,
                File = imageFile
            });
            page.Paragraphs.Add(new Image()
            {
                IsApplyResolution = true,
                File = imageFile
            });
```
Gambar akan ditempatkan dengan resolusi yang disesuaikan atau Anda bisa mengatur properti FixedWidth atau FixedHeight dalam kombinasi dengan IsApplyResolution

## Apa yang baru di Aspose.PDF 23.1.1

Dari Aspose.PDF 23.1.1 mendukung penambahan plugin berikut:

- Plugin Aspose.PdfOrganizer
- Plugin Aspose.PdfExtractor

## Apa yang baru di Aspose.PDF 23.1

Sejak versi 23.1 mendukung pembuatan anotasi PrinterMark.

Tanda printer adalah simbol grafis atau teks yang ditambahkan ke halaman untuk membantu personel produksi dalam mengidentifikasi komponen pekerjaan pelat berganda dan menjaga keluaran yang konsisten selama produksi. Contoh yang umum digunakan dalam industri percetakan meliputi:

- Target registrasi untuk menyelaraskan pelat
- Ramping abu-abu dan bar warna untuk mengukur warna dan kepadatan tinta
- Tanda potong menunjukkan di mana media keluaran harus dipotong

Kami akan menunjukkan contoh opsi dengan bar warna untuk mengukur warna dan kepadatan tinta.
Kami akan menunjukkan contoh opsi dengan bar warna untuk mengukur warna dan kepadatan tinta.

```cs
var outFile = myDir + "ColorBarTest.pdf");

using (var doc = new Document())
{
    Page page = doc.Pages.Add();
    page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);
    AddAnnotations(page);
    doc.Save(outFile);
}

void AddAnnotations(Page page)
{
    var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
    var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
    var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

    var colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    var colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    var colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.ColorOfCMYK = ColorsOfCMYK.Magenta;
    var colorBarYellow = new ColorBarAnnotation(page, new Aspose.Pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.Annotations.Add(colorBarBlack);
    page.Annotations.Add(colorBarCyan);
    page.Annotations.Add(colorBaMagenta);
    page.Annotations.Add(colorBarYellow);
}
```
Juga mendukung ekstraksi gambar vektor. Coba gunakan kode berikut untuk mendeteksi dan mengekstrak grafik vektor:

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## Apa yang baru di Aspose.PDF 22.12

Dari rilis ini mendukung untuk mengonversi PDF ke Gambar DICOM

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```    

## Apa yang baru di Aspose.PDF 22.09

Sejak 22.09 mendukung penambahan properti untuk memodifikasi urutan rubrik subjek (E=, CN=, O=, OU=, ) dalam tanda tangan.

```cs
    using (var fileSign = new PdfFileSignature())
    {
        fileSign.BindPdf(inputPdf);
        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new PKCS7Detached(inputPfx, "123456789");
        signature.CustomAppearance = new SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.CN, SubjectNameElements.O }
            //or
            //DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.OU, SubjectNameElements.S, SubjectNameElements.C }
        };
        fileSign.Sign(1, true, rect, signature);
        fileSign.Save(outputPdf);
    }
```
## Apa yang Baru di Aspose.PDF 22.6

Sejak 22.5 mendukung ekstraksi teks SubScript dan SuperScript dari PDF.

Jika dokumen PDF mengandung teks SubScript dan SuperScript seperti H2O, maka mengekstrak teks dari PDF juga harus mengekstrak informasi pemformatan mereka (dalam teks polos yang diekstrak).
Jika PDF mengandung teks miring, itu juga harus disertakan dalam konten yang diekstrak.

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## Apa yang Baru di Aspose.PDF 22.4

Rilis ini mencakup informasi untuk Aspose.PDF untuk .NET:

- PDF ke ODS: Mengenali teks dalam subscript dan superscript;

**contoh**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods"), options);
```

- PDF ke XMLSpreadSheet2003: Mengenali teks dalam subscript dan superscript;

- PDF ke Excel: Mengenali teks dalam subscript dan superscript;
- PDF ke Excel: Mengenali teks dalam subskrip dan superskrip;

- Menghapus tanda tangan UR saat menyimpan dokumen;

- Menghapus bendera Suspects di MarkInfo saat menyimpan dokumen;

- Menghapus Info saat menyimpan dokumen

## Apa yang baru di Aspose.PDF 22.3

Rilis ini mencakup pembaruan berikut:

- Dukungan untuk AFRelationship;

- Validasi header PDF;

- Menghapus subfilter adbe.x509.rsa_sha1 saat menyimpan dokumen;

- Memformat Field sebagai Angka dan Format Tanggal;

- Melarang penggunaan enkripsi RC4 di FDF 2.0ю

## Apa yang baru di Aspose.PDF 22.2

Dari versi 22.2, dimungkinkan untuk menandatangani dokumen menggunakan PdfFileSignature dengan LTV, dan dengan kemampuan untuk mengubah hashing dari SHA1 menjadi SHA256.

```csharp
Contoh penggunaan:
var inputPdf = "51168.pdf";
var inputPfx = "51168.pfx";
var inputPfxPassword = "111111";
var outputPdf = "51168.pdf";

using (var doc = new Document(inputPdf))
{
    using (PdfFileSignature signature = new PdfFileSignature(doc))
    {
        var pkcs = new PKCS7(inputPfx, inputPfxPassword)
        {
            UseLtv = true,
            TimestampSettings = new TimestampSettings("http://freetsa.org/tsr", string.Empty, DigestHashAlgorithm.Sha256)
        };
        signature.Sign(1, false, new System.Drawing.Rectangle(300, 100, 1, 1), pkcs);
        signature.Save(outputPdf);
    }
}
```
## Apa yang baru di Aspose.PDF 22.1

Sekarang, Aspose.PDF untuk .NET mendukung memuat dokumen dari salah satu format dokumen paling populer, Portable Document Format (PDF) versi 2.0.

## Apa yang baru di Aspose.PDF 21.11

### Izinkan karakter non-latin dalam kata sandi

```csharp
Aspose.Pdf.Facades.PdfFileSecurity fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity();
fileSecurity.AllowExceptions = true;
    try
{
 fileSecurity.BindPdf(exportDoc);
 bool res = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
 Console.WriteLine(res);
 fileSecurity.Save(output("encrypted.pdf"));
}
    catch(Exception e)
{
    Console.WriteLn("Exception: " + e.Message);
}
```

## Apa yang baru di Aspose.PDF 21.10

### Bagaimana mendeteksi teks tersembunyi?

Silakan gunakan TextState.Invisible untuk mendapatkan informasi tentang ketidakterlihatan teks dari pengaturan mode rendering.

Kami menggunakan kode berikut untuk pengujian:

```csharp
Document pdf = new Document(dataDir + "TestPage.pdf");
Console.WriteLine(pdf.FileName);
var page = pdf.Pages[1];
var textFragmentAbsorber = new TextFragmentAbsorber();
page.Accept(textFragmentAbsorber);
var textFragmentCollection = textFragmentAbsorber.TextFragments;
for (int i = 1; i <= textFragmentCollection.Count; i++)
{
    TextFragment fragment = textFragmentCollection[i];
    Console.WriteLine("Fragment {0} at {1}", i, fragment.Rectangle.ToString());
    Console.WriteLine("Text: {0}", fragment.Text);
    Console.WriteLine("RenderingMode: {0}", fragment.TextState.RenderingMode.ToString());
    Console.WriteLine("Invisibility: {0}", fragment.TextState.Invisible);
    Console.WriteLine("---");
}
```
### Bagaimana cara mendapatkan informasi tentang jumlah lapisan dalam dokumen PDF?

```csharp
Silakan gunakan potongan kode:
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## Apa yang baru di Aspose.PDF 21.9

Sesuaikan warna latar belakang untuk tampilan tanda tangan dan warna font label di area tanda tangan dengan Aspose.PDF untuk .NET.

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    var pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//setel warna
        ForegroundColor = Color.DarkGreen,
        BackgroundColor = Color.LightSeaGreen,
    };
    pdfSign.Sign(1, true, rect, pkcs);
    pdfSign.Save(outFile);
}
```

## Apa yang baru di Aspose.PDF 21.8

### Bagaimana cara mengubah warna teks dalam Tanda Tangan Digital?

Dalam versi 21.8  properti ForegroundColor, memungkinkan mengubah warna teks dalam Tanda Tangan Digital.

```csharp
```
```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //membuat persegi panjang untuk lokasi tanda tangan
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//atur warna teks
        ForegroundColor = Color.Green
    };
    // menandatangani file PDF
    pdfSign.Sign(1, true, rect, pkcs);
    //menyimpan file PDF keluaran
    pdfSign.Save(outFile);
}
```

## Apa yang baru di Aspose.PDF 21.7

### Pembuatan PDF berdasarkan XML dan XLS dengan parameter

Untuk menambahkan parameter XSL kita perlu membuat [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) sendiri dan mengatur sebagai properti di [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). Potongan kode berikut menunjukkan cara menggunakan kelas ini dengan file contoh yang dijelaskan di atas.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //Contoh penggunaan XsltArgumentList
         XsltArgumentList argsList = new XsltArgumentList();
        argsList.AddParam("isBoldName", "", "yes");
        //---------------------

        var pdfDocument = new Aspose.Pdf.Document(TransformXml(XmlContent, XsltContent, argsList), options);
        pdfDocument.Save(_dataDir + "data_xml.pdf");
    }

 public static MemoryStream TransformXml(string inputXml, string xsltString, XsltArgumentList argsList=null)
    {
            var transform = new XslCompiledTransform();
            using (var reader = XmlReader.Create(new StringReader(xsltString)))
            {
                transform.Load(reader);
            }
            var memoryStream = new MemoryStream();

            var results = new StreamWriter(memoryStream);
            using (var reader = XmlReader.Create(new StringReader(inputXml)))
            {
                transform.Transform(reader, argsList, results);
            }

            memoryStream.Position = 0;
            return memoryStream;
    }
```
## Apa yang Baru di Aspose.PDF 21.6

Dengan Aspose.PDF untuk .NET Anda dapat menyembunyikan gambar menggunakan ImagePlacementAbsorber dari dokumen:

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // Menyembunyikan gambar di halaman pertama
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## Apa yang Baru di Aspose.PDF 21.5

### Bagaimana cara mengekstrak nama lengkap font dari deskripsi/sumber daya di PDF?

Anda bisa mendapatkan font lengkap dengan awalan dengan properti BaseFont untuk kelas Font.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
}
pdf.Dispose();
```

## Apa yang Baru di Aspose.PDF 21.4

### Tambahkan API untuk menggabungkan gambar

Aspose.PDF 21.4 memungkinkan Anda untuk menggabungkan Gambar.
Aspose.PDF 21.4 memungkinkan Anda untuk menggabungkan Gambar.

```csharp
private static void MergeAsJpeg()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.jpg", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\49616_600.jpg", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream =
                 PdfConverter.MergeImages(inputImagesStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.jpg", FileMode.Create))
               {
                   byte[] buffer = new byte[32768];
                   int read;
                   while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                   {
                       outputStream.Write(buffer, 0, read);
                   }
               }
           }
       }
    }
}
```
Anda juga dapat menggabungkan gambar Anda sebagai format Tiff:

```csharp
private static void MergeAsTiff()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.tiff", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\600.tiff", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream = PdfConverter.MergeImagesAsTiff(inputImagesStreams))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.tiff", FileMode.Create))
               {
                   byte[] buffer = new byte[32768];
                   int read;
                   while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                   {
                       outputStream.Write(buffer, 0, read);
                   }
               }
           }
       }
    }
}
```

## Apa yang baru di Aspose.PDF 21.3

### Paparan publik dari properti untuk mendeteksi Perlindungan Informasi Azure
### Paparan Publik Properti untuk Mendeteksi Perlindungan Informasi Azure

Dengan cuplikan kode berikut, Anda harus dapat mengakses muatan terenkripsi dari file PDF Anda, yang dilindungi dengan Perlindungan Informasi Azure:

```csharp
 public void Azure_Information_Protection()
 {
     string inputFile = @"c:\pdf.pdf";
     Document document = new Document(inputFile);
     if (document.EmbeddedFiles[1].AFRelationship == AFRelationship.EncryptedPayload)
     {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
              // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
              // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
              // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
     }
}
```

## Apa yang Baru di Aspose.PDF 21.1

### Menambahkan dukungan untuk mengambil warna latar belakang TextFragment

Dalam versi ini dari Aspose.PDF, fungsi tersedia untuk mengambil warna latar belakang.
Dalam versi Aspose.PDF ini, fungsi telah tersedia untuk mengambil warna latar belakang.

Harap pertimbangkan kode berikut:

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// Terima absorber untuk semua halaman
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Dapatkan fragmen teks yang diekstrak
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Loop melalui fragmen
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Text: '{0}'", textFragment.Text);
    Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### Setelah dikonversi ke HTML, font sepenuhnya tertanam dalam output

Juga, di Aspose.PDF 21.1, setelah mengonversi PDF ke HTML, font yang tertanam dalam dokumen HTML output menjadi tersedia. Hal ini dimungkinkan dengan opsi simpan boolean baru HtmlSaveParameter.SaveFullFont.

Berikut adalah potongan kode:

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
