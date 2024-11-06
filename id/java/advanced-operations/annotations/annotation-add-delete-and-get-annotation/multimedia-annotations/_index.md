---
title: PDF Multimedia Annotation 
linktitle: Multimedia Annotation
type: docs
weight: 40
url: id/java/multimedia-annotation/
description: Aspose.PDF untuk Java memungkinkan Anda untuk menambahkan, mendapatkan, dan menghapus anotasi multimedia dari dokumen PDF Anda.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anotasi dalam dokumen PDF terkandung dalam koleksi Anotasi objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page). Koleksi ini hanya berisi semua anotasi untuk halaman individu tersebut: setiap halaman memiliki koleksi Anotasinya sendiri. Untuk menambahkan anotasi ke halaman tertentu, tambahkan ke koleksi Anotasi halaman tersebut menggunakan metode Add.

Gunakan kelas [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation) di namespace Aspose.PDF.InteractiveFeatures.Annotations untuk menyertakan file SWF sebagai anotasi dalam dokumen PDF sebagai gantinya.
 Sebuah anotasi layar menentukan sebuah wilayah dari halaman di mana klip media dapat diputar.

Ketika Anda perlu menambahkan tautan video eksternal dalam dokumen PDF, Anda dapat menggunakan [MovieAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation). Sebuah Anotasi Film berisi grafik animasi dan suara untuk ditampilkan di layar komputer dan melalui speaker.

Sebuah [Sound Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation) harus analog dengan anotasi teks kecuali bahwa alih-alih catatan teks, ia berisi suara yang direkam dari mikrofon komputer atau diimpor dari file. Ketika anotasi diaktifkan, suara akan diputar. Anotasi harus berperilaku seperti anotasi teks dalam banyak hal, dengan ikon yang berbeda (secara default, sebuah pengeras suara) untuk menunjukkan bahwa itu mewakili suara.

Namun, ketika ada persyaratan untuk menyematkan media di dalam dokumen PDF, Anda perlu menggunakan [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation).
The following methods/properties of RichMediaAnnotation class can be used.

- Stream CustomPlayer { set; }: Memungkinkan pengaturan pemutar yang digunakan untuk memutar video.
- string CustomFlashVariables { set; }: Memungkinkan untuk mengatur variabel yang diteruskan ke aplikasi flash. Baris ini adalah kumpulan pasangan “key=value” yang dipisahkan dengan ‘&'.
- void AddCustomData(strig name, Stream data): Menambahkan data tambahan untuk pemutar. Misalnya source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: Acara mengaktifkan pemutar; nilai yang mungkin adalah Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Mengatur data video/audio untuk diputar.
- void Update(): Membuat struktur data dari anotasi. Metode ini harus dipanggil terakhir
- void SetPoster(Stream): Mengatur poster video yaitu gambar yang ditampilkan saat pemutar tidak aktif

## Tambahkan Anotasi Layar

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Layar ke file PDF:

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // Membuat Anotasi Layar
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
}
```


## Tambahkan Anotasi Suara

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Suara ke file PDF:

```java
          public static void AddSoundAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // Membuat Anotasi Suara
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Demo Anotasi Suara");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```

## Tambahkan RichMediaAnnotation

Cuplikan kode berikut menunjukkan cara menambahkan RichMediaAnnotation ke file PDF:

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // beri nama pada data video. Data ini akan disematkan ke dalam dokumen dengan nama ini
        // dan direferensikan dari variabel flash dengan nama ini.
        // videoName seharusnya tidak mengandung path ke file; ini lebih kepada "kunci" untuk mengakses
        // data di dalam dokumen PDF

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // kita juga menggunakan skin untuk pemutar video
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // di sini kita harus menentukan stream yang berisi kode dari pemutar video
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // menggabungkan baris variabel flash untuk pemutar. harap dicatat bahwa pemutar yang berbeda
        // mungkin memiliki format baris variabel flash yang berbeda.
        // Lihat dokumentasi untuk pemutar Anda.
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // tambahkan kode skin.
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // atur poster untuk video
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // atur konten video
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // atur jenis konten (video)
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // aktifkan pemutar dengan klik
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // perbarui data anotasi. Metode ini harus dipanggil setelah semua
        // penugasan/pengaturan. Metode ini menginisialisasi struktur data anotasi
        // dan menyematkan data yang diperlukan.
        rma.update();

        // tambahkan anotasi pada halaman.
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```


## Dapatkan MultimediaAnnotation

Silakan coba gunakan potongan kode berikut untuk mendapatkan MultimediaAnnotation dari dokumen PDF.

```java
public static void GetMultimediaAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();

        for (Annotation ma : mediaAnnotations) {
            System.out.println(ma.getAnnotationType() + " " + ma.getRect());
        }
    }
```

## Hapus MultimediaAnnotation

Potongan kode berikut menunjukkan cara menghapus MultimediaAnnotation dari file PDF.

```java
    public static void DeletePolyAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();
        for (Annotation ma : mediaAnnotations) {
            page.getAnnotations().delete(ma);
        }
        document.save(_dataDir + "RichMediaAnnotation_del.pdf");
    }
```


## Tambahkan Anotasi Widget

Formulir interaktif menggunakan [Widget Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation) untuk mewakili tampilan bidang dan mengelola interaksi pengguna. Kami menggunakan elemen formulir ini yang ditambahkan ke PDF untuk memudahkan memasukkan, mengirim informasi, atau melakukan beberapa interaksi pengguna lainnya.

Anotasi Widget adalah representasi grafis dari bidang formulir pada halaman tertentu, jadi kami tidak dapat membuatnya langsung sebagai anotasi.

Setiap Anotasi Widget akan memiliki grafik yang sesuai (tampilan) tergantung pada jenisnya. Setelah pembuatan, aspek visual tertentu dapat diubah, seperti gaya batas dan warna latar belakang. Properti lain seperti warna teks dan font dapat diubah melalui bidangnya, setelah terpasang pada satu.

Dalam beberapa kasus, Anda mungkin ingin suatu bidang muncul di lebih dari satu halaman, mengulangi nilai yang sama.
 Dalam hal ini, bidang yang biasanya memiliki satu widget mungkin memiliki beberapa widget terpasang: TextField, ListBox, ComboBox, dan CheckBox biasanya memiliki tepat satu, sedangkan RadioGroup memiliki beberapa widget, satu untuk setiap tombol radio. Seseorang yang mengisi formulir dapat menggunakan salah satu widget tersebut untuk memperbarui nilai bidang, dan ini tercermin dalam semua widget lainnya juga.

Setiap bidang formulir untuk setiap tempat dalam dokumen mewakili satu Anotasi Widget. Data spesifik lokasi dari Anotasi Widget ditambahkan ke halaman tertentu. Setiap bidang formulir memiliki beberapa variasi. Sebuah tombol dapat berupa tombol radio, kotak centang, atau tombol tekan. Sebuah widget pilihan dapat berupa kotak daftar atau kotak kombo.

Dalam contoh ini, kita akan belajar bagaimana menambahkan tombol tekan untuk navigasi dalam dokumen.

## Tambahkan Tombol ke Dokumen

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Cetak dokumen saat ini");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setNormalCaption("Cetak Dokumen");

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);

        printButton.setBorder(border);
        printButton.getCharacteristics().setBorder(Color.fromArgb(255, 0, 0, 255));
        printButton.getCharacteristics().setBackground(Color.fromArgb(255, 0, 191, 255));
        document.getForm().add(printButton);

        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

Tombol ini memiliki batas dan mengatur latar belakang. Kami juga menetapkan nama tombol (Name), tooltip (AlternateName), label (NormalCaption), dan warna teks label (Color).

## Menggunakan Tindakan Navigasi Dokumen

Ada contoh yang lebih kompleks dari penggunaan Widget Annotations - navigasi dokumen dalam dokumen PDF. Ini mungkin diperlukan untuk mempersiapkan presentasi dokumen PDF.

Contoh ini menunjukkan cara membuat 4 tombol:

```java
public static void AddDocumentNavigationActions() {
// Memuat file PDF
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "Ke halaman pertama", "Ke halaman sebelumnya", "Ke halaman berikutnya", "Ke halaman terakhir" };
String[] normalCaptions = { "Pertama", "Sebelumnya", "Berikutnya", "Terakhir" };
int[] actions = { PredefinedAction.FirstPage, PredefinedAction.PrevPage, PredefinedAction.NextPage,
PredefinedAction.LastPage };
Color clrBorder = Color.fromArgb(255, 0, 255, 0);
Color clrBackGround = Color.fromArgb(255, 0, 96, 70);

for (int i = 0; i < 4; i++) {
buttons[i] = new ButtonField(document, new Rectangle(32 + i * 80, 28, 104 + i * 80, 68));
buttons[i].setAlternateName(alternateNames[i]);
buttons[i].setColor(Color.getWhite());
buttons[i].setNormalCaption(normalCaptions[i]);
buttons[i].setOnActivated(new NamedAction(actions[i]));
Border border = new Border(buttons[i]);
border.setStyle(BorderStyle.Solid);
border.setWidth(2);
buttons[i].setBorder(border);
buttons[i].getCharacteristics().setBorder(clrBorder);
buttons[i].getCharacteristics().setBackground(clrBackGround);
}

for (int pageIndex = 1; pageIndex <= 1; pageIndex++)
for (int i = 0; i < 4; i++)
document.getForm().add(buttons[i], "btn" + pageIndex + "_" + (i + 1), pageIndex);

document.getForm().get("btn1_1").setReadOnly(true);
document.getForm().get("btn1_2").setReadOnly(true);

document.getForm().get("btn" + document.getPages().size() + "_3").setReadOnly(true);
document.getForm().get("btn" + document.getPages().size() + "_4").setReadOnly(true);
document.save(_dataDir + "sample_widgetannot_2.pdf");
}
```


## Cara menghapus Anotasi Widget

Aspose.PDF untuk Java memiliki aturan untuk menghapus anotasi dari file Anda:

```java
public static void DeleteWidgetAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Memfilter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // menghapus anotasi
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
```

Dalam dokumen PDF, Anda dapat melihat dan mengelola konten 3D berkualitas tinggi yang dibuat dengan perangkat lunak CAD 3D atau pemodelan 3D dan disematkan dalam dokumen PDF.
 Dapat memutar elemen 3D ke semua arah seolah-olah Anda memegangnya di tangan Anda.

Mengapa Anda memerlukan tampilan 3D gambar sama sekali?

Selama beberapa tahun terakhir, teknologi telah membuat terobosan besar di semua bidang berkat pencetakan 3D. Teknologi pencetakan 3D dapat diterapkan untuk mengajarkan keterampilan teknologi dalam konstruksi, teknik mesin, desain sebagai alat utama. Teknologi ini berkat munculnya perangkat pencetakan pribadi dapat berkontribusi pada pengenalan bentuk-bentuk baru organisasi proses pendidikan, meningkatkan motivasi, dan pembentukan kompetensi yang diperlukan bagi lulusan
dan guru.

Tugas utama pemodelan 3D adalah ide tentang objek masa depan atau objek karena, untuk merilis sebuah objek, Anda memerlukan pemahaman tentang fitur desainnya secara detail untuk regenerasi berturut-turut dalam desain industri atau arsitektur.

## Tambahkan Anotasi 3D

Anotasi 3D ditambahkan menggunakan model yang dibuat dalam format U3D dengan Aspose.PDF untuk Java
1. Buat [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) baru
1. Muat data model 3D yang diinginkan (dalam kasus kami "Ring.u3d") untuk membuat [Konten PDF3D](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)
1. Buat objek [Karya Seni 3d](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork) dan tautkan ke dokumen dan Konten3D
1. Sesuaikan objek pdf3dArtWork:

    - SkemaPencahayaan3D - (kami akan mengatur `CAD` dalam contoh)
    - ModeRender3D - (kami akan mengatur `Solid` dalam contoh)
    - Isi `ViewArray`, buat setidaknya satu [Tampilan 3D](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView) dan tambahkan ke array.

1. Tetapkan 3 parameter dasar dalam anotasi:
    - `halaman` di mana anotasi akan ditempatkan,
    - `persegi panjang`, di dalam mana anotasi,
    - dan objek `3dArtWork`.
1. Untuk presentasi objek 3D yang lebih baik, atur bingkai Perbatasan
1. Atur tampilan default (misalnya - ATAS)

1. Tambahkan beberapa parameter tambahan: nama, poster pratinjau dll.
1. Tambahkan Anotasi ke [Halaman](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)
1. Simpan hasilnya

## Contoh

Silakan periksa potongan kode berikut untuk menambahkan Anotasi 3D.

```java
    public class Example3DAnnotation
    {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
    // Muat file PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
    pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
    pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.getPages().add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
    pdf3dAnnotation.setDefaultViewIndex(1);
    pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
    pdf3dAnnotation.setName("Ring.u3d");
    //atur gambar pratinjau jika diperlukan
    //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
    document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

    document.save(_dataDir+"sample_3d.pdf");
    }
}
```


This code example showed us such a model:

![Demo anotasi 3D](3d_demo.png)