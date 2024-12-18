---
title: Perbarui Tautan dalam PDF 
linktitle: Perbarui Tautan
type: docs
weight: 20
url: /id/java/update-links/
description: Memperbarui tautan dalam PDF secara programatis. Panduan ini tentang cara memperbarui tautan dalam PDF dalam bahasa Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Perbarui Tautan dalam File PDF

Seperti dibahas dalam Menambahkan Hyperlink dalam File PDF, kelas [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) memungkinkan penambahan tautan dalam file PDF. Ada juga kelas serupa yang digunakan untuk mendapatkan tautan yang ada dari dalam file PDF. Gunakan ini jika Anda perlu memperbarui tautan yang ada. Untuk memperbarui tautan yang ada:

1. Muat file PDF.
1. Pergi ke halaman tertentu dalam file PDF.
1. Tentukan tujuan tautan menggunakan properti Destination dari objek [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction).

1. Halaman tujuan ditentukan menggunakan konstruktor [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination).

### Setel Target Tautan ke Halaman dalam Dokumen yang Sama

Cuplikan kode berikut menunjukkan cara memperbarui tautan dalam file PDF dan menetapkan targetnya ke halaman kedua dari dokumen.

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // Memuat file PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // Mendapatkan anotasi tautan pertama dari halaman pertama dokumen
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modifikasi tautan: ubah tujuan tautan
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // Menentukan tujuan untuk objek tautan
        // Mewakili tujuan eksplisit yang menampilkan halaman dengan koordinat (kiri, atas) diposisikan di sudut kiri atas 
        // jendela dan isi halaman diperbesar dengan faktor zoom.
        // Parameter pertama adalah nomor halaman tujuan.
        // Yang kedua adalah koordinat kiri
        // Yang ketiga adalah koordinat atas
        // Argumen keempat adalah faktor zoom saat menampilkan halaman yang bersangkutan. Menggunakan 2 berarti halaman akan ditampilkan dengan zoom 200%
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // Menyimpan dokumen dengan tautan yang diperbarui
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Mengatur Tujuan Tautan ke Alamat Web

Untuk memperbarui hyperlink agar mengarah ke alamat web, buat objek [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) dan masukkan ke properti Action dari LinkAnnotation. Cuplikan kode berikut menunjukkan cara memperbarui tautan dalam file PDF dan menetapkan targetnya ke alamat web.

```java
    public static void SetLinkDestinationToWebAddress() {        
        // Memuat file PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // Mendapatkan anotasi tautan pertama dari halaman pertama dokumen
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modifikasi tautan: ubah aksi tautan dan tetapkan target sebagai alamat web
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // Simpan dokumen dengan tautan yang diperbarui
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Set Link Target to Another PDF File

Cuplikan kode berikut menunjukkan cara memperbarui tautan dalam file PDF dan mengatur targetnya ke file PDF lain.

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // Memuat file PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // Baris berikut memperbarui tujuan, tidak memperbarui file
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // Baris berikut memperbarui file
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // Menyimpan dokumen dengan tautan yang diperbarui
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### Update LinkAnnotation Text Color

Anotasi tautan tidak mengandung teks.
 Sebaliknya, teks ditempatkan dalam konten halaman di bawah anotasi. Oleh karena itu, untuk mengubah warna teks, ganti warna teks halaman alih-alih mencoba mengubah warna anotasi. Potongan kode berikut menunjukkan cara memperbarui warna anotasi tautan dalam file PDF.

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // Muat file PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // Cari teks di bawah anotasi
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // Ubah warna teks.
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // Simpan dokumen dengan tautan yang diperbarui
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```