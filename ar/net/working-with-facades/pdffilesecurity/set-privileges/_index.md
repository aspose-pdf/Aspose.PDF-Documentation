---
title: تعيين الامتيازات على ملف PDF
type: docs
weight: 50
url: ar/net/set-privileges/
description: يشرح هذا الموضوع كيفية تعيين الامتيازات على ملف PDF موجود باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## تعيين الامتيازات على ملف PDF موجود

لتعيين امتيازات ملف PDF، قم بإنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) واستدعاء طريقة SetPrivilege. يمكنك تحديد الامتيازات باستخدام الكائن DocumentPrivilege ثم تمرير هذا الكائن إلى طريقة SetPrivilege. يوضح لك مقتطف الشيفرة التالي كيفية تعيين امتيازات ملف PDF.

```csharp
public static void SetPrivilege1()
 {
    // إنشاء كائن DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // إنشاء كائن PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

انظر إلى الطريقة التالية مع تحديد كلمة مرور:

```csharp
 public static void SetPrivilege2()
 {
    // إنشاء كائن DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // إنشاء كائن PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## إزالة ميزة الحقوق الموسعة من ملف PDF

تدعم مستندات PDF ميزة الحقوق الموسعة لتمكين المستخدم النهائي من ملء البيانات في حقول النموذج باستخدام Adobe Acrobat Reader ثم حفظ نسخة من النموذج المملوء. ومع ذلك، فإنه يضمن عدم تعديل ملف PDF وإذا تم إجراء أي تعديل على هيكل PDF، فإن ميزة الحقوق الموسعة تُفقد. عند عرض مثل هذا المستند، يتم عرض رسالة خطأ تشير إلى أن الحقوق الموسعة تمت إزالتها لأن المستند تم تعديله. مؤخرًا، تلقينا متطلبًا لإزالة الحقوق الموسعة من مستند PDF.

لإزالة الحقوق الموسعة من ملف PDF، تم إضافة طريقة جديدة باسم RemoveUsageRights() إلى فئة PdfFileSignature. وتمت إضافة طريقة أخرى باسم ContainsUsageRights() لتحديد ما إذا كان ملف PDF المصدر يحتوي على حقوق موسعة.

{{% alert color="primary" %}}
بدءًا من Aspose.PDF لـ .NET الإصدار 9.5.0، تم تحديث أسماء الطرق التالية. يرجى ملاحظة أن الطرق السابقة لا تزال في واجهة برمجة التطبيقات ولكنها تم وضع علامة عليها على أنها قديمة وسيتم إزالتها. لذلك، يُوصى بتجربة استخدام الطرق المحدثة.

- تم إعادة تسمية طريقة IsContainSignature(.) إلى ContainsSignature(..).

- تم إعادة تسمية طريقة IsCoversWholeDocument(..) إلى CoversWholeDocument(..).{{% /alert %}}

يظهر الكود التالي كيفية إزالة حقوق الاستخدام من الوثيقة:

```csharp
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```