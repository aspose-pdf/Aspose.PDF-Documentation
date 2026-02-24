---
title: Bekerja dengan Grafik Vektor menggunakan Python
linktitle: Bekerja dengan Grafik Vektor
type: docs
weight: 100
url: /id/python-net/working-with-vector-graphics/
description: Artikel ini menjelaskan fitur-fitur bekerja dengan alat GraphicsAbsorber menggunakan Python.
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: Gunakan alat GraphicsAbsorber dalam PDF dengan Python
Abstract: Dokumentasi Aspose.PDF untuk Python via .NET tentang artikel Bekerja dengan Grafik Vektor menyediakan panduan komprehensif bagi pengembang yang ingin memanipulasi grafik vektor dalam dokumen PDF menggunakan kelas GraphicsAbsorber. Kelas ini memfasilitasi ekstraksi, pemindahan, penghapusan, dan duplikasi elemen grafik vektor di seluruh halaman PDF.
---

Pada bab ini, kita akan menjelajahi cara menggunakan kelas `GraphicsAbsorber` yang kuat untuk berinteraksi dengan grafik vektor dalam dokumen PDF. Apakah Anda perlu memindahkan, menghapus, atau menambahkan grafik, panduan ini akan menunjukkan cara melakukan tugas-tugas tersebut secara efektif.

## Pendahuluan

Grafik vektor adalah komponen penting dalam banyak dokumen PDF, digunakan untuk merepresentasikan gambar, bentuk, dan elemen grafis lainnya. Aspose.PDF menyediakan kelas `GraphicsAbsorber`, yang memungkinkan pengembang mengakses dan memanipulasi grafik ini secara programatis. Dengan menggunakan metode `Visit` dari `GraphicsAbsorber`, Anda dapat mengekstrak grafik vektor dari halaman tertentu dan melakukan berbagai operasi, seperti memindahkan, menghapus, atau menyalinnya ke halaman lain.

## Mengekstrak Grafik

Langkah pertama dalam bekerja dengan grafik vektor adalah mengekstraknya dari dokumen PDF. Berikut cara melakukannya menggunakan kelas `GraphicsAbsorber`:

1. Buka Dokumen PDF.
1. Inisialisasi GraphicsAbsorber.
1. Pilih Halaman Target.
1. Ekstrak Grafik dari Halaman.
1. Iterasi dan Tampilkan Elemen yang Diekstrak.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

Kelas GraphicsAbsorber merupakan bagian dari namespace aspose.pdf.vector dan dirancang khusus untuk berinteraksi dengan grafik vektor dalam dokumen PDF.

## Memindahkan Grafik

Setelah Anda mengekstrak grafik, Anda dapat memindahkannya ke posisi berbeda pada halaman yang sama. Berikut cara mencapainya:

1. Buka Dokumen PDF.
1. Inisialisasi GraphicsAbsorber.
1. Pilih Halaman Target.
1. Ekstrak Elemen Grafik.
1. Menangguhkan Pembaruan untuk Kinerja.
1. Memodifikasi Posisi Elemen Grafik.
1. Melanjutkan Pembaruan dan Menerapkan Perubahan.
1. Menyimpan Dokumen yang Diperbarui.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Menghapus Grafik

Ada skenario di mana Anda mungkin ingin menghapus grafik tertentu dari halaman. Aspose.PDF untuk Python menawarkan dua metode untuk melakukannya:

### Metode 1: Menggunakan Batas Persegi Panjang

Contoh berikut menunjukkan cara menghapus elemen grafik vektor yang berada dalam area persegi panjang tertentu pada halaman pertama dokumen PDF menggunakan pustaka Aspose.PDF untuk Python via .NET. Proses ini melibatkan identifikasi elemen grafik dalam persegi panjang yang ditentukan dan menghapusnya untuk membersihkan atau memodifikasi konten PDF.

1. Buka Dokumen PDF.
1. Inisialisasi GraphicsAbsorber.
1. Pilih Halaman Target.
1. Ekstrak Elemen Grafik.
1. Menetapkan Persegi Panjang Target.
1. Menangguhkan Pembaruan untuk Kinerja.
1. Menghapus Elemen Grafik dalam Persegi Panjang.
1. Melanjutkan Pembaruan dan Menerapkan Perubahan.
1. Menyimpan Dokumen yang Diperbarui.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Metode 2: Menggunakan Kumpulan Elemen yang Dihapus

Contoh berikut menunjukkan cara menghapus elemen grafik vektor yang berada dalam area persegi panjang tertentu pada halaman pertama dokumen PDF menggunakan pustaka Aspose.PDF untuk Python via .NET. Proses ini melibatkan identifikasi elemen grafik dalam persegi panjang yang ditentukan dan menghapusnya untuk membersihkan atau memodifikasi konten PDF.

1. Buka Dokumen PDF.
1. Inisialisasi GraphicsAbsorber.
1. Pilih Halaman Target.
1. Menetapkan Persegi Panjang Target.
1. Mengekstrak Elemen Grafik.
1. Membuat Koleksi untuk Penghapusan.
1. Mengidentifikasi Elemen di Dalam Persegi Panjang.
1. Menangguhkan Pembaruan demi Kinerja.
1. Menghapus Elemen Grafik.
1. Melanjutkan Pembaruan dan Menerapkan Perubahan.
1. Menyimpan Dokumen yang Diperbarui.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Menambahkan Grafik ke Halaman Lain

Grafik yang diserap dari satu halaman dapat ditambahkan ke halaman lain dalam dokumen yang sama.
Berikut dua metode untuk mencapai ini:

### Metode 1: Menambahkan Grafik Secara Individual

Contoh selanjutnya untuk menyalin elemen grafik vektor dari halaman pertama dokumen PDF dan menempelkannya ke halaman kedua. Operasi ini difasilitasi oleh kelas GraphicsAbsorber, yang memungkinkan ekstraksi dan manipulasi grafik vektor dalam dokumen PDF.

1. Buka Dokumen PDF.
1. Inisialisasi GraphicsAbsorber.
1. Pilih Halaman Target.
1. Mengekstrak Elemen Grafik dari Halaman Pertama.
1. Menangguhkan Pembaruan pada Halaman Kedua demi Kinerja.
1. Menambahkan Elemen Grafik yang Diekstrak ke Halaman Kedua.
1. Melanjutkan Pembaruan dan Menerapkan Perubahan.
1. Menyimpan Dokumen yang Diperbarui.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Metode 2: Menambahkan Grafik sebagai Koleksi

Contoh selanjutnya untuk menggandakan elemen grafik vektor dari halaman pertama dokumen PDF dan menempatkannya ke halaman kedua. Hal ini dicapai dengan menggunakan kelas GraphicsAbsorber, yang memfasilitasi ekstraksi dan manipulasi grafik vektor dalam dokumen PDF.

1. Buka Dokumen PDF.
1. Inisialisasi GraphicsAbsorber.
1. Pilih Halaman Target.
1. Mengekstrak Elemen Grafik dari Halaman Pertama.
1. Menangguhkan Pembaruan pada Halaman Kedua demi Kinerja.
1. Menambahkan Elemen Grafik yang Diekstrak ke Halaman Kedua.
1. Melanjutkan Pembaruan dan Menerapkan Perubahan.
1. Menyimpan Dokumen yang Diperbarui.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
