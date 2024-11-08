---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 9.3.1
type: docs
weight: 60
url: /ar/java/public-api-changes-in-aspose-pdf-for-java-9-3-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة التغييرات في واجهة برمجة التطبيقات العامة المقدمة في **Aspose.PDF for Java 9.3.1.** وهي تشمل ليس فقط الأساليب العامة الجديدة والمهمَلة، ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.PDF for Java والتي قد تؤثر على الكود الموجود. أي سلوك تم تقديمه يمكن اعتباره تراجعًا ويعدل السلوك الموجود فهو مهم بشكل خاص وموثق هنا.

{{% /alert %}}

## تم جعل الأساليب التالية داخلية:

com.aspose.pdf.DocumentInfo.setCreator(String)<p>
com.aspose.pdf.DocumentInfo.setProducer(String)<p>
com.aspose.pdf.FileParams.getEngineDict()

## تم جعل الثوابت المهمة التالية داخلية، يجب استخدام الدوال الثابتة بدلاً منها:

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

## الحقل التالي تمت إضافته:

public static Rectangle com.aspose.pdf.Rectangle.getEmpty() - يعيد مستطيل فارغ