---
title: تعيين الصلاحيات، تشفير وفك تشفير ملف PDF
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 20
url: ar/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: تشفير ملف PDF باستخدام C# باستخدام أنواع وخوارزميات تشفير مختلفة. كذلك، فك تشفير ملفات PDF باستخدام كلمة مرور المالك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تعيين الصلاحيات، تشفير وفك تشفير ملف PDF",
    "alternativeHeadline": "كيفية تشفير وفك تشفير ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, تشفير pdf, فك تشفير pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "تشفير ملف PDF باستخدام C# باستخدام أنواع وخوارزميات تشفير مختلفة. كذلك، فك تشفير ملفات PDF باستخدام كلمة مرور المالك."
}
</script>
الكود التالي يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## تعيين الامتيازات على ملف PDF موجود

لتعيين الامتيازات على ملف PDF، قم بإنشاء كائن من فئة [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) وحدد الحقوق التي تريد تطبيقها على المستند. بمجرد تعريف الامتيازات، امرر هذا الكائن كوسيطة إلى طريقة [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). يوضح الكود التالي كيفية تعيين امتيازات ملف PDF.

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// الطريق إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// تحميل ملف PDF المصدر
using (Document document = new Document(dataDir + "input.pdf"))
{
    // إنشاء كائن امتيازات المستند
    // تطبيق قيود على جميع الامتيازات
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // السماح فقط بقراءة الشاشة
    documentPrivilege.AllowScreenReaders = true;
    // تشفير الملف بكلمة مرور المستخدم وكلمة مرور المالك.
    // يجب تعيين كلمة المرور، بحيث عندما يشاهد المستخدم الملف بكلمة مرور المستخدم،
    // تكون خيارات قراءة الشاشة فقط ممكنة
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // حفظ المستند المحدث
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## تشفير ملف PDF باستخدام أنواع وخوارزميات التشفير المختلفة

يمكنك استخدام الطريقة [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) للكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) لتشفير ملف PDF. يمكنك إدخال كلمة المرور الخاصة بالمستخدم، وكلمة مرور المالك، والأذونات إلى الطريقة [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). بالإضافة إلى ذلك، يمكنك إدخال أي قيمة من القائمة البيانية [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). توفر هذه القائمة البيانية تركيبات مختلفة من خوارزميات التشفير وأحجام المفاتيح. يمكنك إدخال القيمة التي تختارها. أخيرًا، احفظ ملف PDF المشفر باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) للكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>يرجى تحديد كلمات مرور مستخدم ومالك مختلفة عند تشفير ملف PDF.

- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح PDF.
- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح ملف PDF.
- **كلمة مرور المالك**، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة، التحرير، الاستخراج، التعليق، إلخ. سيمنع Acrobat/Reader هذه الأمور بناءً على إعدادات الأذونات. سيتطلب Acrobat هذه الكلمة إذا أردت تعيين/تغيير الأذونات.

الكود التالي يوضح لك كيفية تشفير ملفات PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// فتح المستند
Document document = new Document(dataDir+ "Encrypt.pdf");
// تشفير PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// حفظ PDF المحدث
document.Save(dataDir);
```

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

مع تزايد تبادل المستخدمين لملفات PDF المشفرة لمنع الوصول غير المصرح به إلى الوثائق، مثل الطباعة/النسخ/المشاركة/استخراج المعلومات عن محتويات ملف PDF.
يزداد تبادل المستخدمين لملفات PDF المشفرة لمنع الوصول غير المصرح به إلى الوثائق، مثل الطباعة / النسخ / المشاركة / استخراج المعلومات عن محتويات ملف PDF.
في هذا الصدد، هناك حاجة للوصول إلى ملف PDF المشفر، حيث يمكن الحصول على هذا الوصول فقط من قبل مستخدم مصرح له. أيضا، يبحث الناس عن حلول متنوعة لفك تشفير ملفات PDF عبر الإنترنت.

من الأفضل حل هذه المشكلة مرة واحدة باستخدام مكتبة Aspose.PDF.

لفك تشفير ملف PDF، تحتاج أولاً إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) وفتح PDF باستخدام كلمة مرور المالك.
لفك تشفير ملف PDF، يجب أولاً إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) وفتح PDF باستخدام كلمة مرور المالك.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// فتح المستند
Document document = new Document(dataDir+ "Decrypt.pdf", "password");
// فك تشفير PDF
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// حفظ PDF المحدث
document.Save(dataDir);
```

## تغيير كلمة مرور ملف PDF

إذا كنت تريد تغيير كلمة مرور ملف PDF، يجب أولاً فتح ملف PDF باستخدام كلمة مرور المالك مع كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
إذا أردت تغيير كلمة المرور لملف PDF، يجب أولاً فتح الملف باستخدام كلمة مرور المالك مع كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- كلمة مرور المستخدم، إذا تم تعيينها، هي ما يجب أن تقدمه لفتح ملف PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، لن يتم فتح المستخدم.
>- كلمة مرور المالك، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة، التعديل، الاستخراج، التعليق، إلخ. سيمنع Acrobat/Reader هذه الأمور بناءً على إعدادات الأذونات. سيطلب Acrobat هذه الكلمة إذا كنت تريد تعيين/تغيير الأذونات.

يوضح الكود التالي كيفية تغيير كلمة المرور لملف PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// فتح المستند
Document document = new Document(dataDir+ "ChangePassword.pdf", "owner");
// تغيير كلمة المرور
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// حفظ PDF المحدث
document.Save(dataDir);
```

## كيفية - تحديد ما إذا كان ملف PDF المصدر محميًا بكلمة مرور

**Aspose.PDF لـ .NET** يوفر إمكانيات رائعة للتعامل مع مستندات PDF. عند استخدام فئة Document من فضاء الأسماء Aspose.PDF لفتح مستند PDF محمي بكلمة مرور، نحتاج إلى توفير معلومات كلمة المرور كوسيط لمنشئ Document وفي حالة عدم توفير هذه المعلومات، يتم إنشاء رسالة خطأ. في الواقع، عند محاولة فتح ملف PDF باستخدام كائن Document، يحاول المنشئ قراءة محتويات ملف PDF وفي حالة عدم توفير كلمة المرور الصحيحة، يتم إنشاء رسالة خطأ (يحدث ذلك لمنع الوصول غير المصرح به للمستند).

عند التعامل مع ملفات PDF المشفرة، قد تواجه سيناريو ترغب فيه بالكشف عما إذا كان لدى PDF كلمة مرور للفتح و/أو كلمة مرور للتعديل.
عند التعامل مع ملفات PDF المشفرة، قد تواجه السيناريو الذي قد تكون مهتمًا بالكشف عما إذا كان لدى PDF كلمة مرور للفتح و/أو كلمة مرور للتحرير.

### الحصول على معلومات حول أمان مستند PDF

يحتوي PdfFileInfo على ثلاث خصائص للحصول على معلومات حول أمان مستند PDF.

1. الخاصية PasswordType تعيد قيمة تعداد PasswordType:
    - PasswordType.None - المستند غير محمي بكلمة مرور
    - PasswordType.User - تم فتح المستند بكلمة مرور المستخدم (أو كلمة مرور فتح المستند)
    - PasswordType.Owner - تم فتح المستند بكلمة مرور المالك (أو كلمة مرور الأذونات، التحرير)
    - PasswordType.Inaccessible - المستند محمي بكلمة مرور ولكن يلزم كلمة مرور لفتحه بينما تم تقديم كلمة مرور غير صالحة (أو بدون كلمة مرور).
2. الخاصية البوليانية HasOpenPassword - تُستخدم لتحديد ما إذا كان الملف الذي تم إدخاله يتطلب كلمة مرور عند فتحه.
3. الخاصية البوليانية HasEditPassword - تُستخدم لتحديد ما إذا كان الملف الذي تم إدخاله يتطلب كلمة مرور لتحرير محتوياته.

### تحديد كلمة المرور الصحيحة من المصفوفة
### تحديد كلمة المرور الصحيحة من مصفوفة

أحيانًا يكون هناك حاجة لتحديد كلمة المرور الصحيحة من مصفوفة كلمات المرور وفتح المستند بكلمة المرور الصحيحة. يوضح الشفرة البرمجية التالية الخطوات لتكرار المرور عبر مصفوفة كلمات المرور ومحاولة فتح المستند بكلمة المرور الصحيحة.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// تحميل ملف PDF المصدر
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// تحديد ما إذا كان ملف PDF المصدر مشفرًا
Console.WriteLine("File is password protected " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Number of Page in document are = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

