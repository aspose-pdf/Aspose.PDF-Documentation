---
title: استخراج معلومات الصورة والتوقيع
linktitle: استخراج معلومات الصورة والتوقيع
type: docs
weight: 30
url: /ar/java/extract-image-and-signature-information/
description: يمكنك استخراج الصور من حقل التوقيع واستخراج معلومات التوقيع باستخدام فئة SignatureField مع Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الصورة من حقل التوقيع

يدعم Aspose.PDF for Java ميزة التوقيع الرقمي لملفات PDF باستخدام فئة [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) وأثناء توقيع المستند، يمكنك أيضًا تعيين صورة لظهور التوقيع. الآن، توفر هذه الـ API أيضًا القدرة على استخراج معلومات التوقيع وكذلك الصورة المرتبطة بحقل التوقيع.

من أجل استخراج معلومات التوقيع، قمنا بإدخال طريقة [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) في فئة [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 الرجاء إلقاء نظرة على مقتطف الشيفرة التالي الذي يوضح الخطوات لاستخراج صورة من كائن SignatureField:

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### استبدال صورة التوقيع

في بعض الأحيان قد يكون لديك متطلب لاستبدال صورة حقل توقيع موجود بالفعل داخل ملف PDF. لتحقيق هذا المتطلب، أولاً نحتاج إلى البحث عن حقول النموذج داخل ملف PDF، وتحديد حقول التوقيع، والحصول على الأبعاد (الأبعاد المستطيلة) لحقل التوقيع ثم ختم صورة فوق الأبعاد نفسها.

## استخراج معلومات التوقيع

يدعم Aspose.PDF for Java ميزة التوقيع الرقمي لملفات PDF باستخدام فئة [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField). حاليًا، يمكننا أيضًا تحديد صلاحية الشهادة ولكن لا يمكننا استخراج الشهادة بأكملها. المعلومات التي يمكن استخراجها هي المفتاح العام، بصمة الإبهام، المُصدر، إلخ.

لاستخراج معلومات التوقيع، قدمنا طريقة [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) إلى فئة [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 يرجى إلقاء نظرة على مقتطف الكود التالي الذي يوضح الخطوات لاستخراج الشهادة من كائن SignatureField:

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```