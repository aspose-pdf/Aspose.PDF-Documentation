---
title: Konversi format file lain ke PDF dengan Python
linktitle: Konversi format file lain ke PDF
type: docs
weight: 80
url: /id/python-net/convert-other-files-to-pdf/
lastmod: "2025-09-01"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan mengonversi format file lain seperti EPUB, MD, PCL, XPS, PS, XML, dan LaTeX ke dokumen PDF.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cara Mengonversi format file lain ke PDF dengan Python
Abstract: Artikel ini memberikan panduan komprehensif tentang mengonversi berbagai format file ke PDF menggunakan Python, memanfaatkan kemampuan Aspose.PDF untuk Python via .NET. Dokumen ini menjabarkan proses konversi untuk beberapa format, termasuk EPUB, Markdown, PCL, Teks, XPS, PostScript, XML, XSL-FO, dan LaTeX/TeX. Setiap bagian menyediakan cuplikan kode spesifik dan instruksi untuk mengimplementasikan konversi ini. Artikel ini menekankan kegunaan fitur Aspose.PDF, seperti opsi pemuatan yang disesuaikan untuk setiap tipe file, guna memastikan konversi yang akurat dan efisien. Selain itu, artikel ini menyoroti ketersediaan aplikasi konversi online gratis bagi pengguna untuk mencoba fungsionalitas secara langsung. Panduan ini berfungsi sebagai sumber praktis bagi pengembang yang ingin mengintegrasikan kemampuan konversi PDF ke dalam aplikasi Python mereka.
---

Artikel ini menjelaskan cara **mengonversi berbagai jenis format file lain ke PDF menggunakan Python**. Artikel ini mencakup topik berikut.

## Konversi OFD ke PDF

OFD singkatan dari Open Fixed-layout Document (juga disebut format Open Fixed Document). Ini adalah standar nasional Tiongkok (GB/T 33190-2016) untuk dokumen elektronik, diperkenalkan sebagai alternatif PDF.

Langkah-langkah Mengonversi OFD ke PDF dengan Python:

1. Siapkan opsi pemuatan OFD menggunakan OfdLoadOptions().
1. Muat dokumen OFD.
1. Simpan sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Konversi LaTeX/TeX ke PDF

Format file LaTeX adalah format file teks dengan markup dalam turunan LaTeX dari keluarga bahasa TeX dan LaTeX merupakan format turunan dari sistem TeX. LaTeX (ˈleɪtɛk/lay-tek atau lah-tek) adalah sistem penyiapan dokumen dan bahasa markup dokumen. Ini banyak digunakan untuk komunikasi dan publikasi dokumen ilmiah di banyak bidang, termasuk matematika, fisika, dan ilmu komputer. Ia juga memainkan peran kunci dalam penyiapan dan publikasi buku serta artikel yang berisi materi multibahasa kompleks, seperti Korea, Jepang, karakter Cina, dan Arab, termasuk edisi khusus.

LaTeX menggunakan program penataan huruf TeX untuk memformat outputnya, dan ia sendiri ditulis dalam bahasa makro TeX.

{{% alert color="success" %}}
**Coba konversi LaTeX/TeX ke PDF secara online**

Aspose.PDF untuk Python via .NET mempersembahkan aplikasi gratis online ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF LaTeX/TeX ke PDF dengan Aplikasi Gratis](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Langkah-langkah Mengonversi TEX ke PDF dengan Python:

1. Siapkan opsi pemuatan LaTeX menggunakan LatexLoadOptions().
1. Muat dokumen LaTeX.
1. Simpan sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
## Konversi OFD ke PDF

OFD singkatan dari Open Fixed-layout Document (kadang disebut format Open Fixed Document). Ini adalah standar nasional Tiongkok (GB/T 33190-2016) untuk dokumen elektronik, diperkenalkan sebagai alternatif PDF.

Langkah-langkah Mengonversi OFD ke PDF dengan Python:

1. Siapkan opsi pemuatan OFD menggunakan OfdLoadOptions().
1. Muat dokumen OFD.
1. Simpan sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Konversi LaTeX/TeX ke PDF

Format file LaTeX adalah format file teks dengan markup dalam turunan LaTeX dari keluarga bahasa TeX dan LaTeX adalah format turunan dari sistem TeX. LaTeX (ˈleɪtɛk/lay-tek atau lah-tek) adalah sistem penyiapan dokumen dan bahasa markup dokumen. Ia banyak digunakan untuk komunikasi dan publikasi dokumen ilmiah di banyak bidang, termasuk matematika, fisika, dan ilmu komputer. Ia juga memiliki peran penting dalam penyiapan dan publikasi buku serta artikel yang berisi materi multibahasa kompleks, seperti Sanskrit dan Arab, termasuk edisi kritis. LaTeX menggunakan program penataan huruf TeX untuk memformat outputnya, dan ia sendiri ditulis dalam bahasa makro TeX.

{{% alert color="success" %}}
**Coba konversi LaTeX/TeX ke PDF secara online**

Aspose.PDF untuk Python via .NET mempersembahkan aplikasi gratis online ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF LaTeX/TeX ke PDF dengan Aplikasi Gratis](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Langkah-langkah Mengonversi TEX ke PDF dengan Python:

1. Siapkan opsi pemuatan LaTeX menggunakan LatexLoadOptions().
1. Muat dokumen LaTeX.
1. Simpan sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Konversi EPUB ke PDF

**Aspose.PDF untuk Python via .NET** memungkinkan Anda dengan mudah mengonversi file EPUB ke format PDF.

EPUB (singkatan dari electronic publication) adalah standar buku elektronik yang gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub. EPUB dirancang untuk konten yang dapat mengalir ulang, artinya pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu.

<abbr title="electronic publication">EPUB</abbr> juga mendukung konten tata letak tetap. Format ini dimaksudkan sebagai satu format yang dapat digunakan penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Format ini menggantikan standar Open eBook. Versi EPUB 3 juga didukung oleh Book Industry Study Group (BISG), sebuah asosiasi perdagangan buku terkemuka untuk praktik terbaik standar, penelitian, informasi, dan acara, untuk pengemasan konten.

{{% alert color="success" %}}
**Coba mengonversi EPUB ke PDF secara online**

Aspose.PDF untuk Python via .NET mempersembahkan aplikasi gratis online ["EPUB ke PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF EPUB ke PDF dengan Aplikasi Gratis](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Langkah-langkah Mengonversi EPUB ke PDF dengan Python:

1. Muat Dokumen EPUB dengan EpubLoadOptions().
1. Konversi EPUB ke PDF.
1. Cetak Konfirmasi.

Potongan kode berikut menunjukkan cara mengonversi file EPUB ke format PDF dengan Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.EpubLoadOptions()
    document = ap.Document(path_infile, load_options)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Mengonversi Markdown ke PDF

**Fitur ini didukung oleh versi 19.6 atau lebih tinggi.**

{{% alert color="success" %}}
**Coba mengonversi Markdown ke PDF secara online**

Aspose.PDF untuk Python via .NET mempersembahkan aplikasi gratis online ["Markdown ke PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF Markdown ke PDF dengan Aplikasi Gratis](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Potongan kode ini oleh Aspose.PDF untuk Python via .NET membantu mengonversi file Markdown menjadi PDF, memungkinkan berbagi dokumen yang lebih baik, preservasi format, dan kompatibilitas pencetakan.

Potongan kode berikut menunjukkan cara menggunakan fungsi ini dengan pustaka Aspose.PDF:

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.MdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Mengonversi PCL ke PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) adalah bahasa printer Hewlett-Packard yang dikembangkan untuk mengakses fitur standar printer. Tingkat PCL 1 hingga 5e/5c adalah bahasa berbasis perintah yang menggunakan urutan kontrol yang diproses dan diinterpretasikan sesuai urutan penerimaan. Pada tingkat konsumen, aliran data PCL dihasilkan oleh driver printer. Output PCL juga dapat dengan mudah dihasilkan oleh aplikasi khusus.

{{% alert color="success" %}}
**Coba mengonversi PCL ke PDF secara online**

Aspose.PDF untuk .NET mempersembahkan aplikasi gratis online ["PCL ke PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PCL ke PDF dengan Aplikasi Gratis](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

Untuk memungkinkan konversi dari PCL ke PDF, Aspose.PDF memiliki kelas [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) yang digunakan untuk menginisialisasi objek LoadOptions. Selanjutnya objek ini diteruskan sebagai argumen saat inisialisasi objek Document dan membantu mesin render PDF menentukan format input dokumen sumber.

Potongan kode berikut menunjukkan proses mengonversi file PCL menjadi format PDF.

Langkah-langkah Mengonversi PCL ke PDF dengan Python:

1. Muat opsi untuk PCL menggunakan PclLoadOptions().
1. Muat dokumen.
1. Simpan sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Mengonversi Teks Praformat ke PDF

**Aspose.PDF untuk Python via .NET** mendukung fitur mengonversi teks biasa dan file teks pra-format ke format PDF.

Mengonversi teks ke PDF berarti menambahkan fragmen teks ke halaman PDF. Untuk file teks, ada 2 jenis teks: pra-format (misalnya, 25 baris dengan 80 karakter per baris) dan teks tidak terformat (teks biasa). Tergantung pada kebutuhan, kita dapat mengontrol penambahan ini sendiri atau mempercayakannya kepada algoritma perpustakaan.

{{% alert color="success" %}}
**Coba mengonversi TEKS ke PDF secara online**

Aspose.PDF untuk Python via .NET mempersembahkan aplikasi gratis online ["Teks ke PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF TEKS ke PDF dengan Aplikasi Gratis](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Langkah-langkah Mengonversi TEKS ke PDF dengan Python:

1. Baca file teks input baris per baris.
1. Atur font monospaced (Courier New) untuk penyelarasan teks yang konsisten.
1. Buat Dokumen PDF baru dan tambahkan halaman pertama dengan margin dan pengaturan font kustom.
1. Iterasi melalui baris file teks. Untuk mensimulasikan Mesin tik, kami menggunakan font 'monospace_font' dengan ukuran 12.
1. Batasi pembuatan halaman hingga 4 halaman.
1. Simpan PDF akhir ke path yang ditentukan.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    with open(path_infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Mengonversi PostScript ke PDF

Contoh ini menunjukkan cara mengonversi file PostScript menjadi dokumen PDF menggunakan Aspose.PDF untuk Python via .NET.

1. Buat instance 'PsLoadOptions' untuk menginterpretasikan file PS dengan benar.
1. Muat file 'PostScript' ke dalam objek Document menggunakan opsi pemuatan.
1. Simpan dokumen dalam format PDF ke jalur output yang diinginkan.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PsLoadOptions()

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Mengonversi XPS ke PDF

**Aspose.PDF for Python via .NET** mendukung fitur mengonversi file <abbr title="XML Paper Specification">XPS</abbr> ke format PDF. Periksa artikel ini untuk menyelesaikan tugas Anda.

Jenis file XPS terutama terkait dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), yang sebelumnya bernama kode Metro dan mencakup konsep pemasaran Next Generation Print Path (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penampilan dokumen ke dalam sistem operasi Windows-nya.

Potongan kode berikut menunjukkan proses mengonversi file XPS ke format PDF dengan Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XpsLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba mengonversi format XPS ke PDF secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi gratis online ["XPS ke PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya.

[![Konversi Aspose.PDF XPS ke PDF dengan Aplikasi Gratis](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Mengonversi XSL-FO ke PDF

Potongan kode berikut dapat digunakan untuk mengonversi XSLFO ke format PDF dengan Aspose.PDF untuk Python via .NET:

```python

    from os import path
    import aspose.pdf as ap

    path_xsltfile = path.join(self.data_dir, xsltfile)
    path_xmlfile = path.join(self.data_dir, xmlfile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XslFoLoadOptions(path_xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately
    )
    document = ap.Document(path_xmlfile, load_options)
    document.save(path_outfile)

    print(xmlfile + " converted into " + outfile)
```

## Mengonversi XML dengan XSLT ke PDF

Contoh ini menunjukkan cara mengonversi file XML menjadi PDF dengan terlebih dahulu mengubahnya menjadi HTML menggunakan templat XSLT dan kemudian memuat HTML ke dalam Aspose.PDF.

1. Buat instance 'HtmlLoadOptions' untuk mengonfigurasi konversi HTML-ke-PDF.
1. Muat file HTML yang telah diubah ke dalam objek Document Aspose.PDF.
1. Simpan dokumen sebagai PDF pada jalur output yang ditentukan.
1. Hapus file HTML sementara setelah konversi berhasil.

```python

    from os import path
    import aspose.pdf as ap

    def transform_xml_to_html(xml_file, xslt_file, html_file):
        from lxml import etree
        """
        Transform XML to HTML using XSLT and return as a stream
        """
        # Parse XML document
        xml_doc = etree.parse(xml_file)

        # Parse XSLT stylesheet
        xslt_doc = etree.parse(xslt_file)
        transform = etree.XSLT(xslt_doc)

        # Apply transformation
        result = transform(xml_doc)

        # Save result to HTML file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(result))


    def convert_XML_to_PDF(template, infile, outfile):
        path_infile = path.join(data_dir, infile)
        path_outfile = path.join(data_dir, "python", outfile)
        path_template = path.join(data_dir, template)
        path_temp_file = path.join(data_dir, "temp.html")

        load_options = ap.HtmlLoadOptions()
        transform_xml_to_html(path_infile, path_template, path_temp_file)

        document = ap.Document(path_temp_file, load_options)
        document.save(path_outfile)

        if path.exists(path_temp_file):
            os.remove(path_temp_file)

        print(infile + " converted into " + outfile)
```

