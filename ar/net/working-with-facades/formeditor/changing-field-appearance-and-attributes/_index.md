---
title: مظهر الحقل والسمات
type: docs
weight: 20
url: /ar/net/changing-field-appearance-and-attributes/
description: يشرح هذا القسم كيفية تغيير مظهر وسمات الحقول باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

تسمح لك فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) من [مساحة الأسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) ليس فقط بتغيير مظهر وإحساس حقل النموذج، ولكن أيضًا سلوك الحقل. في هذه المقالة، سنرى كيف يمكننا استخدام فئة FormEditor لتغيير مظهر الحقل، سمات الحقل، وحد الحقل أيضًا.

{{% /alert %}}

## تفاصيل التنفيذ

يستخدم أسلوب [SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) لتغيير مظهر حقل النموذج. يأخذ AnnotationFlag كمعامل. AnnotationFlag هو تعداد يحتوي على أعضاء مختلفين مثل Hidden أو NoRotate إلخ.

يُستخدم [SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) لتغيير الخاصية لحقل النموذج. المعامل الممرر لهذه الطريقة هو تعداد PropertyFlag الذي يحتوي على أعضاء مثل ReadOnly أو Required إلخ.

توفر فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) أيضًا طريقة لتعيين حد الحقل. يخبر الحقل بكمية الأحرف التي يمكن ملؤها بها. يظهر لك المثال البرمجي أدناه كيفية استخدام جميع هذه الطرق.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangingFieldAppearance-ChangingFieldAppearance.cs" >}}