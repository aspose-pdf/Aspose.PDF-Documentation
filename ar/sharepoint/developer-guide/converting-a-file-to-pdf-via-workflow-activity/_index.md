---
title: تحويل ملف إلى PDF عبر نشاط سير العمل
linktitle: تحويل ملف إلى PDF عبر نشاط سير العمل
type: docs
weight: 50
url: /ar/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-06-18"
description: يمكن استخدام PDF SharePoint API في سير عمل SharePoint يقوم بتحويل مستند إلى PDF.
---

{{% alert color="primary" %}}

دعم سير العمل هو وظيفة رئيسية في Microsoft Office SharePoint Server. تساعد سير العمل على أتمتة نقل المستندات وفقًا لمنطق الأعمال وتبسيط تكلفة ووقت تنظيم المستندات. يوضح هذا المقال كيفية استخدام Aspose.PDF for SharePoint في سير عمل يقوم بتحويل مستند إلى PDF.

{{% /alert %}}
## **إعداد سير العمل**

هذا المثال ينشئ سير عمل يحول أي عنصر جديد في مكتبة المستندات إلى تنسيق PDF ويخزنه في مكتبة مستندات أخرى. يستخدم المثال مكتبة **Personal Documents** كمكتبة المصدر ومجلد فرعي **Pdf** داخل مكتبة **Shared Documents** كمكتبة الوجهة.

يدعم Aspose.PDF for SharePoint تحويل ملفات HTML والنص والصور.

### **تصميم سير العمل باستخدام SharePoint Designer**

1. افتح **SharePoint Designer** واتصل بالموقع حيث سيتم تنفيذ سير العمل.
1. اختر **Workflows** من **site objects** ثم افتح **List Workflow**.
1. حدد مكتبة **Personal Documents** لإنشاء وإرفاق سير عمل قائمة جديد بمكتبة المستندات.

   **تحديد Personal Documents من القائمة**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. أنشئ وأرفق سير عمل القائمة إلى مكتبة **Personal Documents** بكتابة اسم سير العمل ووصفه.
1. انقر **OK** لإكمال هذه الخطوة.

   **إنشاء سير عمل قائمة**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



يظهر محرر خطوة سير العمل. يُستخدم هذا لتحديد الشروط والإجراءات لسير الأعمال. الآن أضف إجراءً لتحويل مستند جديد إلى PDF دون أي شرط، من **Aspose Actions**.

1. حدد الإجراء **Convert file to PDF via Aspose.PDF** من قائمة **Action**.

   **اختيار إجراء**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. قم بتكوين معلمات الإجراء:
   1. عيّن معلمة **this folder** إلى مجلد الوجهة.
   1. إما اترك معلمات الإجراء الأخرى كالقيم الافتراضية أو اضبطها باستخدام نافذة خصائص الإجراء. القيمة الافتراضية لمعلمة **Overwrite** هي false.

      **محرر Workflow**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**إعداد مكتبة الوجهة**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**إعداد الخصائص**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. من قائمة **Workflow**، اختر **Workflow Settings**.
1. حدد **ابدأ سير العمل تلقائيًا عندما يتم إنشاء عنصر جديد** وامسح الخيارات الأخرى من **خيارات البدء**.

   **ضبط خيارات البدء**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)



تم الانتهاء من تصميم سير العمل.

1. احفظ وانشر سير العمل لتطبيقه على موقع SharePoint.

### **اختبار سير العمل**

لاختبار سير العمل:

1. افتح موقع SharePoint وقم بتحميل مستند جديد إلى مكتبة المستندات **Personal Documents**.
   يدعم Aspose.PDF for SharePoint التحويل من ملفات HTML وملفات النصوص والصور (JPG, PNG, GIF, TIFF و BMP*) إلى PDF. تم تكوين سير العمل ليبدأ تلقائيًا عند إنشاء عنصر جديد، لذا يتم معالجة الملفات تلقائيًا.
1. قم بتحديث المتصفح.
   يظهر حالة سير العمل في عمود سير العمل، **Aspose.PDF Workflow** في هذه الحالة.

   **إضافة مستند إلى المكتبة المصدرية**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)




1. افتح مكتبة المستندات الهدف لعرض المستند المحوَّل. **Shared Documents/Pdf** هو المسار في هذا المثال.

   **مكتبة الوجهة**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)

