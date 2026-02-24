---
title: Ekstrak Tabel dari Dokumen PDF
linktitle: Ekstrak Tabel
type: docs
weight: 20
url: /id/python-net/extracting-table/
description: Aspose.PDF untuk Python melalui .NET memungkinkan melakukan berbagai manipulasi dengan tabel yang terdapat dalam dokumen pdf Anda.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengekstrak Tabel dari PDF menggunakan Python
Abstract: Artikel ini membahas proses mengekstrak tabel dari dokumen PDF menggunakan Python, khususnya dengan memanfaatkan Library Aspose.PDF untuk Python melalui .NET. Artikel ini menyediakan contoh kode yang menunjukkan cara memuat dokumen PDF, mengiterasi halaman-halamannya, dan menggunakan kelas `TableAbsorber` untuk mengidentifikasi serta mengekstrak data tabel. Kode tersebut mengiterasi setiap tabel, baris, dan sel, mengumpulkan fragmen teks dan mencetak teks yang diekstrak. Metode ini disorot sebagai alat yang kuat untuk tugas ekstraksi dan analisis data yang melibatkan data tabular dalam PDF.
---

## Ekstrak Tabel dari PDF

Mengekstrak tabel dari PDF menggunakan Python dapat sangat berguna untuk ekstraksi dan analisis data. Dengan Library Aspose.PDF untuk Python melalui .NET, Anda dapat bekerja secara efisien dengan tabel yang tertanam dalam dokumen PDF untuk berbagai tugas terkait data.

Potongan kode ini membuka file PDF yang ada, memindai setiap halaman untuk tabel, dan mengekstrak konten teks selnya. Kode ini menggunakan 'TableAbsorber' untuk mendeteksi tabel dan kemudian mengiterasi baris serta sel untuk mencetak teks di dalamnya.

1. Memuat PDF ke dalam objek ap.Document.
1. Mengulang melalui halaman.
1. Membuat objek TableAbsorber.
1. Mengiterasi tabel.
1. Mengiterasi baris dan sel.
1. Mengekstrak dan mencetak teks dari sel.

Contoh ini membaca PDF, menemukan semua tabel, dan mencetak isi selnya baris per baris.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```


