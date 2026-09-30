---
title: "Anotasi dan teks khusus menggunakan Java"
linktitle: "Anotasi dan teks khusus"
type: docs
weight: 40
url: /id/java/annotation-and-special-text/
description: Pelajari cara mengekstrak teks dari anotasi cap, teks yang disorot, dan konten superskrip atau subskrip dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Mengekstrak teks yang disorot

Iterasi melalui anotasi halaman dan baca teks yang ditandai dari `HighlightAnnotation`.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui objek [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) pada [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Periksa apakah setiap anotasi adalah [`HighlightAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) sebelum meng-cast-nya ke kelas anotasi yang bertipe.
1. Baca teks yang ditandai dari setiap anotasi sorotan dan cetak ke konsol.

```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## Mengekstrak teks dari anotasi stempel

Baca aliran tampilan normal dari anotasi stamp dan teruskan `TextAbsorber`.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui objek [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) pada [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Filter anotasi ke yang tipe‑nya adalah `Stamp`.
1. Buat sebuah [`TextAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) dan minta entri tampilan normal dari kamus tampilan anotasi stempel.
1. Kunjungi tampilan [`XForm`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) dan cetak teks yang diekstrak.

```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## Mengekstrak detail teks superskrip dan subskrip

Gunakan `TextFragmentAbsorber` ketika Anda membutuhkan teks yang diekstrak serta tanda superskrip atau subskrip pada setiap fragmen.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) untuk analisis teks tingkat fragmen.
1. Kunjungi [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target dan kumpulkan itu objek [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Iterasikan melalui fragmen-fragmen tersebut dan baca teks bersama dengan flag superskrip dan subskrip dari `fragment.getTextState()`.
1. Tuliskan detail yang diekstrak ke file output.

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
