---
title: إنشاء وتصدير القالب
linktitle: إنشاء وتصدير القالب
type: docs
weight: 10
url: /ar/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: يمكنك إنشاء وتصدير القوالب إلى PDF في SharePoint باستخدام PDF SharePoint API.
---

{{% alert color="primary" %}}

This article shows how to create and export templates using Aspose.PDF for SharePoint.

From Aspose.PDF for SharePoint 1.9.2, PDF template support also covers SharePoint subsites.

{{% /alert %}}

## إنشاء وتصدير القوالب

{{% alert color="primary" %}}

To use the Aspose.PDF for SharePoint export feature, first create a list that uses “PDF Templates”.

Creating a list that uses PDF Templates:

![Create PDF Template List](creating-and-exporting-template_1.png)

يتم إنشاء قالبين للمستندات، قوالب نماذج المهام وقوالب قائمة المهام:

![Document Templates](creating-and-exporting-template_2.png)

يتيح لك نموذج القالب إدخال المعلومات التالية:

- **Name**: the template's file name.
- **العنوان**: عنوان القالب. (افتراضيًا، هو نفس اسم الملف.)
- **Description**: a description of the template. A good description makes the template easier to use.
- **أنواع القائمة المعينة**: معرفات القائمة المفصولة بفواصل (ذات صلة بالقالب. قد يحتوي هذا الحقل أيضًا على القيمة
- **AllListTypes**. This field is only applicable when the **Type** field is set to **List**).
- **أنواع المحتوى المعينة**: معرفات أنواع المحتوى المفصولة بفواصل المرتبطة بالقالب. قد يحتوي هذا الحقل على **AllListTypes**. ينطبق هذا الحقل فقط عند تعيين الحقل **النوع** على **العنصر**.
- **النوع**: إما قالب القائمة أو قالب العنصر.
- **الحالة**: الخيارات نشطة، وغير نشطة (غير مرئية للجميع)، وتصحيح الأخطاء (مرئية فقط للمسؤولين).

The Task List Templates form:

![Task List Templates](creating-and-exporting-template_3.png)

نموذج قوالب نموذج المهمة:

![Task Form Templates](creating-and-exporting-template_4.png)

عند حفظها، تظهر القوالب الجديدة في قائمة القوالب، وتكون جاهزة للاستخدام:

قالبان لقائمة المهام:*

![Task List Templates](creating-and-exporting-template_5.png)

نموذج نماذج المهام:

![Task Form Templates](creating-and-exporting-template_6.png)

### تطوير القوالب

A template is an XML file based on Aspose XML PDF. To make a template for a list, place special markers related to the SharePoint target content type field's internal name into the XML PDF file.

### علامات

- **SPListItemsCount** – تم استبداله بعدد عناصر القائمة.
- **SPListTitle** – replaced by list title.
- **SPTableIterator** - يتم وضعه في خلية الجدول الأولى ووضع علامة على الجدول للتكرار الكامل.
- **SPRowIterator** - يتم وضعه في خلية الجدول الأول ووضع علامة على الجدول لتكرار الصف.
- **SPField** – تم استبداله بقيمة حقل العنصر.

كمرجع، يرجى تنزيل [ملفات قالب XML](attachments/8421394/8618082.zip).

### تصدير إلى PDF

عندما يتم تكوين القالب بالكامل، تكون جاهزًا لتصدير القوائم أو العناصر إلى ملفات PDF.

تصدير قائمة إلى PDF باستخدام قالب قائمة المهام:

![Export to PDF](creating-and-exporting-template_7.png)

{{% /alert %}}

