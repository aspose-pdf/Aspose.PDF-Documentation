---
title: استخراج الصور من ملف PDF والتعرف على الباركود
type: docs
weight: 20
url: /ar/net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

عادةً ما تحتوي مستندات PDF على نصوص، صور، جداول، مرفقات، رسوم بيانية، تعليقات وأجسام أخرى ذات صلة. هناك حالات يتم فيها تضمين الباركود داخل ملف PDF وبعض العملاء لديهم الحاجة لتحديد الباركود الموجود داخل ملف PDF. يشرح المقال التالي الخطوات حول كيفية استخراج الصور من صفحات PDF وتحديد الباركود داخلها.

{{% /alert %}}

وفقًا لنموذج كائن المستند لـ Aspose.PDF لـ .NET، يحتوي ملف PDF على صفحة أو أكثر حيث تحتوي كل صفحة على مجموعة من الصور والنماذج والخطوط في كائن الموارد.
وفقًا لنموذج كائن المستند في Aspose.PDF لـ .NET، يحتوي ملف PDF على صفحة واحدة أو أكثر حيث تحتوي كل صفحة على مجموعة من الصور والنماذج والخطوط في كائن الموارد.

**C#**

```csharp

//فتح المستند
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// التنقل عبر الصفحات الفردية لملف PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // التنقل عبر كل صورة مستخرجة من صفحات PDF
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            //حفظ الصورة الناتجة
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // تعيين موضع البث إلى بداية البث
            imageStream.Position = 0;
   
            // إنشاء كائن BarCodeReader
   
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // الحصول على نص BarCode من صورة BarCode
                string code = barcodeReader.GetCodeText();
   
                // كتابة نص BarCode إلى خرج الوحدة الطرفية
                Console.WriteLine("BARCODE : " + code);
            }
   
            // إغلاق كائن BarCodeReader لإطلاق ملف الصورة
   
            barcodeReader.Close();
        }
    }
}

```
لمزيد من التفاصيل حول المواضيع المغطاة في هذه المقالة، يرجى زيارة الروابط التالية

- [استخراج الصور من ملف PDF](/net/extract-images-from-the-pdf-file/)
- [قراءة الباركود](https://docs.aspose.com/barcode/net/read-barcodes/)
