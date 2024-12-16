---
title: ضبط انتهاء صلاحية ملف PDF في بايثون
type: docs
weight: 80
url: /ar/python-java/set-pdf-expiration-in-python/
---

<ins>لضبط انتهاء صلاحية مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **SetExpiration**.

**كود بايثون**
```

doc = self.Document()
pdf = self.Document()
pdf = self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2014; var month=4; today = new Date(); today = new Date(today.getFullYear(), today.getMonth()); expiry = new Date(year, month); if (today.getTime() > expiry.getTime()) app.alert('الملف منتهي الصلاحية. تحتاج إلى ملف جديد.');");

doc.setOpenAction(javascript);

# حفظ المستند المحدث بالمعلومات الجديدة
doc.save(self.dataDir + "set_expiration.pdf");

print "تحديث معلومات المستند، يرجى التحقق من ملف الإخراج."
```

**تحميل الكود الجاهز للتشغيل**

قم بتحميل **ضبط انتهاء صلاحية ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)

```python
# تأكد من استيراد مكتبة aspose-pdf
import aspose.pdf as ap

# أنشئ وثيقة جديدة
document = ap.Document()

# قم بتعيين تاريخ انتهاء الصلاحية
document.expiration = "2025-01-01"

# احفظ الوثيقة
document.save("document_with_expiration.pdf")