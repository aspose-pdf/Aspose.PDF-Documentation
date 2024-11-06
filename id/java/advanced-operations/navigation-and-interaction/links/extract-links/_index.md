---
title: Ekstrak Tautan dari File PDF 
linktitle: Ekstrak Tautan
type: docs
weight: 30
url: id/java/extract-links/
description: Ekstrak tautan dari PDF dengan Java. Topik ini menjelaskan cara mengekstrak tautan menggunakan kelas AnnotationSelector. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Tautan dari File PDF

Tautan diwakili sebagai anotasi dalam file PDF, jadi untuk mengekstrak tautan, ekstrak semua objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).

1. Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Dapatkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) yang ingin Anda ekstrak tautannya.
1. Gunakan kelas [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) untuk mengekstrak semua objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) dari halaman yang ditentukan.

1. Berikan objek [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) ke metode Accept dari objek Page.
1. Dapatkan semua anotasi tautan yang dipilih ke dalam objek IList menggunakan metode [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) dari objek [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector).

Cuplikan kode berikut menunjukkan cara mengekstrak tautan dari file PDF.

```java
    public static void ExtractLinksFromThePDFFile() {        
        // Memuat file PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("Anotasi terletak: " + annot.getRect());
        }
                
        // Simpan dokumen dengan tautan yang diperbarui
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```