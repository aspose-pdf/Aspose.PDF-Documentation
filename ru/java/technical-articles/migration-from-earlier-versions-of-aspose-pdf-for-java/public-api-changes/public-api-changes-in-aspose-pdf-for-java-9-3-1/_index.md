---
title: Изменения в публичном API Aspose.PDF для Java 9.3.1
type: docs
weight: 60
url: ru/java/public-api-changes-in-aspose-pdf-for-java-9-3-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

На этой странице перечислены изменения в публичном API, введенные в **Aspose.PDF для Java 9.3.1.** Здесь указаны не только новые и устаревшие публичные методы, но также описание любых изменений в поведении Aspose.PDF для Java, которые могут повлиять на существующий код. Любое поведение, которое может быть воспринято как регрессия и изменяет существующее поведение, особенно важно и документировано здесь.

{{% /alert %}}

## Следующие методы были сделаны внутренними:

com.aspose.pdf.DocumentInfo.setCreator(String)<p>
com.aspose.pdf.DocumentInfo.setProducer(String)<p>
com.aspose.pdf.FileParams.getEngineDict()

## Следующие устаревшие константы были сделаны внутренними, необходимо использовать статические геттеры вместо них:

com.aspose.pdf.ImageFormatInternal.Bmp<p>
com.aspose.pdf.ImageFormatInternal.Emf<p>

com.aspose.pdf.ImageFormatInternal.Exif<p>
com.aspose.pdf.ImageFormatInternal.Gif<p>
com.aspose.pdf.ImageFormatInternal.Jpeg<p>
com.aspose.pdf.ImageFormatInternal.Icon<p>
com.aspose.pdf.ImageFormatInternal.MemoryBmp<p>
com.aspose.pdf.ImageFormatInternal.Png<p>
com.aspose.pdf.ImageFormatInternal.Tiff<p>
com.aspose.pdf.ImageFormatInternal.Wmf<p>
com.aspose.pdf.TextEncodingInternal.ASCII<p>
com.aspose.pdf.TextEncodingInternal.BigEndianUnicode<p>
com.aspose.pdf.TextEncodingInternal.Default<p>
com.aspose.pdf.TextEncodingInternal.Unicode<p>
com.aspose.pdf.TextEncodingInternal.UTF32<p>
com.aspose.pdf.TextEncodingInternal.UTF32BE<p>
com.aspose.pdf.TextEncodingInternal.UTF7<p>
com.aspose.pdf.TextEncodingInternal.UTF8<p>
com.aspose.pdf.TextEncodingInternal.UTF8Unmarked

## Следующее поле добавлено:

public static Rectangle com.aspose.pdf.Rectangle.getEmpty() - возвращает пустой прямоугольник