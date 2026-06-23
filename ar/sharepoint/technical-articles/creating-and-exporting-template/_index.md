---
title: إنشاء وتصدير القالب
linktitle: إنشاء وتصدير القالب
type: docs
weight: 10
url: /ar/sharepoint/creating-and-exporting-template/
lastmod: "2026-06-18"
description: يمكنك إنشاء وتصدير القوالب إلى PDF في SharePoint باستخدام واجهة برمجة تطبيقات PDF SharePoint.
---

{{% alert color="primary" %}}

توضح هذه المقالة كيفية إنشاء وتصدير القوالب باستخدام Aspose.PDF لـ SharePoint.

ابتداءً من Aspose.PDF لـ SharePoint 1.9.2، يدعم قوالب PDF أيضًا مواقع SharePoint الفرعية.

{{% /alert %}}

## **إنشاء وتصدير القوالب**
{{% alert color="primary" %}}

لاستخدام ميزة التصدير في Aspose.PDF لـ SharePoint، أنشئ أولاً قائمة تستخدم “قوالب PDF”.

إنشاء قائمة تستخدم قوالب PDF:

![todo:image_alt_text](creating-and-exporting-template_1.png)

تم إنشاء قالبين للمستندات، Task Form Templates و Task List Templates:

![todo:image_alt_text](creating-and-exporting-template_2.png)



تتيح لك نموذج القالب إدخال المعلومات التالية:

- **Name**: اسم ملف القالب.
- **Title**: عنوان القالب. (افتراضيًا، يكون نفس اسم الملف.)
- **Description**: وصف للقالب. الوصف الجيد يجعل القالب أسهل في الاستخدام.
- **Assigned List Types**: معرّفات قوائم مفصولة بفواصل (مرتبطة بالقالب. قد يحتوي هذا الحقل أيضًا على القيمة **AllListTypes**. هذا الحقل ينطبق فقط عندما يكون الحقل **Type** مضبوطًا على **List**).
- **Assigned Content Types**: معرّفات نوع المحتوى مفصولة بفواصل (مرتبطة بالقالب. قد يتم تعيين هذا الحقل إلى **AllListTypes**. هذا الحقل ينطبق فقط عندما يكون الحقل **Type** مضبوطًا على **Item**).
- **Type**: إما قالب قائمة أو قالب عنصر.
- **Status**: الخيارات هي نشط، غير نشط (غير مرئي للجميع)، وتصحيح (مرئي فقط للمسؤولين).

**نموذج قوالب قوائم المهام:**

![todo:image_alt_text](creating-and-exporting-template_3.png)




**نموذج قوالب نماذج المهام:**

![todo:image_alt_text](creating-and-exporting-template_4.png)




عند حفظها، تظهر القوالب الجديدة في قائمة القوالب، جاهزة للاستخدام:

**قالبان لقائمة المهام:**

![todo:image_alt_text](creating-and-exporting-template_5.png)



**قالب نماذج مهمة:**

![todo:image_alt_text](creating-and-exporting-template_6.png)



#### **تطوير القوالب**
القالب هو ملف XML يعتمد على Aspose XML PDF. لإنشاء قالب لقائمة، ضع علامات خاصة مرتبطة بالاسم الداخلي لحقل نوع المحتوى المستهدف في SharePoint داخل ملف XML PDF.
##### **علامات**
- **SPListItemsCount** – تم استبداله بعدد عناصر القائمة.
- **SPListTitle** – تم استبداله بعنوان القائمة.
- **SPTableIterator** – يُوضع في أول خلية من الجدول ويُعلّم الجدول للتكرار الكامل.
- **SPRowIterator** – يُوضع في أول خلية من الجدول ويُعلّم الجدول للتكرار على الصفوف.
- **SPField** – تم استبداله بقيمة حقل العنصر.

للمراجعة، يرجى التحميل [ملفات XML للقوالب](attachments/8421394/8618082.zip).
#### **تصدير إلى PDF**
عند اكتمال تكوين القالب، تكون جاهزًا لتصدير القوائم أو العناصر إلى ملفات PDF.

**تصدير قائمة إلى PDF باستخدام قالب قائمة مهام:**

![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}
