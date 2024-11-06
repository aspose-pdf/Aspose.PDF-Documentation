---
title: تحويل صفحات PDF إلى صور وتعرف الباركود
type: docs
weight: 10
url: ar/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

عادةً ما تتضمن مستندات PDF نصوصًا، صورًا، جداول، مرفقات، رسوم بيانية، تعليقات توضيحية وكائنات أخرى. يحتاج بعض عملائنا إلى تضمين الباركود في المستندات ثم تحديد الباركود في ملف PDF. يشرح المقال التالي كيفية تحويل الصفحات في ملف PDF إلى صور وتحديد الباركود في الصور باستخدام Aspose.Barcode لـ .NET.

{{% /alert %}}
### **تحويل الصفحات إلى صور وتعرف الباركود**

{{% alert color="primary" %}}

Aspose.PDF لـ .NET هو منتج قوي جدًا لإدارة مستندات PDF. يسهل تحويل الصفحات في مستندات PDF إلى صور. Aspose.BarCode لـ .NET هو منتج قوي بالمثل لتوليد وتعرف الباركود.
{{% /alert %}}

تدعم الفئة PdfConverter تحت فضاء الأسماء Aspose.PDF.Facades تحويل صفحات PDF إلى تنسيقات صور متعددة.
#### **استخدام Aspose.PDF.Facades**

{{% alert color="primary" %}}

تحتوي فئة PdfConverter على طريقة تسمى GetNextImage التي تولد صورة من الصفحة الحالية لملف PDF. لتحديد تنسيق الصورة الناتجة، تقبل هذه الطريقة وسيطاً من تعداد System.Drawing.Imaging.ImageFormat.

يحتوي Aspose.Barcode على مساحة اسم تُدعى BarCodeRecognition، والتي تحتوي على فئة BarCodeReader. تتيح لك فئة BarCodeReader قراءة الباركود، تحديدها، وتعريفها من ملفات الصور.

لأغراض هذا المثال، قم أولاً بتحويل صفحة في ملف PDF إلى صورة باستخدام Aspose.PDF.Facades.PdfConverter.
لأغراض هذا المثال، قم أولاً بتحويل صفحة في ملف PDF إلى صورة باستخدام Aspose.PDF.Facades.PdfConverter.

##### **أمثلة برمجية**
**C#**
{{< highlight csharp>}}

```csharp
 //إنشاء كائن PdfConverter

PdfConverter converter = new PdfConverter();

//ربط ملف PDF الإدخال

converter.BindPdf("Source.pdf");

// تحديد صفحة البداية للمعالجة

converter.StartPage = 1;

// تحديد الصفحة النهائية للمعالجة

converter.EndPage = 1;

// إنشاء كائن Resolution لتحديد دقة الصورة الناتجة

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

// تهيئة عملية التحويل

converter.DoConvert();

// إنشاء كائن MemoryStream لاحتواء الصورة الناتجة

MemoryStream imageStream = new MemoryStream();

// التحقق من وجود الصفحات ثم تحويلها إلى صورة واحدة تلو الأخرى

while (converter.HasNextImage())

{

    // حفظ الصورة في تنسيق الصورة المحدد

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    // تعيين موضع الدفق إلى بداية الدفق

// تعيين موضع البث إلى بداية البث
imageStream.Position = 0;

// إنشاء كائن BarCodeReader
Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

// String txtResult.Text = "";

while (barcodeReader.Read())
{
    // الحصول على نص الباركود من صورة الباركود
    string code = barcodeReader.GetCodeText();

    // كتابة نص الباركود إلى إخراج Console
    Console.WriteLine("BARCODE : " + code);
}

// إغلاق كائن BarCodeReader لتحرير ملف الصورة
barcodeReader.Close();

// إغلاق مثيل PdfConverter وتحرير الموارد
converter.Close();

// إغلاق البث الذي يحمل كائن الصورة
imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}
في الأجزاء البرمجية أعلاه، يتم حفظ الصورة الناتجة في كائن MemoryStream.
{{% /alert %}}
```
في الشفرة المذكورة أعلاه، يتم حفظ الصورة الناتجة في كائن MemoryStream.

{{% /alert %}}

{anchor:devices]
#### **استخدام فئة PngDevice**
في Aspose.PDF.Devices، هناك الفئة PngDevice. تسمح لك هذه الفئة بتحويل صفحات في مستندات PDF إلى صور PNG.

لغرض هذا المثال، قم بتحميل ملف PDF المصدر إلى الوثيقة وتحويل صفحات الوثيقة إلى صور PNG. عندما يتم إنشاء الصور، استخدم فئة BarCodeReader تحت Aspose.BarCodeRecognition لتحديد وقراءة الباركودات في الصور.

{{% alert color="primary" %}}

أمثلة الكود المعطاة هنا تتنقل خلال صفحات مستند PDF وتحاول تحديد الباركودات على كل صفحة.

{{% /alert %}}
##### **أمثلة برمجية**
**C#**

{{< highlight csharp >}}

 //فتح مستند PDF

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// التنقل عبر الصفحات الفردية لملف PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())

استخدام (MemoryStream imageStream = new MemoryStream())
{
    // إنشاء كائن Resolution
    Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);

    // توظيف كائن PngDevice مع مرور كائن Resolution كمعامل لمنشئه
    Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);

    // تحويل صفحة معينة وحفظ الصورة إلى التيار
    pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

    // تعيين موضع التيار إلى بداية التيار
    imageStream.Position = 0;

    // إنشاء كائن BarCodeReader
    Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

    // String txtResult.Text = "";

    بينما (barcodeReader.Read())
    {
        // الحصول على نص الباركود من صورة الباركود
        string code = barcodeReader.GetCodeText();
}
```

string code = barcodeReader.GetCodeText();

// اكتب نص الباركود إلى مخرجات الكونسول

Console.WriteLine("BARCODE : " + code);

}

// أغلق كائن BarCodeReader لتحرير ملف الصورة

barcodeReader.Close();

}

}

{{< /highlight >}}

{{% alert color="primary" %}}

لمزيد من المعلومات حول الموضوعات المغطاة في هذا المقال، يرجى زيارة:

- تحويل صفحات PDF إلى صيغ صور مختلفة (واجهات)
- تحويل كل صفحات PDF إلى صور PNG
- [قراءة الباركود](https://docs.aspose.com/barcode/net/read-barcodes/)

{{% /alert %}}
```
