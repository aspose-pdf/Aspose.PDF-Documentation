---
title:  استخراج البيانات من AcroForm باستخدام C#
linktitle:  استخراج البيانات من AcroForm
type: docs
weight: 50
url: ar/net/extract-data-from-acroform/
description: يسهل Aspose.PDF استخراج بيانات حقل النموذج من ملفات PDF. تعرف على كيفية استخراج البيانات من AcroForms وحفظها في تنسيق JSON، XML، أو FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج حقول النموذج من مستند PDF

بالإضافة إلى تمكينك من إنشاء حقول النموذج وملء حقول النموذج، يسهل Aspose.PDF لـ .NET استخراج بيانات حقل النموذج أو المعلومات حول حقول النموذج من ملفات PDF.

في الكود المثال أدناه نوضح كيفية التكرار عبر كل صفحة في مستند PDF لاستخراج معلومات حول جميع AcroForm في PDF بالإضافة إلى قيم حقول النموذج. يفترض هذا الكود المثال أنك لا تعرف اسم حقول النموذج مسبقًا.

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // Get values from all fields
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("Field Name : {0} ", formField.PartialName);
        Console.WriteLine("Value : {0} ", formField.Value);
    }
}
```
إذا كنت تعرف اسم حقول النموذج التي ترغب في استخراج القيم منها، فيمكنك استخدام المؤشر في مجموعة Documents.Form لاسترداد هذه البيانات بسرعة. انظر في أسفل هذا المقال لمثال على الكود حول كيفية استخدام هذه الوظيفة.

## استرجاع قيمة حقل النموذج بواسطة العنوان

خاصية Value لحقل النموذج تتيح لك الحصول على قيمة حقل معين. للحصول على القيمة، احصل على حقل النموذج من مجموعة النموذج لكائن الوثيقة. هذا المثال يختار حقل TextBoxField ويسترجع قيمته باستخدام خاصية القيمة.

## استخراج حقول النموذج من مستند PDF إلى JSON

الشفرة التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## استخراج البيانات إلى ملف XML من ملف PDF

تتيح لك فئة النموذج تصدير البيانات إلى ملف XML من ملف PDF باستخدام طريقة ExportXml. لتصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من فئة النموذج ثم استدعاء طريقة ExportXml باستخدام كائن FileStream. أخيرًا، يمكنك إغلاق كائن FileStream وتجاهل كائن النموذج. يظهر الشفرة التالية كيفية تصدير البيانات إلى ملف XML.

يعمل الشفرة التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// فتح المستند
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// إنشاء ملف xml.
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// تصدير البيانات
form.ExportXml(xmlOutputStream);
// إغلاق تدفق الملف
xmlOutputStream.Close();

// إغلاق المستند
form.Dispose();
```
## تصدير البيانات إلى ملف FDF من ملف PDF

تتيح لك فئة النموذج تصدير البيانات إلى ملف FDF من ملف PDF باستخدام طريقة ExportFdf. لتصدير البيانات إلى FDF، تحتاج إلى إنشاء كائن من فئة النموذج ثم استدعاء طريقة ExportFdf باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام طريقة Save لفئة النموذج. يوضح الشفرة التالية كيفية تصدير البيانات إلى ملف FDF.

تعمل الشفرة التالية أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// فتح المستند
form.BindPdf(dataDir + "input.pdf");

// إنشاء ملف fdf.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// تصدير البيانات
form.ExportFdf(fdfOutputStream);

// إغلاق تيار الملف
fdfOutputStream.Close();

// حفظ المستند المُحدث
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## تصدير البيانات إلى ملف XFDF من ملف PDF

تسمح لك فئة النموذج بتصدير البيانات إلى ملف XFDF من ملف PDF باستخدام طريقة ExportXfdf. لتصدير البيانات إلى XFDF، تحتاج إلى إنشاء كائن من فئة النموذج ثم استدعاء طريقة ExportXfdf باستخدام كائن FileStream. أخيرًا، يمكنك حفظ ملف PDF باستخدام طريقة Save الخاصة بفئة النموذج. يوضح لقطة الكود التالية كيفية تصدير البيانات إلى ملف XFDF.

لقطة الكود التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// فتح المستند
form.BindPdf(dataDir + "input.pdf");

// إنشاء ملف xfdf.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// تصدير البيانات
form.ExportXfdf(xfdfOutputStream);

// إغلاق مجرى الملف
xfdfOutputStream.Close();

// حفظ المستند المحدث
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```

