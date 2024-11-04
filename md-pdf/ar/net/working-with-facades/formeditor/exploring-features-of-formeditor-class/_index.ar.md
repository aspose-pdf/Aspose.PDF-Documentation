---
title: استكشاف ميزات فئة FormEditor
type: docs
weight: 10
url: /net/exploring-features-of-formeditor-class/
description: يمكنك تعلم تفاصيل استكشاف ميزات فئة FormEditor مع مكتبة Aspose. PDF لـ .NET
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

تحتوي مستندات PDF أحيانًا على نموذج تفاعلي يُعرف باسم AcroForm. إنه يشبه تمامًا النموذج المستخدم في صفحات الويب. تحتوي هذه النماذج على أنواع مختلفة من عناصر التحكم مثل مربعات النصوص ومربعات الاختيار والأزرار وما إلى ذلك. قد يحتاج مطور يعمل مع ملفات PDF أحيانًا إلى تحرير هذه النماذج. في هذه المقالة، سننظر في التفاصيل حول كيفية تمكيننا [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) من القيام بذلك.

{{% /alert %}}

## تفاصيل التنفيذ

يمكن للمطورين استخدام [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) ليس فقط لإضافة نماذج وحقول نماذج جديدة في مستند PDF، ولكن أيضًا يتيح لك تحرير الحقول الموجودة. نطاق هذه المقالة يقتصر على ميزات [Aspose.PDF for .NET](/pdf/net/) التي تتعامل مع تحرير النماذج.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) هي الفئة التي تحتوي على معظم الطرق والخصائص التي تسمح للمطورين بتحرير حقول النماذج. يمكنك ليس فقط إضافة حقول جديدة، ولكن أيضًا إزالة الحقول الحالية، نقل حقل إلى موقع آخر، تغيير اسم الحقل، أو السمات وما إلى ذلك. قائمة الميزات التي توفرها هذه الفئة شاملة للغاية، ومن السهل جدًا العمل مع حقول النماذج باستخدام هذه الفئة.

يمكن تقسيم هذه الطرق إلى فئتين رئيسيتين، إحداهما تُستخدم لمعالجة الحقول، والأخرى تُستخدم لتعيين السمات الجديدة لهذه الحقول. الطرق التي يمكننا جمعها تحت الفئة الأولى تشمل AddField، AddListItem، RemoveListItem، CopyInnerField، CopyOuterField، DelListItem، MoveField، RemoveField، و RenameField إلخ. في الفئة الثانية من الطرق يمكن تضمين SetFieldAlignment، SetFieldAppearance، SetFieldAttribute، SetFieldLimit، SetFieldScript. يُظهر لك مقتطف الشفرة التالي بعض الطرق لفئة FormEditor في العمل:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}