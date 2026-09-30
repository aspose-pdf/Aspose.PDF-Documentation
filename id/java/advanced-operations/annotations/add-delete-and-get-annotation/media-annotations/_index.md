---
title: "Anotasi media dalam PDF"
linktitle: "Anotasi media"
type: docs
weight: 40
url: /id/java/media-annotations/
description: Pelajari cara bekerja dengan API anotasi PDF suara, layar, media kaya, dan 3D dalam Java, dengan panduan langkah demi langkah untuk alur kerja multimedia umum.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Alur kerja anotasi PDF terkait media dalam Java"
Abstract: Halaman ini menjelaskan alur kerja anotasi media umum di Aspose.PDF for Java, termasuk skenario suara, layar, media kaya, 3D, penghapusan, dan inspeksi. Repositori saat ini tidak menyertakan kelas contoh media `workingwithannotations` yang berdedikasi, sehingga artikel ini langsung mendokumentasikan pola API Java dengan panduan langkah demi langkah.
---
Anotasi media dalam PDF biasanya mencakup konten multimedia yang tersemat atau terhubung seperti klip suara, wilayah pemutaran layar, kontainer media kaya, dan model 3D.

## Menambahkan anotasi media kaya

Gunakan contoh ini ketika halaman PDF harus menampung konten video tersemat dengan pemutar khusus, gambar poster, dan kulit.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan sebuah halaman.
1. Buat sebuah [`RichMediaAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/richmediaannotation/), konfigurasikan aset pemutar, poster, dan aliran konten.
1. Tambahkan anotasi ke halaman dan simpan dokumen output.

```java
public static void richMediaAnnotationsAdd(Path mediaDir, Path outputFile) throws Exception {
    String pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";

    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation richMediaAnnotation = new RichMediaAnnotation(
                page,
                new Rectangle(100, 500, 300, 600, true));

        String playerPath = pathToAdobeApp + "\\Players\\Videoplayer.swf";
        richMediaAnnotation.setCustomPlayer(new FileInputStream(playerPath));
        richMediaAnnotation.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        String skinPath = pathToAdobeApp + "\\" + skinName;
        richMediaAnnotation.addCustomData(skinName, new FileInputStream(skinPath));

        Path posterPath = mediaDir.resolve(posterName);
        richMediaAnnotation.setPoster(new FileInputStream(posterPath.toString()));

        Path videoPath = mediaDir.resolve(videoName);
        try (FileInputStream videoStream = new FileInputStream(videoPath.toString())) {
            richMediaAnnotation.setContent(videoName, videoStream);
        }

        richMediaAnnotation.setType(RichMediaAnnotation.ContentType.Video);
        richMediaAnnotation.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);
        richMediaAnnotation.update();

        page.getAnnotations().add(richMediaAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Menghapus anotasi media kaya

Contoh ini menghapus anotasi media kaya yang ada pada halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi jenis [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`RichMedia`.
1. Hapus anotasi yang dikumpulkan dan simpan dokumen yang diperbarui.

```java
public static void richMediaAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.RichMedia) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            page.getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Mendapatkan anotasi multimedia

Gunakan contoh ini untuk memeriksa anotasi layar, suara, dan media kaya yang sudah ada pada halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tentukan set tipe anotasi multimedia yang ingin Anda deteksi.
1. Iterasikan anotasi halaman dan cetak tipe serta persegi panjang untuk setiap kecocokan.

```java
public static void multimediaAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Set<AnnotationType> targetTypes = Set.of(
                AnnotationType.Screen,
                AnnotationType.Sound,
                AnnotationType.RichMedia);

        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (targetTypes.contains(annotation.getAnnotationType())) {
                System.out.println(annotation.getAnnotationType() + " [" + annotation.getRect() + "]");
            }
        }
    }
}
```

## Menambahkan anotasi 3D

Contoh ini menambahkan tampilan model 3D interaktif dengan perspektif yang telah ditentukan dan opsi rendering.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Muat model ke dalam [`PDF3DContent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dcontent/) dan konfigurasikan sebuah [`PDF3DArtwork`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dartwork/).
1. Buat [`PDF3DAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdf3dannotation/), tambahkan ke halaman, dan simpan dokumen.

```java
public static void annotation3dAdd(Path modelFile, Path outputFile) {
    try (Document document = new Document()) {
        PDF3DContent pdf3dContent = new PDF3DContent(modelFile.toString());
        PDF3DArtwork pdf3dArtwork = new PDF3DArtwork(document, pdf3dContent);
        pdf3dArtwork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtwork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        Matrix3D topMatrix = new Matrix3D(
                1, 0, 0,
                0, -1, 0,
                0, 0, -1,
                0.10271, 0.08184, 0.273836);

        Matrix3D frontMatrix = new Matrix3D(
                0, -1, 0,
                0, 0, 1,
                -1, 0, 0,
                0.332652, 0.08184, 0.085273);

        pdf3dArtwork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top"));
        pdf3dArtwork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left"));

        Page page = document.getPages().add();

        PDF3DAnnotation pdf3dAnnotation = new PDF3DAnnotation(
                page,
                new Rectangle(100, 500, 300, 700, true),
                pdf3dArtwork);

        pdf3dAnnotation.setBorder(new com.aspose.pdf.Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName(modelFile.getFileName().toString());

        page.getAnnotations().add(pdf3dAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan anotasi layar

Gunakan contoh ini ketika sebuah halaman harus merujuk ke file media melalui wilayah pemutaran layar.

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan sebuah halaman.
1. Buat sebuah [`ScreenAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/screenannotation/) untuk file media dan persegi panjang target.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void screenAnnotationWithMediaAdd(Path mediaFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ScreenAnnotation screenAnnotation = new ScreenAnnotation(
                page,
                new Rectangle(170, 190, 470, 380, true),
                mediaFile.toString());

        page.getAnnotations().add(screenAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan anotasi suara

Contoh ini menempatkan anotasi suara pada halaman dan mengaitkannya dengan file WAV.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`SoundAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation/) untuk file audio target dan konfigurasikan metadata-nya.
1. Tambahkan anotasi ke halaman dan simpan dokumen output.

```java
public static void soundAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Path mediaFile = inputFile.getParent().resolve("file_example_WAV_1MG.wav");

        SoundAnnotation soundAnnotation = new SoundAnnotation(
                page,
                new Rectangle(20, 700, 60, 740, true),
                mediaFile.toString());

        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Sound Annotation demo");

        soundAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(20, 700, 60, 740, true)));

        page.getAnnotations().add(soundAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Topik anotasi terkait

- [Anotasi interaktif](/pdf/id/java/interactive-annotations/)
- [Anotasi markup](/pdf/id/java/markup-annotations/)
- [Anotasi keamanan](/pdf/id/java/security-annotations/)
- [Anotasi bentuk](/pdf/id/java/shape-annotations/)
- [Anotasi teks](/pdf/id/java/text-based-annotations/)
- [Watermark anotasi](/pdf/id/java/watermark-annotations/)
- [Mengimpor dan mengekspor anotasi](/pdf/id/java/import-export-annotations/)
