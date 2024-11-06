---
title: الحصول على معلومات ملف PDF
type: docs
weight: 50
url: ar/net/get-pdf-file-information/
description: تشرح هذه القسم كيفية الحصول على معلومات ملف PDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

من أجل الحصول على معلومات محددة لملف PDF، تحتاج إلى إنشاء كائن من فئة [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). بعد ذلك، يمكنك الحصول على قيم الخصائص الفردية مثل الموضوع، العنوان، الكلمات المفتاحية، والمنشئ وما إلى ذلك.

يعرض لك مقطع الشيفرة التالي كيفية الحصول على معلومات ملف PDF.

```csharp
 public static void GetPdfInfo()
        {
            // فتح المستند
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // الحصول على معلومات PDF
            Console.WriteLine("الموضوع: {0}", fileInfo.Subject);
            Console.WriteLine("العنوان: {0}", fileInfo.Title);
            Console.WriteLine("الكلمات المفتاحية: {0}", fileInfo.Keywords);
            Console.WriteLine("المنشئ: {0}", fileInfo.Creator);
            Console.WriteLine("تاريخ الإنشاء: {0}", fileInfo.CreationDate);
            Console.WriteLine("تاريخ التعديل: {0}", fileInfo.ModDate);
            // تحقق مما إذا كان ملف PDF صالحًا ومشفرًا أيضًا
            Console.WriteLine("هل هو ملف PDF صالح: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("هل هو مشفر: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("عرض الصفحة: {0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("ارتفاع الصفحة: {0}", fileInfo.GetPageHeight(1));
        }
```

## احصل على معلومات ميتا

من أجل الحصول على المعلومات، نستخدم خاصية [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header). باستخدام 'Hashtable' نحصل على جميع القيم الممكنة.

```csharp
public static void GetMetaInfo()
        {
            // إنشاء مثيل لكائن PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // استرجاع جميع السمات المخصصة الموجودة
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // استرجاع سمة مخصصة واحدة
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```