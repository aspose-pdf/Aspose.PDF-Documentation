---
title: Bekerja dengan Operator
linktitle: Bekerja dengan Operator
type: docs
weight: 170
url: /id/java/operators/
description: Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF. Kelas operator menyediakan fitur hebat untuk manipulasi PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Pengenalan Operator PDF dan Penggunaannya

Operator adalah kata kunci PDF yang menentukan beberapa tindakan yang harus dilakukan, seperti melukis bentuk grafis pada halaman. Kata kunci operator dibedakan dari objek bernama oleh tidak adanya karakter solidus awal (2Fh). Operator hanya bermakna di dalam aliran konten.

Aliran konten adalah objek aliran PDF yang datanya terdiri dari instruksi yang menggambarkan elemen grafis yang akan dilukis pada halaman. Detail lebih lanjut tentang operator PDF dapat ditemukan di [spesifikasi PDF](https://www.adobe.com/devnet/pdf/pdf_reference.html).

### Detail Implementasi

Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF.
 Contoh yang dipilih menambahkan gambar ke dalam file PDF untuk mengilustrasikan konsep tersebut. Untuk menambahkan gambar dalam file PDF, operator yang berbeda diperlukan. Contoh ini menggunakan [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), dan [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- Operator [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) menyimpan status grafis PDF saat ini.
- Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF. Contoh yang dipilih menambahkan gambar ke dalam file PDF untuk menggambarkan konsep tersebut. Untuk menambahkan gambar ke dalam file PDF, operator yang berbeda diperlukan. Contoh ini menggunakan [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), dan [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).
Operator (concatenate matrix) digunakan untuk mendefinisikan bagaimana gambar harus ditempatkan pada halaman PDF.
- Operator [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) menggambar gambar pada halaman.
- Operator [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) memulihkan kondisi grafis.

Untuk menambahkan gambar ke dalam file PDF:

1. Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan buka dokumen PDF masukan.
1. Dapatkan halaman tertentu yang akan ditambahkan gambar.
1. Tambahkan gambar ke dalam koleksi Sumber Daya halaman.
1. Gunakan operator untuk menempatkan gambar pada halaman:
   - Pertama, gunakan operator [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) untuk menyimpan status grafis saat ini.
   - Kemudian gunakan operator [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) untuk menentukan di mana gambar akan ditempatkan.
   - Gunakan operator [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) untuk menggambar gambar pada halaman.
1. Akhirnya, gunakan operator [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) untuk menyimpan status grafis yang diperbarui.

Cuplikan kode berikut menunjukkan cara menggunakan operator PDF.

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // Buat dokumen PDF baru
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // Dapatkan halaman tempat gambar perlu ditambahkan
        Page page = pdfDocument.getPages().get_Item(1);

        // Tetapkan koordinat
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Muat gambar ke dalam stream
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        // Tambahkan gambar ke koleksi Gambar dari Sumber Daya Halaman
        page.getResources().getImages().add(imageStream);

        // Menggunakan operator GSave: operator ini menyimpan status grafik saat ini
        page.getContents().add(new GSave());
        // Buat objek Rectangle dan Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Menggunakan operator ConcatenateMatrix (menggabungkan matriks): menentukan
        // bagaimana gambar harus ditempatkan
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Menggunakan operator Do: operator ini menggambar gambar
        page.getContents().add(new Do(ximage.getName()));
        // Menggunakan operator GRestore: operator ini mengembalikan status grafik
        page.getContents().add(new GRestore());

        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## Menggambar XForm pada Halaman menggunakan Operator

Topik ini menunjukkan cara menggunakan operator GSave/GRestore, operator ConcatenateMatrix untuk memposisikan xForm, dan operator Do untuk menggambar xForm pada halaman.

Kode di bawah ini membungkus konten yang ada dari file PDF dengan pasangan operator GSave/GRestore. Pendekatan ini membantu mendapatkan keadaan grafis awal di akhir konten yang ada. Tanpa pendekatan ini, transformasi yang tidak diinginkan mungkin tetap ada di akhir rantai operator yang ada.

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // Contoh ini menunjukkan
        // penggunaan operator GSave/GRestore
        // penggunaan operator ConcatenateMatrix untuk memposisikan xForm
        // penggunaan operator Do untuk menggambar xForm pada halaman

        // Bungkus konten yang ada dengan pasangan operator GSave/GRestore
        // ini untuk mendapatkan keadaan grafis awal di akhir konten yang ada
        // jika tidak, mungkin ada beberapa transformasi yang tidak diinginkan di akhir
        // rantai operator yang ada
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // Tambahkan operator simpan keadaan grafis untuk membersihkan keadaan grafis dengan benar setelah
        // perintah baru
        pageContents.add(new GSave());

        // Buat xForm
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // Tentukan lebar dan tinggi gambar
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Muat gambar ke dalam stream
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        // Tambahkan gambar ke koleksi Images dari Sumber Daya XForm
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // Menggunakan operator Do: operator ini menggambar gambar
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // Tempatkan form pada koordinat x=100 y=500
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // Gambar form dengan operator Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // Tempatkan form pada koordinat x=100 y=300
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // Gambar form dengan operator Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // Kembalikan keadaan grafis dengan GRestore setelah GSave
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## Hapus Objek Grafis menggunakan Kelas Operator

Kelas operator menyediakan fitur hebat untuk manipulasi PDF. Ketika sebuah file PDF berisi grafis yang tidak dapat dihapus menggunakan metode [DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), kelas operator dapat digunakan untuk menghapusnya.

Cuplikan kode berikut menunjukkan cara menghapus grafis. Harap dicatat bahwa jika file PDF berisi label teks untuk grafis, mereka mungkin tetap ada di file PDF, menggunakan pendekatan ini. Oleh karena itu, cari operator grafis untuk metode alternatif untuk menghapus gambar tersebut.

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // Operator pengecatan jalur yang digunakan
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## Mengubah Ruang Warna Dokumen PDF

{{% alert color="primary" %}}

Aspose.PDF untuk Java 9.0.0 mendukung perubahan ruang warna dokumen PDF. Dimungkinkan untuk mengubah warna RGB ke CMYK dan sebaliknya.

{{% /alert %}}

Metode berikut telah diimplementasikan dalam kelas [Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator) untuk memungkinkan Anda mengubah ruang warna. Gunakan untuk mengubah beberapa warna RGB/CMYK tertentu ke ruang warna CMYK/RGB, dengan tetap menjaga dokumen PDF lainnya seperti apa adanya.

{{% alert color="primary" %}}
**Perubahan API Publik**
Metode berikut diimplementasikan:

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara mengubah ruang warna menggunakan Aspose.PDF untuk Java.

```java
Document doc = new Document("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("Nilai operator warna RGB dalam dokumen pdf");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // Mengonversi warna RGB ke CMYK
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("Perintah tidak didukung");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// Menguji hasilnya
System.out.println("Nilai operator warna CMYK yang telah dikonversi dalam dokumen pdf hasil");
doc = new Document("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```