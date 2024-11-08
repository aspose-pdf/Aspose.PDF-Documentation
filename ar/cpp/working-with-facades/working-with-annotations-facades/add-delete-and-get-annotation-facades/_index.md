---
title: إضافة، حذف والحصول على تعليق توضيحي - الواجهات
type: docs
weight: 10
url: /ar/cpp/add-delete-and-get-annotation-facades/
---

## <ins>**إضافة تعليق توضيحي في ملف PDF موجود باستخدام PdfContentEditor**
**PdfContentEditor** يسمح لك بإضافة أنواع مختلفة من التعليقات التوضيحية في ملف PDF موجود. يمكنك استخدام الطريقة المناسبة لفئة **PdfContentEditor** لإضافة نوع معين من التعليقات التوضيحية في مستند PDF موجود. على سبيل المثال، في مقتطفات الشيفرة التالية، استخدمنا طرق **CreateText(...)** و **CreateFreeText(...)**، لإضافة تعليقات وتعليقات نصية حرة في ملف PDF الموجود على التوالي. تحتاج إلى القيام بالخطوات التالية، من أجل إضافة التعليقات التوضيحية باستخدام فئة **PdfContentEditor**:

- إنشاء كائن من Facades::PdfContentEditor.
- استخدام طريقة **BindPdf(...)** لتحميل ملف PDF موجود.
- استدعاء الطريقة المناسبة لإنشاء تعليق توضيحي. مثل **CreateText(...),CreateFreeText(...), إلخ.**
- حفظ مستند PDF باستخدام طريقة **Save(...)**.
### **إضافة تعليقات إلى مستند PDF موجود**

يظهر لك مقتطف الشيفرة التالي كيفية إضافة تعليق في ملف PDF موجود.
```

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-AddAnnotation-AddAnnotation.cpp" >}}
## <ins>**حذف جميع التعليقات التوضيحية من ملف PDF موجود**
يوفر Aspose.PDF لـ C++ أيضًا فئة **PdfAnnotationEditor**، والتي تمكنك من حذف جميع التعليقات التوضيحية من مستند PDF. من أجل حذف جميع التعليقات التوضيحية من ملف PDF الموجود، تحتاج إلى إنشاء كائن من فئة **PdfAnnotationEditor** وفتح المستند الموجود. بعد ذلك، يمكنك استخدام طريقة **DeleteAnnotations(...)** لفئة PdfAnnotationEditor لحذف التعليقات التوضيحية. يُظهر لك مقتطف الكود التالي كيفية استخدام PdfAnnotationEditor لتحقيق الغرض:



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteAllAnnotations-1.cpp" >}}
## <ins>**حذف جميع التعليقات التوضيحية حسب النوع المحدد**
يمكنك استخدام فئة **PdfAnnotationEditor** لحذف جميع التعليقات التوضيحية، بواسطة نوع تعليق توضيحي محدد، من ملف PDF الموجود. من أجل القيام بذلك، تحتاج إلى إنشاء كائن **PdfAnnotationEditor** وربط ملف PDF المدخل باستخدام طريقة **BindPdf**. بعد ذلك، قم باستدعاء طريقة **DeleteAnnotations**، مع المعامل النصي، لحذف جميع التعليقات التوضيحية من الملف؛ يمثل المعامل النصي نوع التعليق التوضيحي المراد حذفه. وأخيراً، استخدم طريقة **Save** لحفظ ملف PDF المحدث. يوضح لك مقتطف الشفرة التالي كيفية حذف جميع التعليقات التوضيحية حسب نوع التعليق التوضيحي المحدد.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteParticularAnnotation-1.cpp" >}}
## <ins>**تحديث/تعديل التعليقات التوضيحية في ملف PDF موجود**
من أجل تحديث تعديل تعليق توضيحي في مستند PDF، يمكنك استخدام طريقة **ModifyAnnotations(...)** الخاصة بفئة **PdfAnnotationEditor** التي تأخذ كائن التعليق التوضيحي إلى جانب مؤشر البداية والنهاية للتعليقات التوضيحية. سيظهر لك مقتطف الشفرة التالي كيفية استخدام طريقة **ModifyAnnotations(...)**:

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ModifyAnnotations-1.cpp" >}}## <ins>**استيراد التعليقات التوضيحية من XFDF إلى ملف PDF**
تسمح لك طريقة **ImportAnnotationFromXfdf** من فئة **PdfAnnotationEditor** باستيراد التعليقات التوضيحية إلى ملف PDF. من أجل استيراد التعليقات التوضيحية، تحتاج إلى إنشاء كائن **PdfAnnotationEditor** وربط ملف PDF باستخدام طريقة **BindPdf**. بعد ذلك، تحتاج إلى إنشاء تعداد لأنواع التعليقات التوضيحية التي تريد استيرادها إلى ملف PDF. يمكنك بعد ذلك استخدام طريقة **ImportAnnotationFromXfdf** لاستيراد التعليقات التوضيحية. وأخيرًا، احفظ ملف PDF المحدث باستخدام طريقة **Save** للكائن **PdfAnnotationEditor**. يوضح لك المقتطف البرمجي التالي كيفية استيراد التعليقات التوضيحية من ملف XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ImportAnnotations-1.cpp" >}}
## **تصدير التعليقات التوضيحية من ملف PDF إلى XFDF**
تسمح لك طريقة **ExportAnnotationXfdf** بتصدير التعليقات التوضيحية من ملف PDF. من أجل تصدير التعليقات التوضيحية، تحتاج إلى إنشاء كائن **PdfAnnotationEditor** وربط ملف PDF باستخدام طريقة **BindPdf**. بعد ذلك، تحتاج إلى إنشاء تعداد لأنواع التعليقات التوضيحية التي تريد تصديرها من ملف PDF. يمكنك بعد ذلك استخدام طريقة **ExportAnnotationXfdf** لاستيراد التعليقات التوضيحية. وأخيراً، قم بحفظ ملف PDF المحدث باستخدام طريقة **Save** لكائن **PdfAnnotationEditor**. يوضح لك مقتطف الشيفرة التالي كيفية تصدير التعليقات التوضيحية إلى ملف XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExportAnnotations-1.cpp" >}}
## <ins>**استخراج التعليقات التوضيحية من ملف PDF موجود**
طريقة **ExtractAnnotations** تتيح لك استخراج التعليقات التوضيحية من ملف PDF. من أجل استخراج التعليقات التوضيحية، تحتاج إلى إنشاء كائن **PdfAnnotationEditor** وربط ملف PDF باستخدام طريقة **BindPdf**. بعد ذلك، تحتاج إلى إنشاء تعداد لأنواع التعليقات التوضيحية التي تريد استخراجها من ملفات PDF. يمكنك بعد ذلك استخدام طريقة **Extract Annotations** لاستخراج التعليقات التوضيحية إلى ArrayPtr. بعد ذلك، يمكنك التجول خلال هذه القائمة والحصول على التعليقات التوضيحية الفردية. وأخيرًا، احفظ ملف PDF المحدث باستخدام طريقة **Save** لكائن **PdfAnnotationEditor**. يعرض لك مقطع الشفرة التالي كيفية استخراج التعليقات التوضيحية من ملفات PDF.



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExtractAnnotations-1.cpp" >}}