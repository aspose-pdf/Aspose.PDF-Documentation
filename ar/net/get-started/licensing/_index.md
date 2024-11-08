---
title: رخصة Aspose PDF
linktitle: الترخيص والقيود
type: docs
weight: 90
url: /ar/net/licensing/
description: يدعو Aspose. PDF لـ .NET عملائه للحصول على رخصة كلاسيكية ورخصة مقيدة. بالإضافة إلى استخدام رخصة محدودة لاستكشاف المنتج بشكل أفضل.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## قيود نسخة التقييم

نريد من عملائنا اختبار مكوناتنا بشكل شامل قبل الشراء، لذا تسمح نسخة التقييم باستخدامها كما لو كانت النسخة العادية.

- **PDF مُنشأ بعلامة مائية تقييمية.** توفر نسخة التقييم من Aspose.PDF لـ .NET كامل وظائف المنتج، لكن جميع الصفحات في المستندات PDF المولدة تحتوي على علامة مائية "للتقييم فقط. تم الإنشاء باستخدام Aspose.PDF. حقوق النشر 2002-2020 Aspose Pty Ltd" في الأعلى.

- **حد عدد عناصر المجموعة التي يمكن معالجتها.**
في نسخة التقييم، يمكنك معالجة أربعة عناصر فقط من أي مجموعة (على سبيل المثال، 4 صفحات، 4 حقول نموذج، إلخ).
في النسخة التقييمية من أي مجموعة، يمكنك معالجة أربعة عناصر فقط (على سبيل المثال، 4 صفحات فقط، 4 حقول نموذج، إلخ).

>إذا كنت ترغب في تجربة Aspose.HTML لـ .NET بدون قيود النسخة التقييمية، يمكنك أيضًا طلب ترخيص مؤقت لمدة 30 يومًا. يرجى الرجوع إلى [كيفية الحصول على ترخيص مؤقت؟](https://purchase.aspose.com/temporary-license)

## الترخيص الكلاسيكي

يمكن تحميل الترخيص من ملف أو كائن تيار. أسهل طريقة لتعيين الترخيص هي وضع ملف الترخيص في نفس المجلد مع ملف Aspose.PDF.dll وتحديد اسم الملف بدون مسار، كما هو موضح في المثال أدناه.

إذا كنت تستخدم أي مكون آخر من Aspose لـ .NET بالإضافة إلى Aspose.PDF لـ .NET، يرجى تحديد الفضاء الاسمي للترخيص مثل [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### تحميل ترخيص من ملف

أسهل طريقة لتطبيق الترخيص هي وضع ملف الترخيص في نفس المجلد مع ملف Aspose.PDF.dll وتحديد اسم الملف فقط بدون مسار.

عندما تستدعي طريقة [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index)، يجب أن يكون اسم الترخيص الذي تمرره هو اسم ملف الترخيص الخاص بك.
عندما تستدعي طريقة [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index)، يجب أن يكون اسم الرخصة الذي تمرره هو اسم ملف الترخيص الخاص بك.

```csharp
public static void SetLicenseExample()
{
    // تهيئة كائن الترخيص
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // تعيين الترخيص
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // حدث خطأ ما
        throw;
    }
    Console.WriteLine("تم تعيين الترخيص بنجاح.");
}
```
### تحميل الترخيص من كائن الدفق

المثال التالي يظهر كيفية تحميل الترخيص من دفق.

```csharp
public static void SetLicenseFromStream()
{
    // تهيئة كائن الترخيص
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // تحميل الترخيص من دفق الملف
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // تعيين الترخيص
    license.SetLicense(myStream);
    Console.WriteLine("تم تعيين الترخيص بنجاح.");
}
```
## رخصة محسوبة

تتيح Aspose.PDF للمطورين تطبيق مفتاح محسوب. إنه آلية ترخيص جديدة. ستُستخدم آلية الترخيص الجديدة بالتزامن مع طريقة الترخيص الحالية. يمكن للعملاء الذين يرغبون في الفوترة بناءً على استخدام ميزات الواجهة البرمجية استخدام الترخيص المحسوب. لمزيد من التفاصيل، يرجى الرجوع إلى قسم الأسئلة الشائعة حول الترخيص المحسوب.

تم تقديم فئة جديدة باسم Metered لتطبيق مفتاح محسوب. فيما يلي كود عينة يوضح كيفية تعيين المفاتيح العامة والخاصة المحسوبة.

 لمزيد من التفاصيل، يرجى الرجوع إلى قسم [الأسئلة الشائعة حول الترخيص المحسوب](https://purchase.aspose.com/faqs/licensing/metered).

```csharp
public static void SetMeteredLicense()
{
    // تعيين المفاتيح العامة والخاصة المحسوبة
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // الوصول إلى خاصية setMeteredKey وتمرير المفاتيح العامة والخاصة كمعاملات
    metered.SetMeteredKey(
        "<أدخل المفتاح العام هنا>",
        "<أدخل المفتاح الخاص هنا>");

    // تحميل الوثيقة من القرص.
    Document doc = new Document("input.pdf");
    // الحصول على عدد صفحات الوثيقة
    Console.WriteLine(doc.Pages.Count);
}
```
يرجى ملاحظة أن التطبيقات التي تعمل مع **Aspose.PDF for .NET** يجب أن تستخدم أيضاً الفئة License.

نقطة تحتاج إلى النظر:
يرجى ملاحظة أن الموارد المضمنة مضمنة في التجميع بالطريقة التي تمت إضافتها بها، أي إذا أضفت ملف نصي كمورد مضمن في التطبيق وفتحت الملف التنفيذي الناتج في المفكرة، سترى المحتويات الدقيقة للملف النصي. لذا عند استخدام ملف الترخيص كمورد مضمن، يمكن لأي شخص فتح ملف exe في محرر نصوص بسيط ورؤية/استخراج محتويات الترخيص المضمن.

لذلك، من أجل وضع طبقة إضافية من الأمان عند تضمين الترخيص مع التطبيق، يمكنك ضغط/تشفير الترخيص وبعد ذلك، يمكنك تضمينه في التجميع. لنفترض أن لدينا ملف ترخيص Aspose.PDF.lic، دعونا نقوم بإنشاء Aspose.PDF.zip بكلمة مرور test ونضمن هذا الملف المضغوط في الحل. يمكن استخدام القطعة التالية من الكود لتهيئة الترخيص:

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //احصل على عدد الصفحات في المستند
            Console.WriteLine(doc.Pages.Count);
        }

        private static Stream GetSecureLicenseFromStream()
        {
            var assembly = Assembly.GetExecutingAssembly();
            var memoryStream = new MemoryStream();
            using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
            {
                using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
                {
                    var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
                    unpackedLicense?.Open().CopyTo(memoryStream);
                }
            }

            memoryStream.Position = 0;
            return memoryStream;
        }
    }
}
```
### تطبيق ترخيص تم شراؤه قبل 2005/01/22

لا يدعم Aspose.PDF لـ .NET التراخيص القديمة بعد الآن. إذا كان لديك ترخيص من قبل 22 يناير 2005 وقمت بالتحديث إلى إصدار أحدث من Aspose.PDF، يرجى التواصل مع فريق المبيعات لدينا للحصول على ملف ترخيص جديد.
