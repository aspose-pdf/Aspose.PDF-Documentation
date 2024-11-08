---

title: تحويل PDF إلى تنسيقات PDF/A  
linktitle: تحويل PDF إلى تنسيقات PDF/A  
type: docs  
weight: 100  
url: /ar/php-java/convert-pdf-to-pdfa/  
lastmod: "2024-05-20"  
description: يوضح لك هذا الموضوع كيف يسمح لك Aspose.PDF بتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A.  
sitemap:  
    changefreq: "monthly"  
    priority: 0.8  

---

**Aspose.PDF for PHP** يسمح لك بتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A. قبل القيام بذلك، يجب التحقق من صحة الملف. يوضح هذا المقال كيفية القيام بذلك.

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من توافق PDF/A. جميع الأدوات المتاحة في السوق لديها "تمثيل" خاص بها لتوافق PDF/A. يرجى التحقق من هذا المقال حول [أدوات التحقق من PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) كمرجع. اخترنا منتجات Adobe للتحقق من كيفية إنتاج Aspose.PDF لملفات PDF لأن Adobe هي في مركز كل ما يتعلق بـ PDF.

قبل تحويل ملف PDF إلى ملف متوافق مع PDF/A، قم بالتحقق من صحة PDF باستخدام طريقة validate.
 يتم تخزين نتيجة التحقق في ملف XML ثم يتم تمرير هذه النتيجة أيضًا إلى طريقة التحويل. يمكنك أيضًا تحديد الإجراء للعناصر التي لا يمكن تحويلها باستخدام التعداد [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## تحويل PDF إلى PDF/A

يظهر مقتطف الشيفرة التالي كيفية تحويل ملفات PDF إلى PDF متوافق مع PDF/A-1b.

```php
// إنشاء كائن Document جديد وتحميل ملف PDF المدخل.
$document = new Document($inputFile);

// تحويل المستند إلى تنسيق PDF/A-1a وتحديد ملف السجل وإجراء الخطأ.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// حفظ المستند المحول إلى ملف الإخراج.
$document->save($outputFile);
```

لإجراء التحقق فقط، استخدم سطر الشيفرة التالي:

```php
// إنشاء كائن Document جديد وتحميل ملف PDF المدخل.
$document = new Document($inputFile);

// تحويل المستند إلى تنسيق PDF/A-1a وتحديد ملف السجل وإجراء الخطأ.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// التحقق من PDF لـ PDF/A-1a
if ($document->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "صالح";
}
else
{
    echo "غير صالح";
}
```

{{% alert color="primary" %}}
**حاول تحويل PDF إلى PDF/A عبر الإنترنت**

تقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا على الإنترنت ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك تجربة استقصاء الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى PDF/A باستخدام التطبيق المجاني](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}