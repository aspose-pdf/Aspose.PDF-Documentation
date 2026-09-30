---
title: "Mendapatkan dan mencari gambar dalam PDF"
linktitle: "Mendapatkan dan mencari gambar"
type: docs
weight: 40
url: /id/java/search-and-get-images-from-pdf-document/
description: Pelajari cara mencari dan memeriksa gambar dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mencari dan memeriksa gambar dalam file PDF dengan Java"
Abstract: Artikel ini menunjukkan cara mencari dan memeriksa gambar dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembacaan geometri penempatan gambar, mendeteksi tipe warna, mengekstrak teks alternatif, dan menghitung resolusi gambar yang efektif dari operator halaman.
---
Aspose.PDF for Java dapat memeriksa informasi penempatan gambar serta data gambar tingkat rendah.

## Mendapatkan parameter penempatan gambar

Gunakan contoh ini ketika Anda perlu memeriksa geometri gambar dan resolusi efektif pada sebuah halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Gunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) untuk mengumpulkan penempatan gambar.
1. Keluarkan ukuran, koordinat, dan resolusi untuk setiap gambar yang ditempatkan.

```java
public static void extractImageParams(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("image width: " + imagePlacement.getRectangle().getWidth());
            System.out.println("image height: " + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX: " + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY: " + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution: " + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution: " + imagePlacement.getResolution().getY());
        }
    }
}
```

## Mendeteksi tipe warna gambar

Gunakan contoh ini ketika Anda perlu menghitung gambar skala abu-abu dan RGB dalam halaman PDF.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Gunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) untuk mengiterasi gambar halaman.
1. Baca [`ColorType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) dari setiap gambar dan keluarkan totalnya.

```java
public static void extractImageTypesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        int grayscaled = 0;
        int rgb = 0;

        document.getPages().get_Item(1).accept(absorber);

        System.out.println("--------------------------------");
        System.out.println("Total Images = " + absorber.getImagePlacements().size());

        int imageCounter = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            ColorType colorType = imagePlacement.getImage().getColorType();
            if (colorType == ColorType.Grayscale) {
                grayscaled++;
                System.out.println("Image " + imageCounter + " is Grayscale...");
            } else if (colorType == ColorType.Rgb) {
                rgb++;
                System.out.println("Image " + imageCounter + " is RGB...");
            }
            imageCounter++;
        }

        System.out.println("--------------------------------");
        System.out.println("Grayscale Images = " + grayscaled);
        System.out.println("RGB Images = " + rgb);
    }
}
```

## Mengekstrak teks alternatif gambar

Gunakan contoh ini ketika Anda perlu memeriksa teks aksesibilitas yang terkait dengan gambar halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Gunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) untuk mengumpulkan penempatan gambar.
1. Baca teks alternatif untuk setiap gambar dan keluarkan hasilnya.

```java
public static void extractImageAltText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("Name in collection: " + imagePlacement.getImage().getNameInCollection());
            List<String> lines = imagePlacement.getImage().getAlternativeText(document.getPages().get_Item(1));
            if (!lines.isEmpty()) {
                System.out.println("Alt Text: " + lines.get(0));
            } else {
                System.out.println("Alt Text: ");
            }
        }
    }
}
```

## Menghitung informasi gambar dari operator halaman

Gunakan contoh ini ketika Anda perlu mendapatkan ukuran gambar efektif dan resolusi dari operator konten halaman tingkat rendah.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan kumpulkan nama sumber gambar.
1. Lacak keadaan grafik saat mengiterasi operator halaman.
1. Selesaikan setiap operasi gambar dan hitung dimensi serta resolusi efektifnya.

```java
public static void extractImageInformationFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int defaultResolution = 72;
        List<Matrix> graphicsState = new ArrayList<>();
        List<String> imageNames = Arrays.asList(document.getPages().get_Item(1).getResources().getImages().getNames());

        graphicsState.add(new Matrix(1, 0, 0, 1, 0, 0));

        for (Operator operator : document.getPages().get_Item(1).getContents()) {
            if (operator instanceof GSave) {
                graphicsState.add(new Matrix(graphicsState.get(graphicsState.size() - 1)));
            } else if (operator instanceof GRestore) {
                graphicsState.remove(graphicsState.size() - 1);
            } else if (operator instanceof ConcatenateMatrix concatenateMatrix) {
                Matrix current = graphicsState.get(graphicsState.size() - 1);
                graphicsState.set(graphicsState.size() - 1, current.multiply(concatenateMatrix.getMatrix()));
            } else if (operator instanceof Do doOperator) {
                if (imageNames.contains(doOperator.getName())) {
                    Matrix lastCtm = graphicsState.get(graphicsState.size() - 1);
                    int index = imageNames.indexOf(doOperator.getName()) + 1;
                    XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(index);

                    double scaledWidth = Math.sqrt(Math.pow(lastCtm.getA(), 2) + Math.pow(lastCtm.getB(), 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCtm.getC(), 2) + Math.pow(lastCtm.getD(), 2));

                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    String info = String.format(
                            "%s image %s (%.2f:%.2f): res %.2f x %.2f",
                            inputFile,
                            doOperator.getName(),
                            scaledWidth,
                            scaledHeight,
                            resHorizontal,
                            resVertical);
                    System.out.println(info);
                }
            }
        }
    }
}
```
