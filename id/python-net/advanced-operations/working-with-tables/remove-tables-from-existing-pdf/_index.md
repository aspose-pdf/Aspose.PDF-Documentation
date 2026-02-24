---
title: Hapus Tabel dari PDF yang ada
linktitle: Hapus Tabel
type: docs
weight: 50
url: /id/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menghapus tabel dari PDF menggunakan Python
Abstract: Artikel ini membahas fungsionalitas Aspose.PDF untuk Python via .NET, khususnya fokus pada manipulasi tabel dalam dokumen PDF. Perpustakaan ini memungkinkan pengguna untuk menyisipkan atau membuat tabel baik pada file PDF baru maupun yang sudah ada, serta memanipulasi atau menghapus tabel dari PDF yang ada. Artikel ini memperkenalkan kelas `TableAbsorber`, yang penting untuk mengidentifikasi dan berinteraksi dengan tabel dalam PDF. Metode baru, `remove()`, telah ditambahkan untuk memungkinkan penghapusan tabel. Dokumen ini menyediakan dua potongan kode - satu yang menunjukkan cara menghapus satu tabel dari PDF, dan yang lainnya menggambarkan penghapusan beberapa tabel. Contoh-contoh ini menyoroti penerapan praktis kelas `TableAbsorber` untuk menghapus tabel dari dokumen PDF.
---

## Hapus Tabel dari Dokumen PDF

Aspose.PDF untuk Python memungkinkan Anda menghapus sebuah tabel dari PDF. Ia membuka PDF yang ada, mendeteksi tabel pertama pada halaman pertama dengan TableAbsorber, menghapus tabel tersebut menggunakan [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods). Setelah itu menyimpan PDF yang diperbarui ke file baru.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## Hapus semua Tabel dari Dokumen PDF

Dengan perpustakaan kami, Anda dapat menghapus semua tabel dari halaman tertentu dalam PDF. Kode membuka PDF yang ada, mendeteksi semua tabel pada halaman kedua dengan TableAbsorber, mengiterasi tabel yang terdeteksi, menghapus masing‑masing, dan kemudian menyimpan PDF yang telah dimodifikasi ke file baru. Ini berguna ketika Anda perlu menghapus tabel secara massal dari sebuah halaman sementara membiarkan konten PDF yang lain tetap utuh.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


