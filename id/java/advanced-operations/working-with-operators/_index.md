---
title: Bekerja dengan Operator PDF di Java
linktitle: Bekerja dengan Operator
type: docs
weight: 90
url: /id/java/working-with-operators/
description: Pelajari cara menggunakan operator PDF level rendah di Java untuk manipulasi aliran konten, penempatan gambar, penggunaan ulang XForm, dan pembersihan grafis.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gunakan operator PDF level rendah untuk kontrol aliran konten di Java
Abstract: Artikel ini menjelaskan cara bekerja dengan operator PDF tingkat rendah di Aspose.PDF for Java. Pelajari cara menempatkan gambar secara tepat, menggambar konten XForm yang dapat digunakan kembali, dan menghapus operator grafis dari halaman PDF.
---
## Pengantar Operator PDF dan Penggunaannya

Operator adalah kata kunci PDF yang menentukan suatu tindakan yang harus dilakukan, seperti menggambar bentuk grafis di halaman. Kata kunci operator dibedakan dari objek bernama dengan tidak adanya karakter solidus awal (2Fh). Operator hanya memiliki makna di dalam aliran konten.

Aliran konten adalah objek aliran PDF yang datanya terdiri dari instruksi yang menggambarkan elemen grafis yang akan digambar pada halaman. Detail lebih lanjut tentang operator PDF dapat ditemukan di [spesifikasi PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Gunakan halaman ini ketika Anda membutuhkan kontrol langsung atas aliran konten PDF di Java, seperti menempatkan gambar dengan perhitungan matriks eksplisit, menggunakan kembali grafik yang sama berkali-kali melalui XForm, atau menghapus instruksi gambar tingkat rendah dari halaman.

## Tambahkan gambar dengan operator PDF

Gunakan operator tingkat rendah ketika penempatan gambar harus dikontrol secara tepat pada tingkat aliran konten, bukan melalui API tata letak tingkat tinggi.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan dapatkan target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Tambahkan aliran gambar masukan ke sumber daya halaman dan pertahankan nama sumber daya yang dikembalikan.
1. Buat sebuah [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) yang mendefinisikan area target dan bangun sebuah [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) dari batasnya.
1. Gunakan [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) untuk mempertahankan keadaan grafik saat ini, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) untuk menempatkan gambar, [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) untuk melukisnya, dan [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) untuk mengembalikan keadaan sebelumnya.
1. Simpan dokumen PDF yang diperbarui.

```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## Gambar konten XForm yang dapat digunakan kembali pada halaman

Gunakan pendekatan ini ketika gambar atau grafik yang sama harus dirender lebih dari satu kali tanpa menggandakan sumber daya dalam file PDF.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/); dapatkan target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), dan aksesnya [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. Bungkus konten halaman yang ada dengan [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) dan [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) sehingga transformasi selanjutnya tidak bocor ke aliran konten asli.
1. Buat sebuah [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) resource, tambahkan gambar ke sumber daya formulir, dan gunakan [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) plus [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) untuk menggambar gambar di dalam formulir.
1. Tempatkan formulir yang sama pada beberapa koordinat halaman dengan menambahkan matriks translasi dan mengeksekusi nama formulir dengan `Do` operator.
1. Pulihkan keadaan grafik dan simpan PDF keluaran.

```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## Hapus operator grafik dari halaman

Gunakan contoh ini ketika sebuah halaman berisi operator gambar vektor yang harus dihapus langsung dari aliran konten.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan dapatkan target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Iterasi melalui operator konten halaman dan kumpulkan contoh dari [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/), dan [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. Hapus operator yang terkumpul dari konten halaman dan simpan PDF yang diperbarui.

Teknik ini hanya menghapus instruksi gambar yang ditargetkan. Jika halaman juga berisi label teks terkait atau operator non-grafik lainnya, item-item tersebut tetap berada dalam aliran konten dan mungkin memerlukan proses pembersihan terpisah.

```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## Topik Terkait

- [Operasi PDF lanjutan di Java](/pdf/id/java/advanced-operations/)
- [Bekerja dengan gambar dalam PDF menggunakan Java](/pdf/id/java/working-with-images/)
- [Bekerja dengan halaman PDF di Java](/pdf/id/java/working-with-pages/)
- [Bekerja dengan Grafik Vektor di Java](/pdf/id/java/working-with-vector-graphics/)
